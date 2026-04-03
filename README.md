# Simple-Invoice-Scanner 📄🚀
Ein schlanker und effizienter Python-Parser, um wichtige Daten aus PDF-Rechnungen zu extrahieren und direkt in einer CSV-Datei zu speichern. Das Tool nutzt RegEx (Regular Expressions) für einen schnellen Volltext-Scan, ohne jede Zeile einzeln iterieren zu müssen. In dem examples Ordner befinden sich Muster Rechngungen im unterschiedlichen Format. Mit diesen kann das Programm getestet werden.

## ✨ Features
Volltext-Analyse: Schneller als herkömmliche Zeilen-Loops.

Intelligente Mustererkennung: Findet Rechnungsnummern, Beträge (Netto/Brutto) und E-Mails in verschiedenen Formaten.

CSV-Export: Speichert die extrahierten Daten direkt im Excel-freundlichen Format (UTF-8 mit BOM).

Robust: Erkennt unterschiedliche Schreibweisen wie "Re-Nr", "Invoice", "Endsumme" etc.

## 🛠 Tech-Stack
Python 3.x

PyPDF2: Zum Auslesen der PDF-Inhalte.

Pandas: Für die Datenstrukturierung und den CSV-Export.

Re (Regex): Für die hochpräzise Mustersuche.

## 🚀 Quick Start
1. Voraussetzungen

Stelle sicher, dass du Python installiert hast. Installiere die benötigten Bibliotheken mit:

```bash
pip install PyPDF2 pandas
```

2. Nutzung

Lege deine Rechnung als .pdf in den examples Ordner.

Starte das Skript:

Die extrahierten Daten findest du sofort in der neu erstellten .csv.

## 🔍 Unterstützte Muster
Der Parser ist aktuell auf folgende Formate optimiert:

Rechnungsnummern: z.B. Re-147/2025, M1675, INV-202 connection.

Beträge: Erkennt die 4 größten Währungen (€,£,¥,$).

E-Mails: Standardmäßige Validierung von .com, .de, .net, .org. Wenn keine vorhanden ist wird das so vermerkt

## 🚧 Roadmap

Hier ein Ausblick auf die Funktionen, die gerade entwickelt werden:

[✅] Ordner-Scan (Batch Processing): Automatische Analyse aller PDFs in einem angegebenen Verzeichnis, statt nur einer Datei.

[✅] Betrags-Konvertierung: Umwandlung der Text-Beträge (z.B. "1.200,50") in echte Zahlen (float), um direkt Berechnungen durchzuführen.

[✅ ] Währungserkennung: Automatische Unterscheidung zwischen €, $ und anderen Währungen.

[ ] Dubletten-Check: Prüfung, ob eine Rechnungsnummer bereits in der CSV existiert, um doppelte Einträge zu vermeiden.

[ ] GUI-Interface: Eine kleine Benutzeroberfläche, damit man keine Konsole mehr bedienen muss.

