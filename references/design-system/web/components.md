# Eduface componentpatronen

Kant-en-klare bouwblokken op basis van `tokens.css`. Kopieer en pas tekst aan.
Alles gebruikt token-classes, dus alles blijft vanzelf consistent.

**Dit is de standaard manier van bouwen: React met Tailwind.** Bouw hier gewoon in, dat is het snelst. Alleen als Dante expliciet zegt dat iets naar Framer moet, schakel je over naar `framer.md`; daar staan de beperkingen die Framer oplegt.

Ruimte zit altijd op de parent (`flex flex-col gap-*`), nooit als losse marge op een child. Zie `core/compositie.md` punt 7: elke witruimte heeft één eigenaar.

---

## Knoppen

```jsx
// Primair (navy) - standaard actie
<button className="inline-flex items-center justify-center rounded-lg bg-primary px-5 py-2.5
                   text-sm font-medium text-primary-foreground transition
                   hover:opacity-90 focus-visible:outline-2 focus-visible:outline-ring">
  Boek een demo
</button>

// Accent (groen) - ALLEEN de hero-CTA, maximaal een per pagina.
// Overal anders is de knop navy. Groen = 'kijk hier', niet 'klik hier'.
<button className="inline-flex items-center justify-center rounded-lg bg-accent px-5 py-2.5
                   text-sm font-semibold text-accent-foreground transition hover:opacity-90">
  Probeer Eduface gratis
</button>

// Secundair (outline)
<button className="inline-flex items-center justify-center rounded-lg border border-border-strong
                   bg-background px-5 py-2.5 text-sm font-medium text-foreground transition
                   hover:bg-surface">
  Bekijk hoe het werkt
</button>
```

## Card

```jsx
<div className="flex flex-col gap-3 rounded-2xl border border-border bg-background p-6
                shadow-sm transition hover:shadow-md">
  <div className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-surface">
    {/* icoon */}
  </div>
  <h3 className="text-display-sm text-foreground">Snelle feedback</h3>
  <p className="text-base text-muted">
    Studenten krijgen binnen seconden onderbouwde feedback op hun werk.
  </p>
</div>
```

## Badge / label

```jsx
<span className="inline-flex items-center gap-1.5 rounded-full bg-surface px-3 py-1
                 text-xs font-medium text-green-deep">
  Nieuw
</span>
```

## Sectie-container (het ritme van de pagina)

```jsx
// Wikkel elke sectie hierin. Wisselt netjes wit / surface af.
<section className="px-6 py-20 md:py-28">
  <div className="mx-auto flex max-w-6xl flex-col gap-4">
    <p className="text-sm font-medium text-green-deep">Voor docenten</p>
    <h2 className="text-display-md text-foreground">Eén belofte per sectiekop</h2>
    <p className="max-w-2xl text-lg text-muted">
      Korte ondersteunende zin. Benefit plus hoe het werkt, net als Default.
    </p>
    {/* content / grid */}
  </div>
</section>
```

Tip: geef de ene sectie `bg-background` en de volgende `bg-surface` voor rustig contrast.

## Hero

```jsx
<section className="px-6 pt-24 pb-16 text-center md:pt-32">
  <div className="mx-auto flex max-w-4xl flex-col items-center gap-6">
    <h1 className="text-display-lg md:text-display-xl text-foreground">
      Betere feedback. Sneller nagekeken.
    </h1>
    <p className="max-w-2xl text-lg text-muted md:text-xl">
      Eduface geeft studenten directe, onderbouwde feedback en neemt docenten het nakijkwerk uit handen.
    </p>
    <div className="flex items-center justify-center gap-3">
      <button className="rounded-lg bg-accent px-6 py-3 text-sm font-semibold text-accent-foreground">
        Boek een demo
      </button>
      <button className="rounded-lg border border-border-strong px-6 py-3 text-sm font-medium text-foreground">
        Bekijk hoe het werkt
      </button>
    </div>
  </div>
</section>
```

## Navbar

```jsx
<header className="sticky top-0 z-50 border-b border-border bg-background/80 backdrop-blur">
  <nav className="mx-auto flex max-w-6xl items-center justify-between px-6 py-3">
    <span className="text-xl font-bold text-foreground" style={{ fontFamily: "var(--font-display)" }}>
      Eduface
    </span>
    <div className="hidden items-center gap-8 text-sm text-muted md:flex">
      <a href="/product" className="hover:text-foreground">Product</a>
      <a href="/docenten" className="hover:text-foreground">Voor docenten</a>
      <a href="/prijzen" className="hover:text-foreground">Prijzen</a>
      <a href="/blog" className="hover:text-foreground">Blog</a>
    </div>
    <button className="rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground">
      Boek een demo
    </button>
  </nav>
</header>
```

## Quote / testimonial

```jsx
<figure className="flex flex-col gap-4 rounded-2xl border border-border bg-surface p-8">
  <blockquote className="text-xl text-foreground">
    "Het scheelt ons docenten uren nakijkwerk per week."
  </blockquote>
  <figcaption className="text-sm text-muted">
    Naam, functie, universiteit
  </figcaption>
</figure>
```

---

## Vuistregels
- Knoppen: navy is de primaire knop. Groen is alleen de hero-CTA, maximaal één per pagina. Zie `core/regels.md`.
- Cards in een grid: zelfde radius, zelfde padding, zelfde schaduw. Altijd.
- Iconen: één set, één lijndikte, in `text-muted` of `text-green-deep`.
- Witruimte boven decoratie. Bij twijfel: meer ruimte, minder elementen.
