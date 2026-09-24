#!/usr/bin/env python3
"""
AI Script Manager – a simple terminal‑based launcher / monitor for AI‑related
or any other scripts.

Features
--------
* List scripts in a configurable directory (default: ./scripts)
* Run a selected script in a subprocess (non‑blocking)
* Stream the subprocess’ stdout/stderr live in the terminal
* Stop a running script at any time
* Keep a rotating log of each run (timestamped files under ./logs)
* Simple menu‑driven interface (no external dependencies)

Usage
-----
$ python ai_script_manager.py
    # or make it executable: chmod +x ai_script_manager.py && ./ai_script_manager.py
"""

import os
import sys
import subprocess
import threading
import time
from datetime import datetime
from pathlib import Path
from queue import Queue, Empty

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if os.name == "nt":
    try:
        import msvcrt
    except ImportError:
        msvcrt = None
else:
    import select

def stdin_has_input():
    """Return True if a keypress is waiting on stdin (platform-aware, non-blocking)."""
    if os.name == "nt":
        if msvcrt is None:
            return False
        try:
            return bool(msvcrt.kbhit())
        except OSError:
            return False
    try:
        return bool(select.select([sys.stdin], [], [], 0)[0])
    except (OSError, ValueError):
        return False

# ------------------- Configuration -------------------
SCRIPTS_DIR = Path("./scripts")   # Folder where your AI scripts live
LOG_DIR     = Path("./logs")      # Where run‑logs will be stored
REFRESH_RATE = 0.2                # Seconds between UI updates while a script runs
# ----------------------------------------------------

def ensure_dirs():
    """Make sure the scripts and logs directories exist."""
    SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

def list_scripts():
    """Return a list of executable files (prefers .py, but any file with exec bit)."""
    if not SCRIPTS_DIR.is_dir():
        return []
    files = []
    for p in SCRIPTS_DIR.iterdir():
        if p.is_file():
            # Prefer .py files, but also accept any file that's executable
            if p.suffix.lower() == ".py" or os.access(p, os.X_OK):
                files.append(p)
    return sorted(files, key=lambda x: x.name.lower())

def display_menu(scripts):
    """Print the numbered list of scripts and the special options."""
    print("\n=== AI Script Manager ===")
    if not scripts:
        print("No scripts found in:", SCRIPTS_DIR.resolve())
    else:
        for idx, scr in enumerate(scripts, start=1):
            print(f"{idx:>3}. {scr.name}")
    print("\nOptions:")
    print("  r  – Refresh script list")
    print("  l  – Show log directory")
    print("  q  – Quit")
    print("Enter choice: ", end="", flush=True)

def enqueue_output(pipe, queue):
    """Thread target: read lines from a pipe and put them into a queue."""
    try:
        for line in iter(pipe.readline, b''):
            queue.put(line.decode(errors="replace"))
    except Exception:
        pass
    finally:
        pipe.close()

def run_script(script_path):
    """Launch the script, stream its output, and allow the user to stop it."""
    print(f"\n▶️  Starting: {script_path.name}")
    print("-" * 60)

    # Prepare log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_DIR / f"{script_path.stem}_{timestamp}.log"
    log_fh = open(log_file, "w", encoding="utf-8", buffering=1)

    # Start subprocess
    proc = subprocess.Popen(
        [sys.executable, str(script_path)] if script_path.suffix == ".py" else [str(script_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,   # combine stderr with stdout for simplicity
        bufsize=1,
    )

    # Queues for streaming output
    q = Queue()
    t = threading.Thread(target=enqueue_output, args=(proc.stdout, q), daemon=True)
    t.start()

    try:
        while True:
            # Check if process has finished
            if proc.poll() is not None:
                # Process ended – drain remaining output
                try:
                    while True:
                        line = q.get_nowait()
                        print(line, end="")
                        log_fh.write(line)
                except Empty:
                    break
                print("\n" + "-" * 60)
                print(f"⏹️  Script finished (exit code {proc.returncode})")
                print(f"📝 Log saved to: {log_file}")
                break

            # Try to get new output lines (non‑blocking)
            try:
                while True:
                    line = q.get_nowait()
                    print(line, end="")
                    log_fh.write(line)
            except Empty:
                pass

            # Prompt for stop command (non‑blocking check)
            # We'll use a short sleep and then check if user typed 's' + Enter.
            # For simplicity, we just check if there's input waiting on stdin.
            if stdin_has_input():
                cmd = sys.stdin.readline().strip()
                if cmd.lower() == "s":
                    print("\n🛑  Stopping script…")
                    proc.terminate()
                    # Wait a bit, then kill if needed
                    try:
                        proc.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        proc.kill()
                        proc.wait()
                    print("⏹️  Script terminated.")
                    print(f"📝 Partial log saved to: {log_file}")
                    break
            time.sleep(REFRESH_RATE)
    finally:
        log_fh.close()

def main():
    ensure_dirs()

    while True:
        scripts = list_scripts()
        display_menu(scripts)
        try:
            choice = input().strip().lower()
        except EOFError:
            print("\n👋  Goodbye!")
            break

        if choice == "q":
            print("👋  Goodbye!")
            break
        elif choice == "l":
            print("\nLog files in:", LOG_DIR.resolve())
            for log in sorted(LOG_DIR.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)[:10]:
                print(f"  {log.name}")
            continue
        elif choice == "r":
            continue  # just refresh the list
        elif choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(scripts):
                run_script(scripts[idx-1])
            else:
                print("❌  Invalid number.")
        else:
            print("❌  Unknown option – try again.")

if __name__ == "__main__":
    main()