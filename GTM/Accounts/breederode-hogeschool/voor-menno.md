# Breederode: wat is er verkocht, wat moet er staan

_Voor Menno, via Jeroen. Opgesteld 10-09-2026 op basis van de gespreksopnames van 1 en 3 september. Bijgewerkt 23-09-2026 met wat er op de testochtend bij kwam._

**Situatie:** Breederode Hogeschool (Rotterdam, ruim 800 cursisten, onderdeel van Calder Holding). Testochtend op locatie op **woensdag 23 september**, daarna twee weken test, beoogde **go-live 15 oktober** in itslearning. LMS is Fronter/itslearning, ze hebben LTI.

## 1. Blokkerend voor go-live op 15 oktober
1. **LTI-integratie met itslearning/Fronter.** Toegezegd als "twee weken werk na de testperiode". Hebben we dit eerder gedaan op itslearning, of is dit de eerste?
2. **Meerdere onafhankelijke beoordelaars op dezelfde inzending**, elk met eigen login en eigen complete marking. Hun mastertheses en portfolio's werken standaard met het vier-ogenprincipe, dus zonder dit kan de grootste use case niet live.
3. **Tijdregistratie van actieve lees- en feedbacktijd per docent.** Is als bestaande functie genoemd en is nu een **afgesproken succescriterium** van de test. Zonder meting kunnen we de test formeel niet afronden.

## 1b. Nieuw sinds de testochtend van 23 september

_Bijgewerkt na het debriefgesprek met Jeroen op 23-09. Signing date staat op 1 oktober, go-live 15 oktober._

17. **Per docent loggen welk cijfer die gaf.** Bij hun vier-ogenprincipe kijken twee docenten dezelfde inzending na, allebei met feedback en cijfer, en komen ze aan het eind samen tot een consensuscijfer. Jeroens route daarvoor is `sync to LMS: feedback only`, zodat de student wel de feedback ziet en nog niet het cijfer. Dat is gedekt. Wat ontbreekt: als beide docenten in dezelfde tool het cijfer aanpassen, moet loggbaar zijn **wie welk cijfer gaf**, anders is het consensusmoment blind. Dante heeft Breederode gezegd dat we dit kunnen.

18. **Testomgeving bij itslearning.** Samuel heeft de aanvraagmail al, Dante forwardt die naar Maud bij Breederode, zij zet de omgeving op. Twee dingen voor Samuel: wat heb je in die omgeving nodig, en hoe lang moet hij blijven staan? Breederode denkt dat een permanente testomgeving geld kost, wij zeggen dat dat bij andere LMS'en niet zo is. Nog niet dicht.

19. **Rolverdeling voor externe docenten in itslearning.** Er zitten veel externe docenten in vakken die ze niet allemaal horen te zien. De rechten moeten kloppen voordat dit live gaat. Randvoorwaarde voor go-live.

20. **Kan de formulering van inline comments aangestuurd worden via de modelinstructies?** Bij de kalibratie van 22-09 lukte alles behalve dit: het voorbeeld van de docent stond letterlijk in de instructies en het model formuleerde het toch net anders. Dante zegt dat het niet kan, Jeroen zegt van wel. Graag een hard antwoord, want het raakt de kalibratiebelofte.

21. **Wat kan er wel en niet via de modelinstructies?** Breederode denkt dat ze er meer mee kunnen dan het model aankan. Dante maakt een lijst en deelt die met ze. Hulp vanuit engineering scheelt hem veel testwerk en voorkomt dat de test op verwachtingen stukloopt.

## 2. Ja of nee: bestaat dit al in de tool?
4. Beoordelingsformulier automatisch omzetten naar succescriteria, inclusief het zelf genereren van de schaal (1-10 of voldoende/onvoldoende).
5. Per vak of opdracht instellen of de docent het AI-cijfer ziet vóór of pas ná complete marking.
6. Midden in een nakijkronde het model bijstellen en alleen de nog niet afgeronde opdrachten opnieuw laten nakijken.
7. Frequentie van formatieve feedback instelbaar **per rubriekonderdeel** (schrijfvaardigheid onbeperkt, inhoud één keer per week).
8. Rubriekelement met 0% weging: wel feedback, geen invloed op het cijfer.
9. Feedback plus annotaties exporteren of downloaden als document.
10. **Academic Integrity checker**: staat bij ons als beta, is bij Breederode gepresenteerd als iets waar veel instellingen voor kiezen. Wat kan die vandaag echt?

## 3. Verkocht als mogelijkheid, mag na de pilot, maar staat wel op hun netvlies
11. Structurele scoreverschillen tussen docenten zichtbaar maken ("die scoort structureel laag op dit criterium"). Dit is de belangrijkste wens van hun opleidingsmanager en het argument waarmee hun directeur naar Calder gaat.
12. Signaleren welke opdrachten in een kalibratiesessie besproken moeten worden.
13. Toetsanalyse met P-waarden en RIT/RIR. Zij denken dat we dit al hebben, wij hebben dat in het gesprek niet weersproken.
14. Beoordelaar-ID's met een signaal als één docent te vaak dezelfde student beoordeelt.
15. Signaal wanneer een docent de nakijktermijn overschrijdt.
16. Historische opdrachten opnieuw door het model halen om het effect van een toetswijziging te meten.

## 3b. Gevraagd op 23 september, afgekaderd als "hebben we nog niet"

Geen harde toezegging, wel op hun verlanglijst.

22. **Context uit het LMS, inclusief kennisclips.** Dit is de belangrijkste van de lijst, want er is plenair gezegd dat Eduface alle context uit het LMS leest en dat klopt niet. Zij hebben veel kennisclips en stelden zelf voor de transcriptie onder de video te zetten. Vraag: kunnen we die beschrijving onder een video wel inlezen? Video's zelf lezen we nu niet. Jeroen staat achter het bouwen hiervan en het punt komt ook uit de Bath Spa-lessen.
23. **Literatuur van de student uitlezen.** De bronnen die een student in zijn opdracht gebruikt direct laten controleren. Jeroen zegt dat dit ooit gebouwd is in een extern project door een student van Menno. Is daar nog iets van over? Dezelfde use case kwam eerder langs bij de Wageningen-lead via SURF.
24. **Snelle opmerkingen uploaden.** Een docent uploadt zijn eigen opgebouwde bestand met snelle opmerkingen, Eduface haalt daar de opmerkingen uit. Geen Excel, eerder een Google Doc. Dante heeft gezegd dat we hieraan werken.
25. **Groei van de student over drie formatieve rondes.** In één oogopslag zien welke feedback er per ronde gegeven is en of de student die verwerkt heeft.
26. **Andere beoordelingsstijlen**, bijvoorbeeld 3 achievement levels in plaats van 4. Klein, en toegezegd als "dat kunnen we toevoegen".

## 4. Eén claim om te verifiëren
"Wij hebben al honderdduizenden beoordelingsformulieren gezien." Klopt die orde van grootte?

## 5. Wat we al goed hebben afgekaderd, geen werk aan
- Alleen PDF en DOCX. Complexe Excel en SPSS kan niet, dat is expliciet gezegd.
- Geen plagiaatchecker.
- Geen automatische niveau-inschaling (mbo/bachelor/master).
