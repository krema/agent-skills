# Research sources for Agentic Harness Engineering

**Research cutoff/access: 2026-10-13. Package and English edition: 2026-10-14.** 95 sources: 79 scientific works, including surveys/position papers, and 16 engineering/documentation sources.

Selected full-text passages were inspected for 36 scientific works; abstracts and metadata for 43. Relevant passages were inspected for the other 16 sources. This does not establish complete reading, independent replication, or general effectiveness.

Search by source ID, title, or topic. Versions bound each claim. Unversioned documentation records its access date. A publication date that could not be reliably established remains null in JSON.

## Research, mechanisms, and benchmarks

### P01 — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

Yang et al. · Version: 2405.15793v3 · Date: 2024-11-11 · Inspection: selected full-text passages.

Targeted editing, search, and feedback tools improve the evaluated SWE setup. Model and benchmark versions limit transfer. [Original source](https://arxiv.org/abs/2405.15793v3)

### P02 — Agentless: Demystifying LLM-based Software Engineering Agents

Xia et al. · Version: 2407.01489v2 · Date: 2024-10-29 · Inspection: selected full-text passages.

Localization, repair, and validation form a bounded pipeline; counterevidence to the assumption that greater agent autonomy necessarily helps. [Original source](https://arxiv.org/abs/2407.01489v2)

### P03 — SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

Jimenez et al. · Version: 2310.06770v3 · Date: 2024-11-11 · Inspection: abstract + metadata.

Real issue-to-patch tasks with test oracles. Existing tests define observed success, not a complete software specification. [Original source](https://arxiv.org/abs/2310.06770v3)

### P04 — SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement

Antoniades et al. · Version: 2410.20285v6 · Date: 2025-04-02 · Inspection: selected full-text passages.

Structured search can improve repairs; additional compute and value estimators are part of the method, not a free increase in determinism. [Original source](https://arxiv.org/abs/2410.20285v6)

### P05 — ReAct: Synergizing Reasoning and Acting in Language Models

Yao et al. · Version: 2210.03629v3 · Date: 2023-03-10 · Inspection: abstract + metadata.

Interleaves reasoning, tool actions, and observations. An execution pattern without technical enforcement of permissions. [Original source](https://arxiv.org/abs/2210.03629v3)

### P06 — Reflexion: Language Agents with Verbal Reinforcement Learning

Shinn et al. · Version: 2303.11366v4 · Date: 2023-10-10 · Inspection: abstract + metadata.

Verbal feedback is retained for later attempts. Success depends on feedback quality and task characteristics. [Original source](https://arxiv.org/abs/2303.11366v4)

### P07 — Self-Refine: Iterative Refinement with Self-Feedback

Madaan et al. · Version: 2303.17651v2 · Date: 2023-05-25 · Inspection: abstract + metadata.

Iterative feedback from the same model. An improvement hypothesis, not independent evidence of correctness. [Original source](https://arxiv.org/abs/2303.17651v2)

### P08 — Large Language Models Cannot Self-Correct Reasoning Yet

Huang et al. · Version: 2310.01798v2 · Date: 2024-03-14 · Inspection: abstract + metadata.

Intrinsic correction without external feedback can fail on the evaluated reasoning tasks. No universal verdict on newer models. [Original source](https://arxiv.org/abs/2310.01798v2)

### P09 — CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

Gou et al. · Version: 2305.11738v4 · Date: 2024-02-21 · Inspection: abstract + metadata.

Tool observations support correction. Together with P08, relevant to separating critique from a checkable oracle. [Original source](https://arxiv.org/abs/2305.11738v4)

### P10 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

Yao et al. · Version: 2406.12045v1 · Date: 2024-06-17 · Inspection: selected full-text passages.

Evaluates tool/user interaction and policies; pass^k measures repeated success. Service domains transfer only partly to software development. [Original source](https://arxiv.org/abs/2406.12045v1)

### P11 — τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment

Barres et al. · Version: 2506.07982v1 · Date: 2025-06-09 · Inspection: abstract + metadata.

Users and agents change the environment. Helps examine collaboration and state changes separately from answer quality. [Original source](https://arxiv.org/abs/2506.07982v1)

### P12 — AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents

Trivedi et al. · Version: 2407.18901v1 · Date: 2024-07-26 · Inspection: abstract + metadata.

Controlled application environment with functional and side-effect checks. Success also needs limits on unintended changes. [Original source](https://arxiv.org/abs/2407.18901v1)

### P13 — OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

Xie et al. · Version: 2404.07972v2 · Date: 2024-05-30 · Inspection: abstract + metadata.

Real desktop environments with assessable final states. Relevant to agents performing browser/GUI tasks. [Original source](https://arxiv.org/abs/2404.07972v2)

### P14 — WebArena: A Realistic Web Environment for Building Autonomous Agents

Zhou et al. · Version: 2307.13854v4 · Date: 2024-04-16 · Inspection: abstract + metadata.

Reproducible web tasks with functional assessment. Website state and infrastructure belong to the experimental setup. [Original source](https://arxiv.org/abs/2307.13854v4)

### P15 — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

Debenedetti et al. · Version: 2406.13352v3 · Date: 2024-11-24 · Inspection: abstract + metadata.

Tasks and attacks involving tool content provide a pattern for adversarial harness tests. No evidence of comprehensive defense. [Original source](https://arxiv.org/abs/2406.13352v3)

### P16 — InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

Zhan et al. · Version: 2403.02691v3 · Date: 2024-08-04 · Inspection: abstract + metadata.

Attacks through external tool data. A transferable failure pattern for tickets, repository text, and logs. [Original source](https://arxiv.org/abs/2403.02691v3)

### P17 — Defeating Prompt Injections by Design

Debenedetti et al. · Version: 2503.18813v2 · Date: 2025-06-24 · Inspection: selected full-text passages.

Separates control and untrusted data through capabilities and dataflow rules. Guarantees apply to the defined model; remaining limits matter. [Original source](https://arxiv.org/abs/2503.18813v2)

### P18 — The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

Wallace et al. · Version: 2404.13208v1 · Date: 2024-04-19 · Inspection: abstract + metadata.

Trained prioritization of privileged instructions. Results do not establish an equivalent guarantee from additional prompt headings. [Original source](https://arxiv.org/abs/2404.13208v1)

### P19 — StruQ: Defending Against Prompt Injection with Structured Queries

Chen et al. · Version: 2402.06363v2 · Date: 2024-09-25 · Inspection: abstract + metadata.

Separate channels plus specific training. Delimiters alone in an unchanged model are not the same intervention. [Original source](https://arxiv.org/abs/2402.06363v2)

### P20 — Instruction-Following Evaluation for Large Language Models

Zhou et al. · Version: 2311.07911v1 · Date: 2023-11-14 · Inspection: abstract + metadata.

Automatically checkable response conditions. Useful partial oracles with limited coverage of lifecycle rules and functional quality. [Original source](https://arxiv.org/abs/2311.07911v1)

### P21 — Generalizing Verifiable Instruction Following

Pyatkin et al. · Version: 2507.02833v3 · Date: 2025-11-11 · Inspection: abstract + metadata.

New verifiable conditions examine overfitting to known instruction tests. Supports separating development and holdout cases. [Original source](https://arxiv.org/abs/2507.02833v3)

### P22 — Lost in the Middle: How Language Models Use Long Contexts

Liu et al. · Version: 2307.03172v3 · Date: 2023-11-20 · Inspection: abstract + metadata.

Position-dependent use of long context in evaluated models. No universal maximum token count for current harnesses. [Original source](https://arxiv.org/abs/2307.03172v3)

### P23 — DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

Khattab et al. · Version: 2310.03714v1 · Date: 2023-10-05 · Inspection: abstract + metadata.

Declarative modules and metric-based optimization. Metric quality and holdouts remain decisive. [Original source](https://arxiv.org/abs/2310.03714v1)

### P24 — Prompting Is Programming: A Query Language for Large Language Models

Beurer-Kellner, Fischer, Vechev · Version: 2212.06094v3 · Date: 2023-05-30 · Inspection: abstract + metadata.

Programmatic control and output conditions. Deterministic program logic does not automatically make linguistic meaning correct. [Original source](https://arxiv.org/abs/2212.06094v3)

### P25 — JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models

Geng et al. · Version: 2501.10868v3 · Date: 2025-02-27 · Inspection: abstract + metadata.

Examines schema coverage, efficiency, and content quality. JSON conformance is a partial objective; engines cover schemas differently. [Original source](https://arxiv.org/abs/2501.10868v3)

### P26 — ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction

Wang et al. · Version: 2508.00500v4 · Date: 2026-08-03 · Inspection: abstract + metadata.

Learned probabilistic model for proactive monitoring. Risk thresholds are statistical decisions, not deterministic knowledge of future failures. [Original source](https://arxiv.org/abs/2508.00500v4)

### P27 — Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces

Merrill et al. · Version: 2601.11868v1 · Date: 2026-01-17 · Inspection: abstract + metadata.

Version 2.0 includes 89 tasks with solutions and tests. Relevant to build, repair, and toolchain work. [Original source](https://arxiv.org/abs/2601.11868v1)

### P28 — What Makes a Terminal-Bench Task Hard? Separating Genuine Hardness from Fake-Hardness on an Adjudicated Agentic Corpus

Lip et al. · Version: 2609.26826v1 · Date: 2026-09-20 · Inspection: abstract + metadata.

Distinguishes genuine difficulty from faulty oracles, infrastructure problems, and bypass cases. Recent preprint; detailed methods were not inspected. [Original source](https://arxiv.org/abs/2609.26826v1)

### P29 — MTAC-IFBench: Benchmarking Instruction-Following in Multi-Turn Agentic Coding

Wen et al. · Version: 2609.14992v1 · Date: 2026-09-14 · Inspection: selected full-text passages.

Coding tasks with accumulated conditions. Evaluation uses judges as well as scripts; authors discuss judge bias and cost. [Original source](https://arxiv.org/abs/2609.14992v1)

### P30 — Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

Yao et al. · Version: 2605.27922v1 · Date: 2026-05-27 · Inspection: selected full-text passages.

106 tasks in the inspected paper version. Compares complete model/harness configurations; does not automatically isolate causal component effects. [Original source](https://arxiv.org/abs/2605.27922v1)

### P31 — Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents

Bhardwaj · Version: 2602.22302v1 · Date: 2026-02-25 · Inspection: abstract + metadata.

Exploratory contract architecture and its own evaluation. Abstract only; no basis for effectiveness promises or mandatory migration. [Original source](https://arxiv.org/abs/2602.22302v1)

### P32 — Proof of Execution: Runtime Verification for Governed AI Agent Actions

Rhodes, Kang · Version: 2607.05397v1 · Date: 2026-04-26 as reported on the page; metadata anomaly · Inspection: abstract + metadata.

Binds executed steps to contracts under deployment assumptions. Abstract inspected; date and month identifier conflict. Supplementary reading, not central evidence. [Original source](https://arxiv.org/abs/2607.05397v1)

### P33 — VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills

Li et al. · Version: 2606.26524v1 · Date: 2026-06-25 · Inspection: selected full-text passages.

Historical artifact bindings plus SMT checks. Grounding and complete collection remain prerequisites; measured detection is imperfect. [Original source](https://arxiv.org/abs/2606.26524v1)

### P34 — Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents

Zhou et al. · Version: 2606.13174v1 · Date: 2026-06-11 · Inspection: selected full-text passages.

Compiles corrections into rules and completion checks. Simulated users and recurring tasks limit transfer. [Original source](https://arxiv.org/abs/2606.13174v1)

### P35 — Self-Healing Harness for Runtime Oversight of Agent Self-Modification

Tayebati et al. · Version: 2609.24130v1 · Date: 2026-09-21 · Inspection: selected full-text passages.

Checks proposed changes against protected cases. Small experiments and missing comparison arms limit causal claims. [Original source](https://arxiv.org/abs/2609.24130v1)

### P36 — AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents

Wang et al. · Version: 2503.18666v3 · Date: 2025-07-31 · Inspection: selected full-text passages.

Triggers, conditions, and responses at action boundaries. Automatically generated rules and semantic predicates remain incomplete. [Original source](https://arxiv.org/abs/2503.18666v3)

### P37 — Formal Policy Enforcement for Real-World Agentic Systems

Palumbo et al. · Version: 2602.16708v3 · Date: 2026-05-08 · Inspection: selected full-text passages.

Versioned policy compiler and instrumented hosts. Formal guarantees require correct policies, observable facts, and complete mediation. [Original source](https://arxiv.org/abs/2602.16708v3)

### P38 — Enforcing Temporal Constraints for LLM Agents

Kamath et al. · Version: 2512.23738v1 · Date: 2025-12-25 · Inspection: selected full-text passages.

Temporal constraints and controlled tool generation. Conformance of modeled traces is narrower than software's functional correctness. [Original source](https://arxiv.org/abs/2512.23738v1)

### P39 — Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems

Jha et al. · Version: 2510.17276v2 · Date: 2026-03-05 · Inspection: selected full-text passages.

Attacks and defenses using permitted call paths. Overly strict graphs can block necessary replanning; permitted paths can still carry harmful content. [Original source](https://arxiv.org/abs/2510.17276v2)

### P40 — Constrained Decoding Eliminates Structural Failures in Small LLMs but Reveals a Scale-Dependent Semantic Gap

Chavan · Version: 2609.23742v1 · Date: 2026-09-20 · Inspection: abstract + metadata.

Small recent study of small models. Supplementary counterevidence to equating schema success with content correctness. [Original source](https://arxiv.org/abs/2609.23742v1)

### P41 — Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments

Zhang et al. · Version: 2607.18357v1 · Date: 2026-07-20 · Inspection: abstract + metadata.

Generation over structured symbols and references. Narrow formal scope; only the abstract was assessed. [Original source](https://arxiv.org/abs/2607.18357v1)

### P42 — Why Do Multi-Agent LLM Systems Fail?

Cemri et al. · Version: 2503.13657v3 · Date: 2025-10-26 · Inspection: abstract + metadata.

Observed failures in system design, coordination, and verification. Additional roles alone do not supply independent evidence. [Original source](https://arxiv.org/abs/2503.13657v3)

### P43 — AI Agents That Matter

Kapoor et al. · Version: 2407.01502v1 · Date: 2024-07-01 · Inspection: abstract + metadata.

Examines cost, reproducibility, and overfitting. Agent comparisons need traceable budgets and genuine test separation. [Original source](https://arxiv.org/abs/2407.01502v1)

### P44 — Progent: Securing AI Agents with Privilege Control

Shi et al. · Version: 2504.11703v3 · Date: 2026-05-14 · Inspection: selected full-text passages.

Symbolic tool permissions with checked narrowing or expansion. Initial policy and completeness of the tool boundary remain trust assumptions. [Original source](https://arxiv.org/abs/2504.11703v3)

### P45 — Executable Code Actions Elicit Better LLM Agents

Wang et al. · Version: 2402.01030v4 · Date: 2024-06-07 · Inspection: abstract + metadata.

Executable code can outperform narrower action interfaces. Suitable sandboxes and mediated relevant external effects bound execution. [Original source](https://arxiv.org/abs/2402.01030v4)

### P46 — Enforceable Security Policies

Schneider · Version: 2000 / ACM TISSEC · Date: 2000 · Inspection: selected full-text passages.

Characterizes execution-monitor limits. Safety properties are narrower than arbitrary correctness, progress, or every information-flow requirement. [Original source](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)

### P47 — The Protection of Information in Computer Systems

Saltzer, Schroeder · Version: 1975 / Proceedings of the IEEE · Date: 1975 · Inspection: selected full-text passages.

Architectural principles for complete mediation, least privilege, and secure defaults. Foundational work, not an LLM effectiveness study. [Original source](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)

### P48 — in-toto: Providing farm-to-table guarantees for bits and bytes

Torres-Arias et al. · Version: 2019 / USENIX Security · Date: 2019 · Inspection: selected full-text passages.

Authenticated steps and artifact relationships. Integrity evidence does not prove complete tests or functionally correct results. [Original source](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias)

### P49 — Edit automata: enforcement mechanisms for run-time security policies

Ligatti, Bauer, Walker · Version: 2005 / IJIS; online 2004 · Date: 2005 · Inspection: selected full-text passages.

Monitors can suppress or insert actions. Suitable formal rules and authority for replacement actions remain necessary. [Original source](https://users.ece.cmu.edu/~lbauer/papers/2005/ijis2005-editauto.pdf)

### P50 — Solving a Million-Step LLM Task with Zero Errors

Meyerson et al. · Version: 2511.09030v1 · Date: 2025-11-12 · Inspection: selected full-text passages.

MAKER combines predetermined decomposition, voting, and red flags on Hanoi. Correlated errors and open-ended software tasks limit transfer. [Original source](https://arxiv.org/abs/2511.09030v1)

### P51 — The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents

Wang et al. · Version: 2511.03690v2 · Date: 2026-04-22 · Inspection: selected full-text passages.

State/event architecture with production evaluation. Bundled changes and excluded provider failures limit causal attribution. [Original source](https://arxiv.org/abs/2511.03690v2)

### P52 — From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws

Chen et al. · Version: 2606.06324v2 · Date: 2026-07-02 · Inspection: selected full-text passages.

HarnessFix connects traces, diagnosis, scoped repair operators, and regression checks with separate data splits. Local utility still needs measurement. [Original source](https://arxiv.org/abs/2606.06324v2)

### P53 — MemoHarness: Agent Harnesses That Learn from Experience

Huang et al. · Version: 2607.14159v1 · Date: 2026-07-14 · Inspection: selected full-text passages.

Experience bank and case-specific adaptation. Small primary test set, missing uncertainty intervals, and incomplete ablations limit claims. [Original source](https://arxiv.org/abs/2607.14159v1)

### P54 — An LLM Compiler for Parallel Function Calling

Kim et al. · Version: 2312.04511v3 · Date: 2024-06-05 · Inspection: selected full-text passages.

A planner generates dependencies for controlled parallel execution. Incorrect planner references remain a separate failure source. [Original source](https://arxiv.org/abs/2312.04511v3)

### P55 — ADaPT: As-Needed Decomposition and Planning with Language Models

Prasad et al. · Version: 2311.05772v2 · Date: 2024-04-08 · Inspection: selected full-text passages.

Recursive decomposition when execution struggles, with a depth limit. Model-based completion heuristics are not mandatory success evidence. [Original source](https://arxiv.org/abs/2311.05772v2)

### P56 — Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

Zhou et al. · Version: 2310.04406v3 · Date: 2024-06-06 · Inspection: abstract + metadata.

LATS combines search, model evaluations, and feedback. Additional compute and task selection are part of the intervention. [Original source](https://arxiv.org/abs/2310.04406v3)

### P57 — Agent Workflow Memory

Wang et al. · Version: 2409.07429v1 · Date: 2024-09-11 · Inspection: selected full-text passages.

Induced subroutines support offline and online web agents. Memory authorizes neither actions nor current completion. [Original source](https://arxiv.org/abs/2409.07429v1)

### P58 — AutoCodeRover: Autonomous Program Improvement

Zhang et al. · Version: 2404.05427v3 · Date: 2024-07-25 · Inspection: abstract + metadata.

AST-based navigation and test-based fault localization for repair. Results depend on repositories and available tests. [Original source](https://arxiv.org/abs/2404.05427v3)

### P59 — OpenHands: An Open Platform for AI Software Developers as Generalist Agents

Wang et al. · Version: 2407.16741v3 · Date: 2025-04-18 · Inspection: abstract + metadata.

Platform for tool actions and software tasks. Distinct from the later SDK paper; background on runtime architecture. [Original source](https://arxiv.org/abs/2407.16741v3)

### P60 — AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation

Huang et al. · Version: 2312.13010v3 · Date: 2024-05-24 · Inspection: abstract + metadata.

Programmer, test-design, and execution roles for code-generation tasks. Role diversity does not prove verifier independence. [Original source](https://arxiv.org/abs/2312.13010v3)

### P61 — MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

Hong et al. · Version: 2308.00352v7 · Date: 2024-11-01 · Inspection: abstract + metadata.

Standardized workflows and intermediate artifacts organize collaboration. Prompt-based SOPs are not a complete runtime boundary. [Original source](https://arxiv.org/abs/2308.00352v7)

### P62 — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

Liu et al. · Version: 2304.11477v3 · Date: 2023-09-27 · Inspection: abstract + metadata.

Language tasks are formalized and processed by a classical planner. Validity depends on translation and the model. [Original source](https://arxiv.org/abs/2304.11477v3)

### P63 — PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change

Valmeekam et al. · Version: 2206.10498v4 · Date: 2023-11-26 · Inspection: abstract + metadata.

Controlled planning tasks evaluate state changes. Historical model findings support no blanket claim about all current models. [Original source](https://arxiv.org/abs/2206.10498v4)

### P64 — LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks

Kambhampati et al. · Version: 2402.01817v3 · Date: 2024-06-12 · Inspection: abstract + metadata.

Position paper combining proposals and external critics. Its title is not a universal empirical model assessment. [Original source](https://arxiv.org/abs/2402.01817v3)

### P65 — Robust Planning with Compound LLM Architectures: An LLM-Modulo Approach

Gundawar et al. · Version: 2411.14484v1 · Date: 2024-11-20 · Inspection: selected full-text passages.

Four scheduling domains with a verification loop. Correctness assumptions concern covered conditions and sound verifiers; successful search remains uncertain. [Original source](https://arxiv.org/abs/2411.14484v1)

### P66 — Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

Gloaguen et al. · Version: 2602.11988v3 · Date: 2026-09-29 · Inspection: selected full-text passages.

v3: CTXbench; no significant general gain over no context file; higher costs. Developer files outperform generated files. [Original source](https://arxiv.org/abs/2602.11988v3)

### P67 — Measuring AI Ability to Complete Long Software Tasks

Kwa et al. · Version: 2503.14499v4 · Date: 2026-07-10 · Inspection: abstract + metadata.

Time horizon refers to human expert time. A revision date does not automatically establish new model measurements. [Original source](https://arxiv.org/abs/2503.14499v4)

### P68 — DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines

Singhvi et al. · Version: 2312.13382v2 · Date: 2024-02-02 · Inspection: selected full-text passages.

Hard and soft conditions control repair and stopping. Model-based predicates remain fallible. [Original source](https://arxiv.org/abs/2312.13382v2)

### P69 — AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents

Yang et al. · Version: 2410.13825v2 · Date: 2025-05-24 · Inspection: abstract + metadata.

Aligns observation and action spaces as a web-agent baseline. Competing hypothesis to indiscriminate increases in complexity. [Original source](https://arxiv.org/abs/2410.13825v2)

### P70 — AFlow: Automating Agentic Workflow Generation

Zhang et al. · Version: 2410.10762v4 · Date: 2025-04-15 · Inspection: selected full-text passages.

Code-based workflow optimization with evaluation and repeated runs. Selected splits and benchmarks limit transfer. [Original source](https://arxiv.org/abs/2410.10762v4)

### P71 — Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step

Zhong et al. · Version: 2402.16906v6 · Date: 2024-06-06 · Inspection: abstract + metadata.

LDB uses intermediate execution states for debugging. Model-based assessment of those states is not a formal proof. [Original source](https://arxiv.org/abs/2402.16906v6)

### P72 — Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation

Liu et al. · Version: 2305.01210v3 · Date: 2023-10-30 · Inspection: selected full-text passages.

Additional inputs and differential testing expose overlooked errors. Reference solutions and input domains remain assumptions. [Original source](https://arxiv.org/abs/2305.01210v3)

### P73 — Self-Consistency Improves Chain of Thought Reasoning in Language Models

Wang et al. · Version: 2203.11171v4 · Date: 2023-03-07 · Inspection: abstract + metadata.

Aggregates multiple reasoning paths. Shared errors and task class limit majority reliability. [Original source](https://arxiv.org/abs/2203.11171v4)

### P74 — Meta-Harness: End-to-End Optimization of Model Harnesses

Lee et al. · Version: 2603.28052v1 · Date: 2026-03-30 · Inspection: selected full-text passages.

Code- and trace-based optimization. Terminal-Bench uses the same tasks for search and evaluation; mathematics has separate transfer assessment. [Original source](https://arxiv.org/abs/2603.28052v1)

### P75 — Natural-Language Agent Harnesses

Pan et al. · Version: 2603.25723v2 · Date: 2026-05-18 · Inspection: selected full-text passages.

Text describes policy; code implements exact mechanisms. Interpretation-dependent documents must be checked against executed behavior. [Original source](https://arxiv.org/abs/2603.25723v2)

## Surveys and reporting

### S01 — Agent Systems with Harness Engineering: A Systematic Survey

Tang et al. · Version: Journal version; DOI 10.1007/s11704-026-61123-6 · Date: 2026-09-16 · Inspection: abstract + metadata.

Survey of workflows, memory, and skills. Journal metadata and abstract inspected; full-text access remained limited. [Original source](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-61123-6)

### S02 — Agent Harness Engineering: A Survey

Li et al. · Version: Unversioned author PDF; accessed 2026-10-13 · Date: not reliably established · Inspection: selected full-text passages.

Seven harness layers and mapping of public projects. Descriptive taxonomy bounded by publicly available information. [Original source](https://picrew.github.io/LLM-Harness/main.pdf)

### S03 — From Question Answering to Task Completion: A Survey on Agent System and Harness Design

Guo et al. · Version: 2606.20683v1 · Date: 2026-06-14 · Inspection: selected full-text passages.

Six coupled runtime responsibilities and task-dependent harness pressures. Orientation, not isolated effectiveness evidence. [Original source](https://arxiv.org/abs/2606.20683v1)

### S04 — Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime

He et al. · Version: 10.20944/preprints202603.1756.v2 · Date: 2026-04-23 · Inspection: selected full-text passages.

Non-peer-reviewed preprint with a conceptual decomposition and HarnessCard. Reporting proposal for models, control artifacts, and runtime policy. [Original source](https://www.preprints.org/manuscript/202603.1756)

## Engineering and interface contracts

### D01 — Harness engineering: leveraging Codex in an agent-first world

OpenAI / Lopopolo · Version: 2026-02-11 · Date: 2026-02-11 · Inspection: relevant article/documentation passages.

Architecture checks, curated repository guidance, and a short entry map. Internal experience report, not a causal productivity study. [Original source](https://openai.com/index/harness-engineering/)

### D02 — Effective harnesses for long-running agents

Anthropic / Young · Version: 2025-11-26 · Date: 2025-11-26 · Inspection: relevant article/documentation passages.

Initialization, feature lists, progress artifacts, and verifiable session completion. Engineering experience under concrete model/task assumptions. [Original source](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

### D03 — Harness design for long-running apps

Anthropic / Rajasekaran · Version: 2026-03-24 · Date: 2026-03-24 · Inspection: relevant article/documentation passages.

Planning, generation, and evaluation of longer application tasks. Reassess roles and criteria when models or tasks change. [Original source](https://www.anthropic.com/engineering/harness-design-long-running-apps)

### D04 — Demystifying evals for AI agents

Anthropic · Version: 2026-01-09 · Date: 2026-01-09 · Inspection: relevant article/documentation passages.

Separates tasks, trials, transcripts, graders, and outcomes. Useful methodology; independent evaluations remain necessary. [Original source](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

### D05 — Infrastructure noise

Anthropic / Segato · Version: 2026-02-05 · Date: 2026-02-05 · Inspection: relevant article/documentation passages.

Environment resources can affect agent scores. Capture resources, timeouts, and concurrency in run manifests. [Original source](https://www.anthropic.com/engineering/infrastructure-noise)

### D06 — Building effective agents

Anthropic · Version: 2024-12-19 · Date: 2024-12-19 · Inspection: relevant article/documentation passages.

Distinguishes predefined workflows from model-directed agents. Simplicity is a starting choice, not a universal ranking. [Original source](https://www.anthropic.com/engineering/building-effective-agents)

### D07 — Effective context engineering for AI agents

Anthropic · Version: 2025-09-29 · Date: 2025-09-29 · Inspection: relevant article/documentation passages.

Task-appropriate context, retrieval, and compaction. Summaries do not replace authoritative workflow state. [Original source](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### D08 — Writing effective tools for agents

Anthropic · Version: 2025-09-11 · Date: 2025-09-11 · Inspection: relevant article/documentation passages.

Tool names, arguments, and actionable feedback as design parameters. Measure improvement on real tasks. [Original source](https://www.anthropic.com/engineering/writing-tools-for-agents)

### D09 — Managed agents

Anthropic · Version: 2026-04-08 · Date: 2026-04-08 · Inspection: relevant article/documentation passages.

Separates sessions, harnesses, models, and execution environments. Vendor architecture as experience, not a required platform. [Original source](https://www.anthropic.com/engineering/managed-agents)

### D10 — LangGraph: Persistence

LangChain · Version: Live documentation, accessed 2026-10-13 · Date: Live documentation, accessed 2026-10-13 · Inspection: relevant article/documentation passages.

Checkpoints and persistent storage differ from RAM stores. Persistence needs a selected backend and retention contract. [Original source](https://docs.langchain.com/oss/python/langgraph/persistence)

### D11 — LangGraph: Interrupts

LangChain · Version: Live documentation, accessed 2026-10-13 · Date: Live documentation, accessed 2026-10-13 · Inspection: relevant article/documentation passages.

Interrupted nodes restart on resume. Earlier effects need protection against repetition. [Original source](https://docs.langchain.com/oss/python/langgraph/interrupts)

### D12 — Temporal Workflow Execution overview

Temporal · Version: Live documentation, accessed 2026-10-13 · Date: Live documentation, accessed 2026-10-13 · Inspection: relevant article/documentation passages.

Workflow replay checks commands against recorded event history. Reconstruction is not identical fresh LLM generation. [Original source](https://docs.temporal.io/workflow-execution)

### D13 — What is a Temporal Activity?

Temporal · Version: Live documentation, accessed 2026-10-13 · Date: Live documentation, accessed 2026-10-13 · Inspection: relevant article/documentation passages.

Activities may be nondeterministic and retried after failure. External actions remain responsible for idempotency. [Original source](https://docs.temporal.io/activities)

### D14 — Open Policy Agent: Introduction

OPA · Version: Live documentation, accessed 2026-10-13 · Date: Live documentation, accessed 2026-10-13 · Inspection: relevant article/documentation passages.

Separates policy decisions from enforcement. The calling effect path must actually respect the decision. [Original source](https://www.openpolicyagent.org/docs)

### D15 — What is Cedar?

Cedar · Version: Documentation version 4.5, accessed 2026-10-13 · Date: Documentation version 4.5, accessed 2026-10-13 · Inspection: relevant article/documentation passages.

Authorization through principal, action, resource, and context. Schemas validate policies; runtime data needs a separate contract. [Original source](https://docs.cedarpolicy.com/)

### D16 — SLSA Build: Provenance

SLSA · Version: Specification v1.2, accessed 2026-10-13 · Date: Specification v1.2, accessed 2026-10-13 · Inspection: relevant article/documentation passages.

Verifiable relationships between builders, inputs, and outputs. Dependency completeness remains limited; provenance does not replace quality checks. [Original source](https://slsa.dev/spec/v1.2/build-provenance)
