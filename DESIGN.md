---
name: CrediKNN
colors:
  surface: '#0e1511'
  surface-dim: '#0e1511'
  surface-bright: '#343b36'
  surface-container-lowest: '#09100c'
  surface-container-low: '#161d19'
  surface-container: '#1a211d'
  surface-container-high: '#242c27'
  surface-container-highest: '#2f3632'
  on-surface: '#dde4dd'
  on-surface-variant: '#bbcabf'
  inverse-surface: '#dde4dd'
  inverse-on-surface: '#2b322d'
  outline: '#86948a'
  outline-variant: '#3c4a42'
  surface-tint: '#4edea3'
  primary: '#4edea3'
  on-primary: '#003824'
  primary-container: '#10b981'
  on-primary-container: '#00422b'
  inverse-primary: '#006c49'
  secondary: '#adc6ff'
  on-secondary: '#002e6a'
  secondary-container: '#0566d9'
  on-secondary-container: '#e6ecff'
  tertiary: '#ffb2b7'
  on-tertiary: '#67001b'
  tertiary-container: '#ff7886'
  on-tertiary-container: '#780021'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#ffdadb'
  tertiary-fixed-dim: '#ffb2b7'
  on-tertiary-fixed: '#40000d'
  on-tertiary-fixed-variant: '#92002a'
  background: '#0e1511'
  on-background: '#dde4dd'
  surface-variant: '#2f3632'
typography:
  display-lg:
    fontFamily: Outfit
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Outfit
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Outfit
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Outfit
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.03em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-margin: 24px
  gutter: 16px
  section-gap: 64px
---

## Brand & Style
The design system is engineered for a high-end FinTech AI environment where precision meets prestige. The personality is **analytical and sophisticated**, designed to instill a sense of absolute control and technological superiority. 

The aesthetic blends **Modern Minimalism** with **Glassmorphism**. By utilizing a dark-mode-first approach, the system reduces cognitive load and emphasizes data visualization. Visual interest is generated through depth, light refraction, and subtle translucency, moving away from flat enterprise interfaces toward a more immersive, "command-center" experience.

## Colors
The palette is rooted in a deep **Slate Gray** foundation to establish a premium, high-contrast environment. 
- **Emerald Green (#10B981):** Reserved for high-confidence AI scores, approvals, and liquidity indicators.
- **Soft Blue (#3B82F6):** Used for interactive elements, data links, and neutral AI processing states.
- **Coral Red (#F43F5E):** A high-visibility accent for risk alerts, rejections, and critical financial anomalies.
- **Neutral Gradients:** Surfaces utilize a transition from Slate 900 to Slate 800 to create a sense of physical layering.

## Typography
The typography strategy leverages **Outfit** for headlines to provide a modern, geometric clarity that feels innovative. Its wide apertures ensure readability even at high weights. 

**Inter** is utilized for all functional and body text. Given the data-heavy nature of FinTech, Inter provides the necessary neutrality and "tabular lining" features required for reading numerical financial data and complex AI insights. Use `label-sm` with increased letter spacing for category headers and overlines to create a refined, editorial feel.

## Layout & Spacing
The layout follows a **12-column fluid grid** for desktop and a **4-column grid** for mobile. We employ an 8px rhythmic scaling system. 

To maintain the premium feel, generous whitespace (Section Gaps) is used between major data modules to prevent visual clutter. Cards and containers should use a standard 24px internal padding (`3x` base) to allow the glassmorphic background blurs to feel airy and unconstrained.

## Elevation & Depth
Depth is the primary communicator of hierarchy in this design system. 
- **Level 0 (Background):** Solid #0F172A.
- **Level 1 (Cards):** Semi-transparent Slate with a 12px Backdrop Blur. A subtle 1px white border at 10% opacity creates a "glass edge" effect.
- **Level 2 (Modals/Popovers):** Higher transparency, 20px Backdrop Blur, and a deep, diffused shadow (`offset: 0 20px, blur: 40px, color: rgba(0,0,0,0.4)`).
- **Light Source:** All gradients and glass highlights should behave as if a soft light source is positioned at the top-center of the screen.

## Shapes
The shape language is **Rounded**, balancing technical precision with approachability. 
- Standard components (Buttons, Inputs) use a **0.5rem (8px)** corner radius.
- Large containers and Glassmorphic cards use **1rem (16px)** to soften the overall UI.
- Feedback tags and status indicators should use "full-round" (Pill) shapes to distinguish them from interactive buttons.

## Components
### Buttons
Primary buttons use a solid Emerald Green fill with white text for maximum "Commit" visibility. Secondary buttons should use a "Ghost" style: a transparent fill with a 1px Soft Blue border that glows slightly on hover.

### Glass Cards
The signature component. Must include a `backdrop-filter: blur(12px)` and a linear gradient border from top-left (white @ 15%) to bottom-right (white @ 5%).

### Input Fields
Inputs are dark-filled (Slate 900) with a subtle bottom-only border that illuminates in Soft Blue when focused. The label should float or shrink to `label-sm` to maintain context.

### AI Risk Chips
Small, high-contrast badges. Use a low-opacity background of the status color (e.g., Red at 10%) with a high-saturation text color (Red at 100%) to ensure legibility within the dark theme.

### Micro-animations
All state transitions (hover, focus, active) must use a `200ms cubic-bezier(0.4, 0, 0.2, 1)` easing curve to simulate a high-performance, responsive engine.