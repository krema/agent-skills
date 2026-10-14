# Forschungsquellen für Agentic Harness Engineering

**Forschungsstand/Zugriff: 13.10.2026. Paket erstellt: 14.10.2026.** 95 Quellen: 79 wissenschaftliche Arbeiten einschließlich Surveys/Positionspapieren und 16 Engineering-/Dokumentationsquellen.

36 wissenschaftliche Quellen wurden selektiv an Volltextstellen geprüft, 43 an Abstract und Metadaten. Die 16 weiteren Quellen wurden an relevanten Passagen geprüft. Diese Tiefe ist keine vollständige Lektüre, unabhängige Replikation oder allgemeine Wirksamkeitsgarantie.

Suche gezielt nach Quellen-ID, Titel oder Thema. Die angegebenen Fassungen begrenzen die jeweiligen Claims. Bei unversionierter Dokumentation ist das Zugriffsdatum angegeben. Ein nicht zuverlässig festgestelltes Datum bleibt im JSON null.

## Forschung, Mechanismen und Benchmarks

### P01 — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

Yang et al. · Fassung: 2405.15793v3 · Datum: 2024-11-11 · Prüfung: ausgewählte Volltextstellen.

Gezielte Editier-, Such- und Feedbackwerkzeuge verbessern das untersuchte SWE-Setup. Die Modell- und Benchmarkversion begrenzen den Transfer. [Originalquelle](https://arxiv.org/abs/2405.15793v3)

### P02 — Agentless: Demystifying LLM-based Software Engineering Agents

Xia et al. · Fassung: 2407.01489v2 · Datum: 2024-10-29 · Prüfung: ausgewählte Volltextstellen.

Lokalisierung, Reparatur und Validierung als begrenzte Pipeline; Gegenbefund zur Annahme, zusätzliche Agentenautonomie müsse helfen. [Originalquelle](https://arxiv.org/abs/2407.01489v2)

### P03 — SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

Jimenez et al. · Fassung: 2310.06770v3 · Datum: 2024-11-11 · Prüfung: Abstract + Metadaten.

Reale Issue-Patch-Aufgaben mit Testorakel. Bestehende Tests definieren beobachteten Erfolg, keine vollständige Softwarespezifikation. [Originalquelle](https://arxiv.org/abs/2310.06770v3)

### P04 — SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement

Antoniades et al. · Fassung: 2410.20285v6 · Datum: 2025-04-02 · Prüfung: ausgewählte Volltextstellen.

Strukturierte Suche kann Reparaturen verbessern; zusätzliche Rechenleistung und Wertschätzer sind Teil des Verfahrens, keine kostenlose Determinismussteigerung. [Originalquelle](https://arxiv.org/abs/2410.20285v6)

### P05 — ReAct: Synergizing Reasoning and Acting in Language Models

Yao et al. · Fassung: 2210.03629v3 · Datum: 2023-03-10 · Prüfung: Abstract + Metadaten.

Verzahnt Überlegung, Werkzeugaktion und Beobachtung. Ein Arbeitsmuster, ohne technische Erzwingung von Berechtigungen. [Originalquelle](https://arxiv.org/abs/2210.03629v3)

### P06 — Reflexion: Language Agents with Verbal Reinforcement Learning

Shinn et al. · Fassung: 2303.11366v4 · Datum: 2023-10-10 · Prüfung: Abstract + Metadaten.

Sprachliche Rückmeldungen werden für weitere Versuche gespeichert. Erfolg hängt von der Qualität des Feedbacks und der Aufgabe ab. [Originalquelle](https://arxiv.org/abs/2303.11366v4)

### P07 — Self-Refine: Iterative Refinement with Self-Feedback

Madaan et al. · Fassung: 2303.17651v2 · Datum: 2023-05-25 · Prüfung: Abstract + Metadaten.

Iteratives Feedback durch dasselbe Modell. Eine Verbesserungshypothese, kein unabhängiger Korrektheitsnachweis. [Originalquelle](https://arxiv.org/abs/2303.17651v2)

### P08 — Large Language Models Cannot Self-Correct Reasoning Yet

Huang et al. · Fassung: 2310.01798v2 · Datum: 2024-03-14 · Prüfung: Abstract + Metadaten.

Intrinsische Korrektur ohne externes Feedback kann bei den untersuchten Reasoning-Aufgaben scheitern. Kein universelles Urteil über neuere Modelle. [Originalquelle](https://arxiv.org/abs/2310.01798v2)

### P09 — CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

Gou et al. · Fassung: 2305.11738v4 · Datum: 2024-02-21 · Prüfung: Abstract + Metadaten.

Werkzeugbeobachtungen unterstützen die Korrektur. Zusammen mit P08 relevant für die Trennung von Kritik und prüfbarem Orakel. [Originalquelle](https://arxiv.org/abs/2305.11738v4)

### P10 — τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

Yao et al. · Fassung: 2406.12045v1 · Datum: 2024-06-17 · Prüfung: ausgewählte Volltextstellen.

Prüft Tool-/Nutzerinteraktion und Policies; pass^k misst wiederholten Erfolg. Service-Domänen übertragen sich nur teilweise auf Softwareentwicklung. [Originalquelle](https://arxiv.org/abs/2406.12045v1)

### P11 — τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment

Barres et al. · Fassung: 2506.07982v1 · Datum: 2025-06-09 · Prüfung: Abstract + Metadaten.

Nutzer und Agent verändern die Umgebung. Hilft, Zusammenarbeit und Zustandsänderungen getrennt von reiner Antwortqualität zu untersuchen. [Originalquelle](https://arxiv.org/abs/2506.07982v1)

### P12 — AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents

Trivedi et al. · Fassung: 2407.18901v1 · Datum: 2024-07-26 · Prüfung: Abstract + Metadaten.

Kontrollierte App-Welt mit funktionalen und Nebenwirkungsprüfungen. Relevanz: Erfolg braucht auch Grenzen für unbeabsichtigte Änderungen. [Originalquelle](https://arxiv.org/abs/2407.18901v1)

### P13 — OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

Xie et al. · Fassung: 2404.07972v2 · Datum: 2024-05-30 · Prüfung: Abstract + Metadaten.

Reale Desktopumgebungen und auswertbare Endzustände. Ergänzend für Agenten mit Browser-/GUIaufgaben. [Originalquelle](https://arxiv.org/abs/2404.07972v2)

### P14 — WebArena: A Realistic Web Environment for Building Autonomous Agents

Zhou et al. · Fassung: 2307.13854v4 · Datum: 2024-04-16 · Prüfung: Abstract + Metadaten.

Reproduzierbare Webaufgaben mit funktionaler Bewertung. Websitezustand und Infrastruktur gehören zum Versuchsaufbau. [Originalquelle](https://arxiv.org/abs/2307.13854v4)

### P15 — AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

Debenedetti et al. · Fassung: 2406.13352v3 · Datum: 2024-11-24 · Prüfung: Abstract + Metadaten.

Aufgaben und Angriffe auf Toolinhalte; geeignetes Muster für adversariale Harness-Tests. Kein Nachweis einer umfassenden Defense. [Originalquelle](https://arxiv.org/abs/2406.13352v3)

### P16 — InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

Zhan et al. · Fassung: 2403.02691v3 · Datum: 2024-08-04 · Prüfung: Abstract + Metadaten.

Angriffe über externe Werkzeugdaten. Übertragbares Fehlermuster für Tickets, Repositorytexte und Logs. [Originalquelle](https://arxiv.org/abs/2403.02691v3)

### P17 — Defeating Prompt Injections by Design

Debenedetti et al. · Fassung: 2503.18813v2 · Datum: 2025-06-24 · Prüfung: ausgewählte Volltextstellen.

Trennt Steuerung und untrusted Daten mit Fähigkeiten und Datenflussregeln. Garantien beziehen sich auf das definierte Modell; verbleibende Grenzen sind wesentlich. [Originalquelle](https://arxiv.org/abs/2503.18813v2)

### P18 — The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions

Wallace et al. · Fassung: 2404.13208v1 · Datum: 2024-04-19 · Prüfung: Abstract + Metadaten.

Trainierte Priorisierung privilegierter Anweisungen. Das Ergebnis rechtfertigt keine gleichwertige Garantie durch zusätzliche Promptüberschriften. [Originalquelle](https://arxiv.org/abs/2404.13208v1)

### P19 — StruQ: Defending Against Prompt Injection with Structured Queries

Chen et al. · Fassung: 2402.06363v2 · Datum: 2024-09-25 · Prüfung: Abstract + Metadaten.

Getrennte Kanäle plus spezifisches Training. Bloße Trennzeichen in einem unveränderten Modell sind nicht dieselbe Intervention. [Originalquelle](https://arxiv.org/abs/2402.06363v2)

### P20 — Instruction-Following Evaluation for Large Language Models

Zhou et al. · Fassung: 2311.07911v1 · Datum: 2023-11-14 · Prüfung: Abstract + Metadaten.

Automatisch prüfbare Antwortbedingungen. Gute Teilorakel, mit begrenzter Abdeckung von Lifecycle-Regeln und fachlicher Qualität. [Originalquelle](https://arxiv.org/abs/2311.07911v1)

### P21 — Generalizing Verifiable Instruction Following

Pyatkin et al. · Fassung: 2507.02833v3 · Datum: 2025-11-11 · Prüfung: Abstract + Metadaten.

Neue verifizierbare Bedingungen untersuchen Überanpassung an bekannte Instruction-Tests. Begründet getrennte Entwicklungs- und Holdout-Fälle. [Originalquelle](https://arxiv.org/abs/2507.02833v3)

### P22 — Lost in the Middle: How Language Models Use Long Contexts

Liu et al. · Fassung: 2307.03172v3 · Datum: 2023-11-20 · Prüfung: Abstract + Metadaten.

Positionsabhängige Nutzung langer Kontexte in untersuchten Modellen. Keine universelle maximale Tokenzahl für heutigen Harness. [Originalquelle](https://arxiv.org/abs/2307.03172v3)

### P23 — DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

Khattab et al. · Fassung: 2310.03714v1 · Datum: 2023-10-05 · Prüfung: Abstract + Metadaten.

Deklarative Module und Optimierung anhand einer Metrik. Die Güte der Metrik und Holdouts bleibt entscheidend. [Originalquelle](https://arxiv.org/abs/2310.03714v1)

### P24 — Prompting Is Programming: A Query Language for Large Language Models

Beurer-Kellner, Fischer, Vechev · Fassung: 2212.06094v3 · Datum: 2023-05-30 · Prüfung: Abstract + Metadaten.

Programmierte Steuerung und Ausgabebedingungen. Deterministische Programmlogik macht die sprachliche Bedeutung nicht automatisch korrekt. [Originalquelle](https://arxiv.org/abs/2212.06094v3)

### P25 — JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models

Geng et al. · Fassung: 2501.10868v3 · Datum: 2025-02-27 · Prüfung: Abstract + Metadaten.

Untersucht Schemaabdeckung, Effizienz und Inhaltsqualität. JSON-Konformität ist ein Teilziel; unterschiedliche Engines decken Schemas unterschiedlich ab. [Originalquelle](https://arxiv.org/abs/2501.10868v3)

### P26 — ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction

Wang et al. · Fassung: 2508.00500v4 · Datum: 2026-08-03 · Prüfung: Abstract + Metadaten.

Gelerntes probabilistisches Modell für proaktives Monitoring. Risikoschwellen sind statistische Entscheidungen, keine deterministische Kenntnis künftiger Fehler. [Originalquelle](https://arxiv.org/abs/2508.00500v4)

### P27 — Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces

Merrill et al. · Fassung: 2601.11868v1 · Datum: 2026-01-17 · Prüfung: Abstract + Metadaten.

Version 2.0 umfasst 89 Aufgaben mit Lösungen und Tests. Passung zu Build-, Reparatur- und Toolchainaufgaben. [Originalquelle](https://arxiv.org/abs/2601.11868v1)

### P28 — What Makes a Terminal-Bench Task Hard? Separating Genuine Hardness from Fake-Hardness on an Adjudicated Agentic Corpus

Lip et al. · Fassung: 2609.26826v1 · Datum: 2026-09-20 · Prüfung: Abstract + Metadaten.

Unterscheidet echte Schwierigkeit von defekten Orakeln, Infrastrukturproblemen und Bypassfällen. Aktuelles Preprint; Detailmethodik hier nicht geprüft. [Originalquelle](https://arxiv.org/abs/2609.26826v1)

### P29 — MTAC-IFBench: Benchmarking Instruction-Following in Multi-Turn Agentic Coding

Wen et al. · Fassung: 2609.14992v1 · Datum: 2026-09-14 · Prüfung: ausgewählte Volltextstellen.

Kodierungsaufgaben mit zahlreichen fortgeschriebenen Bedingungen. Die Bewertung enthält neben Skripten auch Judges; Autoren diskutieren Judge-Bias und Kosten. [Originalquelle](https://arxiv.org/abs/2609.14992v1)

### P30 — Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

Yao et al. · Fassung: 2605.27922v1 · Datum: 2026-05-27 · Prüfung: ausgewählte Volltextstellen.

106 Aufgaben in der geprüften Paperfassung. Vergleich vollständiger Modell-Harness-Konfigurationen; isoliert nicht automatisch kausale Effekte einzelner Bausteine. [Originalquelle](https://arxiv.org/abs/2605.27922v1)

### P31 — Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents

Bhardwaj · Fassung: 2602.22302v1 · Datum: 2026-02-25 · Prüfung: Abstract + Metadaten.

Explorative Contract-Architektur und eigene Evaluation. Nur Abstract geprüft; keine Basis für ein Wirksamkeitsversprechen oder eine Pflichtmigration. [Originalquelle](https://arxiv.org/abs/2602.22302v1)

### P32 — Proof of Execution: Runtime Verification for Governed AI Agent Actions

Rhodes, Kang · Fassung: 2607.05397v1 · Datum: 2026-04-26 laut Seite; Metadatenanomalie · Prüfung: Abstract + Metadaten.

Bindet ausgeführte Schritte an Contracts unter Deploymentannahmen. Abstract geprüft; Datum und Monatskennung widersprechen sich. Ergänzende Lektüre, keine zentrale Evidenz. [Originalquelle](https://arxiv.org/abs/2607.05397v1)

### P33 — VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills

Li et al. · Fassung: 2606.26524v1 · Datum: 2026-06-25 · Prüfung: ausgewählte Volltextstellen.

Historische Artefaktbindungen plus SMT-Prüfung. Grounding und vollständiger Collector bleiben Voraussetzungen; gemessene Erkennung ist nicht fehlerfrei. [Originalquelle](https://arxiv.org/abs/2606.26524v1)

### P34 — Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents

Zhou et al. · Fassung: 2606.13174v1 · Datum: 2026-06-11 · Prüfung: ausgewählte Volltextstellen.

Korrekturen werden in Regeln und Abschlussprüfungen überführt. Simulierte Nutzer und wiederkehrende Aufgaben begrenzen die Übertragbarkeit. [Originalquelle](https://arxiv.org/abs/2606.13174v1)

### P35 — Self-Healing Harness for Runtime Oversight of Agent Self-Modification

Tayebati et al. · Fassung: 2609.24130v1 · Datum: 2026-09-21 · Prüfung: ausgewählte Volltextstellen.

Änderungsvorschläge werden gegen geschützte Fälle geprüft. Kleine Versuchsbasis und fehlende Vergleichsarme begrenzen kausale Aussagen. [Originalquelle](https://arxiv.org/abs/2609.24130v1)

### P36 — AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents

Wang et al. · Fassung: 2503.18666v3 · Datum: 2025-07-31 · Prüfung: ausgewählte Volltextstellen.

Trigger, Bedingungen und Reaktionen an Aktionsgrenzen. Automatisch erstellte Regeln und semantische Prädikate bleiben unvollständig. [Originalquelle](https://arxiv.org/abs/2503.18666v3)

### P37 — Formal Policy Enforcement for Real-World Agentic Systems

Palumbo et al. · Fassung: 2602.16708v3 · Datum: 2026-05-08 · Prüfung: ausgewählte Volltextstellen.

Versionierter Policycompiler und instrumentierte Hosts. Formale Garantien setzen korrekte Policies, beobachtbare Fakten und vollständige Vermittlung voraus. [Originalquelle](https://arxiv.org/abs/2602.16708v3)

### P38 — Enforcing Temporal Constraints for LLM Agents

Kamath et al. · Fassung: 2512.23738v1 · Datum: 2025-12-25 · Prüfung: ausgewählte Volltextstellen.

Zeitliche Constraints und kontrollierte Toolgenerierung. Spezifikationskonformität der modellierten Traces ist enger als fachliche Richtigkeit der Software. [Originalquelle](https://arxiv.org/abs/2512.23738v1)

### P39 — Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems

Jha et al. · Fassung: 2510.17276v2 · Datum: 2026-03-05 · Prüfung: ausgewählte Volltextstellen.

Angriffe und Verteidigung durch zulässige Aufrufpfade. Zu strikte Graphen können notwendige Umplanung verhindern; zulässige Pfade können problematische Inhalte transportieren. [Originalquelle](https://arxiv.org/abs/2510.17276v2)

### P40 — Constrained Decoding Eliminates Structural Failures in Small LLMs but Reveals a Scale-Dependent Semantic Gap

Chavan · Fassung: 2609.23742v1 · Datum: 2026-09-20 · Prüfung: Abstract + Metadaten.

Kleine aktuelle Untersuchung zu kleinen Modellen. Ergänzender Gegenbefund zur Gleichsetzung von Schemaerfolg und Inhaltsrichtigkeit. [Originalquelle](https://arxiv.org/abs/2609.23742v1)

### P41 — Decode-Time Grammars: Constrained LLM Generation over a Refinement Order of Grammar Fragments

Zhang et al. · Fassung: 2607.18357v1 · Datum: 2026-07-20 · Prüfung: Abstract + Metadaten.

Generierung über strukturierte Symbole und Referenzen. Enger formaler Zielbereich; hier nur Abstract eingeordnet. [Originalquelle](https://arxiv.org/abs/2607.18357v1)

### P42 — Why Do Multi-Agent LLM Systems Fail?

Cemri et al. · Fassung: 2503.13657v3 · Datum: 2025-10-26 · Prüfung: Abstract + Metadaten.

Beobachtete Fehler bei Systemdesign, Abstimmung und Verifikation. Mehr Rollen allein liefern keine unabhängige Evidenz. [Originalquelle](https://arxiv.org/abs/2503.13657v3)

### P43 — AI Agents That Matter

Kapoor et al. · Fassung: 2407.01502v1 · Datum: 2024-07-01 · Prüfung: Abstract + Metadaten.

Bewertet Kosten, Reproduzierbarkeit und Überanpassung. Agentenvergleich braucht nachvollziehbare Budgets und echte Testtrennung. [Originalquelle](https://arxiv.org/abs/2407.01502v1)

### P44 — Progent: Securing AI Agents with Privilege Control

Shi et al. · Fassung: 2504.11703v3 · Datum: 2026-05-14 · Prüfung: ausgewählte Volltextstellen.

Symbolische Toolrechte und geprüfte Verengung beziehungsweise Erweiterung. Die initiale Policy und die Vollständigkeit der Toolgrenze bleiben vertrauensrelevant. [Originalquelle](https://arxiv.org/abs/2504.11703v3)

### P45 — Executable Code Actions Elicit Better LLM Agents

Wang et al. · Fassung: 2402.01030v4 · Datum: 2024-06-07 · Prüfung: Abstract + Metadaten.

Ausführbarer Code kann leistungsfähiger sein als engere Aktionsschnittstellen. Passende Sandboxen und vermittelte relevante Außenwirkungen begrenzen die Ausführung. [Originalquelle](https://arxiv.org/abs/2402.01030v4)

### P46 — Enforceable Security Policies

Schneider · Fassung: 2000 / ACM TISSEC · Datum: 2000 · Prüfung: ausgewählte Volltextstellen.

Charakterisiert Grenzen von Ausführungsmonitoren. Safety-Eigenschaften sind enger als beliebige Korrektheit, Fortschritt oder alle Informationsflussanforderungen. [Originalquelle](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)

### P47 — The Protection of Information in Computer Systems

Saltzer, Schroeder · Fassung: 1975 / Proceedings of the IEEE · Datum: 1975 · Prüfung: ausgewählte Volltextstellen.

Architekturprinzipien zu vollständiger Vermittlung, minimalen Privilegien und sicheren Defaults. Grundlagenarbeit, keine LLM-Wirksamkeitsstudie. [Originalquelle](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html)

### P48 — in-toto: Providing farm-to-table guarantees for bits and bytes

Torres-Arias et al. · Fassung: 2019 / USENIX Security · Datum: 2019 · Prüfung: ausgewählte Volltextstellen.

Authentifizierte Schritte und Artefaktbeziehungen. Integritätsnachweise sind kein Beweis, dass Tests vollständig oder Ergebnisse fachlich richtig sind. [Originalquelle](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias)

### P49 — Edit automata: enforcement mechanisms for run-time security policies

Ligatti, Bauer, Walker · Fassung: 2005 / IJIS; online 2004 · Datum: 2005 · Prüfung: ausgewählte Volltextstellen.

Monitore können Aktionen unterdrücken beziehungsweise ergänzen. Geeignete formale Regeln und Befugnisse für Ersatzaktionen sind weiterhin nötig. [Originalquelle](https://users.ece.cmu.edu/~lbauer/papers/2005/ijis2005-editauto.pdf)

### P50 — Solving a Million-Step LLM Task with Zero Errors

Meyerson et al. · Fassung: 2511.09030v1 · Datum: 2025-11-12 · Prüfung: ausgewählte Volltextstellen.

MAKER kombiniert vorgegebene Zerlegung, Voting und Red Flags auf Hanoi. Korrelierte Fehler und offene Softwareaufgaben begrenzen den Transfer. [Originalquelle](https://arxiv.org/abs/2511.09030v1)

### P51 — The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents

Wang et al. · Fassung: 2511.03690v2 · Datum: 2026-04-22 · Prüfung: ausgewählte Volltextstellen.

Zustands- und Ereignisarchitektur mit Produktionsauswertung. Gebündelte Änderungen und ausgeschlossene Providerfehler begrenzen die kausale Zuordnung. [Originalquelle](https://arxiv.org/abs/2511.03690v2)

### P52 — From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws

Chen et al. · Fassung: 2606.06324v2 · Datum: 2026-07-02 · Prüfung: ausgewählte Volltextstellen.

HarnessFix verbindet Traces, Diagnose, begrenzte Reparaturoperatoren und Regressionsprüfung mit getrennten Datensplits. Lokaler Nutzen bleibt zu messen. [Originalquelle](https://arxiv.org/abs/2606.06324v2)

### P53 — MemoHarness: Agent Harnesses That Learn from Experience

Huang et al. · Fassung: 2607.14159v1 · Datum: 2026-07-14 · Prüfung: ausgewählte Volltextstellen.

Erfahrungsbank und fallbezogene Anpassung. Kleine primäre Testmenge, fehlende Unsicherheitsintervalle und unvollständige Ablationen begrenzen Aussagen. [Originalquelle](https://arxiv.org/abs/2607.14159v1)

### P54 — An LLM Compiler for Parallel Function Calling

Kim et al. · Fassung: 2312.04511v3 · Datum: 2024-06-05 · Prüfung: ausgewählte Volltextstellen.

Ein Planner erzeugt Abhängigkeiten für kontrollierte parallele Ausführung. Fehlerhafte Plannerreferenzen bleiben eine eigene Fehlerquelle. [Originalquelle](https://arxiv.org/abs/2312.04511v3)

### P55 — ADaPT: As-Needed Decomposition and Planning with Language Models

Prasad et al. · Fassung: 2311.05772v2 · Datum: 2024-04-08 · Prüfung: ausgewählte Volltextstellen.

Rekursive Zerlegung bei Ausführungsschwierigkeiten mit Tiefengrenze. Die modellbasierte Completionheuristik ist kein verbindlicher Erfolgsnachweis. [Originalquelle](https://arxiv.org/abs/2311.05772v2)

### P56 — Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

Zhou et al. · Fassung: 2310.04406v3 · Datum: 2024-06-06 · Prüfung: Abstract + Metadaten.

LATS kombiniert Suche, Modellbewertungen und Feedback. Zusätzlicher Compute und Aufgabenwahl sind Teil der Intervention. [Originalquelle](https://arxiv.org/abs/2310.04406v3)

### P57 — Agent Workflow Memory

Wang et al. · Fassung: 2409.07429v1 · Datum: 2024-09-11 · Prüfung: ausgewählte Volltextstellen.

Induzierte Teilroutinen unterstützen Offline- und Online-Webagenten. Erinnerung legitimiert weder Aktionen noch den aktuellen Abschluss. [Originalquelle](https://arxiv.org/abs/2409.07429v1)

### P58 — AutoCodeRover: Autonomous Program Improvement

Zhang et al. · Fassung: 2404.05427v3 · Datum: 2024-07-25 · Prüfung: Abstract + Metadaten.

ASTgestützte Navigation und testbasierte Fehlereingrenzung für Reparaturen. Ergebnisse hängen von Repository und verfügbaren Tests ab. [Originalquelle](https://arxiv.org/abs/2404.05427v3)

### P59 — OpenHands: An Open Platform for AI Software Developers as Generalist Agents

Wang et al. · Fassung: 2407.16741v3 · Datum: 2025-04-18 · Prüfung: Abstract + Metadaten.

Plattform für Toolaktionen und Softwareaufgaben. Vom späteren SDK-Paper zu unterscheiden; hier Hintergrund zum Runtimeaufbau. [Originalquelle](https://arxiv.org/abs/2407.16741v3)

### P60 — AgentCoder: Multi-Agent-based Code Generation with Iterative Testing and Optimisation

Huang et al. · Fassung: 2312.13010v3 · Datum: 2024-05-24 · Prüfung: Abstract + Metadaten.

Programmier-, Testdesign- und Ausführungsrollen auf Codegenerierungsaufgaben. Rollenvielfalt beweist keine Unabhängigkeit der Prüfer. [Originalquelle](https://arxiv.org/abs/2312.13010v3)

### P61 — MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

Hong et al. · Fassung: 2308.00352v7 · Datum: 2024-11-01 · Prüfung: Abstract + Metadaten.

Standardisierte Abläufe und Zwischenartefakte organisieren Zusammenarbeit. Promptbasierte SOPs sind keine vollständige Runtimegrenze. [Originalquelle](https://arxiv.org/abs/2308.00352v7)

### P62 — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency

Liu et al. · Fassung: 2304.11477v3 · Datum: 2023-09-27 · Prüfung: Abstract + Metadaten.

Sprachaufgabe wird formalisiert und durch einen klassischen Planner bearbeitet. Gültigkeit hängt von Übersetzung und Modell ab. [Originalquelle](https://arxiv.org/abs/2304.11477v3)

### P63 — PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change

Valmeekam et al. · Fassung: 2206.10498v4 · Datum: 2023-11-26 · Prüfung: Abstract + Metadaten.

Kontrollierte Planungsaufgaben prüfen Zustandsänderungen. Historische Modellbefunde erlauben keine pauschale Aussage über alle heutigen Modelle. [Originalquelle](https://arxiv.org/abs/2206.10498v4)

### P64 — LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks

Kambhampati et al. · Fassung: 2402.01817v3 · Datum: 2024-06-12 · Prüfung: Abstract + Metadaten.

Positionspapier zur Kombination von Lösungsvorschlägen und externen Kritikern. Der Titel ist keine universelle empirische Modellbewertung. [Originalquelle](https://arxiv.org/abs/2402.01817v3)

### P65 — Robust Planning with Compound LLM Architectures: An LLM-Modulo Approach

Gundawar et al. · Fassung: 2411.14484v1 · Datum: 2024-11-20 · Prüfung: ausgewählte Volltextstellen.

Vier Schedulingdomänen mit Prüfschleife. Korrektheitsannahmen betreffen erfasste Bedingungen und sounde Prüfer; erfolgreiche Suche bleibt offen. [Originalquelle](https://arxiv.org/abs/2411.14484v1)

### P66 — Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

Gloaguen et al. · Fassung: 2602.11988v3 · Datum: 2026-09-29 · Prüfung: ausgewählte Volltextstellen.

v3: CTXbench, kein signifikanter allgemeiner Gewinn gegenüber fehlender Datei; höhere Kosten. Entwicklerdateien übertreffen generierte Dateien. [Originalquelle](https://arxiv.org/abs/2602.11988v3)

### P67 — Measuring AI Ability to Complete Long Software Tasks

Kwa et al. · Fassung: 2503.14499v4 · Datum: 2026-07-10 · Prüfung: Abstract + Metadaten.

Zeithorizont bezieht sich auf menschliche Expertenzeit. Versionsdatum ist kein automatischer Nachweis neuer Modellmessungen. [Originalquelle](https://arxiv.org/abs/2503.14499v4)

### P68 — DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines

Singhvi et al. · Fassung: 2312.13382v2 · Datum: 2024-02-02 · Prüfung: ausgewählte Volltextstellen.

Harte und weiche Bedingungen steuern Reparatur und Abbruch. Modellbasierte Prädikate bleiben fehleranfällig. [Originalquelle](https://arxiv.org/abs/2312.13382v2)

### P69 — AgentOccam: A Simple Yet Strong Baseline for LLM-Based Web Agents

Yang et al. · Fassung: 2410.13825v2 · Datum: 2025-05-24 · Prüfung: Abstract + Metadaten.

Ausrichtung von Beobachtungs- und Aktionsraum als Webagentenbaseline. Gegenhypothese zur pauschalen Komplexitätssteigerung. [Originalquelle](https://arxiv.org/abs/2410.13825v2)

### P70 — AFlow: Automating Agentic Workflow Generation

Zhang et al. · Fassung: 2410.10762v4 · Datum: 2025-04-15 · Prüfung: ausgewählte Volltextstellen.

Codebasierte Workflowoptimierung mit Evaluation und wiederholten Läufen. Gewählte Datensplits und Benchmarks begrenzen den Transfer. [Originalquelle](https://arxiv.org/abs/2410.10762v4)

### P71 — Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step

Zhong et al. · Fassung: 2402.16906v6 · Datum: 2024-06-06 · Prüfung: Abstract + Metadaten.

LDB nutzt Zwischenzustände der Ausführung zur Fehlersuche. Modellgestützte Beurteilung solcher Zustände ist kein formaler Beweis. [Originalquelle](https://arxiv.org/abs/2402.16906v6)

### P72 — Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large Language Models for Code Generation

Liu et al. · Fassung: 2305.01210v3 · Datum: 2023-10-30 · Prüfung: ausgewählte Volltextstellen.

Zusätzliche Inputs und Differential Testing prüfen übersehene Fehler. Referenzlösung und Eingabedomäne bleiben Voraussetzungen. [Originalquelle](https://arxiv.org/abs/2305.01210v3)

### P73 — Self-Consistency Improves Chain of Thought Reasoning in Language Models

Wang et al. · Fassung: 2203.11171v4 · Datum: 2023-03-07 · Prüfung: Abstract + Metadaten.

Mehrere Reasoningpfade werden aggregiert. Geteilte Fehler und die Aufgabenklasse begrenzen die Verlässlichkeit von Mehrheiten. [Originalquelle](https://arxiv.org/abs/2203.11171v4)

### P74 — Meta-Harness: End-to-End Optimization of Model Harnesses

Lee et al. · Fassung: 2603.28052v1 · Datum: 2026-03-30 · Prüfung: ausgewählte Volltextstellen.

Code- und Tracegestützte Optimierung. Terminal-Bench verwendet dieselben Aufgaben für Suche und Auswertung; Mathematik hat getrennten Transfer. [Originalquelle](https://arxiv.org/abs/2603.28052v1)

### P75 — Natural-Language Agent Harnesses

Pan et al. · Fassung: 2603.25723v2 · Datum: 2026-05-18 · Prüfung: ausgewählte Volltextstellen.

Text beschreibt Policy, Code implementiert exakte Mechanismen. Interpretationsabhängige Texte müssen an ausgeführtem Verhalten geprüft werden. [Originalquelle](https://arxiv.org/abs/2603.25723v2)

## Surveys und Reporting

### S01 — Agent Systems with Harness Engineering: A Systematic Survey

Tang et al. · Fassung: Journalfassung; DOI 10.1007/s11704-026-61123-6 · Datum: 2026-09-16 · Prüfung: Abstract + Metadaten.

Survey zu Workflow, Gedächtnis und Skills. Journalmetadaten und Abstract geprüft; Volltextzugang blieb begrenzt. [Originalquelle](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-61123-6)

### S02 — Agent Harness Engineering: A Survey

Li et al. · Fassung: Autoren-PDF; unversioniert, abgerufen 2026-10-13 · Datum: nicht zuverlässig festgestellt · Prüfung: ausgewählte Volltextstellen.

Sieben Harnessschichten und Mapping öffentlicher Projekte. Deskriptive, durch öffentlich zugängliche Informationen begrenzte Taxonomie. [Originalquelle](https://picrew.github.io/LLM-Harness/main.pdf)

### S03 — From Question Answering to Task Completion: A Survey on Agent System and Harness Design

Guo et al. · Fassung: 2606.20683v1 · Datum: 2026-06-14 · Prüfung: ausgewählte Volltextstellen.

Sechs gekoppelte Runtimeaufgaben und aufgabenabhängige Harnessbelastung. Taxonomie bietet Orientierung, keine isolierten Wirksamkeitsnachweise. [Originalquelle](https://arxiv.org/abs/2606.20683v1)

### S04 — Harness Engineering for Language Agents: The Harness Layer as Control, Agency, and Runtime

He et al. · Fassung: 10.20944/preprints202603.1756.v2 · Datum: 2026-04-23 · Prüfung: ausgewählte Volltextstellen.

Nicht begutachteter Preprint mit begrifflicher Zerlegung und HarnessCard. Reportingvorschlag für Modell, Kontrollartefakte und Runtimepolicy. [Originalquelle](https://www.preprints.org/manuscript/202603.1756)

## Engineering und Schnittstellenverträge

### D01 — Harness engineering: leveraging Codex in an agent-first world

OpenAI / Lopopolo · Fassung: 2026-02-11 · Datum: 2026-02-11 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Architekturprüfungen, kuratierte Repositoryführung und kurze Einstiegskarte. Ein interner Erfahrungsbericht; keine kausale Produktivitätsstudie. [Originalquelle](https://openai.com/index/harness-engineering/)

### D02 — Effective harnesses for long-running agents

Anthropic / Young · Fassung: 2025-11-26 · Datum: 2025-11-26 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Initialisierung, Featureliste, Fortschrittsartefakte und überprüfbarer Sitzungsabschluss. Engineering-Erfahrung mit konkreten Modell-/Aufgabenannahmen. [Originalquelle](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

### D03 — Harness design for long-running apps

Anthropic / Rajasekaran · Fassung: 2026-03-24 · Datum: 2026-03-24 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Planung, Generierung und Evaluation längerer App-Aufgaben. Rollen und Kriterien müssen mit Modell- und Aufgabenwechseln neu bewertet werden. [Originalquelle](https://www.anthropic.com/engineering/harness-design-long-running-apps)

### D04 — Demystifying evals for AI agents

Anthropic · Fassung: 2026-01-09 · Datum: 2026-01-09 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Trennt Task, Trial, Transcript, Grader und Outcome. Hilfreiche Methodik; eigene Evaluationen bleiben notwendig. [Originalquelle](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

### D05 — Infrastructure noise

Anthropic / Segato · Fassung: 2026-02-05 · Datum: 2026-02-05 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Umgebungsressourcen können Agentenscores beeinflussen. Ressourcen, Timeouts und Parallelität gehören in den Runmanifest. [Originalquelle](https://www.anthropic.com/engineering/infrastructure-noise)

### D06 — Building effective agents

Anthropic · Fassung: 2024-12-19 · Datum: 2024-12-19 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Unterscheidet vordefinierte Workflows und modellgesteuerte Agenten. Einfachheit ist eine Ausgangsentscheidung, keine universelle Rangfolge. [Originalquelle](https://www.anthropic.com/engineering/building-effective-agents)

### D07 — Effective context engineering for AI agents

Anthropic · Fassung: 2025-09-29 · Datum: 2025-09-29 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Aufgabengerechter Kontext, Abruf und Verdichtung. Zusammenfassungen ersetzen keinen autoritativen Workflowzustand. [Originalquelle](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### D08 — Writing effective tools for agents

Anthropic · Fassung: 2025-09-11 · Datum: 2025-09-11 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Werkzeugnamen, Argumente und verwertbare Rückmeldungen als Designparameter. Verbesserung sollte anhand echter Aufgaben gemessen werden. [Originalquelle](https://www.anthropic.com/engineering/writing-tools-for-agents)

### D09 — Managed agents

Anthropic · Fassung: 2026-04-08 · Datum: 2026-04-08 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Trennung von Sitzung, Harness, Modell und Ausführungsumgebung. Anbieterarchitektur als Erfahrung, keine vorgeschriebene Plattform. [Originalquelle](https://www.anthropic.com/engineering/managed-agents)

### D10 — LangGraph: Persistence

LangChain · Fassung: Live-Dokumentation, abgerufen 2026-10-13 · Datum: Live-Dokumentation, abgerufen 2026-10-13 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Checkpoints und persistente Speicher unterscheiden sich von RAM-Speichern. Persistenz benötigt gewählten Backend- und Retentionsvertrag. [Originalquelle](https://docs.langchain.com/oss/python/langgraph/persistence)

### D11 — LangGraph: Interrupts

LangChain · Fassung: Live-Dokumentation, abgerufen 2026-10-13 · Datum: Live-Dokumentation, abgerufen 2026-10-13 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Unterbrochene Nodes werden beim Resume erneut begonnen. Vorherige Nebenwirkungen müssen gegen Wiederholung abgesichert werden. [Originalquelle](https://docs.langchain.com/oss/python/langgraph/interrupts)

### D12 — Temporal Workflow Execution overview

Temporal · Fassung: Live-Dokumentation, abgerufen 2026-10-13 · Datum: Live-Dokumentation, abgerufen 2026-10-13 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Workflow-Replay prüft Commands gegen gespeicherte Ereignishistorie. Rekonstruktion ist keine erneute identische LLM-Generierung. [Originalquelle](https://docs.temporal.io/workflow-execution)

### D13 — What is a Temporal Activity?

Temporal · Fassung: Live-Dokumentation, abgerufen 2026-10-13 · Datum: Live-Dokumentation, abgerufen 2026-10-13 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Activities dürfen nichtdeterministisch sein und werden bei Fehlern wiederholt. Idempotenz bleibt Aufgabe der externen Aktion. [Originalquelle](https://docs.temporal.io/activities)

### D14 — Open Policy Agent: Introduction

OPA · Fassung: Live-Dokumentation, abgerufen 2026-10-13 · Datum: Live-Dokumentation, abgerufen 2026-10-13 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Trennt Policyentscheidung und Durchsetzung. Der aufrufende Effektpfad muss das Ergebnis tatsächlich beachten. [Originalquelle](https://www.openpolicyagent.org/docs)

### D15 — What is Cedar?

Cedar · Fassung: Dokumentationsstand 4.5, abgerufen 2026-10-13 · Datum: Dokumentationsstand 4.5, abgerufen 2026-10-13 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Autorisierung über Principal, Action, Resource und Context. Schema validiert Policies; Laufzeitdaten brauchen einen separaten Vertrag. [Originalquelle](https://docs.cedarpolicy.com/)

### D16 — SLSA Build: Provenance

SLSA · Fassung: Spezifikation v1.2, abgerufen 2026-10-13 · Datum: Spezifikation v1.2, abgerufen 2026-10-13 · Prüfung: relevante Artikel-/Dokumentationspassagen.

Verifizierbare Zuordnung von Builder, Inputs und Outputs. Vollständigkeit der Dependencies bleibt begrenzt; Provenance ersetzt keine Qualitätsprüfung. [Originalquelle](https://slsa.dev/spec/v1.2/build-provenance)
