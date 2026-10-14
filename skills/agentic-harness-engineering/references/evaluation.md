# Evaluation eines Harness oder einer Harnessänderung

**Laden bei:** Prüfung einer wesentlichen Mechanismusänderung, Benchmarkdesign, Garantiebehauptungen oder einem Audit vorhandener Evals. Grundlage: R09. Diese Anleitung bewertet Harnessverhalten; sie installiert keinen Skill und autorisiert keine externen Testwirkungen.

## Frage, Vergleich und Ergebnis vorher festlegen

Bestimme die konkrete Behauptung: verhindert ein Monitor definierte Verstöße, stellt ein Resumeprotokoll einen unterbrochenen Ablauf wieder her, erkennt ein Prüfer falsche Kandidaten oder verbessert eine Strategie den Task-Erfolg? Wähle die Prüfungen passend dazu. Ein Formatcheck ist kein Verhaltensnachweis. Eine Wirkungsmessung ist nicht für jede rein redaktionelle Änderung erforderlich.

Schreibe repräsentative Aufgaben, relevante Fehler- und Grenzfälle und eine Ergebnisrubrik, bevor die Versuche beginnen. Beurteile Ergebnisse und tatsächliche Aktionen, nicht gewünschte Formulierungen. Gültige alternative Lösungen dürfen bestehen bleiben. Bewahre erwartete Antworten außerhalb des Kontexts eines frischen Testworkers, falls ein solcher eingesetzt wird. Ein Autorenwalkthrough mit bekannter Lösung ist Designreview.

## Metriken auseinanderhalten

| Frage | Geeignete Beobachtung | Verwechslungsgefahr |
|---|---|---|
| Task richtig erledigt? | Passende Endzustände und fachliche Prüfungen. | Modell behauptet Abschluss, Orakel ist schwach. |
| Falscher Kandidat akzeptiert? | Gegenfälle, die eine relevante Bedingung verletzen. | Nur Erfolgsfälle werden getestet. |
| Regelverletzung verhindert? | Tatsächlich ausgeführte Wirkungen und abgewiesene Vorschläge getrennt. | Ein erkannter Verstoß wird als verhinderter Verstoß gezählt. |
| Erlaubte Aufgabe unnötig blockiert? | Repräsentative zulässige Gegenfälle. | Dauerhafte Verweigerung erscheint als hohe Sicherheit. |
| Zuverlässig bei Wiederholung? | Wiederholungen unter dokumentierten Bedingungen. | Einzelerfolg wird als Stabilität ausgegeben. |
| Replay korrekt? | Gespeicherte Antworten/Ereignisse rekonstruieren denselben Controllerzustand. | Ein neuer Liveaufruf wird mit Replay verwechselt. |
| Effizient? | Kosten, Laufzeit, Abbrüche und Prüfarbeit. | Der Evaluations- oder Suchaufwand wird ausgelassen. |

`pass@k` beschreibt mindestens einen Erfolg unter k Versuchen; `pass^k` Erfolg in allen k Wiederholungen. Dokumentiere Schätzer, Wiederholungsprotokoll und Taskaggregation. Beide Metriken ersetzen weder fachliche Abdeckung noch eine Untersuchung seltener Schäden.

## Passenden Testumfang wählen

Für einen deterministischen Predicate-/Controllerfix prüfe betroffene Normal-, Fehler- und Grenzfälle. Für unsichere Routing-, Kontext- oder Reparaturregeln ist eine realistische Ausführung mit tatsächlich verfügbaren Tools und Artefakten aussagekräftiger als ein statisches Durchlesen. Simulierte Interfaces prüfen nur die simulierte Semantik.

Für Leistungsbehauptungen vergleiche Baseline und Änderung bei geeigneter Modell-, Aufgaben- und Budgetkontrolle. Wiederhole ausreichend, um die für die Entscheidung relevante Varianz beurteilen zu können; begründe den Umfang statt eine universelle Versuchszahl zu verwenden. Dokumentiere beobachtete Unsicherheit. Mehrere gleichzeitig geänderte Komponenten erlauben keine einfache kausale Zuordnung zu einem einzigen Feature.

Für Generalisierung halte finale Evaluationsfälle von Suche und wiederholter Auswahl getrennt. Ein mehrfach zur Optimierung verwendeter Test ist kein unberührter Holdout mehr. Bei Onlinegedächtnis sind Reihenfolge, Zustandsinitialisierung und erlaubtes Feedback Teil des Versuchs. Wenn keine unabhängigen Fälle verfügbar sind, begrenze die Aussage auf bekannte Aufgaben und beschreibe eine spätere Transferprüfung.

## Prüfbare Grenzen und Autorisierung

Isoliere Tests von Livekonten, produktiven Ressourcen und installierten Konfigurationen, sofern deren Nutzung nicht bereits zum Auftrag gehört. Autorisierte Implementierung ist keine pauschale Erlaubnis für neue externe Wirkungen. Wenn eine benötigte Liveprüfung nicht möglich ist, liefere die übrige Arbeit und benenne die konkrete ungetestete Entscheidung.

Bewahre zur Interpretation benötigte Revisionen, Inputs, Ergebnisse, Aktionsbeobachtungen und bekannte Umgebungsbedingungen. Prüfe insbesondere die zum Mechanismus passenden Gegenfälle: veralteter Nachweis, uninstrumentierter Effektpfad, gültiges Format mit falschem Inhalt, manipuliertes Orakel, verlorene Remoteantwort, konkurrierende Worker oder Contextreset mit offenem Blocker.

Berichte separat: strukturell geprüft, durch Autorenreview geprüft, tatsächlich ausgeführt und im Downstreamvergleich wirksam. Weder Literaturzitate noch ein erfolgreicher Einzeltest legitimieren „vollständig deterministisch“, „100% Accuracy“ oder „wissenschaftlich validierter Harness“ ohne die passende, begrenzte Begründung.
