# Handoff: 16 connectieverzoeken klaar voor Lemlist

_Voor de sessie die deze berichten in Lemlist zet. Bijgewerkt 2026-07-24._

## Wat naar Lemlist mag

**Precies 16 berichten.** Ze staan in **`projects/targetlijst-nl/lemlist-klaar.csv`**, met per rij: Naam, Organisatie, Functie, LinkedIn, Connectieverzoek, Tekens.

Dat is de enige bron voor de import. Elke rij is:
- een koud **LinkedIn-connectieverzoek** (geen mail), maximaal 300 tekens, taak = geaccepteerd worden
- door Dante persoonlijk goedgekeurd
- voorzien van een geverifieerde LinkedIn-URL (het harde veld voor Lemlist)

De 16: Thijs Groenen, Marcel van Marrewijk, Femke Bex, Conny Spijker, Marjolein Looij, Nynke Wagenaar, Janneke Deterink, Laura van Driel, Dineke van Voorthuijsen, Irma van der Velden, Ernst Eijsvogel, Jeroen van Dam, André Smits, Juliette Wildenburg, Rosa de Boer, Rutger van Hogezand.

## Wat NIET naar Lemlist mag

**Alleen de 16 uit `lemlist-klaar.csv`.** Alles daarbuiten is niet klaar. In `berichten-nl.csv` staat per rij een kolom **`Lemlist`** (Ja / Nee met reden). Alleen `Ja` gaat mee. Concreet niet meenemen:

- **De oude batch-1 concepten** (Cris van Osch, Annelies Pool, Niels Korst, Koos Gubbels, Selma de Nijs). Die staan op `concept` en zijn geschreven op een ouder model met een verkeerde productomschrijving en een opvolgbericht. Ze moeten eerst opnieuw. Niet versturen.
- **Claudia Peters** — vervallen, vervangen door Rutger van Hogezand als Wateropleidingen-ingang.
- **Alles met een niveau-1-haakje** en alles waar nog geen bericht voor ligt.
- **Organisaties die in Close staan of onder een moeder in Close vallen** (Salta/NCOI-familie, Capabel, Team Academy, Inholland, TMO). Die zijn geen koude outreach.

## Regels voor het verzenden zelf

- **Handmatig karakter behouden.** Dit zijn handgemaakte berichten in een kleine markt. Spreid de verzoeken over meerdere dagen, niet in één bak, anders is het zichtbaar als campagne en raakt het de LinkedIn-limieten.
- **Uitnodigingen met een noot** (de 300-tekens tekst) zitten op een strengere LinkedIn-teller dan kale verzoeken. Ga niet uit van onbeperkt.
- **Verzenden vanuit Dante's eigen LinkedIn** (Premium). Controleer of de Lemlist LinkedIn-stap op dat account draait.
- De tekst is exact zoals goedgekeurd. Niet automatisch laten herschrijven of "personaliseren" door Lemlist, dat breekt de zorgvuldig gekozen haakjes.

## Twee LinkedIn-URL's met een encoding-teken

Werken wel, maar zien er raar uit:
- Nynke Wagenaar: schone versie zonder emoji is `https://www.linkedin.com/in/nynke-wagenaar-b4954b67/` (de emoji-variant `%F0%9F%93%8A` brak eerder de scrape, gebruik de schone).
- André Smits: `https://www.linkedin.com/in/andr%C3%A9-smits-66bb35/` (de %C3%A9 is de é, klopt).

## Waar alles staat

- `projects/targetlijst-nl/lemlist-klaar.csv` — de 16, klaar voor import.
- `projects/targetlijst-nl/berichten-nl.csv` — alles, met de kolom `Lemlist` (Ja/Nee).
- Leesbare versie voor Dante: de Artifact "Connectieverzoeken NL" (bewerkbaar, met kopieerknoppen).
