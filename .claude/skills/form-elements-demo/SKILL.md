---
name: form-elements-demo
description: Reference for the Form Elements group of the Figma "Design system" file. Lists which form components exist (Label, Field, Input, Menu, Dropdown, Checkbox, Radio button, Switch, Text area), the variants of each, their configurable properties, and how variants, properties and nested components relate. Use when building, specifying, reviewing or translating a form UI from this design system, or when asked what a form component can do. Covers ONLY the Form Elements group, nothing from Navigation or Data Display.
---

# Form Elements (design system reference)

Source: Figma file `zJIq8btF3pbDe5oVU6RxFE` ("Design system"), the pages between the divider **➡️ Form Elements** (`55:2624`) and the divider **➡️ Navagation** (`55:2649`). Read from the file on 2026-11-16. If the file changed since, re-read it before trusting this.

Scope rule: only the nine components below belong to this group. If a request needs a button, link, badge, table or anything else, it is outside this skill. Say so instead of guessing its variants.

## Vocabulary

- **Variant property**: a dropdown on the component set (Status, Type, Property). Picking values selects one prebuilt variant. Changes appearance or state.
- **Component property**: an override on an instance. Three kinds appear here: **TEXT** (editable string), **BOOLEAN** (show or hide a part), **INSTANCE_SWAP** (replace a nested icon).
- **Component set** vs **standalone component**: a set holds variants and exposes variant properties. A standalone component has no variants, only component properties.
- Names starting with a dot (`.menu item`, `.Check box item`, `.Radio button item`, `.switch item`, `.text area item`) are the **inner building blocks**. They hold the variants. The un-dotted wrapper (label, menu, text area) is what you normally place.
- In the Plugin API a component property key carries an id suffix, for example `Label#27:27`. The display name is the part before `#`. A leading `↓` in a name (for example `↓ Content`) is a naming convention for a text property that belongs to the toggle above it. That reading is inferred from the names, the file has no descriptions.

## Component map

| Component | Type | Variant properties | Component properties |
|---|---|---|---|
| Label | set, 3 variants | Status: Default, Required | none |
| Field | set, 12 variants | Status: Default, Hover, Focus, Disabled. Property: Default, Filled, Error | Label (text), Icon left (swap), Icon left (bool), Icon right (swap), Icon right2 (bool) |
| Input | set, 2 variants | Type: Default, Email | Hint copy (bool), ↓Hint copy (text) |
| .menu item | set, 6 variants | Status: Default, Hover, Disabled. State: Unselected, Selected | Label (text), Icon (bool), ↓ Icon (swap) |
| Menu | standalone | none | Scrollbar (bool) |
| Dropdown | standalone | none | none |
| .Check box item | set, 8 variants | Status: Default, hover, Focus, Disabled. Type: Unselected, Selected | none |
| Check box label | standalone | none | Label (bool), ↓ Content (text) |
| .Radio button item | set, 8 variants | Status: Default, Focus, Hover, Disabled. Type: Unselected, Selected | none |
| Radio button label | standalone | none | Content (bool), ↓ Content (text) |
| .switch item | set, 8 variants | Status: Default, Hover, Focus, Disabled. Type: Unselected, Selected | none |
| Switch label | standalone | none | Label (bool), ↓ Content (text) |
| .text area item | set, 8 variants | Status: Default, Hover, Focus, Disabled. Type: Default, Filled | none |
| Text area | standalone | none | Hint copy (bool), ↓ Hint copy (text), Character count (bool), ↓character count (text) |

Defaults: first value listed is the default for variant properties. Component property defaults are in the sections below.

## Components in detail

### Label
- Variants: `Status=Default`, `Status=Required`. Required is the marked-as-mandatory version (the Label page includes an asterisk element for it).
- Contains the label text and a help icon. No component properties, so change the text by editing the text layer inside the instance.
- Used inside Input, Dropdown and Text area. Not meant for checkbox, radio or switch, those carry their own text.

### Field
The bare input box (no label, no hint). Size 325 x 44.
- Variants: every combination of `Status` x `Property` exists (4 x 3 = 12).
  - `Status`: Default, Hover, Focus, Disabled. These are interaction states.
  - `Property`: Default (empty), Filled (has a value), Error. This is content state, not interaction state. A field can be Hover and Error at the same time (`Status=Hover, Property=Error`).
- Properties:
  - `Label` (text, default "Placeholder"): the text shown inside the box, despite the name. It is the placeholder or value, not the label above the field.
  - `Icon left` (bool, default true) with `Icon left` (swap) for the icon. The boolean's name has a trailing space in the file.
  - `Icon right2` (bool, default true) with `Icon right` (swap). The boolean is named "Icon right2" in the file.
- The booleans show or hide the icon, the swaps choose which icon. Toggle the boolean first, swap second.

### Input
Label + Field + optional hint, stacked. Size 325 x 73 without hint.
- Variants: `Type=Default`, `Type=Email`. Email is the same layout with a leading email icon in the field and sample email copy. Only the content differs, so for a real email field you can also start from Default and set the icon and text yourself.
- Properties: `Hint copy` (bool, default false), `↓Hint copy` (text, default "Hint copy").
- The Field inside is a nested instance. Its Status and Property variants are **not** exposed on Input. To show hover, focus, disabled, filled or error, override the nested Field instance.
- The nested Label instance works the same way (Required is set on the nested Label).

### Menu
A list container for options. Size 199 x 270.
- Standalone, one property: `Scrollbar` (bool, default false). The scrollbar element exists but is hidden by default.
- Contains six `.menu item` instances in a container.
- `.menu item` variants: `Status` (Default, Hover, Disabled) x `State` (Unselected, Selected) = 6. There is **no Focus** variant for menu items.
  - Status is interaction, State is whether the option is the chosen one.
  - Properties: `Label` (text, default "Menu"), `Icon` (bool, default true), `↓ Icon` (swap, default a circle-arrow icon).
- Each item's variants are overridden on the nested item instance, not on Menu.

### Dropdown
Standalone, no component properties and no variants.
- Composition: an **Input** instance (Type=Default, hint copy off, right icon swapped to a drop arrow) on top of a **Menu** instance.
- Everything is configured through the nested Input, Field, Label, Menu and menu item instances. The Dropdown shows the open state (menu visible). The file has no separate closed variant.

### Check box (item + label)
- `.Check box item` is a 40 x 40 box. Variants: `Status` (Default, hover, Focus, Disabled) x `Type` (Unselected, Selected) = 8. Note the option is spelled lowercase `hover` here.
- `Check box label` is the placeable component: item + text. Properties: `Label` (bool, default true), `↓ Content` (text, default "Hello").
- Status and Type of the nested item are not exposed on the label component. Override the nested `.Check box item` instance to set them.

### Radio button (item + label)
- `.Radio button item`: 40 x 40. Variants: `Status` (Default, Focus, Hover, Disabled) x `Type` (Unselected, Selected) = 8.
- `Radio button label`: item + text. Properties: `Content` (bool, default true), `↓ Content` (text, default "Hello"). Same nested-override rule as the checkbox.

### Switch (item + label)
- `.switch item`: 80 x 40. Variants: `Status` (Default, Hover, Focus, Disabled) x `Type` (Unselected, Selected) = 8.
- `Switch label`: item + text. Properties: `Label` (bool, default true), `↓ Content` (text, default "Hello"). Same nested-override rule.
- For switch, `Type=Selected` means on, `Unselected` means off.

### Text area
Multi-line input. Size 342 x 280.
- Composition: Label instance, hint text, `.text area item`, character count text.
- Properties: `Hint copy` (bool, true), `↓ Hint copy` (text, "Hint copy"), `Character count` (bool, true), `↓character count` (text, "Character count 7/120").
- `.text area item` variants: `Status` (Default, Hover, Focus, Disabled) x `Type` (Default, Filled) = 8, each 342 x 184. Default is empty, Filled has content.
- Status and Type are overridden on the nested `.text area item` instance.

## How variants and properties relate

1. **Variants answer "what state is it in".** Status is the interaction state (Default, Hover, Focus, Disabled). A second variant property says what the control holds: Type (Selected or not, Email or not, Default or Filled) or Property (Default, Filled, Error) on Field, State on menu items.
2. **Properties answer "what does it contain".** Text edits the words, booleans show or hide a part, swaps change an icon. They never change the state.
3. **Variants and properties are independent.** Any property setting can be combined with any variant. The one dependency is visual: a BOOLEAN hides its paired TEXT or SWAP, so set the boolean on first.
4. **Wrappers hide the variants of what they contain.** Input, Dropdown, Text area and the three `... label` components nest an item that owns the variants. The wrapper exposes only its own properties. To change a state, reach into the nested instance.
5. **Composition chain:**
   - Input = Label + Field (+ hint)
   - Dropdown = Input + Menu
   - Menu = `.menu item` x 6 (+ scrollbar)
   - Text area = Label + `.text area item` (+ hint, character count)
   - Check box label, Radio button label, Switch label = item + text

## Choosing a component (judgement, not stated in the file)

- One line of text: Input. Same plus a fixed set of options: Dropdown. Several lines: Text area.
- Pick one of several: Radio button. Pick any number: Check box. Immediate on or off: Switch.
- Field alone is a building block. Prefer Input unless a label and hint are truly not wanted.

## Known quirks in the source file

Report these instead of silently working around them:
- Label has a duplicated `Status=Default` variant on its page. The set resolves to the two options Default and Required.
- Text area item has an extra variant option spelled `Focu` (a typo). The focused Filled variant is named `Status=Focu, Type=Filled`, the focused Default one is `Status=Focus, Type=Default`.
- Check box item uses lowercase `hover`, the others use `Hover`.
- Field boolean names are `Icon left ` (trailing space) and `Icon right2`.
- No component carries a description in Figma, so none of the usage guidance above comes from the file's authors.
- Menu items have no Focus state.

## How to answer with this skill

- Name components exactly as in the map, including the dot prefix for inner items.
- State the variant as `Property=Value` pairs, for example `Status=Hover, Property=Error`.
- Say which instance a change belongs to (wrapper or nested item).
- If asked for something not in this group, say it is outside Form Elements.
