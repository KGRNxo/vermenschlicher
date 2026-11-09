#!/usr/bin/env python3
"""Prüft das deutschsprachige Skill-Paket ohne externe Abhängigkeiten."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def datei(pfad: str) -> str:
    try:
        return (ROOT / pfad).read_text(encoding="utf-8")
    except OSError as fehler:
        raise SystemExit(f"Datei {pfad} kann nicht gelesen werden: {fehler}")


def pruefe(bedingung: bool, meldung: str) -> None:
    if not bedingung:
        raise SystemExit(meldung)


def json_datei(pfad: str) -> dict:
    try:
        return json.loads(datei(pfad))
    except json.JSONDecodeError as fehler:
        raise SystemExit(f"Ungültige JSON-Datei {pfad}: {fehler}")


skill = datei("SKILL.md")
readme = datei("README.md")
aenderungen = datei("CHANGELOG.md")
lizenz = datei("LICENSE")
claude = json_datei(".claude-plugin/plugin.json")
marketplace = json_datei(".claude-plugin/marketplace.json")
cursor = json_datei(".cursor-plugin/plugin.json")

meta_match = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
pruefe(meta_match is not None, "SKILL.md muss mit YAML-Metadaten beginnen.")
meta = meta_match.group(1)

name_match = re.search(r"(?m)^name:\s*(\S+)\s*$", meta)
pruefe(name_match is not None and name_match.group(1) == "vermenschlicher",
       "Skill-Name muss 'vermenschlicher' sein.")

for feld in ("version:", "compatibility:", "allowed-tools:"):
    pruefe(re.search(rf"(?m)^{re.escape(feld)}", meta) is None,
           f"Nicht unterstütztes YAML-Feld: {feld}")

version_match = re.search(r'(?m)^  version:\s*["\x27]?(\d+\.\d+\.\d+)["\x27]?\s*$', meta)
pruefe(version_match is not None, "metadata.version fehlt oder ist ungültig.")
version = version_match.group(1)
aenderung_match = re.search(r"(?m)^## (\d+\.\d+\.\d+)$", aenderungen)
pruefe(aenderung_match is not None, "Eine Versionsüberschrift im Änderungsverlauf fehlt.")
pruefe(len({version, aenderung_match.group(1), str(claude.get("version")), str(cursor.get("version"))}) == 1,
       "Skill, Änderungsverlauf und Plugin-Manifeste brauchen dieselbe Versionsnummer.")

beschreibung_match = re.search(r"(?m)^description: \|\n((?:  .*\n)+)", meta + "\n")
pruefe(beschreibung_match is not None, "Skill-Beschreibung im Blockformat fehlt.")
beschreibung = " ".join(beschreibung_match.group(1).split())
erste_zeile = beschreibung.split(". ", 1)[0] + "."
pruefe(all(manifest.get("description") == erste_zeile
           for manifest in (claude, cursor, *marketplace.get("plugins", []))),
       "Die Plugin-Beschreibungen müssen dem ersten Satz der Skill-Beschreibung entsprechen.")

pruefe(claude.get("name") == "vermenschlicher" and claude.get("skills") == ["./"],
       "Claude-Plugin-Name oder Skill-Pfad ist falsch.")
pruefe(cursor.get("name") == "vermenschlicher" and "skills" not in cursor,
       "Cursor-Plugin-Name ist falsch oder ein zusätzlicher Skill-Pfad ist gesetzt.")
pruefe(marketplace.get("name") == "vermenschlicher"
       and len(marketplace.get("plugins", [])) == 1
       and marketplace["plugins"][0].get("name") == "vermenschlicher",
       "Claude-Marketplace muss 'vermenschlicher' als Plugin enthalten.")

skill_dateien = {pfad.relative_to(ROOT) for pfad in ROOT.rglob("SKILL.md")}
pruefe(skill_dateien == {Path("SKILL.md")} and not (ROOT / "SKILL.md").is_symlink(),
       "Es darf nur eine reguläre SKILL.md im Hauptverzeichnis geben.")

muster_skill = [(int(nummer), titel)
                for nummer, titel in re.findall(r"(?m)^### (\d+)\. (.+)$", skill)]
pruefe([nummer for nummer, _ in muster_skill] == list(range(1, 27)),
       "Die 26 ursprünglichen Muster müssen fortlaufend nummeriert sein.")

muster_readme = [(int(nummer), titel)
                 for nummer, titel in re.findall(r"(?m)^\| (\d+) \| \*\*(.+?)\*\*", readme)]
pruefe(muster_readme == muster_skill,
       "Muster und Titel in README.md müssen mit SKILL.md übereinstimmen.")
pruefe("## Die 26 Prüfmuster" in readme,
       "README.md braucht die Überschrift 'Die 26 Prüfmuster'.")

verweise = [int(nummer) for nummer in re.findall(r"§(\d+)", skill)]
pruefe(all(1 <= nummer <= 26 for nummer in verweise),
       "Ein Verweis auf eine Musternummer liegt außerhalb von 1 bis 26.")

wortzahl = len(skill.split())
pruefe(wortzahl <= 5500,
       f"SKILL.md darf höchstens 5.500 Wörter enthalten: aktuell {wortzahl}.")

pruefe("MIT License" in lizenz and "Copyright" in lizenz,
       "Die ursprüngliche MIT-Lizenz einschließlich des Copyright-Hinweises fehlt.")
pruefe("blader/humanizer" in skill and "blader/humanizer" in readme,
       "Der Herkunftshinweis auf blader/humanizer fehlt.")
pruefe("KGRNxo/vermenschlicher" in readme,
       "Die Installationsanweisungen müssen auf das eigene Repository zeigen.")

print(f"Vermenschlicher {version}: Paket gültig, 26 Muster, {wortzahl} Wörter.")
