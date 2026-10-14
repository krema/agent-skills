# Autorenreview der Entscheidungsregeln

**14.10.2026, Fassung 1.** Die Requests und Gradingkriterien wurden vor diesem Review angelegt. Der Autor kennt die Regeln und Kriterien; dies ist **keine unabhängige Ausführungsprüfung eines frischen Agenten**. Geprüft werden die Entscheidungsabdeckung und konkrete Auditbelege. Die Codefixture wurde tatsächlich mit Python ausgeführt, hat aber ausschließlich speicherinterne Effekte.

## C01 — Begrenzter Buildreparatur-Harness

Ein angemessener Entwurf erfasst den autorisierten Workspace, den aktuellen Kandidaten und vorhandene Build-/Testergebnisse. Die Arbeitsschleife erzeugt Änderungen, führt passende Prüfungen aus und verwendet deren Fehler zur Reparatur. Ein Kandidatenwechsel entwertet betroffene Ergebnisse. Das Budget folgt der gegebenen Aufgabe; bei Ausschöpfung bleibt der Kandidat ungelöst. Ein erfolgreicher, nachweisgebundener Abschluss und ein fehlgeschlagener Durchlauf benötigen weder neue Veröffentlichungsrechte noch zusätzliche Rollen. R01/R05/R06 tragen diese Entscheidungen ohne eine vollständige Plattform vorzuschreiben.

**Reviewurteil:** Die Anweisungen erlauben eine angemessene einfache Lösung. Die tatsächliche Followability eines neuen Testworkers bleibt ungeprüft.

## C02 — Audit mit tatsächlich ausgeführter Fixture

Die Ausführung beobachtete fünf Fälle. Der normale positive Report erzeugt einen speicherinternen Effekt; der negative Report erzeugt keinen. `other_subject` veröffentlicht C2 mit einem Report zu C1. `caller_report` veröffentlicht einen Kandidaten mit dem vom Aufrufer stammenden Report. `alternate_path` veröffentlicht C3 direkt, ohne den Dispatcher.

Die Ursachen sind konkret: `dispatch()` benutzt nur `passed`, keine Gegenstandsprüfung und keine verifizierte Herkunft. `Executor.publish()` ist direkt aufrufbar. Das bloße Vergleichen einer Ausstellerzeichenkette wäre noch keine Authentifizierung. Ein Verbesserungsweg muss die relevanten Effekte vermitteln, den Beleg an den aktuellen Kandidaten binden und die Ausstellerautorität passend zur echten Vertrauensgrenze prüfen. Die positive und negative Kontrolle bleiben relevant; sämtliche tatsächlichen Effekte hier sind nur Listeneinträge.

**Reviewurteil:** Die Fixture liefert nachvollziehbare Belege für die R04/R05-Entscheidungen. Der beobachtete Fixturelauf ist kein Nachweis, dass ein frischer Agent den Skill korrekt anwenden würde.

## C03 — Garantie unter Temperatur, Schema und Voting

Eine belastbare Antwort trennt reproduzierbare Controllerentscheidungen von neuer Modellgenerierung und fachlicher Korrektheit. Strukturbedingungen des Schemas und gemeinsame Fehler der Reviewer bleiben eigenständige Grenzen. Passende externe Prüfer können definierte Eigenschaften absichern; ein korrekt übersetztes formales Modell und sounde Prüfungen sind Annahmen. 100% Accuracy für beliebige Entwicklungsaufgaben ist aus den gegebenen Mechanismen nicht ableitbar. R02/R03/R06/R08 enthalten diese Qualifikation im operativen Text.

**Reviewurteil:** Keine unbedingte Garantie aus den Fallangaben; aktuelle empirische Modellwirkung und Followability sind nicht gemessen.

## C04 — Tuning auf bekannten Aufgaben

Die gegebenen Resultate zeigen 14 gegenüber 17 Erfolgen unter 20 bereits verwendeten Aufgaben. Die besten 40 Varianten wurden auf derselben Menge gewählt. Das Ergebnis kann als beobachteter Such-/Tuningeffekt beschrieben werden, ohne einen unabhängigen Transfertest oder ein Konfidenzintervall zu erfinden. Als nächster Schritt eignen sich bislang unbenutzte Aufgaben, dokumentierte Vergleichsbedingungen und dem Entscheidungsbedarf angemessene Wiederholungen einschließlich Suchkosten. R09 und die Evaluationsreferenz unterscheiden diese Ebenen.

**Reviewurteil:** Die instruktionale Begrenzung der Generalisierung ist vorhanden; ein gematchter Versuch wurde hier nicht durchgeführt.

## C05 — Recovery aus statischen Operationen

A ist gemäß dem Protokoll bestätigt und benötigt keine erneute Wirkung. B bleibt nach Verbindungsverlust unklar; ein später autorisierter Abgleich muss zwischen bereits erfolgter Wirkung und sicher erneut ausführbarer Operation unterscheiden. C ist unter der gegebenen, autoritativ vorausgesetzten Protokollsemantik noch nicht versendet; eine Fortsetzung müsste ihre Reservierung und geltende Autorisierung beachten. D bleibt unklar, und ein maschinenlokaler Lock schützt nicht vor einem zweiten Rechner. Für B/D darf eine unbekannte Idempotenzsemantik nicht als Zusage behandelt werden. Die Beratung braucht keinen Liveaufruf und keine neue Genehmigungszeremonie.

**Reviewurteil:** R01/R07 liefern einen Entwurf innerhalb des beauftragten Scopes; reale Remoteverträge und Recoveryausführung wurden nicht geprüft.

## C06 — Fehlerverlust nach Verdichtung

Die begrenzte Änderung hält offene Testfehler mit Kandidatenbezug autoritativ fest und projiziert sie in den nächsten Schritt. Eine Prüfung setzt mit offenem Fehler den Kontext zurück und verlangt, dass ein unbelegter Abschluss weiterhin erkannt wird. Nach einer passenden erfolgreichen Prüfung darf der Blocker aufgelöst werden; nach einer relevanten neuen Änderung ist die Gültigkeit erneut zu beurteilen. Ein großes Agententeam oder Frameworkwechsel ist damit nicht begründet. R07/R08 erlauben diese kleine Intervention und eine zum Problem passende Evaluation.

**Reviewurteil:** Scope und Gegenfälle sind ausreichend ausdrückbar. Ein laufender Agententest zum tatsächlichen Kontextverlust bleibt offen.

## Gesamturteil

Alle sechs Fälle wurden als Autorenreview abgedeckt; die Codefixture bestätigt ihre beschriebenen lokalen Beobachtungen. Es gibt **keine unabhängigen Agententrials, keinen Baseline-/Revisedvergleich und keinen Downstreamnachweis** für diese Skillfassung. Die vorgeschlagenen Entscheidungen sind strukturell und argumentativ überprüft, ihre tatsächliche Befolgung durch einen frischen Agenten bleibt ungetestet.
