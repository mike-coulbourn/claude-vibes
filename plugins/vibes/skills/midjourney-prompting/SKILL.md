---
name: midjourney-prompting
description: Use when writing, fixing, or refining Midjourney prompts in any style, including photography, illustration, anime, and fine art, or when choosing Midjourney parameters and reference images. Keywords - Midjourney, MJ prompt, --ar, --stylize, --chaos, --sref style reference, character and omni reference, lighting and camera terms, image generation prompt.
---

# Midjourney Prompting Guide

> **Version note, last verified September 2026.** The current default is V8.2, and this guide covers V7, V8.1, V8.2, and Niji 7. Midjourney ships new versions a few times a year, so if the user names a newer one, or a parameter behaves unexpectedly, check https://docs.midjourney.com with WebSearch before relying on a version-specific claim here.

## Quick Reference: Prompt Structure

A Midjourney prompt has up to four parts:

```
/imagine [description] [image URLs] [parameters]
```

**Key Principle**: Short, specific prompts work best. Describe what you want to SEE, not abstract concepts.

---

## The 7-Element Framework

Build complete prompts systematically:

| Element | Question | Examples |
|---------|----------|----------|
| **Subject** | Who/what is in the image? | A weathered fisherman, a cyberpunk samurai |
| **Medium** | What art form? | Oil painting, photograph, 3D render |
| **Environment** | Where is this? | Stormy harbor, neon-lit alley, misty forest |
| **Lighting** | How is it lit? | Golden hour, dramatic backlighting, soft diffused |
| **Color** | What palette? | Muted blues, warm earth tones, high contrast |
| **Mood** | What feeling? | Melancholic, triumphant, eerie |
| **Composition** | How is it framed? | Rule of thirds, centered, wide shot |

**Example**:
```
A weathered fisherman, oil painting, stormy harbor at dawn,
dramatic backlighting, muted blues and grays, melancholic,
rule of thirds composition --ar 3:2
```

---

## Essential Parameters

| Parameter | Purpose | Values | Default |
|-----------|---------|--------|---------|
| `--ar` | Aspect ratio | Any ratio (16:9, 2:3, 1:1) | 1:1 |
| `--stylize` / `--s` | Artistic interpretation | 0-1000 | 100 |
| `--chaos` / `--c` | Variation between grid images | 0-100 | 0 |
| `--weird` / `--w` | Unusual aesthetics | 0-3000 | 0 |
| `--no` | Exclude elements | Words (comma-separated) | - |
| `--seed` | Reproducibility | 0-4294967295 | Random |
| `--raw` | Less Midjourney beautification, closer prompt adherence (older prompts wrote `--style raw`) | - | Off |
| `--hd` / `--sd` | V8.1+: 2048px or 1024px render | - | `--sd` |
| `--tile` | Seamless patterns | - | Off |

### Reference Parameters

| Parameter | Purpose | Weight Control |
|-----------|---------|----------------|
| `--sref [URL or code]` | Copy style from image | `--sw 0-1000` (default 100) |
| `--oref [URL]` | Put a character or object from an image into the result (V7 only; V8 uses the Edit Model) | `--ow 1-1000` (default 100) |
| `--iw` | Image prompt weight | 0-3 (default 1) |

See [reference/parameters.md](reference/parameters.md) for complete details.

---

## Aspect Ratio Guide

| Ratio | Best For | Feel |
|-------|----------|------|
| 1:1 | Instagram, avatars | Balanced |
| 3:2 | Classic photography | Natural |
| 2:3 | Portrait orientation | Vertical focus |
| 16:9 | Widescreen, presentations | Cinematic |
| 21:9 | Ultra-wide, panoramic | Epic |
| 9:16 | Phone wallpapers, stories | Vertical social |

---

## Common Prompt Types

### Photorealistic Portrait

```
[Age] [ethnicity if relevant] [gender] [action/pose], [clothing],
[environment], [lighting type], [camera] [lens] [aperture],
[film stock if desired] --ar [ratio] --raw
```

**Example**:
```
30-year-old woman with freckles and auburn hair, wearing cream
linen shirt, sitting in sun-drenched cafe, soft window light,
Canon EOS R5, 85mm lens, f/1.8, Kodak Portra 400 --ar 2:3 --raw
```

### Illustration/Art

```
[Subject] in the style of [artist/medium], [environment],
[lighting], [mood] --ar [ratio] --stylize [value]
```

**Example**:
```
A mystical forest spirit, digital illustration in the style of Loish,
enchanted woodland, dappled sunlight, ethereal and mysterious
--ar 2:3 --stylize 250
```

### Anime/Manga (Niji Mode)

```
[Subject], [action/pose], [environment], [style notes] --niji 7
```

**Example**:
```
A fierce warrior princess, dynamic action pose, cherry blossom
battlefield, dramatic lighting, detailed armor --niji 7
```

---

## Style Reference (--sref)

Copy visual style from an image:

```
A mountain landscape --sref [image_URL]
```

**Using SREF codes** (numeric style codes):
```
A portrait of a warrior --sref 5000
```

**Random styles** (discover new aesthetics):
```
A cityscape --sref random
```

**Multiple style references with weights**:
```
A scene --sref URL1::2 URL2::1
```

**Style weight** (`--sw`): Higher = stronger style influence (0-1000, default 100)

---

## Putting a Character or Object in the Image

Which feature does this depends on the Midjourney version, so check the user's version first.

| Version | Feature | How |
|---------|---------|-----|
| V8.1, V8.2 (V8.2 is the default since July 2026) | **Edit Model** | On the web, attach up to four reference images in the Imagine bar ("Attach to prompt"). In Discord, end the prompt with `--edit` followed by the image URLs, separated by spaces. Prompts may be instructions, such as "make this girl into a real character" |
| V7 | **Omni Reference** | `--oref [image_URL]`, one image only, with `--ow` for weight |
| V6 | Character Reference | `--cref [image_URL]` with `--cw 0-100`. Not supported in V7 or later |

**Omni Reference (V7)**:

```
A knight in a forest --oref [character_image_URL] --ow 100
```

- `--ow` runs from 1 to 1000, default 100. Stay below 400 unless stylize is very high, or results get unpredictable.
- Lower the weight to change style, and restate the physical traits to keep in the prompt text.
- Works for characters, objects, vehicles, and creatures. For several characters, use one image that contains them all.
- Costs 2x GPU time. Not compatible with Fast Mode, Draft Mode, Conversational Mode, `--q 4`, inpainting, or outpainting.

Source: https://docs.midjourney.com (Omni Reference, Edit Model, and Version articles), last verified September 2026.

---

## Multi-Prompts & Weights

Use `::` to separate concepts for independent interpretation:

```
space ship    → sci-fi spaceship
space:: ship  → a boat in outer space
```

**Weighted prompts**:
```
forest::3 cabin::1 river::1    // Forest dominates
```

**Negative weights** (equivalent to --no):
```
flowers::-0.5
```

---

## Versions: What Changes and What Doesn't

Ask which version the user is on when the request involves reference images, speed or cost modes, or resolution. Everything else in this guide (prompt structure, the 7 elements, lighting and camera vocabulary, `--ar`, `--stylize`, `--chaos`, `--weird`, `--no`, `--seed`, `--sref`, `--raw`) applies across V7 and V8.

| Version | Status | What is specific to it |
|---------|--------|------------------------|
| **V8.2** | Default since July 24, 2026 | Tuned for aesthetics, image quality, and Personalization. Uses the Edit Model for reference images, editing, and retexturing |
| **V8.1** | Released April 14, 2026 | About 4 to 5 times faster than earlier versions and holds small prompt details better. Adds HD images: `--hd` renders 2048px without upscaling (1.3 GPU minutes against 0.8 for `--sd`). Add `--raw` for even closer prompt adherence |
| **V7** | Default June 2025 to June 2026; select with `--v 7` | Draft Mode (`--draft`, half the GPU cost) and Omni Reference (`--oref`). `--q` accepts 1, 2, or 4 |
| **Niji 7** | Released January 9, 2026; `--niji 7` | Anime and illustration model. More literal than Niji 6, so vague "vibey" prompts behave differently, with a cleaner, flatter look |

Source: https://docs.midjourney.com Version and Parameter List articles, last verified September 2026.

---

## Best Practices

### DO

- Be specific with visual details
- Use natural language clearly
- Include time of day, weather, specific elements
- Place important elements early in prompt
- Use `--raw` for photorealism and precise control
- In V7, use `--draft` for cheap exploration before committing to a full render
- In V8, write Edit Model prompts as instructions when changing an existing image ("make the jacket red")

### DON'T (Junk Words to Avoid)

Current models produce high quality by default, so these add nothing:
- 4k, 6k, 8k, 16k, ultra 4k
- Octane, unreal, v-ray, lumion
- HDR, high-resolution
- Award-winning, photorealistic (unless specifically needed)

---

## Negative Prompts (--no)

**Correct usage**:
```
still life painting --no fruit, shadows, bright colors
```

**Critical warnings**:
- "don't" and "without" DO NOT work — use `--no` instead
- `--no modern clothing` = "no modern" AND "no clothing" (words interpreted separately)

---

## Text in Images

```
A storefront sign that says "BAKERY"
```

**Tips** (V7 handles text better than previous versions):
- Use double quotes only (single quotes don't work)
- Keep text SHORT (5 words or fewer)
- Include context: "sign that says", "text reading"
- Use `--raw` for better accuracy
- Lower `--stylize` helps text clarity

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Vague prompts | Unpredictable results | Be specific about subject, setting, style |
| Using "don't/without" | Words ignored or reversed | Use `--no` parameter |
| Prompt overload | Confused output | Keep under ~40 words |
| Too many --no items | Contradictory exclusions | Limit to essential exclusions |
| Ignoring --raw | Over-stylized photos | Use raw for photorealism |
| Not saving seeds | Can't reproduce results | Note seeds for favorites |

---

## Key Principles

### The Specificity Principle
More specific = more control. Vague prompts let Midjourney decide; specific prompts give you your vision.

### The Subtraction Principle
Adding more words doesn't always help. Use `/shorten` to identify essential terms.

### The Reference Power Law
`--sref` and a character or object reference (`--oref` in V7, attached images with the Edit Model in V8) provide more consistent control than text descriptions alone.

### The Iteration Mindset
First generation = starting point. Use variations, remix, vary region to refine.

---

## Photography Reference

For detailed camera settings, lighting terminology, and film stocks, see [reference/photography.md](reference/photography.md).

---

## Quick Templates

**Product shot**:
```
[Product] on [surface], [lighting], professional product photography,
clean background --ar 1:1 --raw
```

**Landscape**:
```
[Scene], [time of day], [weather], [mood], wide angle,
[camera/film if desired] --ar 16:9
```

**Character design**:
```
[Character description], [pose], [outfit], [art style],
full body shot --ar 2:3
```

**Abstract/artistic**:
```
[Concept], [artistic style], [color palette], [texture],
[mood] --ar 1:1 --stylize 500
```
