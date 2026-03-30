from PyPDF2 import PdfReader
import re
import pandas as pd

#Lesbare .pdf wird geladen
reader = PdfReader("Rechnungsvorlage.pdf")
page = reader.pages[0]
#Text wird extrahiert
text = page.extract_text()

# temporäre Speicherung
Speicher = {
    "Rechnungsnummer": None,
    "Brutto": None,
    "Netto": None,
    "Email": None,
}



print("--- Analyse beendet ---")

#exit flags um doppelte Einträge zu vermeiden
stop = 0
stop2 = 0


#RegEx, um Muster zu erkennen und die richtigen Daten zu filtern
rechnungs_daten = r"(?:Rechnungs(?:-Nr\.?|nummer)|Re-?Nr\.?|Rechnung|Inv(?:oice)?)\s*[:\-]?\s*(?:Re-)?\s*([A-Z0-9/\-\.]{3,15})"
mail_muster = r"[\w\.-]+@[\w\.-]+\.(com|de|net|org)"
Netto = r"(?:Summe\s+)?(?:Netto|netto)\s*(?:€\s*)?[:\-]?\s*([\d.,]+)(?:\s*€)?"
Brutto = r"(?:Endsumme|Brutto|brutto)\s*(?:€\s*)?[:\-]?\s*([\d.,]+)(?:\s*€)?"


#gesamter Text wird nach dem oben definierten Muster gescannt -> Ressourcen sparsamer als ein for loop (keine iteration)
ergebnis = re.search(rechnungs_daten, text)
e_mail = re.search(mail_muster, text)
Netto_Betrag = re.search(Netto, text)
Brutto_Betrag = re.search(Brutto, text)

#Sobald ein Muster erkannt wurde werdeb die Daten extrahiert und in den temporären Speicher geladen
if ergebnis and stop == 0:
    print(f"Rechnungsnummer: {ergebnis.group()}")
    Speicher["Rechnungsnummer"] = ergebnis.group(1)
    stop = 1                                            #Besonderheit mit stop (dient als exit flag) um doppelte Ergebisse zu vermeiden

if e_mail and stop2 == 0:
    print(f"E-Mail: {e_mail.group()}")
    Speicher["Email"] = e_mail.group()
    stop2 = 1

if Netto_Betrag :
    print(f"Netto: {Netto_Betrag.group()}")
    Speicher["Netto"] = Netto_Betrag.group(1)

if Brutto_Betrag :
    print(f"Brutto: {Brutto_Betrag.group()}")
    Speicher["Brutto"] = Brutto_Betrag.group(1)


print(Speicher)

#Speicher wird zum DataFrame umgewandelt
df = pd.DataFrame([Speicher])

#DataFrame wird in die .csv Datei geschriebenm
df.to_csv("Rechnungen.csv", index = False, sep =';' , encoding='utf-8-sig')




