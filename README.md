# cdn.zettaw.net

Static brand assets for Zettaw, served from this repo at `https://cdn.zettaw.net/`.

| Path | Brand | Colour |
|---|---|---|
| [`/logo/com/`](logo/com/) | **zettaw.com** — parent brand | Blue `#0085FC` |
| [`/logo/ai/`](logo/ai/) | **zettaw.ai** — AI sub-brand | Green `#1AB9AA` |

Brand logos live under `/logo/`. Both kits share one symbol and one file layout: `svg/` masters (horizontal, stacked, symbol, wordmark), `png/` exports, `web/` favicons + manifest.
Each kit's README has colours, clear space, minimum sizes and usage rules.

```html
<img src="https://cdn.zettaw.net/logo/com/svg/zettaw-horizontal.svg" alt="Zettaw" height="40">
<img src="https://cdn.zettaw.net/logo/ai/svg/zettaw-ai-horizontal.svg" alt="Zettaw AI" height="40">
```

## Logto

Assets for the Logto sign-in experience live in [`/logto/`](logto/):

| File | URL | Use |
|---|---|---|
| `logotype.svg` | `https://cdn.zettaw.net/logto/logotype.svg` | Sign-in page logo (horizontal lockup, green — copy of `logo/ai/svg/zettaw-ai-horizontal.svg`) |
| `bg.jpg` | `https://cdn.zettaw.net/logto/bg.jpg` | Sign-in page background (3000×2000), set via custom CSS |

Moved from `logo/logotype.svg` and `background/authbg.jpg`; the old URLs no longer resolve.
