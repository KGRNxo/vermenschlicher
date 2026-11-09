# Vermenschlicher

**Vermenschlicher** überarbeitet deutschsprachige Texte, die künstlich, austauschbar oder unnötig kompliziert klingen. Der Skill bewahrt die Aussage und passt den Stil an den ursprünglichen Autor, die Zielgruppe und die Textart an.

Er basiert auf [Humanizer 3.1.0 von blader](https://github.com/blader/humanizer), übernimmt dessen **26 Prüfmuster vollständig in deutscher Bearbeitung** und ergänzt sie um Regeln für natürliche deutsche Sprache, App-Texte, Marketing, Dokumentation und persönliche Nachrichten. Das Projekt ist unter der MIT-Lizenz veröffentlicht.

### Beispiel

**Vorher**

> Wir freuen uns riesig, dir ein revolutionäres Lernerlebnis präsentieren zu dürfen! Unsere innovative Plattform hebt deine Vorbereitung auf ein völlig neues Level. Mehr als nur eine App. Dein perfekter Begleiter. Schnell. Einfach. Intuitiv. Und das Beste daran? Du bestimmst deinen Erfolg!

**Nachher**

> Mit der App kannst du Aufgaben zu einzelnen Themen üben und deinen Lernstand verfolgen. So erkennst du, welche Inhalte du noch einmal wiederholen solltest.

Das Beispiel zeigt eine stilistische Überarbeitung. Funktionen dürfen nur erwähnt werden, wenn sie beim tatsächlichen Produkt vorhanden sind.

## Installation

Vermenschlicher ist ein Agent-Skill: Er liefert Anweisungen zur Textbearbeitung und enthält keinen eigenen KI-Dienst. Er läuft mit einem kompatiblen Agenten.

### Codex

~~~bash
npx skills add KGRNxo/vermenschlicher --global --agent codex
~~~

Nach der Installation den Agenten bei Bedarf neu starten und beispielsweise schreiben:

~~~text
Verwende $vermenschlicher und überarbeite diesen Text auf natürliches Deutsch:
[Text einfügen]
~~~

### Claude Code als Plugin

Im interaktiven Claude-Code-Fenster:

~~~text
/plugin marketplace add KGRNxo/vermenschlicher
/plugin install vermenschlicher@vermenschlicher
~~~

Danach:

~~~text
/vermenschlicher:vermenschlicher
[Text einfügen]
~~~

Alternativ als Skill über die Skills-CLI:

~~~bash
npx skills add KGRNxo/vermenschlicher --global --agent claude-code
~~~

Je nach Installationsweg und Agenten-Version kann die Aufrufsyntax abweichen. Über einen normalen Textauftrag lässt sich der Skill ebenfalls verwenden.

### Weitere Agenten

~~~bash
npx skills add KGRNxo/vermenschlicher --global --agent '*'
~~~

Ohne „--global“ erfolgt die Installation projektbezogen. Für Agenten ohne Skills-CLI kann die Datei „SKILL.md“ in das vorgesehene Skill-Verzeichnis kopiert werden.

## Verwendung

**Einen Text überarbeiten**

~~~text
Nutze Vermenschlicher. Bewahre alle Fakten und den fachlichen Inhalt:
[Text]
~~~

**Den eigenen Stil übernehmen**

~~~text
Nutze Vermenschlicher und orientiere dich an dieser Schreibprobe:
[Zwei bis drei eigene Absätze]

Überarbeite anschließend diesen Text:
[Text]
~~~

**Eine Datei bearbeiten**

~~~text
Nutze Vermenschlicher für die Prosa in docs/website.md.
Lass Code, Dateipfade, Links, technische Werte und Daten unverändert.
~~~

**Schon beim Schreiben anwenden**

~~~text
Verwende Vermenschlicher beim Schreiben unserer deutschen Website-Texte.
Schreibe konkret und natürlich. Erfinde keine Produkteigenschaften.
~~~

## Was Vermenschlicher besonders berücksichtigt

- Natürliches Deutsch statt wortwörtlich übernommener englischer Stilregeln
- Keine künstlichen Gegensätze oder bedeutungslosen Schlagwortreihen
- Keine standardisierten Schlusspointen, Verkaufsfloskeln oder Chatbot-Grüße
- Deutsche Komposita, Rechtschreibung und Zeichensetzung
- Die individuelle Stimme des Autors statt künstlicher Umgangssprache
- Sorgfältiger Umgang mit Zahlen, Zitaten, Fachbegriffen und Unsicherheiten
- Unterschiedliche Anforderungen an Marketing, App-Oberflächen, Fachtexte und private Nachrichten

## Die fünf auffälligsten Muster

1. „Es geht nicht nur um X, sondern um Y“, obwohl niemand X behauptet hat
2. Einzelne Schlusssätze, die bloß das Vorherige wiederholen
3. Große Wahrheiten ohne konkrete Aussage
4. Einleitungen, die nur das eigentliche Thema ankündigen
5. Verteidigungen gegen Einwände, die im Text gar nicht vorkommen

## Die 26 Prüfmuster

Alle 26 Muster des Originals sind übernommen. Die Reihenfolge und Nummerierung wurden beibehalten, damit Verweise nachvollziehbar bleiben. Erläuterungen und Beispiele sind an das Deutsche angepasst.

### A. Inszenierung statt Aussage

| Nr. | Muster | Worum es geht |
| --- | --- | --- |
| 1 | **Künstlicher Gegensatz: „Nicht X, sondern Y“** | Künstliche Gegensätze durch direkte Aussagen ersetzen |
| 2 | **Wiederholende Schlusssätze und dramatische Satzfragmente** | Leere Pointen und künstlich isolierte Sätze streichen |
| 3 | **Pseudotiefe und bedeutungsvolle Allgemeinplätze** | Abstrakte Lebensweisheiten konkretisieren |
| 4 | **Angekündigte Einleitungen** | Sofort mit der Information beginnen |
| 5 | **Einwände, die niemand erhoben hat** | Unnötige Verteidigungen entfernen |

### B. Mechanischer Rhythmus

| Nr. | Muster | Worum es geht |
| --- | --- | --- |
| 6 | **Erzwungene Dreiergruppen** | Nur die tatsächlich erforderlichen Punkte nennen |
| 7 | **Gleichförmige Satzanfänge** | Satzbau nach Inhalt statt nach Schema wählen |
| 8 | **Gedankenstriche als universelles Bindemittel** | Gedankliche Zusammenhänge passend formulieren |
| 9 | **Gestapelte Unsicherheitsmarker** | Doppelungen kürzen, echte Vorbehalte bewahren |
| 10 | **Mechanische Bindestrichverbindungen** | Deutsche Komposita korrekt schreiben |
| 11 | **Unnötiges Passiv und fehlende Handelnde** | Handelnde und Vorgänge klar benennen |

### C. Aufgeblasene Bedeutung und geliehene Autorität

| Nr. | Muster | Worum es geht |
| --- | --- | --- |
| 12 | **Überstrapazierte KI-Wörter** | Konkrete Wörter statt aufgeblähter Formeln |
| 13 | **Übertriebene historische oder persönliche Bedeutung** | Bedeutung nur dort behaupten, wo sie belegt ist |
| 14 | **Unklare Beziehungen** | Tatsächliche Beziehungen konkret nennen |
| 15 | **Angehängte Scheinfolgerungen** | Unbelegte Deutungen aus Nebensätzen entfernen |
| 16 | **Aufdringliche Werbesprache** | Eigenschaften statt leerer Superlative nennen |
| 17 | **Geliehene Autorität** | Quellen konkret angeben oder Behauptungen streichen |
| 18 | **Vermeidung einfacher Verben** | Unnötige Umschreibungen durch klare Verben ersetzen |

### D. Mechanische Formatierung

| Nr. | Muster | Worum es geht |
| --- | --- | --- |
| 19 | **Fettdruck als Dekoration** | Hervorhebungen gezielt einsetzen |
| 20 | **Dekorative Überschriften** | Überschriften sollen ihren Inhalt beschreiben |
| 21 | **Unpassende Anführungszeichen** | Deutsche Typografie und Zielformat beachten |

### E. Reste aus Chat und Entwurf

| Nr. | Muster | Worum es geht |
| --- | --- | --- |
| 22 | **Chatbot-Reste** | Chat-Floskeln aus eigenständigen Texten entfernen |
| 23 | **Wissensgrenzen als Textfüllung und erfundene Vermutungen** | Fehlende Fakten nicht durch Spekulationen ersetzen |
| 24 | **Wiederholung der Überschrift im ersten Satz** | Inhaltliche Doppelungen streichen |
| 25 | **Schreiben über den Text statt über die Sache** | Gegenstand beschreiben, nicht den Schreibprozess |

### F. Am Leser vorbeigeschrieben

| Nr. | Muster | Worum es geht |
| --- | --- | --- |
| 26 | **Bekanntes unnötig erneut erklären** | Bereits bekannten Kontext nicht erneut ausbreiten |

## Zusätzliche deutsche Stilregeln

Vermenschlicher ergänzt diese 26 Muster um zusätzliche Regeln für deutsche KI-Formulierungen, Textfluss und glaubwürdige Tonalität.

**Zu vermeiden, wenn es nur Füllung ist:** „Hier kommt X ins Spiel“, „Die eigentliche Frage lautet“, „Das Beste daran?“, „Eine neue Ära“, „Auf ein neues Level heben“, „Dein perfekter Begleiter“, „Alles, was du brauchst“.

**Ebenfalls auffällig:** „Einfach. Schnell. Verständlich.“ oder „Keine Ablenkung. Keine Umwege. Nur Ergebnisse.“ Solche Sätze erzeugen einen künstlichen Rhythmus und sagen meist wenig über den konkreten Gegenstand aus.

Der Skill verhindert auch das gegenteilige Extrem: Er erzeugt keine absichtlichen Fehler, erzwungene Umgangssprache oder willkürlichen Einschübe, nur um künstlich „menschlich“ zu wirken.

Alle Regeln und Ausnahmen stehen vollständig in [SKILL.md](SKILL.md).

## Grenzen

- Ein sprachliches Merkmal beweist keine KI-Autorenschaft.
- Auch menschliche Autoren verwenden einzelne der genannten Formulierungen bewusst.
- Ziel ist bessere Lesbarkeit und ein passender Schreibstil, **nicht das Umgehen von KI-Detektoren**.
- Das Ergebnis kann Fakten nur dann korrekt bewahren, wenn der Ausgangstext sie enthält. Bei Recht, Medizin, Finanzen und Technik haben Genauigkeit und notwendige Einschränkungen Vorrang.
- Ein Agent verarbeitet die Regeln mit seinem eigenen Sprachmodell. Die Qualität hängt deshalb auch vom Modell, der Schreibprobe und dem Ausgangstext ab.

## Entwicklung und Prüfung

Die zentrale Skill-Datei liegt im Repository-Hauptverzeichnis. Der Validator prüft Metadaten, Versionsnummern, 26 Muster und die Übereinstimmung zwischen README und Skill:

~~~bash
python3 scripts/validate-package.py
~~~

Die übrigen Dateien enthalten Plugin-Metadaten, Hilfstexte und Vorlagen. Für Änderungen an Formulierungsregeln ist „SKILL.md“ maßgeblich. Details stehen in [AGENTS.md](AGENTS.md).

## Herkunft und Lizenz

**Vermenschlicher** ist eine deutsche Weiterentwicklung von [Humanizer](https://github.com/blader/humanizer) von blader, Ausgangsversion 3.1.0. Die 26 Prüfmuster des Originals beruhen unter anderem auf [„Signs of AI writing“](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) aus Wikipedia und dem WikiProject AI Cleanup.

Die ursprüngliche MIT-Lizenz einschließlich Copyright-Hinweis bleibt in [LICENSE](LICENSE) erhalten. Diese Fassung enthält zusätzlich eigenständig formulierte deutsche Beispiele und Regeln. Sie ist kein offizielles deutschsprachiges Release des Originalprojekts.
