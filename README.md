# Simple-Invoice-Scanner 📄🚀
Ein schlanker und effizienter Python-Parser, um wichtige Daten aus PDF-Rechnungen zu extrahieren und direkt in einer CSV-Datei zu speichern. Das Tool nutzt RegEx (Regular Expressions) für einen schnellen Volltext-Scan, ohne jede Zeile einzeln iterieren zu müssen.

# ✨ Features
Volltext-Analyse: Schneller als herkömmliche Zeilen-Loops.

Intelligente Mustererkennung: Findet Rechnungsnummern, Beträge (Netto/Brutto) und E-Mails in verschiedenen Formaten.

CSV-Export: Speichert die extrahierten Daten direkt im Excel-freundlichen Format (UTF-8 mit BOM).

Robust: Erkennt unterschiedliche Schreibweisen wie "Re-Nr", "Invoice", "Endsumme" etc.

# 🛠 Tech-Stack
Python 3.x

PyPDF2: Zum Auslesen der PDF-Inhalte.

Pandas: Für die Datenstrukturierung und den CSV-Export.

Re (Regex): Für die hochpräzise Mustersuche.

# 🚀 Quick Start
## 1. Voraussetzungen

Stelle sicher, dass du Python installiert hast. Installiere die benötigten Bibliotheken mit:

Bash
pip install PyPDF2 pandas
## 2. Nutzung

Lege deine Rechnung als Rechnungsvorlage.pdf in den Projektordner.

Starte das Skript:

Die extrahierten Daten findest du sofort in der neu erstellten test.csv.

# 🔍 Unterstützte Muster
Der Parser ist aktuell auf folgende Formate optimiert:

Rechnungsnummern: z.B. Re-147/2025, M1675, INV-202 connection.

Beträge: Erkennt deutsche Formate (z.B. 2.840,00 € oder Summe Netto 186,99).

E-Mails: Standardmäßige Validierung von .com, .de, .net, .org.

