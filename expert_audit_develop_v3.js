/**
 * expert_audit_and_develop_v3 — Claude Code workflow (Skill-style .js).
 *
 * Readable rewrite of expert_audit_develop_v2.js (not a functional fork):
 * identical meta/phases (Audit = four parallel expert agents; Develop = one
 * synthesizing agent) and the same return object {auditResults, improvedScript}.
 *
 * Deliberate differences:
 *   v1 (expert_audit_develop.js)   — 3 phases: reads the target from disk
 *                                    (./ai_script_manager_final.py), flattened agent
 *                                    calls with {schema: {type: 'string'}}.
 *   v2 (expert_audit_develop_v2.js) — 2 phases: takes the script text via `args`;
 *                                    flattened form, {schema} on every agent call.
 *   v3 (this file)                  — 2 phases: same logic as v2, rewritten in
 *                                    multi-line form without {schema}.
 *
 * Runtime contract (NOT standalone-executable): requires the Claude Code
 * workflow runtime, which provides the globals `agent`, `parallel`, `phase`,
 * and `args` (the string of script content to audit). `node --check`
 * validates syntax only.
 */
export const meta = {
  name: 'expert_audit_and_develop_v3',
  description: 'Audit and improve a script provided as args',
  phases: [
    { title: 'Audit', detail: 'Four experts audit code quality, security, performance, documentation' },
    { title: 'Develop', detail: 'Expert synthesizes feedback and produces an improved script' }
  ]
};

const scriptContent = args; // args is expected to be a string containing the script content

phase('Audit');
const auditResults = await parallel(
  [
    () => agent(`Audit the following script for code quality, style, and maintainability. Provide a concise bullet list of issues and suggestions for improvement.

SCRIPT:
${scriptContent}`),
    () => agent(`Perform a security review of the following script. Identify any vulnerabilities, unsafe practices, and recommend mitigations.

SCRIPT:
${scriptContent}`),
    () => agent(`Analyze the performance of the following script. Look for inefficiencies, possible bottlenecks, and suggest optimizations.

SCRIPT:
${scriptContent}`),
    () => agent(`Review the documentation and comments in the following script. Assess clarity, completeness, and suggest improvements.

SCRIPT:
${scriptContent}`)
  ]
);

const auditSummary = `
Code Quality:
${auditResults[0]}

Security:
${auditResults[1]}

Performance:
${auditResults[2]}

Documentation:
${auditResults[3]}
`;

phase('Develop');
const improvedScript = await agent(
  `You are an expert software engineer. Based on the following audit feedback, produce an improved version of the script. Address all issues raised while preserving the original functionality. Return only the revised script content.

AUDIT FEEDBACK:
${auditSummary}

ORIGINAL SCRIPT:
${scriptContent}`
);

return { auditResults: { codeQuality: auditResults[0], security: auditResults[1], performance: auditResults[2], documentation: auditResults[3] }, improvedScript };