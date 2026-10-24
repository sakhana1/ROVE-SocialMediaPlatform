---
name: Editorial Plum
colors:
  surface: '#fff7fc'
  surface-dim: '#e9d3ee'
  surface-bright: '#fff7fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#feefff'
  surface-container: '#fce7ff'
  surface-container-high: '#f8e1fd'
  surface-container-highest: '#f2dbf7'
  on-surface: '#24162a'
  on-surface-variant: '#4c4451'
  inverse-surface: '#3a2b40'
  inverse-on-surface: '#fdebff'
  outline: '#7d7483'
  outline-variant: '#cec3d3'
  surface-tint: '#7b42b1'
  primary: '#56178c'
  on-primary: '#ffffff'
  primary-container: '#6f35a5'
  on-primary-container: '#deb8ff'
  inverse-primary: '#deb7ff'
  secondary: '#765181'
  on-secondary: '#ffffff'
  secondary-container: '#f3c5fe'
  on-secondary-container: '#734e7e'
  tertiary: '#7c0030'
  on-tertiary: '#ffffff'
  tertiary-container: '#9e1e45'
  on-tertiary-container: '#ffb2bf'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0dbff'
  primary-fixed-dim: '#deb7ff'
  on-primary-fixed: '#2c0050'
  on-primary-fixed-variant: '#622698'
  secondary-fixed: '#f9d8ff'
  secondary-fixed-dim: '#e4b7ef'
  on-secondary-fixed: '#2d0c3a'
  on-secondary-fixed-variant: '#5c3968'
  tertiary-fixed: '#ffd9de'
  tertiary-fixed-dim: '#ffb2be'
  on-tertiary-fixed: '#3f0015'
  on-tertiary-fixed-variant: '#8d0d3a'
  background: '#fff7fc'
  on-background: '#24162a'
  surface-variant: '#f2dbf7'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.03em
  headline-xl:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-lg:
    fontFamily: DM Sans
    fontSize: 15px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-md:
    fontFamily: DM Sans
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: DM Sans
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-lg: 2rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system delivers an editorial, desktop-first social discovery experience. Designed for tastemakers, visual creators, and modern digital curators, it elevates media consumption above chaotic engagement algorithms into an intentional, gallery-like space.

The aesthetic philosophy bridges modern Scandinavian minimalism with high-end editorial publishing:
- Generous breathing room framing high-resolution imagery and video.
- Deep, regal plum tones replacing generic indigo/blue tech palettes to evoke craftsmanship, luxury, and intimacy.
- Tactile, crisp layout boundaries that give media items the structured permanence of physical magazine prints while maintaining frictionless digital fluidity.

## Colors

The palette relies on deep plum foundations, vibrant purple focal points, and soft lavender surfaces to achieve an intimate yet energetic atmosphere.

### Functional Roles
- **Primary Action Purple (`#6F35A5`)**: High-priority interactive triggers, active tab indicators, and primary call-to-action states.
- **Primary Plum (`#4A2856`)**: Structural brand anchors, prominent headers, and high-emphasis brand moments.
- **Lavender Accent (`#F3EAFE`)**: Subtle tinting for active pill backgrounds, hover fills, badge backplates, and selection states.
- **Like Accent (`#E05275`)**: Dedicated purely to affective micro-interactions (hearts, saved reactions, curated favorites).
- **Background & Surface**: `#FAF9FC` serves as the canvas ground to eliminate harsh monitor glare, while pure `#FFFFFF` elevates content cards, persistent panels, and media containers.
- **Borders & Dividers (`#EEE8F1`)**: Hairline boundaries framing feeds, modals, and persistent navigation bars.
- **Text Tiers**: `#2E2034` provides deep contrast for primary editorial text without harsh pure-black rigidity; `#8C8193` softens timestamps, labels, and secondary metadata.
- **System States**: `#2E8555` signifies verification and success; `#D33F49` handles warnings, destructive actions, and input validation failures.

## Typography

Typography establishes an editorial rhythm through a dual-type architecture:
- **Headings & Display (`Manrope`)**: Geometric warmth with tight tracking provides structural character for navigation identities, section headers, user profile titles, and the wordmark.
- **Body (`Inter`)**: Precision clarity and exceptional x-height optimize caption reading, multi-line comment threads, and settings panels.
- **Controls & Navigation Labels (`DM Sans`)**: Balanced tracking gives crisp distinction to sidebars, chips, interactive buttons, and compact contextual timestamps.

## Layout & Spacing

The layout is built for expansive desktop canvases, anchoring workflow and exploration through clear architectural pillars:

### Grid & Breakpoints
- **Desktop (1280px+)**: A persistent 260px left sidebar anchors navigation. The main content zone utilizes a centered feed (max-width: 680px for single-column feed, or up to 960px when paired with a contextual auxiliary rail for suggested accounts, trending hashtags, or direct message previews). Grid layouts (Explore, Profile media) follow a rigid 3-column configuration with 24px gutters.
- **Tablet (768px - 1279px)**: The left sidebar condenses to an 80px icon-only vertical utility strip. Feed margins compress to 24px, maintaining a single-column layout.
- **Mobile (< 768px)**: Reflows into a top persistent navigation bar with a bottom utility navigation dock. Margins reduce to 16px, edge-to-edge media cards eliminate lateral container radius.

### Spacing Philosophy
Rhythm follows an 8px spatial module. Micro-elements (icon-to-text, avatar-to-handle) rely on 8px (`space-sm`), component-internal cushions use 16px (`space-md`), and structural modules (card-to-card, feed sections) breathe across 24px to 40px intervals (`space-lg` to `space-xl`).

## Elevation & Depth

This system avoids heavy, dark drop shadows, adopting an airy, multi-planar depth model constructed through hairline borders, ambient plum-tinted shadows, and translucent frosted backdrops.

### Surface Tiers
- **Flat Ground (`#FAF9FC`)**: The overall viewport canvas.
- **Base Level (`#FFFFFF`)**: Static cards, sidebar frame, and content wells bordered by a crisp `1px solid #EEE8F1`.
- **Raised (`box-shadow: 0 4px 20px -2px rgba(46, 32, 52, 0.05)`)**: Feed cards on scroll, active post hover states, contextual popovers, and sticky header bars.
- **Overlay & Modals (`box-shadow: 0 20px 48px -4px rgba(46, 32, 52, 0.12)`)**: Lightboxes, full-screen post inspector, and story carousels. Modals sit atop a frosted backdrop (`rgba(46, 32, 52, 0.45)` with `backdrop-filter: blur(12px)`).

## Shapes

The interface embraces a tailored curved visual language ranging between 10px and 16px:
- **Small Controls (Buttons, Inputs, Badges)**: 10px to 12px for an approachable yet refined touch.
- **Containers (Feed Cards, Dialogs, Floating Bars)**: 16px corner radii to frame visual media softly without cutting into photo aspect ratios.
- **Interactive Avatars & Status Pills**: Full circular curvature (`rounded-full` / 9999px) to establish visual contrast against rectangular media containers.

## Components

### Persistent Navigation Sidebar
- **Layout**: Fixed left edge, 260px wide, height 100vh, bordered along the right edge with `1px solid #EEE8F1`.
- **Wordmark**: ROVE set in `Manrope` ExtraBold, 22px, tracking -0.03em, colored `#4A2856`, seated at the top with 32px vertical breathing room.
- **Nav Items**: Height 48px, 12px horizontal padding, 12px corner radius. Inactive: `#2E2034` with 20px stroked icons. Hover: `#FAF9FC`. Active: `#F3EAFE` background with `#6F35A5` bold typography and solid filled icon glyphs.

### Buttons & CTAs
- **Primary**: Background `#6F35A5`, text `#FFFFFF`, 12px radius, font `DM Sans` 14px semi-bold. Subtle hover lift with background transition to `#4A2856`.
- **Secondary / Outlined**: 1px border `#EEE8F1`, background `#FFFFFF`, text `#2E2034`. Hover state shifts background to `#F3EAFE` and border to `#6F35A5`.
- **Ghost / Icon**: Transparent ground, 40px x 40px bounding box, hover state `#FAF9FC`, active scale transform 0.96.

### Media Feed Card
- **Structure**: Surface `#FFFFFF`, 16px border-radius, hairline border `1px solid #EEE8F1`, ambient lift shadow.
- **Header**: 56px height, displaying a 36px circular avatar with an optional gradient story ring, handle, location metadata, and trailing contextual menu trigger (`...`).
- **Media Well**: Aspect ratio 1:1, 4:5, or 16:9 with edge-to-edge frame fitting within the top card boundary.
- **Action Rail**: 48px height, housing Like (`#E05275` when active), Comment, Share, and trailing Bookmark toggle.

### Input Fields & Search Bar
- **Top Search Bar**: Height 42px, background `#FAF9FC`, border `1px solid #EEE8F1`, 12px border radius, leading search lens icon in `#8C8193`, placeholder text `#8C8193`. Focus shifts background to `#FFFFFF`, border to `#6F35A5`, and renders an ambient lavender glow ring (`0 0 0 3px #F3EAFE`).

### Chips & Filter Pills
- **Style**: Height 32px, 16px radius, padding 0 14px. Default state: background `#FFFFFF`, border `1px solid #EEE8F1`, text `#8C8193`. Selected state: background `#4A2856`, border `1px solid #4A2856`, text `#FFFFFF`.

### Checkboxes & Radios
- **Style**: 18px dimensions, 6px radius (checkbox) or circular (radio), border `1.5px solid #8C8193`. Checked state fills `#6F35A5` with a crisp `#FFFFFF` checkmark indicator.