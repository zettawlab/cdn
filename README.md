# cdn.zettaw.net

Static brand assets for Zettaw, served from this repo at `https://cdn.zettaw.net/`.

| Path | Brand | Colour |
|---|---|---|
| [`/com/`](com/) | **zettaw.com** — parent brand | Blue `#0085FC` |
| [`/ai/`](ai/) | **zettaw.ai** — AI sub-brand | Green `#1AB9AA` |

Both kits share one symbol and one file layout: `svg/` masters, `png/` exports, `web/` favicons + manifest.
Each kit's README has colours, clear space, minimum sizes and usage rules.

```html
<img src="https://cdn.zettaw.net/com/svg/zettaw-symbol.svg" alt="Zettaw" width="48">
<img src="https://cdn.zettaw.net/ai/svg/zettaw-ai-symbol.svg" alt="Zettaw AI" width="48">
```

## Logto

Assets for the Logto sign-in experience live in [`/logto/`](logto/):

| File | URL | Use |
|---|---|---|
| `logotype.svg` | `https://cdn.zettaw.net/logto/logotype.svg` | Sign-in page logo (old Baloo 2 wordmark, green) |
| `bg.jpg` | `https://cdn.zettaw.net/logto/bg.jpg` | Sign-in page background (3000×2000), set via custom CSS |

Moved from `logo/logotype.svg` and `background/authbg.jpg`; the old URLs no longer resolve.
