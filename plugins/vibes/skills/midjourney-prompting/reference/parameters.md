# Complete Midjourney V7 Parameter Reference

## Core Parameters

### Aspect Ratio (--ar)

Controls image dimensions.

```
--ar 16:9    // Widescreen
--ar 2:3     // Portrait
--ar 1:1     // Square (default)
--ar 21:9    // Ultra-wide/cinematic
```

**Note**: Cannot use decimals. Use `--ar 139:100` instead of `--ar 1.39:1`.

---

### Stylize (--s or --stylize)

Controls how much Midjourney's artistic interpretation affects the image.

| Value | Effect |
|-------|--------|
| `--s 0` | Minimal artistic styling, closest to literal prompt |
| `--s 50` | Low styling, more control |
| `--s 100` | Default balance |
| `--s 250` | Increased artistic interpretation |
| `--s 500` | Heavy stylization |
| `--s 1000` | Maximum artistic expression |

**Tips**:
- Lower values for technical accuracy (photos, products)
- Higher values for artistic/creative work
- V6/V7 respond differently than V5 — experiment

---

### Chaos (--c or --chaos)

Controls variation between the four images in a grid.

| Value | Effect |
|-------|--------|
| `--c 0` | Very similar grid images (default) |
| `--c 25` | Moderate variation |
| `--c 50` | High variation |
| `--c 100` | Maximum variation |

**Use cases**:
- Low chaos: When you know exactly what you want
- High chaos: Exploring different interpretations

---

### Weird (--w or --weird)

Adds unusual, quirky, or unexpected aesthetics.

| Value | Effect |
|-------|--------|
| `--w 0` | Normal output (default) |
| `--w 250` | Subtle weirdness |
| `--w 1000` | Noticeable oddness |
| `--w 3000` | Maximum weirdness |

**Note**: Can produce unexpected results. Start low and increase gradually.

---

### Quality (--q or --quality)

Controls generation time and detail level.

| Value | Effect |
|-------|--------|
| `--q 0.25` | Fastest, lowest detail |
| `--q 0.5` | Quick, reduced detail |
| `--q 1` | Default quality |

**Note**: Higher values don't mean "better" — they mean more generation time. Default is usually fine.

---

### No (--no)

Excludes elements from the image.

```
--no text, watermark, frame
--no people
--no modern elements
```

**Important**:
- Words are interpreted separately: `--no red car` = no red AND no car
- Don't use "without" or "don't" in the prompt — they don't work
- Limit to essential exclusions

---

### Seed (--seed)

Sets the starting noise pattern for reproducibility.

```
--seed 12345
```

**Range**: 0 to 4294967295

**Use cases**:
- Reproduce or iterate on a specific result
- Create variations with consistent style
- A/B test prompt changes

---

### Tile (--tile)

Creates seamless, tileable patterns.

```
geometric pattern, blue and gold --tile
```

**Best for**: Textures, patterns, backgrounds

---

### Stop (--stop)

Stops generation partway through for softer, less detailed results.

```
--stop 50    // Stop at 50%
--stop 80    // Stop at 80%
```

**Range**: 10-100

---

## Style Parameters

### Style Raw (--style raw)

Reduces Midjourney's auto-beautification for more literal interpretation.

```
A still life arrangement --style raw
```

**When to use**:
- Photorealistic images
- When you have detailed, specific prompts
- When you want precise control

**When NOT to use**:
- Short, simple prompts (let MJ fill in gaps)
- Highly stylized artistic work

---

### Niji Mode (--niji)

Anime and Japanese illustration style.

```
warrior princess in battle --niji 6
```

**Niji 5 exclusive styles** (not available in Niji 6):
- `--style scenic`: Cinematic backgrounds
- `--style cute`: Chibi, adorable
- `--style expressive`: Emotional, detailed linework

**Niji 6**: Only supports default or `--style raw`

---

### Version (--v)

V7 is the default and recommended version.

```
--v 7      // Latest and default (V7)
```

Only use older versions if you have a specific reason:
```
--v 6.1    // V6.1 (older)
--v 6      // V6 (older)
```

---

### Draft Mode (--draft)

V7-exclusive feature for fast exploration at half cost.

```
A landscape scene --draft
```

**Use for**:
- Quick iterations and exploration
- Testing prompt concepts
- Finding the right direction before final quality

**Note**: 10x faster than standard mode.

---

## Reference Parameters

### Style Reference (--sref)

Copies visual style from an image.

**Basic usage**:
```
A forest scene --sref https://example.com/style-image.jpg
```

**Using SREF codes**:
```
A portrait --sref 5000
```

**Random style discovery**:
```
A cityscape --sref random
```

**Multiple style references**:
```
A scene --sref URL1 URL2 URL3
```

**Weighted style references**:
```
A scene --sref URL1::2 URL2::1
```

### Style Weight (--sw)

Controls strength of style reference.

| Value | Effect |
|-------|--------|
| `--sw 0` | Minimal style influence |
| `--sw 100` | Default |
| `--sw 500` | Strong style influence |
| `--sw 1000` | Maximum style influence |

---

### Character Reference (--cref)

Maintains character appearance across images.

**Basic usage**:
```
A wizard in a library --cref https://example.com/character.jpg
```

**Multiple characters** (blends features):
```
--cref URL1 URL2
```

### Character Weight (--cw)

| Value | Effect |
|-------|--------|
| `--cw 0` | Face only, different hair/clothes |
| `--cw 50` | Moderate consistency |
| `--cw 100` | Full consistency: face, hair, clothes (default) |

**Important**: Works best with Midjourney-generated characters. Real photos may distort.

---

### Image Weight (--iw)

Controls influence of image prompts.

```
[image_URL] A forest scene --iw 2
```

**Range**: 0-3 (V6/V7), 0-2 (V5)
**Default**: 1

---

## Personalization (--p)

Applies your trained aesthetic preferences.

**Requirements**: Rank ~200 image pairs on Midjourney's Personalize Page

```
A landscape --p
```

**Note**: Personalization is ON by default in V7.

---

## Multi-Prompts & Weights

### Double Colon (::)

Separates concepts for independent interpretation.

```
space ship     // Interpreted as "spaceship"
space:: ship   // Interpreted as "space" and "ship" separately
```

### Prompt Weights

```
forest::2 cabin::1        // Forest twice as important
ocean::3 sunset::2 boat::1
```

### Negative Weights

```
flowers::-0.5    // Reduces flowers (like --no)
```

---

## V7 Advantages

V7 is Midjourney's most capable model:

- **Superior prompt understanding** — More accurate complex prompt interpretation
- **Better coherence** — Improved hands, bodies, object relationships
- **Richer textures and details** — Higher quality output by default
- **Draft Mode** — 10x faster exploration at half cost
- **Personalization ON by default** — Applies learned preferences automatically
- **Omni Reference** — Enhanced reference capabilities

---

## Useful Commands

### /describe

Reverse-engineer prompts from any image.

1. Type `/describe`
2. Upload image
3. Receive 4 prompt suggestions

**Note**: Suggestions are guesses, not exact. Always review and refine.

### /shorten

Optimize long prompts by identifying essential words.

```
/shorten [your long prompt]
```

### /prefer remix

Enable Remix Mode for editing prompts during variations.

---

## Parameter Combinations

**Photorealism**:
```
--style raw --ar 2:3 --s 50
```

**Artistic freedom**:
```
--stylize 500 --chaos 25
```

**Consistent character series**:
```
--cref [URL] --cw 100 --seed [number]
```

**Style exploration**:
```
--sref random --sw 500 --c 50
```

**Seamless textures**:
```
--tile --style raw --ar 1:1
```
