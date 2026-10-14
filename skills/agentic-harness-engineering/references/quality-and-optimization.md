# Fachliche Qualität und Auswahl von Methoden

**Laden bei:** Accuracyproblemen, falschen Abschlüssen, Toolfehlern, Kontextproblemen oder der Auswahl von Zerlegung, Suche, Rollen und Lernverfahren. Grundlage: R06/R08. Die Quellenbewertung steht in [evidence.md](evidence.md), das Messverfahren in [evaluation.md](evaluation.md).

## Das Orakel vor der zusätzlichen Schleife prüfen

Verknüpfe die erwartete Eigenschaft mit einer tatsächlichen Prüfung. Tests decken untersuchte Inputs ab; Typ- und Schemaprüfungen decken andere Bedingungen ab; formal sounde Prüfer gelten für ihr korrekt spezifiziertes Modell. Ein bestandener Prüfschritt ist nur ein Nachweis für seine erfassten Bedingungen.

Bei generierten Tests prüfe, ob sie auf dem fehlerhaften Ausgangszustand scheitern und auf einer gültigen Lösung bestehen, sofern diese Kontrolle verfügbar ist. Prüfe zusätzlich, ob sie an eine einzelne Implementierung überangepasst sind. Für relevante Eingabedomänen helfen gezielte Grenzfälle, Property-/Differential Testing oder andere passende Orakel. Eine Referenzlösung kann selbst falsch oder unvollständig sein; benenne diese Annahme.

Bei Planern prüfe, ob formale Repräsentation, initialer Zustand und Ressourcen die fachliche Aufgabe erfassen. Die Korrektheit eines Solveroutputs ersetzt keine korrekte Übersetzung. Bei einem LLM-Judge berücksichtige Fehlbewertungen und gemeinsame Modellfehler; mehrere Rollen ergeben keine automatische Prüferunabhängigkeit.

## Reparatur durch konkretes Feedback steuern

Lass Kandidaten erzeugen, tatsächlich prüfen und anhand identifizierter Fehler verbessern. Wenn nur Selbstkritik verfügbar ist, kennzeichne die Schleife als Heuristik. Unterscheide eine verbindliche Assertion von einer Empfehlung, bei der Weiterarbeit erlaubt ist. Nach ausgeschöpftem Budget bleiben harte unbewiesene Bedingungen offen; ein weicher Wunsch darf je nach Auftrag mit dokumentierter Einschränkung ungelöst bleiben.

Wenn ein Kandidat seinen Prüfer verändern kann, trenne die Bewertung vom Kandidaten oder sichere die relevanten Prüfspezifikationen. Mehr Reparaturversuche an einem schwachen Orakel können dessen Lücken ausnutzen. Beobachte Fehlakzeptanz neben erfolgreicher Reparatur.

## Methode passend zum Engpass wählen

| Beobachtung | Zu prüfende Methode | Bedingung / Gegenhypothese |
|---|---|---|
| Ungültige Toolinputs | Typisierte Eingaben, Schema/Grammatik und bessere Fehlerrückmeldung. | Semantische Werte bleiben separat zu prüfen. |
| Schwierige Navigation oder Änderungen | Aufgabegeeignete Such-, Editier- und Beobachtungsinterfaces. | Zu enge Werkzeuge können nötige Ausdruckskraft verlieren. |
| Schwieriger Teil einer ansonsten lösbaren Aufgabe | Adaptive Zerlegung mit prüfbaren Teilzielen. | Zerlegung kann falsche Abhängigkeiten oder Abschlussheuristiken erzeugen. |
| Unabhängige Schritte dominieren Laufzeit | Geprüfter DAG und paralleles Scheduling. | Wirklich abhängige oder konfligierende Schritte dürfen nicht parallelisiert werden. |
| Mehrere plausible Lösungskandidaten | Budgetierte Suche, Sampling und geeignete Auswahlprüfung. | Korrelierte Fehler und ungeeignete Wertfunktionen können zusätzliche Suche entwerten. |
| Kontextverlust | Gezielte Kontextprojektion und dauerhafter Arbeitszustand. | Mehr Text oder starke Verdichtung können selbst Nachteile haben. |
| Wiederkehrende Teilabläufe | Begrenzte Wiederverwendung von Erfahrungen. | Veraltete oder falsche Erinnerungen müssen revidierbar bleiben. |
| Spezialisierte Information oder unabhängige Beurteilung fehlt | Zusätzliche Rolle mit klaren Inputs und Zuständigkeiten. | Eine einfache Pipeline bleibt Vergleichsbasis; Koordination kostet Ressourcen. |
| Wiederkehrender Harnessfehler mit brauchbaren Traces | Begrenzte Harnessreparatur oder Workflowoptimierung. | Ohne getrennte Evals kann nur an bekannte Aufgaben angepasst werden. |

Die Tabelle beschreibt mögliche Interventionen, keine automatische Eskalationsfolge. Wähle die kleinste plausible Änderung, die den beobachteten Fehler adressiert. Bei einer bereits exakt berechenbaren Aufgabe verwende einen geeigneten klassischen Algorithmus als Alternative oder Baseline.

## Grenzen der Generalisierung

MAKERs langer fehlerfreier Ablauf beruht auf einer engen, vorgegeben zerlegbaren Aufgabe; daraus folgt kein Anspruch auf beliebige Softwarekorrektheit. Mehrheitsvoting benötigt günstige Fehlerbedingungen und ein angemessenes Auswahlverfahren. AGENTS.md v3 spricht gegen einen pauschalen Erfolgsgewinn zusätzlicher Kontextdateien, nicht gegen jede nützliche Repositoryanweisung.

Bei Harnesslernen speichere Fehlerkontext, Änderung und tatsächliche Ergebnisse, damit eine Verbesserung nachvollziehbar bleibt. Behalte einen getrennten Einführungsweg für Änderungen an verbindlichen Grenzmechanismen. Onlineanpassung einer Strategie ist nicht gleichbedeutend mit autorisiertem Umschreiben der eigenen Berechtigungen. Vergleiche Verbesserungen und geschützte Gegenfälle auf getrennten, bislang nicht zur Optimierung genutzten Aufgaben, wenn Generalisierung behauptet wird.
