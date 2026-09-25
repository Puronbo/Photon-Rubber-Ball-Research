# STATE OF THE SCIENCE 2026 — 中文译本
## （线程外部参考；仅作信息用途）

状态：**信息型** —— 研究于 2026-09-25 完成，来源均含日期（逐条内联引用；每条均可独立复核）。
本文件**不**为语料作任何物理声明，**不改动任何 battery 数值**，定位与 AUDIT_OF_THE_UNIVERSE 相同：
记录外部文献当前的表述，使线程的推想（LAW_A、RANKS、VERIFIED linkage、POSSIBILITIES）能对照一个
有日期、有引用的基线来书写与阅读。证据标签：**ESTABLISHED** = 定理/已测量；**OPEN** = 未解决；
**CONJECTURE** = 属信念/未定案；**FRAMING** = 线程自身的表述框架，非外部物理。

> 规范本为英文原版 `STATE_OF_THE_SCIENCE_2026.md`（2026-09-25 修订）；本文件为其中文翻译伴生件。
> 任何数值/编号如有出入，以英文原版为准；修改须走 corrigendum 处置并在两侧同步。

凡此处声明触及语料物理处，语料必须经 battery 与 CORRIGENDUM 流程。下文无一数字为门控断言；
不得将本文件数字作为 results_of_record.py 的依据引用。

---

## 1. 数论棱镜（节点 B1, C1, E1；battery checks 19-23 领域）

### 1.1 有界素数间隙 —— ESTABLISHED（定理级），孪生素数仍为 OPEN
- Zhang 2013: H1 < 7e7（首个有限无条件上界）。Polymath8a: 4680。Maynard 2014: 600，
  并证 Hm < ∞ 对所有 m。Polymath8b (2014)：无条件 **H1 ≤ 246**；广义 Elliott–Halberstam
  猜想下 **H1 ≤ 6**，且这是**筛法的极限**（Selberg 奇偶阻碍）。截至 2026-09 无进一步无条件改进
  被接受；246 仍是当前最好结果。来源：Castryck, Tao et al., "The bounded gaps between primes
  Polymath project — a retrospective," KU Leuven；Maynard, Ann. of Math. 181 (2015) 383–413。
- battery 关联：check 19（倍增 1,2,4,8）与 check 21（Euler）为数学事实断言；246 一带仅被线程
  引作"领域将小素数间隙括在 246"——该表述依旧成立。

### 1.2 大素数间隙（下界）—— ESTABLISHED（定理级），另有一篇 2026-08 新预印本
- Westzynthius 1931: limsup g_n/log p_n = ∞。Rankin 1938 改进。Erdős 猜想（2014）：
  由 Ford–Green–Konyagin–Tao 与 Maynard 独立证明（均 Ann. of Math. 2016）；合并 FGKMT 2018 (JAMS)：
  g_n > c·(log p_n)(log log p_n)(log log log log p_n)/(log log log p_n) 无穷多次成立。
- **实时进展**：2026-08 一份预印本（署名与角色被报道为一个 OpenAI "GPT-5.6 Sol" 系统）声称将下界
  改进为 g_n > c·(log p_n)(log log p_n)/(log log log log p_n) = G(X) ≫ (log X log₂X)/log₄X ——
  比 FGKMT 提升因子 log₃X/(log₄X)²——并宣告 Lean 形式化（B. Alexeev, 2026-08）。截至 2026-09-25
  尚未经同行评审；按未验证预印本对待，正如语料对待自身未验证条目。若通过评审，仅强化大间隙一侧；
  Cramér 属另一独立（上界）主张。

### 1.3 Cramér 猜想 —— OPEN；强形式被广泛怀疑为假
- 三种形式：(a) g_n = O((log p_n)²)；(b) limsup g_n/(log p_n)² = 1（"强 Cramér"）；
  (c) 逐点 g_n < (log p_n)²。三者均未证未否。
- 已知上界：RH ⇒ g_n = O(√p_n·log p_n)（Cramér，条件）；最佳无条件 g_n = O(p_n^0.525)
  （Baker–Harman–Pintz 2001）。
- 数据对照：已知最大 Cramér–Shanks–Granville 比值 g/(log p)² 为 **0.9206**（素数
  1693182318746371）；创纪录 merit 间隙（2017, Gapcoin, merit 41.9388）的 CSG 比值仅
  **0.2059**。即所有已知数据都在 1 之下——与 (c) 相符，远低于 (b) 的 1。
- Maier 定理（1985）在短区间打破纯 Cramér 随机模型；Granville 引入整除性的修正模型给出
  limsup ≈ c ≥ 2e^(−γ) ≈ 1.1229 而非 1。主流解读（Granville、Pintz、Adleman–McCurley）：
  **强形式（limsup = 1）很可能为假**；O((log)²) 阶量级仍可能成立。

### 1.4 素数间隙纪录（数据，截至 2026-05）—— ESTABLISHED（经测量计算）
- 已识别端点（probable primes）的最大间隙：**16,045,848**，紧随一个 385,713 位 PRP，
  merit 18.07 —— A. Höglund, 2024-03。
- **严格素数**端点的最大间隙：**1,113,106**（merit 25.90，18,662 位）—— Cami, Jansen, Andersen。
- 已知最大 **merit**：41.9388（87 位素数后间隙 8350，Gapcoin 2017）；第二 merit 40.246
  （间隙 42185402，210 位，R. Smith）。merit > 40 的间隙仅知两个。
- 最大极大间隙（maximal gap）：**1,854**（第 85 个极大间隙，紧随素数 101412319996363309069
  —— R. Smith, 2026）。到第 n 个素数的极大间隙数约为 2 ln n（ESTABLISHED 信念）。
- 线程后果（RANKS "不规则素数样间距"，battery check 18）：真实素数间隙在任意可达 log₁₀ 高度上
  merit 最大约 25-42、CSG < 1；所以阶梯的 log₁₀ 步长起伏（在 60 个十进跨度骨架上约 1-2 个十进的
  噪声）完全**落在真实素数样间距的统计规范之内**。相似关系仍是相似关系（FRAMING），如今有了有日期的
  纪录数据背书。

### 1.5 Euler 多项式 n²+n+41 —— ESTABLISHED（定理）
- n²+n+41 在 n = 0..39 全为素数，n = 40 时为合数（= 41²）—— battery check 21（准确）。
- Rabinowitsch (1913)：n²+n+A 对所有 0 ≤ n ≤ A−2 为素数 **当且仅当** Q(√(1−4A)) 类数 = 1。
  A = 41 对应 Q(√(−163))，类数 1（Heegner–Stark）。奇幸运值 A = 2,3,5,11,17,41 分别对应
  Heegner 数 7,11,19,43,67,163。
- Ulam 螺旋：令此类多项式获得视觉威力的对角线线簇，仅有部分解释（某些二元二次型），**无完整理论**
  （作为"解释"仍为 OPEN）。线程对 41 的使用（B1 棱镜）落在坚实的定理级地基上。

### 1.6 倍增 1,2,4,8、Bott 周期性 —— ESTABLISHED（定理）
- Hurwitz：实数**赋范**可除代数仅有 ℝ、ℂ、ℍ、𝕆（维 1,2,4,8）；Cayley–Dickson 每步失去一个
  性质（ℍ 非交换；𝕆 非结合；16 维 sedenions 有零因子）。Frobenius：有限的**结合**可除代数
  仅有 ℝ、ℂ、ℍ。
- Bott 周期性：稳定群的 π_k 周期为 8（实 O）/ 2（复 U）——8 重实周期是 1,2,4,8 链的同伦回声。
  另有 Adams：恰为 S⁰,S¹,S³,S⁷ 是可平行化球面。（battery checks 19-20 断言倍增链与 i 周期-4
  —— 与 Bott 一致。）
- Freudenthal–Tits 魔方：例外群 F4,E6,E7,E8 由除代数对构建，且一侧为八元数——线程 C2 注
  所依据的结构事实。注意**物理**半边（下文）并未定案。

### 1.7 八元数 / E8 物理 —— SPECULATIVE（研究纲领，非共识）
- 活跃纲领：八元数/迹动力学路线（Adler 迹动力学；Chamseddine–Connes 谱作用原理；分裂双八元数；
  E8×E8 分支至 SU(3)×E6 等；例外 Jordan 代数特征方程常数；预测 6 种力，含一个 MOND 式
  "U(1)grav" 场）。参考：INSPIRE 记录 "Trace dynamics, octonions and unification: an E8 × E8 ..."
  （Singh et al.）。
- 形式阻碍：Distler & Garibaldi (J. Math. Phys. 2010) — "There is no E8 gauge theory" ——
  对实现标准费米子族的直接 E8 GUT 的严格 no-go；Lisi 更早的 E8 设想从未成为完整理论。2026 状态：
  数学丰富，物理上对主流缺乏说服力；线程 C2 仅作 FRAMING。

---

## 2. 计量流棱镜（节点 M1-A；Mie、Hertz、JKR、热学）—— 无开放项
- Hertz 1882 / Johnson–Kendall–Roberts 1971 / Mie 1908 / Dicke 1946 均为教科书级验证，
  语料使用已由 battery 断言（checks 1-16），含 corrigendum 76 的圆 JKR 标度修正
  （零载点半径 a ∝ R^(2/3)，即面积 ~ s^(4/3)）。无需研究。

---

## 3. 自我与中心棱镜（节点 P1/P2, F/A）—— 真正开放的项

### 3.1 Hubble 张力 —— OPEN；2026 年尚未解决
- SH0ES（Cepheid–SN Ia 阶梯）：H0 = 73.04 ± 1.04（SH0ES-22; Riess et al. 2022）。Planck 基底
  ΛCDM：67.36 ± 0.54（Planck 2020）。2026 年七路由协方差综述（Cepheid + TRGB + JAGB + Mira +
  SBF + TF + SNe II）给出 73.30 ± 0.92，即 **高于 Planck 5.6σ**。DESI BAO（2025）落在 Planck
  一侧附近（~68）。张力：**持续存在，约 5-5.6σ，无被接受的解决方案**。
- 检验中的系统误差：JWST Cepheid 拥挤在 8.2σ 被排除（Riess 2024，>1000 颗 Cepheid）；
  TRGB 路线（Freedman/CCHP）给出约 69-70，其提出者认为部分差值为阶梯系统误差；Pantheon+/
  CSP 的差异使 H0 移动 +2.0/+0.8 km/s/Mpc（2026 芝加哥-卡内基 JWST TRGB 论文）。活动结论
  （2026 综述）：需要更多独立分析；**未解决**。
- 语料立场更新：AUDIT_OF_THE_UNIVERSE 的"开放异常"表述正确且仍然有效。

### 3.2 大吸引子 / Shapley / bulk flow —— 结构 ESTABLISHED，各向异流动异常 OPEN
- GA（Lynden-Bell 1987 推断）现被理解为主要是 **Shapley 超星系团**过密区（l=311.5°, b=32.3°）
  加上其对跖的**偶极排斥体**空洞（Hoffman et al. 2017）：一个驱动本域运动的引力偶极系统。
- 测得的偶极 bulk flow（Pantheon+ SNe Ia, 0.015 ≤ z ≤ 0.06；2024）：**132 ± 109 km/s 朝
  (l,b) = (326.1°, 27.8°)**，即朝 Shapley，方向置信 >99.9%；有效深度约 103 Mpc；对跖方向落在
  偶极排斥体上。（速度的极大相对误差本身值得尊重：方向显著，量值较不显著。）
- 更大尺度：CosmicFlows-4 最小方差估计（2023-2025，Phil. Trans. R. Soc. A 2025 / CF4++ 2025）
  发现 bulk flow 随半径**增大**而非衰减——在 R = 200 h⁻¹ Mpc 处观测到的振幅在 ΛCDM 下出现的
  概率仅约 ~0.003%。这是对宇宙学原理的 OPEN 异常；CF4++ 团队正在搜寻均一性尺度。
- **关键反制（对节点 P1 的诚实）**：以上均不使 Shapley/GA 成为"宇宙中心"。宇宙学原理受到 CMB
  各向同性（Planck：偶极之外无优先方向；太阳系运动偶极 369 km/s，顶点 (l,b) ≈ (264°, 48°)，
  属无害帧运动）、巡天大尺度均一性（约 250 h⁻¹ Mpc 之上体平均密度平坦至 ~1%）、以及 BAO/CMB
  标准尺的检验。线程 P1 "朝中心攀升"是 FRAMING：宇宙无观测到的中心；阶梯的"向心"方向是构造的
  坐标，不是某个地点。

### 3.3 真空灾难（宇宙学常数）—— OPEN；数值为 56-122 阶，不是干净的 120
- 实测 ρ_vac（Planck 2015）：5.96e-27 kg/m³ ≘ 3.35 GeV/m³。QFT 零点能估计与之相比：
  视方法为 **50 至 122 个数量级**。朴素 Planck 质量截断：约 120（部分引用 122-123）——著名的
  "物理学最差预测"。洛伦兹协变正则化（维数正则化/重整化）将偏差降到 **约 56-60 阶**（2026 AJP
  教学文章；维基百科现行版）。无论取何值：未解决之 OPEN 问题，无被接受机制，诚实的表述是一个区间，
  其中朴素 120 属"广为引用但依赖方法"。
- 语料备注：若有叙事引用"约 120 阶"，其引用的是朴素值；可辩护区间为 56-122。语料当前无文本做此
  声明（grep 已核）。

### 3.4 量子引力离散性 —— OPEN，无证据；强无效上限
- 尚无任何时空离散性的观测迹象被确认（LQG/因果集现象学原则性上仍未受实测）。
- 飞行时间法强无效结果：GRB 221009A / LHAASO（Piran & Ofengeim, PRD 109 L081501, 2024）：
  线性（n=1）LIV 尺度 ≥ 5.9-6.2 E_Pl；二次（d=6）≥ 5.8e-8 E_Pl。
- 少数派分析（Song & Ma, arXiv:2504.00918, 2025）声称 E_LV ≈ 3.0e17 GeV（~10⁻² E_Pl）并以
  17 个 GRB 光子 3.1σ 拒绝无色散真空——有争议、非共识，且 ≤7 TeV 数据可无需 LIV 解释
  （源端固有 multi-TeV 瞬发辐射；如 GRB 221009A 的瞬发 TeV 分量）。按"主张"而非"结果"对待。

### 3.5 暗物质粒子 —— OPEN
- 截至 2026 无任何粒子候选被探测：WIMP 上限持续加深（LZ、XENONnT）；axial 窗口部分未探测；
  自相互作用约束收紧。WIMP 与 axion 参数空间均仍开放。POSSIBILITIES_AND_RELEVANCY 的
  "DM 粒子未识别"表述准确。

---

## 4. 线程可倚赖（有日期、有引用）——以及不可断言的

扎实（定理或测量、日期见上）：
1. H1 ≤ 246 / H1 ≤ 6（GEH、筛法极限）；2. FGKMT 大间隙下界（2018）+ 2026-08 预印本仅作
   预印本对待；3. Cramér：三形式均未证，强形式很可能为假，数据 CSG < 1（最大 0.9206）；
   4. 间隙纪录（PRP 端 16,045,848；严格端 1,113,106；merit 41.94；极大 1,854）；
   5. Euler n²+n+41 = Rabinowitsch ⁺ Heegner 163（已证）；6. 1,2,4,8 = Hurwitz/Frobenius/
   Adams + Bott 8 周期性（已证）；7. Hubble 张力活跃于 5-5.6σ 且未解决（2026 综述）；
   8. Shapley+DR 偶极解释了本域 bulk flow；CF4/CF4++ 大尺度流异常开放；无普遍中心（宇宙学原理
   完好）；9. 真空灾难真实，56-122 阶（方法依赖），开放；10. 无 QG 离散性证据，LIV 无效结果强；
   DM 粒子未探测。

有风险（不得作为语料物理断言）：
- 任何关于 Shapley/GA/Laniakea 的"中心"主张；强 Cramér 精确常数；八元数/E8 物理统一；
  任何"恰为 120"的真空灾难；LIV 尺度"3e17 GeV"主张；2026-08 预印本评审前的边界。

---

## 来源（研究于 2026-09-25；实时核验）
- Wikipedia：Prime gap（纪录含 2026-05 极大间隙 1854 与 merit 41.94；CSG 0.9206）；
  Cramér's conjecture（BHP 上界、Maier/Granville/2e-γ、2026-08 预印本 + Lean 注）；
  formula for primes（Rabinowitsch；41 的类数说明）；cosmological constant problem
  （ρ_vac 5.96e-27 kg/m³；50-122 阶；维数正则化约 56-60）。原页带修订时间戳 2026-09；
  数据 as-of 日期内联给出。
- Polymath/Maynard：Castryck, Tao et al.，bounded-gaps 回顾（KU Leuven）；Maynard,
  Ann. of Math. 181 (2015) 383-413；FGKMT, JAMS 31 (2018) 65-105。
- Hubble 张力 2026 综述："Chicago-Carnegie Hubble Program ... JWST TRGB"（ApJ, 2026）；
  "Distance-ladder Measurements of H0"（RAA/1674-4527, 2026）[H0 = 73.30 ± 0.92, 5.6σ]；
  Riess et al. 2022/2024；Planck 2020；DESI 2025。
- Bulk flow："Bulk Flow Motion Detection with Pantheon+"（ApJ 965/…, 2024）[132 km/s,
  l=326, b=28, Shapley l=311.5/b=32.3, DR 对跖]；"Challenges to the standard cosmological
  model from large-scale bulk flow estimates"（Phil. Trans. R. Soc. A 383, 2025）
  [0.003% @ 200 h⁻¹ Mpc]；"In search of the Local Universe dynamical homogeneity scale with
  CF4++"（A&A 2025）。
- LIV/QG：Piran & Ofengeim, PRD 109 L081501 (2024)；Song & Ma, arXiv:2504.00918 (2025)——
  作非共识；GRB 221009A LHAASO, Science Adv. 9 (2023)。
- 八元数/E8：Singh et al., "Trace dynamics, octonions and unification"（INSPIRE 记录）；
  Distler & Garibaldi, J. Math. Phys. 51 (2010) 062502（no-go）。
- 本文件内嵌数值（间隙长、速度、H0 值）转录自所引来源；若发现转录错误，修订**本文件**并加
  corrigendum 条目（与 battery 数值同等纪律，尽管本文件仅为信息型）。