---
name: agentic-harness-engineering
description: Entwirf, prüfe oder verbessere Harnesses für agentische Softwareentwicklung anhand von Forschung zu Lifecyclekontrolle, Regeldurchsetzung, Ausführungszuverlässigkeit und fachlicher Qualität. Verwende den Skill bei Harnessarchitektur, Harnessaudits oder konkreten Zuverlässigkeitsproblemen agentischer Entwicklungsabläufe.
---

# Agentic Harness Engineering

Überführe ein Harnessziel in ausführbare Entscheidungen und überprüfbare Ergebnisse. Ein Harness organisiert Modellaufrufe, Werkzeuge, Kontext, Zustand, Prüfungen und Aktionen. Die Anleitung gilt für unterschiedliche eigene Harnesses, Frameworks und Softwareagenten; sie setzt keine bestimmte Plattform, Repositorystruktur oder Freigabefolge voraus.

## Auftrag und Ziel bestimmen

**R01 — Arbeite im beauftragten Modus:** Beratung/Entwurf, Audit oder Implementierung. Nutze vorhandene Aufgaben, Artefakte und Autorisierungen. Bei einem Audit untersuche die tatsächlichen Aufruf- und Datenpfade; kennzeichne nicht prüfbare Teile. Implementiere nur im angefragten Umfang und bewahre vorhandene Verträge. Leite aus dem Skill keine zusätzlichen menschlichen Freigaben, Installation oder externen Aktionen ab.

**R02 — Trenne die Ziele:** deterministische Controllerentscheidungen, Replay gespeicherter Ereignisse, reproduzierbare Neuausführung, Regelkonformität und fachlicher Task-Erfolg. Frage nur nach fehlenden Angaben, die die Entscheidung verändern. Ein neuer Modellaufruf oder eine veränderte Außenwelt ist kein Replay. Ein JSONschema, Temperatur 0 oder Mehrheitsvoting beweist keine fachliche Richtigkeit.

Bestimme die relevante Aufgabe, Fehlerklasse, zulässigen Wirkungen und beobachtbaren Erfolgsbedingungen. Bei bekannten Abläufen ist eine einfache Pipeline eine geeignete Vergleichsbasis; bei offenen Aufgaben darf Lösungssuche flexibel bleiben. Eine kleine Beratung erfordert keinen vollständigen Controllerneubau.

## Regeln und Prüfung platzieren

**R03 — Klassifiziere Anforderungen vor der Umsetzung.** Für maschinenprüfbare verbindliche Bedingungen definiere Prädikat, vertrauenswürdige Eingaben, Prüfpunkt und Fehlerentscheidung. Für Präferenzen oder modellbewertete Kriterien kennzeichne Unsicherheit. Ein deterministischer Branch auf einem LLM-Urteil garantiert die Richtigkeit des Urteils nicht. Wenn die Erfüllung einer verbindlichen Voraussetzung unbekannt ist, behandle sie nicht als erfüllt.

**R04 — Wenn Regeln relevante Aktionen verbindlich begrenzen sollen, prüfe sie am tatsächlichen Ausführungspfad.** Untersuche innerhalb des vereinbarten Bedrohungsmodells alternative Tools, Shell-, API- und delegierte Zugriffe. Ein nachträglicher Logeintrag verhindert keine Aktion. Verbleibende uninstrumentierte Wege begrenzen jede Garantie. Lies hierfür [control-and-enforcement.md](references/control-and-enforcement.md).

**R05 — Wenn ein Prüfergebnis eine spätere Aktion legitimiert, binde es an Gegenstand und Herkunft.** Prüfe den aktuellen Kandidaten beziehungsweise Ressourcenzustand, die relevanten Eingaben, Prüfspezifikation und den Belegaussteller. Nach relevanten Änderungen prüfe erneut oder begründe, welche Nachweise gültig bleiben. Hashes erkennen Änderungen; sie authentifizieren allein keinen Aussteller und beweisen keine Testqualität. Wähle die Integritätssicherung passend zur tatsächlichen Vertrauensgrenze.

**R06 — Wenn externe Prüfer verfügbar sind, verwende ihre Ergebnisse zur begrenzten Reparatur.** Compiler, Tests, Solver und Zustandsvergleiche prüfen unterschiedliche Eigenschaften. Übernimm generierte Tests oder formal übersetzte Aufgaben nicht ungeprüft als vollständiges Orakel. Bestimme eine zur Aufgabe passende Abbruchbedingung; ein ungelöster oder nicht überprüfter Kandidat bleibt als solcher erkennbar. Lies für Orakel, Suche und Kontext [quality-and-optimization.md](references/quality-and-optimization.md).

## Kontinuität und Verbesserung

**R07 — Bei langen oder wiederaufnehmbaren Läufen halte autoritativen Zustand außerhalb des Modellkontexts.** Speichere die für die Aufgabe erforderlichen Entscheidungen, Kandidatenbezüge, offenen Blocker und unklaren Wirkungen. Verwende für Replay aufgezeichnete Modellantworten und Toolresultate. Wenn Retry Außenwirkungen wiederholen könnte, kläre Operationsidentität, Remoteabgleich und Idempotenz; behaupte keine Genau-einmal-Wirkung allein wegen eines lokalen Locks. Lies [execution-and-recovery.md](references/execution-and-recovery.md).

**R08 — Wähle zusätzliche Methoden nach dem beobachteten Engpass.** Zerlegung, parallele DAGausführung, Suche, Voting, Rollen, Gedächtnis und Harnesslernen sind Optionen. Begründe ihren Einsatz und das zusätzliche Budget. Übertrage weder enge Benchmarkresultate noch eine spezielle Plattformarchitektur als universelle Pflicht. Bei neuen Situationen dürfen alternative Lösungen bestehen bleiben, wenn sie die definierten Bedingungen erfüllen.

**R09 — Prüfe Änderungen an wesentlichen Mechanismen und qualifiziere Erfolgsbehauptungen.** Verwende die relevanten Normal-, Fehler- und Grenzfälle. Für Leistungsverbesserungen vergleiche passende Baseline und Änderung bei dokumentierten Bedingungen; trenne Such-/Tuningfälle von unbenutzten Evaluationsfällen. Test-Erfolg, Fehlakzeptanz, ausgeführte Regelverstöße, blockierte zulässige Fälle, Kosten und Wiederholungsstabilität beantworten unterschiedliche Fragen. Lies [evaluation.md](references/evaluation.md), wenn du eine Änderung validierst oder Evals beurteilst.

## Ergebnis liefern

Liefere zum beauftragten Modus passende Architekturentscheidungen, konkrete Auditbefunde oder überprüfte Änderungen. Verbinde wesentliche Empfehlungen mit Auslöser, Aktion, Voraussetzung und beobachtbarem Erfolg beziehungsweise Fehler. Nenne tatsächliche Tests und verbleibende Grenzen. Stelle eine formal modellierte Eigenschaft, einen empirischen Befund und eine Engineeringhypothese nicht als dieselbe Garantie dar.

Bei strittigen Garantien, Quellenfragen oder der Übertragung eines Paperresultats lies [evidence.md](references/evidence.md); verwende [sources.md](references/sources.md) oder [sources.json](references/sources.json) zur gezielten Quellenauflösung. Der Forschungsstand ist vom **13.10.2026**. Prüfe bei einer konkreten Implementierung versionsabhängige APIverträge gegen die eingesetzte Version. Die Literatur macht weder diesen Skill noch einen damit entworfenen Harness automatisch wirksamkeitsvalidiert.
