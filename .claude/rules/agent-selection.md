# Agent Selection

Kies altijd de meest specifieke skill/agent voor een taak. Val niet terug op een generieke `general-purpose` agent als er een specifieke skill bestaat die de taak dekt.

## Waarom dit belangrijk is
`general-purpose` op een hoog aandeel van het credit-verbruik is een teken dat een taak geen specifieke skill triggerde en er zelf een generic agent voor werd gespawnd. Dat is duurder en minder scherp dan de specifieke skill gebruiken.

## Hoe toe te passen
- Check eerst de skill-lijst voordat je een taak zelf oppakt of een generic agent spawnt.
- Match de taak expliciet op een bestaande skill/agent (bijv. persoon onderzoeken → `person-research`, batch personen → `shift-research`/agent 3, pijplijn-berichten → `outreach`/agent 4, losse mails buiten de pijplijn → `outreach`, enz.).
- **SHIFT-pijplijn: de markt gaat altijd mee.** De keten is `lead-sourcing` (1) → `contact-sourcing` (2) → `shift-research` (3) → `outreach` (4) → `lemlist-import` (5), en elk van die vijf leest het marktprofiel in `GTM/Campaigns/shift/markets/<code>/`. Noemt Dante geen markt, vraag het in één regel; geef de markt door aan elke subagent die je aanroept (`--markt <code>`). De oude `-nl`-skills zijn sinds 10-09-2026 vervangen en alleen nog een verwijzing.
- Noem de skill-naam expliciet in je eigen aanpak ("gebruik person-research voor...") in plaats van er impliciet omheen te werken.
- Gebruik `general-purpose` alleen als er écht geen skill past bij de taak.
