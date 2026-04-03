from PyPDF2 import PdfReader
import re
import pandas as pd
import os

# temporäre Speicherung
Speicher = {
    "Rechnungsnummer": None,
    "Brutto(€)": None,
    "Netto(€)": None,
    "Email": None,
}

Rechenfaktor = 0.0

#duplicate_check = pd.read_csv("test.csv")      -> Prototyp, noch in Arbeit

#Alle PDFs aus dem Ordner examples werden geladen
os.listdir("examples")
print(os.listdir("examples"))

#loop, der für jede file einmal iteriert
for file in os.listdir("examples"):

    if file.endswith(".pdf"):       #stellt sicher, dass nur PDFs verarbeitet werden
        print(file)
        # Lesbare .pdf wird geladen
        reader = PdfReader(os.path.join("examples", file))
        page = reader.pages[0]
        # Text wird extrahiert
        text = page.extract_text()

        # exit flags um doppelte Einträge zu vermeiden
        stop = 0
        stop2 = 0

        # RegEx, um Muster zu erkennen und die richtigen Daten zu filtern
        rechnungs_daten = r"(?:Rechnungs(?:-Nr\.?|nummer)|Re-?Nr\.?|Rechnung|Inv(?:oice)?)\s*.*?\b([A-Z0-9\-\./]{3,15})"
        mail_muster = r"[\w\.-]+@[\w\.-]+\.(com|de|net|org)"
        Netto = r"(?:Netto|netto).*?([\d.]+,\d{2})"
        Brutto = r"(?:Brutto|brutto|Endsumme|Total|Gesamt).*?([\d.]+,\d{2})"
        Währung_Muster = r"(€|$|¥|£)"

        # gesamter Text in der PDF wird nach dem oben definierten Muster gescannt
        ergebnis = re.search(rechnungs_daten, text)
        e_mail = re.search(mail_muster, text)
        Netto_Betrag = re.search(Netto, text)
        Brutto_Betrag = re.search(Brutto, text)
        Währung = re.search(Währung_Muster, text)


#Wärhungsbestimmung: Datei wird nach Keywords durchsucht um Währung zu bestimmen
        if Währung:

            symbol = Währung.group()

            Faktoren = {"€": 1.0, "$": 0.87, "¥": 0.0054, "£": 1.15}        #Rechenfaktoren für die jeweilige Währung
            Rechenfaktor = Faktoren.get(symbol, 1.0)

        else:
            Rechenfaktor = 1.0      #Wenn keine Währung gefunden wurde nimmt das Programm an, dass es sich um den Euro handelt


        # Sobald ein Muster erkannt wurde werden die Daten extrahiert und in den temporären Speicher geladen
        if ergebnis and stop == 0:
            #print(f"Rechnungsnummer: {ergebnis.group()}")
            Speicher["Rechnungsnummer"] = ergebnis.group(1)
            stop = 1  # Besonderheit mit stop (dient als exit flag) um doppelte Ergebisse zu vermeiden

        if e_mail and stop2 == 0:
            #print(f"E-Mail: {e_mail.group()}")
            Speicher["Email"] = e_mail.group()
            stop2 = 1       #exit flag
        else:
            Speicher["Email"] = "Nicht vorhanden"

        if Netto_Betrag:
            #Casting zu float -> entfernen vom ersten Punkt und ersetzen vom Komma zum Punkt

            Netto_float = float(Netto_Betrag.group(1).replace(".", "").replace(",", "."))

            Netto_float = Netto_float * Rechenfaktor        #vorher definierter Rechenfaktor wird verrechnet
            #print(f"Netto: {Netto_float}")
            Speicher["Netto(€)"] = Netto_float

        if Brutto_Betrag:
            #Casting zu float -> entfernen vom ersten Punkt und ersetzen vom Komma zum Punkt
            Brutto_float = float(Brutto_Betrag.group(1).replace(".", "").replace(",", "."))

            Brutto_float = Brutto_float * Rechenfaktor      #vorher definierter Rechenfaktor wird verrechnet
            #print(f"Brutto: {Brutto_float}")

            Speicher["Brutto(€)"] = Brutto_float


        print(Speicher)

        # Speicher wird zum DataFrame umgewandelt
        df = pd.DataFrame([Speicher])

        # DataFrame wird in die Rechnungen.csv Datei geschriebenm
        df.to_csv("Rechnungen.csv", index=False, sep=';', encoding='utf-8-sig', mode='a', header=Speicher)








