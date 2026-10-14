# Steuerung, Regeln und Nachweise

**Laden bei:** verbindlichen Aktionsregeln, Phasenbedingungen, Privilegien, Nachweisen oder dem Audit eines Controllers. Grundlage: R03–R05; Quellen und Grenzen stehen in [evidence.md](evidence.md).

## Von einer Anweisung zu einer ausführbaren Bedingung

Wähle den Mechanismus nach der Regel. Eine Formatbedingung braucht einen Parser; eine Ressourcenregel eine wirksame Aktionsgrenze; eine Reihenfolgeregel ein beobachtbares Ereignismodell; eine fachliche Bedingung ein geeignetes Orakel. Natürlichsprachliche Policy kann diese Absicht beschreiben. Exakte Bedingungen müssen durch den eingesetzten Mechanismus tatsächlich ausgewertet werden.

| Beobachtbare Anforderung | Mögliche Umsetzung | Fehler- oder Unsicherheitsfall |
|---|---|---|
| Eingabe muss ein Format erfüllen. | Schema-/Grammatikprüfung plus semantische Validierung benötigter Werte. | Valides Format mit falscher Referenz bleibt ungültig. |
| Aktion verlangt frühere Prüfung. | Zustandsübergang oder temporaler Monitor über gebundene Ereignisse. | Prüfung für einen anderen Kandidaten erfüllt die Bedingung nicht. |
| Zugriff ist auf bestimmte Ressourcen begrenzt. | Berechtigungsprüfung im Executor oder in einer nicht umgehbaren Vermittlung. | Der tatsächlich aufgelöste Zugriff verletzt die Grenze, obwohl ein Textpfad passend aussieht. |
| Eigenschaft ist nur semantisch bewertbar. | Kalibrierte Review-/Judgeentscheidung, ergänzt durch passende externe Prüfungen. | Unsichere Bewertung als solche ausweisen; keine formale Garantie erfinden. |
| Bekannte Schritte haben Abhängigkeiten. | Geprüfter DAG oder Zustandsautomat. | Zyklus, unbekannte Referenz oder fehlender Zustand verhindert entsprechende Ausführung. |

Ein starres Phasenmodell ist sinnvoll, wenn Übergänge und Voraussetzungen stabil bekannt sind. Bei offener Lösungssuche kann ein kleiner Kontrollkern nur die invarianten Grenzen prüfen. Keine Architektur erzwingt allein durch ihre Bezeichnung vollständige Korrektheit.

## Tatsächliche Ausführung vermitteln

Beginne mit den Aktionen und Ressourcen, die der Auftrag als relevant festlegt. Verfolge, wo das Modell einen Vorschlag abgibt, wo die Policy entscheidet und wo die Wirkung stattfindet. Prüfe, ob ein anderer Executor, ein Unterprozess, ein MCP-/APItool oder delegierte Arbeit dieselbe relevante Wirkung ohne Prüfung erzeugen kann.

Wenn eine verbindliche Grenze einen Pfad nicht erfasst, behebe den Pfad oder beschränke die zugesicherte Eigenschaft. Ein Post-Action-Hook eignet sich zur Diagnose, nicht zum Verhindern der bereits ausgeführten Aktion. Ein Modell, das eine Aktion als sicher einstuft, ersetzt keine fehlende Ressourcenprüfung.

Vertrauenswürdige Regeln und Berechtigungen müssen ihre Autorität aus der vorgesehenen Instanz erhalten. Repositorytexte, Toolantworten und Modellvorschläge dürfen verbindliche Rechte nicht selbst erweitern. Erzeugte Policy ist ein Kandidat, der gegen den tatsächlichen Auftrag und die Vertrauensgrenzen zu prüfen ist. Begrenze freie Codeausführung dort, wo sie geschützte Wirkungen umgehen könnte; ausdrucksstarke Codeaktionen können innerhalb einer passenden Umgebung weiterhin nützlich sein.

## Nachweise für denselben Gegenstand

Wenn ein Abschluss oder eine Wirkung von einem Nachweis abhängt, identifiziere:

- den Kandidaten oder Ressourcenzustand, auf den sich der Nachweis bezieht;
- relevante Inputs, Prüfkonfiguration und gegebenenfalls Umgebung;
- die Instanz, die das Ergebnis tatsächlich ausgestellt hat;
- Resultat und Grenzen der ausgeführten Prüfung.

Das passende Bindungsverfahren kann ein vertrauenswürdiger Prozesszustand, eine Datenbankrelation, ein Manifest oder eine Attestation sein. Kryptografische Signaturen sind kein Pflichtmechanismus für jeden lokalen Ablauf. Dort, wo der Kandidat seine eigenen Nachweise, Prüfer oder Freigabeidentität verändern könnte, ist deren Integrität separat zu sichern.

Prüfe am späteren Entscheidungszeitpunkt, ob die Bindung noch gilt. Bei konkurrierenden Änderungen kann eine Prüfung vor der Aktion einen anderen Zustand als die Aktion selbst gesehen haben. Wähle je nach System einen Snapshot, eine atomare Zustandsprüfung, Versionierung oder einen entsprechend begrenzten Effektadapter. Ein Hash ohne einen vollständigen relevanten Inputbezug löst dieses Problem nicht automatisch.

## Fehlerentscheidungen sichtbar machen

Unterscheide bestätigte Erfüllung, festgestellte Verletzung, ausstehende Prüfung und unbekannte Tatsache. Die Bezeichnungen `ALLOW`, `DENY`, `WAIT`, `UNKNOWN` sind ein mögliches Interface, keine vorgeschriebene API. Bei unbekannter verbindlicher Voraussetzung darf keine positive Entscheidung allein aus einer Modellbehauptung entstehen. Behalte einen begründeten Weg zur Wiederaufnahme oder Klärung, statt einen sicheren, aber unbrauchbaren Dauerabbruch als Erfolg zu zählen.

## Relevante Gegenfälle

Prüfe die Fälle, die die konkrete Grenze falsifizieren könnten: passende Reihenfolge mit falschem Gegenstand, gefälschter Aussteller, veränderte Prüfeingaben, gültiges JSON mit unzulässiger Ressource, alternativer Effektpfad und zulässiger Sonderfall. Ein Monitor kann sicher abweisen und dennoch zu viele erlaubte Aufgaben blockieren. Messe beides, wenn du seine Wirksamkeit beurteilst.
