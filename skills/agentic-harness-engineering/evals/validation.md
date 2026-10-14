# Validierung dieser Skillfassung

**Erstellt und geprüft: 14.10.2026.** Das Paket ist **strukturell validiert; die Befolgung durch einen unabhängigen Agenten ist noch ungetestet**.

Die Erstellung folgt Recherche- und Skillauthoringvorgaben. Gemeinsame Entscheidungen stehen im Einstieg, umfangreichere Mechanismen in bedingt ladbaren Referenzen. Das Paket setzt keine bestimmte Plattform, Repositorystruktur, Freigabefolge oder externe Companion-Skills voraus. Es enthält keine Installationsaktion und keine zusätzlichen Ausführungsrechte.

## Tatsächlich geprüft

- Der vorhandene Skillvalidator prüft Frontmatter, Namen und Scaffoldfelder.
- Ergänzende Strukturprüfungen prüfen portable lokale Verweise, Ressourcen, Quellen-/Regel-IDs, vollständige Fallrubriken, Metadaten und Abwesenheit privater Maschinenpfade oder Runtimeabhängigkeiten außerhalb des Pakets.
- Sechs allgemeine Requests und Ergebnisrubriken wurden vor dem Autorenreview erstellt. Die Kriterien liegen in einer eigenen Datei und sollen nicht in den Kontext eines frischen Testworkers geladen werden.
- Die synthetische Auditfixture wurde mit Python ausgeführt. Ein positiver und ein negativer Normalfall sowie drei problematische Effektpfade wurden beobachtet. Alle Effekte bleiben im Arbeitsspeicher.
- Der [Autorenreview](author-review.md) dokumentiert Entscheidungen und Grenzen für die sechs Fälle.

Die tatsächlichen mechanischen Ergebnisse stehen in [structural-checks.json](structural-checks.json), die Fixturebeobachtungen in [fixture-observations.json](fixture-observations.json). Diese Dateien werden nach den Prüfungen geschrieben und gehören zur gelieferten Fassung.

## Was diese Prüfung nicht zeigt

Ein Fixturelauf validiert den synthetischen Testinput, nicht automatisch die Entscheidungen eines Agenten, der den Skill verwendet. Der Autor kannte die Kriterien, daher ist sein Review keine blinde Verhaltensprüfung. Es wurden keine unabhängigen Agententrials und keine Produktiv- oder Remoteaktionen durchgeführt. Die unabhängige Followabilityprüfung wurde in diesem Auftrag nicht delegiert; deshalb wird kein frischer Testworker behauptet.

Noch empirisch zu prüfen sind insbesondere Modus-/Scopetrennung in neuen Aufgaben, sinnvolle Referenzwahl, vollständiges Verfolgen realer Effektpfade, tatsächliche Recoveryentscheidungen und qualifizierte Aussagen unter Druck zu pauschalen Garantien. Eine Leistungssteigerung durch den Skill würde passende Baseline-/Revisedversuche und repräsentative Aufgaben benötigen.

Die Literatur und die Fixture rechtfertigen weder einen universellen Determinismusanspruch noch eine allgemeine Accuracyzusage. Der Forschungsstand bleibt der 13.10.2026; bei versionsabhängigen Implementierungen ist der tatsächliche Vertrag neu zu prüfen.
