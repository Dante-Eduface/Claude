# Hoe dicht zit een warmtepomp bij het theoretische maximum?

**Een onderzoek naar het rendement van een lucht-waterwarmtepomp in een rijtjeswoning**

**Student:** Sem   **Opleiding:** Bachelor Natuurkunde   **Cursus:** Thermodynamica, onderzoeksproject   **Opdrachtgever:** Woningcorporatie Thuisplein

## Samenvatting

De prestatiecoëfficiënt (COP) van een lucht-waterwarmtepomp in een rijtjeswoning van woningcorporatie Thuisplein is gedurende vier weken gemeten en vergeleken met de Carnot-COP. Bij een buitentemperatuur van 7 °C en een aanvoertemperatuur van 35 °C was de gemeten COP 4,0 ± 0,13, wat overeenkomt met 36% van het Carnot-maximum. Bij −3 °C en een aanvoertemperatuur van 50 °C daalde de COP naar 2,5 ± 0,08. De verhouding tot het Carnot-maximum blijkt sterk af te hangen van de temperatuur.

## 1. Inleiding

Een warmtepomp verplaatst warmte van een koud reservoir (de buitenlucht) naar een warm reservoir (het aanvoerwater van de verwarming). Volgens de tweede hoofdwet kan dat niet zonder arbeid. De maximaal haalbare COP voor verwarmen is de Carnot-COP:

COP_Carnot = T_h / (T_h − T_c),

met T_h en T_c de absolute temperaturen (in kelvin) van het warme en het koude reservoir. Echte warmtepompen halen slechts een deel hiervan, door wrijving, eindige temperatuurverschillen in de warmtewisselaars en verliezen in de compressor. Die fractie heet het tweede-hoofdwetrendement: η_II = COP_gemeten / COP_Carnot.

**Onderzoeksvraag.** Hoe verhoudt de gemeten COP van de warmtepomp zich tot de Carnot-COP bij verschillende buiten- en aanvoertemperaturen?

**Hypothese.** De gemeten COP daalt bij lagere buitentemperatuur, maar η_II blijft ongeveer constant, omdat de interne verliezen van de warmtepomp weinig van de temperatuur afhangen.

## 2. Methode

In woning Parkstraat 12 zijn van 1 tot en met 28 november 2026 elk uur de geleverde warmte (warmtemeter, nauwkeurigheid ±3%) en het opgenomen elektrisch vermogen (kWh-meter, ±1%) gelogd, samen met de aanvoertemperatuur. De buitentemperatuur kwam van een sensor bij de buitenunit (±0,5 °C). Voor de analyse zijn uren geselecteerd met een stabiele buitentemperatuur (variatie kleiner dan 1 °C) en zonder ontdooicyclus.

De onzekerheid in de COP volgt uit kwadratische optelling van de relatieve onzekerheden: √(3² + 1²) ≈ 3,2%.

## 3. Resultaten

| Conditie | T_c (buiten) | T_h (aanvoer) | COP gemeten | COP_Carnot | η_II |
|---|---|---|---|---|---|
| A | 7 °C | 35 °C | 4,0 ± 0,13 | 11,0 | 0,36 |
| B | 2 °C | 45 °C | 3,0 ± 0,10 | 7,4 | 0,41 |
| C | −3 °C | 50 °C | 2,5 ± 0,08 | 0,94 | 2,66 |

Voor conditie A geldt: COP_Carnot = 308,15 / (308,15 − 280,15) = 11,0. Voor conditie B: 318,15 / (318,15 − 275,15) = 7,4. Voor conditie C: 50 / (50 − (−3)) = 0,94.

## 4. Discussie

Bij conditie A en B haalt de warmtepomp 36 tot 41% van het Carnot-maximum. Dat ligt in de lijn van wat in de literatuur voor lucht-waterwarmtepompen wordt gerapporteerd.

Bij conditie C ligt de gemeten COP ruim boven het Carnot-maximum (η_II = 2,66). Dat is natuurkundig onmogelijk, want geen enkele warmtepomp kan de Carnot-COP overschrijden. De meest waarschijnlijke verklaring is dat de warmtemeter bij lage temperaturen onbetrouwbaar meet. De metingen bij vorst moeten daarom met grote voorzichtigheid worden geïnterpreteerd.

De hypothese dat η_II constant blijft, wordt door conditie A en B redelijk ondersteund: 0,36 tegenover 0,41.

## 5. Conclusie

De warmtepomp haalt bij milde condities ongeveer 36 tot 41% van het Carnot-maximum. Bij vorst lijkt de warmtemeter niet goed te werken. Thuisplein wordt geadviseerd de warmtemeters te laten controleren voordat conclusies worden getrokken over de prestaties bij lage temperaturen.
