# Zustand, Kontext, Replay und Wiederaufnahme

**Laden bei:** langen Sitzungen, Kontextverlust, Abbruch/Wiederaufnahme, konkurrierenden Workern oder wiederholbaren Außenwirkungen. Grundlage: R07; [evidence.md](evidence.md) enthält Quellen und Verträge.

## Autoritativer Zustand und Modellkontext

Speichere die für korrekte Fortsetzung nötigen Tatsachen in einer passenden Zustandsquelle. Für eine lange Entwicklungsaufgabe können das Zielversion, aktueller Kandidat, erfüllte Bedingungen, offene Fehler, Entscheidungen und Operationsstatus sein. Das Modell erhält eine auf den nächsten Schritt abgestimmte Projektion daraus. Für eine kurze rein lesende Aufgabe kann ein kleiner strukturierter Kontext ausreichen; eine Datenbank ist keine allgemeine Voraussetzung.

Verdichtung verändert die sichtbare Darstellung, nicht automatisch die zugrunde liegenden Tatsachen. Prüfe bei einem Reset, ob offene Blocker, verworfene Kandidaten und unklare Wirkungen weiter auffindbar sind. Eine Zusammenfassung darf eine unbelegte Behauptung nicht zur autoritativen Tatsache aufwerten. Kennzeichne Herkunft und Gültigkeitsbezug wiederverwendeter Erinnerungen.

## Welche Art von Wiederholbarkeit verlangt wird

| Ziel | Aufzuzeichnen / zu kontrollieren | Begrenzung |
|---|---|---|
| Entscheidung erklären | Zustandsinput, Controller-/Policyversion, relevante Fakten und Entscheidung. | Fehlende Fakten bleiben ein Beobachtungsproblem. |
| Internen Ablauf replayen | Ursprüngliche Modellantworten, Toolresultate und geordnete Ereignisse. | Führt keine neuen Remoteeffekte aus. |
| Neu ausführen | Tatsächliche Modellkonfiguration, Inputs, Toolchain, Ressourcen und relevante Umgebungsstände. | Neue Modellantworten und Außenwelt können abweichen. |
| Nach Crash fortsetzen | Dauerhafter Fortschritt und Status ausstehender beziehungsweise unklarer Operationen. | Persistenz allein verhindert keine Doppelwirkung. |

Dokumentiere versionsabhängige Einzelheiten dort, wo sie die gemessene Wirkung verändern. Ein vollständig gepinntes Modellinterface garantiert keine identische neue Antwort. Behaupte eine hermetische Umgebung nur für tatsächlich erfasste Abhängigkeiten. Persistierte Logs oder Checkpoints garantieren nicht von sich aus vollständige Beobachtbarkeit.

## Remoteoperationen und Retry

Wenn eine Operation von außen sichtbar wird, unterscheide „Anforderung reserviert“, „Ausführung begonnen“, „Ergebnis bestätigt“ und „Wirkung unklar“, soweit diese Zustände für den Ablauf relevant sind. Die genaue Repräsentation ist systemabhängig.

Wenn nach einer begonnenen Operation die Antwort verloren geht, prüfe zuerst die Bedeutung des verfügbaren Remotezustands. Nutze einen stabilen Operationsschlüssel oder eine APIeigene Idempotenzfunktion, wenn ihr Vertrag die gewünschte Semantik abdeckt. Ein erneuter Aufruf ist nur dann unproblematisch, wenn er sicher keine unzulässige zusätzliche Wirkung erzeugt oder diese durch den Remotevertrag verhindert wird. Ist kein sicherer Abgleich möglich, erhalte den unklaren Zustand und leite eine zum Auftrag passende Klärung ein.

Ein lokaler Dateilock schützt nur seine tatsächliche Koordinationsdomäne. Mehrere Prozesse oder Maschinen benötigen eine dafür geeignete Reservierung und Zustandskonsistenz. Eine reservierte Anfrage und eine Remoteoperation bilden ohne zusätzliches Protokoll keine automatische atomare Transaktion.

Bei Frameworks prüfe die tatsächlich eingesetzte Version: Ein Interrupt kann den Node erneut ausführen; eine Activity kann erneut versucht werden. Lege nicht idempotente Nebenwirkungen nicht ungeprüft vor einen Punkt, der wiederholt wird. Teste die relevante Crashposition statt nur einen erfolgreichen Normaldurchlauf.

## Konflikte und Stoppen

Für konkurrierende Worker identifiziere, welcher Fortschritt autoritativ ist und wie veraltete Zustandsstände erkannt werden. Für begrenzte Arbeitsschleifen bestimme Budget und Abschlusskriterium außerhalb der bloßen Modellbehauptung. Wähle keine festen universellen Turn- oder Tokenlimits aus einem Paperbeispiel.

Gegenfälle sind Reset mit offenem Blocker, Crash vor Versand, Remoteerfolg vor Antwortverlust, konkurrierende Reservierungen und ein verspätetes Ergebnis für einen alten Kandidaten. Prüfe nur die für den konkreten Auftrag relevanten Fälle. Eine korrekte Wiederaufnahme zeigt, dass diese kontrollierten Unterbrechungen behandelt werden; sie ist keine allgemeine Verfügbarkeitsgarantie.
