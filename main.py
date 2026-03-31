from PyPDF2 import PdfReader
import re
import pandas as pd
import os

# temporäre Speicherung
Speicher = {
    "Rechnungsnummer": None,
    "Brutto": None,
    "Netto": None,
    "Email": None,
}

#duplicate_check = pd.read_csv("test.csv")

#Alle PDFs aus dem Ordner examples werden geladen
os.listdir("examples")
print(os.listdir("examples"))

#loop, der für jede file einmal iteriert
for file in os.listdir("examples"):

    if file.endswith(".pdf"):
        print(file)
        # Lesbare .pdf wird geladen
        reader = PdfReader(os.path.join("examples", file))
        page = reader.pages[0]
        # Text wird extrahiert
        text = page.extract_text()



        print("--- Analyse beendet ---")

        # exit flags um doppelte Einträge zu vermeiden
        stop = 0
        stop2 = 0

        # RegEx, um Muster zu erkennen und die richtigen Daten zu filtern
        rechnungs_daten = r"(?:Rechnungs(?:-Nr\.?|nummer)|Re-?Nr\.?|Rechnung|Inv(?:oice)?)\s*.*?\b([A-Z0-9\-\./]{3,15})"
        mail_muster = r"[\w\.-]+@[\w\.-]+\.(com|de|net|org)"
        Netto = r"(?:Netto|netto).*?([\d.]+,\d{2})"
        Brutto = r"(?:Brutto|brutto|Endsumme|Total|Gesamt).*?([\d.]+,\d{2})"

        # gesamter Text wird nach dem oben definierten Muster gescannt -> Ressourcen sparsamer als ein for loop (keine iteration)
        ergebnis = re.search(rechnungs_daten, text)
        e_mail = re.search(mail_muster, text)
        Netto_Betrag = re.search(Netto, text)
        Brutto_Betrag = re.search(Brutto, text)

        # Sobald ein Muster erkannt wurde werdeb die Daten extrahiert und in den temporären Speicher geladen
        if ergebnis and stop == 0:
            print(f"Rechnungsnummer: {ergebnis.group()}")
            Speicher["Rechnungsnummer"] = ergebnis.group(1)
            stop = 1  # Besonderheit mit stop (dient als exit flag) um doppelte Ergebisse zu vermeiden

        if e_mail and stop2 == 0:
            print(f"E-Mail: {e_mail.group()}")
            Speicher["Email"] = e_mail.group()
            stop2 = 1

        if Netto_Betrag:
            print(f"Netto: {Netto_Betrag.group()}")
            Speicher["Netto"] = Netto_Betrag.group(1)

        if Brutto_Betrag:
            print(f"Brutto: {Brutto_Betrag.group()}")
            Speicher["Brutto"] = Brutto_Betrag.group(1)

        print(Speicher)

        # Speicher wird zum DataFrame umgewandelt
        df = pd.DataFrame([Speicher])

        # DataFrame wird in die Rechnungen.csv Datei geschriebenm
        df.to_csv("Rechnungen.csv", index=False, sep=';', encoding='utf-8-sig', mode='a', header=Speicher)








