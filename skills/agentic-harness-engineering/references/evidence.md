# Evidenz und Übertragung in ausführbare Entscheidungen

**Paket erstellt: 14.10.2026. Forschungsstand und Quellenzugriff: 13.10.2026.** Ziel: allgemeiner Entwurf, Audit und Verbesserung von Harnesses für agentische Softwareentwicklung. Keine projektspezifische Repositorystruktur, Freigabefolge, Plattform oder Installation wird vorausgesetzt.

Die gezielte narrative Recherche umfasst **95 Quellen**: 79 wissenschaftliche Arbeiten einschließlich Surveys/Positionspapieren und 16 Engineering-/Dokumentationsquellen. 36 wissenschaftliche Quellen wurden an ausgewählten Volltextstellen, 43 an Abstract und Metadaten geprüft; 16 weitere an relevanten Artikel-/Dokumentationspassagen. Das ist keine vollständige Lektüre, Replikation oder exhaustive systematische Recherche. Der [Katalog](sources.md), das [JSON](sources.json) und [Suchprotokoll](search-log.md) dokumentieren Fassungen, Zugriff und Tiefe.

**EMP:** empirischer Befund im untersuchten Setup. **FORM:** Eigenschaft innerhalb eines expliziten formalen Modells. **API:** dokumentierter Interface-/Spezifikationsvertrag. **ENG:** Erfahrung oder eigene Engineeringableitung. **PREF:** Nutzerziel/Scope. Die Skillregeln sind überwiegend bedingte Engineeringableitungen mit diesen Grundlagen. ArXiv-Metadaten allein belegen kein Peer Review; Begutachtungsstatus und unabhängige Replikation aller Arbeiten wurden nicht verifiziert.

## Abgedeckte Entscheidungen

| Frage | Untersuchte Stränge | Übertragung / offene Grenze |
|---|---|---|
| Wo gehört Steuerung hin? | Pipeline, adaptive Zerlegung, DAG, symbolische Planung. | Bekannte Voraussetzungen können in Code liegen; offene Lösungssuche braucht Spielraum. |
| Wie werden Regeln wirksam? | Runtime Enforcement, Privilegien, Datenfluss, klassische Securitymonitore. | Garantie setzt passende Fakten und vermittelte Effektpfade voraus. |
| Wie verbessert sich fachliche Qualität? | Testorakel, externe Kritik, Suche, Tooldesign, Kontext. | Keine universelle Accuracysteigerung eines einzelnen Verfahrens. |
| Wie bleiben lange Läufe nachvollziehbar? | Ereignisorientierte Runtime, Checkpoints, Retry und Idempotenz. | Persistenz beweist weder identische Neuausführung noch globale Genau-einmal-Wirkung. |
| Wie kann der Harness lernen? | Workflowsuche, Codeoptimierung, Diagnosen, Erfahrungsbanken. | Tuningeffekt und Transfer müssen getrennt beurteilt werden. |

## E01 — Ein einfacher Kontrollkern lässt adaptive Arbeit zu

[P02](https://arxiv.org/abs/2407.01489v2) (2407.01489v2, 29.10.2024), [P04](https://arxiv.org/abs/2410.20285v6) (2410.20285v6) und [P55](https://arxiv.org/abs/2311.05772v2) (2311.05772v2, 08.04.2024); Architektur-/Methodenstellen selektiv geprüft, EMP/ENG. Pipeline und Suche sind unterschiedliche Interventionen mit unterschiedlichen Budgets. ADaPT benutzt eine LLM-Erfolgsheuristik. **Skillfolge:** bekannte Übergänge typisieren, wenn das Ziel sie verlangt; autonome Innenarbeit und passende Alternativen erhalten. Keine Pflicht zu einem universellen Zustandsautomaten.

## E02 — Garantien enden am Beobachtungs- und Ausführungsmodell

[P46](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)/[P47](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html) (klassische Monitorliteratur), [P36](https://arxiv.org/abs/2503.18666v3) (2503.18666v3), [P37](https://arxiv.org/abs/2602.16708v3) (2602.16708v3), [P38](https://arxiv.org/abs/2512.23738v1) (2512.23738v1) und [P44](https://arxiv.org/abs/2504.11703v3) (2504.11703v3); relevante Mechanismen und Grenzen selektiv geprüft, FORM/EMP/ENG. Korrekte Fakten und wirksame Instrumentierung sind Voraussetzungen. Unbeobachtete Kommunikation und modellbasierte Checks begrenzen Garantien. **Skillfolge:** tatsächliche relevante Effektpfade prüfen und ungeschützte Bereiche offenlegen.

## E03 — Richtige Struktur ist nur eine Prüfebene

[P25](https://arxiv.org/abs/2501.10868v3) (2501.10868v3), [P20](https://arxiv.org/abs/2311.07911v1)/[P21](https://arxiv.org/abs/2507.02833v3) sowie [P40](https://arxiv.org/abs/2609.23742v1)/[P41](https://arxiv.org/abs/2607.18357v1); Abstract-/Metadatenprüfung. [P68](https://arxiv.org/abs/2312.13382v2) (2312.13382v2, 02.02.2024): Semantik und Beispiele selektiv geprüft, EMP/ENG. Assert kann nach Reparaturbudget abbrechen, Suggest weiterlaufen; Prädikate können selbst ein LLM verwenden. **Skillfolge:** syntaktische, semantische und verbindliche Bedingungen trennen; das Urteil eines Judges bleibt kein formaler Wahrheitsbeweis.

## E04 — Externe Orakel sind nützlich, aber abdeckungsgebunden

[P65](https://arxiv.org/abs/2411.14484v1) (2411.14484v1, 20.11.2024), §3–4, und [P72](https://arxiv.org/abs/2305.01210v3) (2305.01210v3, 30.10.2023), Testverfahren/Orakel selektiv geprüft, EMP/FORM/ENG. Schedulingprüfer setzen vollständige Aufgabenbedingungen voraus; Differential Testing setzt Referenz und Eingabedomäne voraus. [P08](https://arxiv.org/abs/2310.01798v2)/[P09](https://arxiv.org/abs/2305.11738v4) liefern gegenläufige Hinweise zu intrinsischer beziehungsweise toolgestützter Korrektur. **Skillfolge:** Akzeptanz an passende Prüfer binden, Übersetzung und Prüfabdeckung nicht als gegeben behandeln; erfolglose Suche bleibt möglich.

## E05 — Herkunft ist keine fachliche Qualität

[P48](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) (in-toto, 2019) und [D16](https://slsa.dev/spec/v1.2/build-provenance) (SLSA v1.2): relevante Provenancepassagen geprüft, API/ENG. Herkunftsbeziehungen helfen, Resultate an Artefakte und Aussteller zu binden. Sie machen ein unzureichendes Orakel nicht vollständig. **Skillfolge:** Gegenstand, relevante Inputs und Aussteller passend zur Vertrauensgrenze prüfen; keine allgemeine Signaturpflicht für jeden lokalen Ablauf.

## E06 — Runtimezuverlässigkeit und Task-Erfolg sind verschiedene Größen

[P51](https://arxiv.org/abs/2511.03690v2) (2511.03690v2, 22.04.2026), §4–5 und Limitationen selektiv geprüft, beobachtend/EMP/ENG. Der Produktionsvergleich bündelt Änderungen und schließt Providerfehler aus. Tabelle 3 nennt maximal 32,1 ms Crash Recovery, entgegen einer Textaussage unter 20 ms. **Skillfolge:** Zustand und Ereignisse als Architekturoption nutzen; keine kausale Accuracy- oder allgemeine Latenzzusage daraus ableiten.

## E07 — Wiederaufnahme kann Operationen wiederholen

[D10](https://docs.langchain.com/oss/python/langgraph/persistence)–[D13](https://docs.temporal.io/activities): Live-Dokumentationspassagen am 13.10.2026 geprüft, API/ENG. Persistenz, Interrupt-Resume und Activity-Retry haben unterschiedliche Verträge. Erneute Ausführung kann Idempotenz erfordern. **Skillfolge:** bei der tatsächlich eingesetzten Version den Wiederholpunkt prüfen; unklare Remoteeffekte zuerst abgleichen. Lokale Locks und persistierte Historie allein beweisen keine globale Genau-einmal-Semantik.

## E08 — Mehr Information oder Rollen helfen nicht pauschal

[P01](https://arxiv.org/abs/2405.15793v3) und [P57](https://arxiv.org/abs/2409.07429v1): Interface-/Gedächtnismethoden selektiv geprüft. [P45](https://arxiv.org/abs/2402.01030v4), [P42](https://arxiv.org/abs/2503.13657v3) und [P69](https://arxiv.org/abs/2410.13825v2): Abstract/Metadaten. [P66](https://arxiv.org/abs/2602.11988v3) (2602.11988v3, 29.09.2026), §3–4 selektiv geprüft, EMP/ENG. Kontextdateien zeigen gegenüber None keinen signifikanten allgemeinen Erfolgsgewinn; Entwicklerdateien übertreffen generierte Dateien. **Skillfolge:** Informationen und Methoden nach dem Engpass wählen; knappe Pipeline bleibt Vergleichsbasis, weder generelles Verbot noch Pflicht zusätzlicher Anweisungen.

## E09 — Lange fehlerfreie Beispiele sind aufgabenabhängig

[P50](https://arxiv.org/abs/2511.09030v1) (2511.09030v1, 12.11.2025), Zerlegung/Voting und Grenzen selektiv geprüft. [P73](https://arxiv.org/abs/2203.11171v4) (2203.11171v4) und [P56](https://arxiv.org/abs/2310.04406v3) (2310.04406v3): Abstract/Metadaten, EMP/ENG. MAKER nutzt eine vorgegebene repetitive Hanoi-Zerlegung und besondere Fehlerbedingungen. **Skillfolge:** Suche und Voting nur mit begründetem Budget und geeigneter Auswahl prüfen; ein klassischer Algorithmus bleibt Alternative für exakt berechenbare Aufgaben.

## E10 — Harnessoptimierung braucht getrennte Transferprüfung

[P35](https://arxiv.org/abs/2609.24130v1), [P52](https://arxiv.org/abs/2606.06324v2) (2606.06324v2), [P53](https://arxiv.org/abs/2607.14159v1) (2607.14159v1), [P70](https://arxiv.org/abs/2410.10762v4) (2410.10762v4), [P74](https://arxiv.org/abs/2603.28052v1) (2603.28052v1); Verfahren und relevante Evaluationsgrenzen selektiv geprüft, EMP/ENG. HarnessFix trennt Datensplits; MemoHarness hat kleine primäre Holdouts und fehlende Unsicherheitsintervalle. Meta-Harness verwendet für Terminal-Bench dieselben Such-/Testaufgaben. **Skillfolge:** Verbesserung auf bekannten Fällen nicht als allgemeine Wirksamkeit ausgeben; Regression und Transfer separat prüfen.

## E11 — Portable Textpolicy braucht ausgeführte Mechanismen

[P75](https://arxiv.org/abs/2603.25723v2) (2603.25723v2, 18.05.2026), Mechanismusaufteilung und Appendix G selektiv geprüft, EMP/ENG. Text kann wichtige Bedeutung verlieren oder unterschiedlich interpretiert werden; exakte Mechanismen bleiben im Code. [S02](https://picrew.github.io/LLM-Harness/main.pdf)–[S04](https://www.preprints.org/manuscript/202603.1756) liefern deskriptive Taxonomien/Reporting. **Skillfolge:** Policytext als überprüfbares Artefakt nutzen; eine Beschreibung von Regeln ist keine Beobachtung ihrer tatsächlichen Durchsetzung.

## Evidenz zu Verhalten

| Regel | Bedingte Aktion und Begründung | Gegengewicht / Fallback | Beobachtbarer Abschluss |
|---|---|---|---|
| R01 | Modus und bestehenden Scope erhalten; PREF/ENG. | Allgemeine Anleitung legt keine Projektfreigaben fest. | Artefakte und tatsächliche Änderungen passen zum Auftrag. |
| R02 | Unterschiedliche Zuverlässigkeitsziele trennen; E03/E06/E07, ENG. | Ohne neues Experiment keine Downstreamzusage. | Report benennt geprüfte Eigenschaft und Grenze. |
| R03 | Verbindliche prüfbare Bedingungen technisch ausdrücken; E02/E03. | Für semantische Kriterien Unsicherheit und andere Orakel. | Verletzung oder unbekannte Voraussetzung legitimiert keine positive Transition. |
| R04 | Relevante Wirkung am echten Pfad vermitteln; E02. | Begrenztes Bedrohungsmodell offenlegen. | Bypassversuch und zulässiger Fall an der tatsächlichen Grenze prüfen. |
| R05 | Legitimierenden Beleg an Gegenstand/Herkunft binden; E05. | Mechanismus passend zur Vertrauensgrenze wählen. | Veralteter oder manipuliert ausgestellter Beleg wird erkannt. |
| R06 | Externe Prüfung zur Reparatur verwenden, wenn verfügbar; E04. | Schwaches Orakel nicht als vollständig behandeln. | Falscher Kandidat scheitert; Budgetende bleibt ungelöst. |
| R07 | Lange wiederaufnehmbare Arbeit persistent repräsentieren; E06/E07. | Kurze einfache Aufgaben brauchen keine unnötige Infrastruktur. | Reset/Crash erhält relevante Tatsachen und unklare Wirkungen. |
| R08 | Methode nach Engpass und Budget wählen; E01/E08/E09/E10. | Einfache Baseline oder deterministischer Solver bleiben zulässig. | Vergleich rechtfertigt die zusätzliche Methode oder begrenzt die Hypothese. |
| R09 | Relevante Wirkung testen und Aussagen qualifizieren; E10, [P10](https://arxiv.org/abs/2406.12045v1)/[P43](https://arxiv.org/abs/2407.01502v1). | Bei fehlenden Live-/Holdoutversuchen die Behauptung begrenzen. | Tatsächlich ausgeführte Checks und nicht geprüfte Wirkung sind getrennt dokumentiert. |

## Konfidenz, Lücken und Aktualisierung

Hohe konzeptionelle Sicherheit besteht bei der Trennung von Format, fachlicher Prüfung, Effektgrenze und Belegvertrauen. Mittlere Übertragungssicherheit besteht für bestimmte Kontext-, Tool- und Reparaturstrategien. Ein universeller Nutzen zusätzlicher Rollen oder selbstoptimierender Harnesses ist nicht belegt. Dieses Paket wurde nicht durch einen Downstreamvergleich empirisch wirksamkeitsvalidiert.

Neue relevante Modelle, Runtime-/APIverträge, gegenläufige Studien, Fehler in der Faktenextraktion oder ein anderes Bedrohungsmodell begründen eine gezielte Aktualisierung betroffener Regeln und Evals. Der Skill legt dafür keinen automatischen Zeitplan an. Die Validierung dieser Fassung steht in [validation.md](../evals/validation.md).
