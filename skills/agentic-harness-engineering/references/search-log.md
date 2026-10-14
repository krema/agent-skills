# Forschungsumfang und Auswahl

**Quellenzugriff: 13.10.2026. Verallgemeinerung zum Skill: 14.10.2026.** Die Fragestellung betrifft Methoden, mit denen Harnesses für agentische Entwicklung verlässlich steuern, Regeln wirksam durchsetzen, fachliche Ergebnisse prüfen und lange Abläufe fortsetzen können. Lokale Projektpräferenzen und Codeauditbefunde wurden nicht als allgemeine Skillpflicht übernommen.

Die Recherche ist eine gezielte narrative Synthese mit verfolgten Originalzitaten, Versionsprüfung und Gegenbefunden. Sie ist kein vorregistrierter systematischer Review. Suchsnippets und fremde Zusammenfassungen dienten der Entdeckung, nicht als Ersatz für die angegebene Inspektionstiefe. Der Katalog zählt nur tatsächlich an Abstract/Metadaten beziehungsweise relevanten Passagen geprüfte Dokumente.

## Suchstränge

| Strang | Begriffe und Titelvarianten | Quellenfamilien |
|---|---|---|
| Entwicklungsagenten und Interfaces | SWE-agent, Agentless, SWE-Search, CodeAct, OpenHands, AutoCodeRover | P01–P04, P45, P58–P59 |
| Regeln und Garantien | runtime enforcement, AgentSpec, FORGE/PCAS, AgentC, VIGIL, Progent, CaMeL, enforceable security policies | P17–P19, P31–P39, P44, P46–P49 |
| Qualität und Prüforakel | instruction following, constrained decoding, JSONSchemaBench, external critique, EvalPlus, DSPy Assertions | P06–P09, P20–P25, P40–P41, P68, P72 |
| Planung und Zerlegung | LLMCompiler, ADaPT, LATS, LLM+P, PlanBench, LLM-Modulo | P54–P56, P62–P65 |
| Kontinuität und Kontext | long-running agent harness, context engineering, OpenHands SDK, workflow memory, AGENTS.md, AgentOccam | P22, P51, P57, P66, P69; Runtime-/Engineeringdokumente |
| Evaluation und Gegenbefunde | tau-bench/pass^k, Harness-Bench, MTAC-IFBench, long software tasks, agent failures, infrastructure noise | P10–P16, P27–P30, P42–P43, P67 |
| Harnesslernen und portable Policy | HarnessFix, MemoHarness, AFlow, Meta-Harness, Natural-Language Agent Harnesses, Self-Healing Harness | P35, P52–P53, P70, P74–P75 |
| Taxonomie und Reporting | agent harness engineering survey, Control Agency Runtime, HarnessCard | S01–S04 |

Die erste Recherche erfasste 65 Dokumente, eine weitere literaturzentrierte Sichtung ergänzte 30. Für die Skillfassung wurden daraus die allgemeinen Entscheidungsbedingungen abgeleitet; es wurden keine neuen Wirksamkeitsmessungen oder Quellenzugriffe am 14.10.2026 behauptet. Die Suchstränge sind eine Übersicht, keine vollständige Aufzeichnung aller Requests.

Wichtige Methodensichtungen betreffen Monitorannahmen, Orakelabdeckung, Replay-/Retryverträge, empirische Vergleichsbedingungen und Generalisierung. Hinweise auf ein bestimmtes Modell oder eine Plattform gelten für die dokumentierte Fassung, nicht automatisch für heutige APIs oder jedes andere Modell.

## Versionen und Widersprüche

AGENTS.md **2602.11988v3** verwendet CTXbench und andere Schlussfolgerungsformulierungen als ältere Fassungen. FORGE **2602.16708v3** ist von früheren PCAS-Fassungen zu unterscheiden. HarnessFix **2606.06324v2**, NLAH **2603.25723v2** und OpenHands SDK **2511.03690v2** sind im Katalog fixiert.

Bei Harness-Bench galt die Paperfassung mit 106 Aufgaben, acht Kategorien und 5.194 Traces; Websitezahlen wichen ab. OpenHands SDK nennt eine maximale Crash-Recovery-Latenz in der Tabelle, die einer Textaussage widerspricht. P32 hat eine dokumentierte Datumsauffälligkeit und trägt keine zentrale Skillregel. S02 ist ein unversioniertes Autoren-PDF ohne zuverlässig festgestelltes Veröffentlichungsdatum. Diese Einschränkungen werden nicht durch das Erstellungsdatum des Skills behoben.

## Zugang und Abdeckung

OpenReviewseiten zu S01/S02 zeigten eine Browserprüfung. S02 war als öffentliches Autoren-PDF zugänglich; für S01 wurden Journalmetadaten und Abstract geprüft. Die [MDPI-Seite zu ReliHarness](https://www.mdpi.com/2079-9292/15/18/4166) blieb über das verwendete Webwerkzeug unzugänglich und wurde nicht zu den 95 Quellen gezählt.

Die Auswahl bevorzugt öffentlich zugängliche, überwiegend englischsprachige Quellen und Software-/Terminalaufgaben. Proprietäre Implementierungen, sämtliche traditionellen Lehrbücher und jede neuere Einzelstudie sind nicht vollständig abgedeckt. Surveys helfen zur Einordnung; ihre Literaturverzeichnisse wurden nicht als eigene Volltextlektüre gezählt. Forschung wurde beendet, als wesentliche Entscheidungen unterstützt oder verbleibende Unsicherheit ausdrücklich dokumentiert war.
