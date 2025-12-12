# Vocabulary Patterns in AI-Generated Text

Comprehensive reference of words, phrases, and vocabulary patterns that indicate AI authorship.

## High-Signal Words

These words appear 50-700x more frequently in AI-generated text than human writing:

### Extreme Frequency (100x+ more common in AI)
| Word/Phrase | Frequency vs Human | Notes |
|-------------|-------------------|-------|
| "complex and multifaceted" | 700x | Almost exclusively AI |
| "intricate interplay" | 100x | Strong AI signal |
| "played a crucial role" | 70x | Very common AI phrase |
| "delve" / "delving" | 50x+ | Most discussed AI tell |
| "tapestry" (metaphorical) | 50x+ | "Rich tapestry of..." |

### Strong Signal Words (10-50x more common)

**Verbs:**
- delve, delved, delving
- embark, embarking
- foster, fostering
- underscore, underscoring
- leverage, leveraging
- navigate, navigating
- unravel, unraveling
- unlock, unlocking
- unveil, unveiling
- illuminate, illuminating
- elucidate, elucidating
- resonate, resonating
- transcend, transcending
- spearhead, spearheading
- hone, honing
- harness, harnessing
- captivate, captivating
- enrich, enriching
- revolutionize, revolutionizing

**Adjectives:**
- multifaceted
- nuanced
- pivotal
- paramount
- profound
- meticulous
- intricate
- holistic
- robust
- groundbreaking
- cutting-edge
- revolutionary
- game-changing
- invaluable
- unwavering
- commendable

**Nouns:**
- tapestry
- realm
- landscape (metaphorical)
- journey (metaphorical)
- quest
- labyrinth
- symphony
- treasure trove
- beacon
- crucible
- enigma
- paradigm
- synergy
- cornerstone
- testament

**Adverbs:**
- furthermore
- moreover
- notably
- importantly
- ultimately
- subsequently
- nonetheless
- arguably

### Moderate Signal Words (5-10x more common)

These are flagged but require corroborating evidence:

- comprehensive
- crucial
- vital
- essential
- significant
- remarkable
- exceptional
- innovative
- transformative
- dynamic
- seamless
- streamlined

## Overused Phrases

### Highest Confidence Phrases
These phrases almost always indicate AI authorship:

```
"It's important to note that..."
"It's worth noting that..."
"It should be noted that..."
"In today's fast-paced world..."
"In the ever-evolving landscape of..."
"A deeper understanding of..."
"Unlock the power of..."
"At its core..."
"That being said..."
"To put it simply..."
"In light of this..."
"Without further ado..."
"Let me explain..."
"Certainly, [here is/here are]..."
"As of my last..."
"I hope this helps!"
```

### Strong Signal Phrases

**Opening phrases:**
- "Have you ever wondered..."
- "In the realm of..."
- "When it comes to..."
- "In the world of..."
- "Let's dive into..."
- "Welcome to..."

**Transition phrases:**
- "With that in mind..."
- "Building on this..."
- "Taking it a step further..."
- "On another note..."
- "Moving forward..."

**Conclusion phrases:**
- "In summary..."
- "In conclusion..."
- "To summarize..."
- "All in all..."
- "At the end of the day..."
- "The bottom line is..."

**Correlative constructions:**
- "Not only...but also..."
- "Whether...or..."
- "On the one hand...on the other hand..."
- "Both...and..."

### Hedging Language Clusters

AI overuses qualifiers. Watch for clusters of:

```
arguably
somewhat
generally
might
could
perhaps
potentially
in many cases
often
typically
tends to
may be
it seems
appears to
likely
possibly
```

When 3+ hedging terms appear in close proximity, it's a moderate AI signal.

## Vocabulary Frequency Analysis

### Type-Token Ratio (TTR)

**What it measures**: Unique words / total words

**Counterintuitive finding**:
- ChatGPT: 0.69 TTR (higher diversity)
- Human students: 0.61 TTR (lower diversity)

This means AI sometimes has MORE vocabulary diversity, but lower "meaningful" diversity. AI uses varied words but says similar things.

### Hapax Legomenon Rate

**What it measures**: Words appearing only once in the text

**Key finding**: Human text has higher hapax rates - humans use more truly unique word choices that they don't repeat.

### Stop Word Patterns

**What they are**: Function words (the, is, at, which, on)

**AI pattern**: More uniform stop word distribution
**Human pattern**: More varied, context-dependent usage

## Latinate vs Germanic Vocabulary

AI tends toward formal Latinate vocabulary:

| AI Prefers | Human Often Uses |
|------------|------------------|
| utilize | use |
| commence | start/begin |
| terminate | end |
| facilitate | help |
| implement | do/make |
| demonstrate | show |
| possess | have |
| obtain | get |
| require | need |
| assist | help |

This pattern alone is weak but combines with other signals.

## Model-Specific Vocabulary

### ChatGPT/GPT-4 Favorites
- "delve"
- "tapestry"
- "nuanced"
- "multifaceted"
- "It's not about X; it's about Y"

### Claude Favorites
- Extended analogies
- "That said..."
- Methodical numbering
- Cautious qualifications

### Gemini Favorites
- Current event references
- Practical/applied framing
- Conversational transitions

## Detection Implementation

### Scoring Approach

```
For each text:
1. Count occurrences of high-signal words
2. Calculate density (flagged words / total words)
3. Check for phrase patterns
4. Weight by signal strength

Suggested thresholds:
- 0-2 flagged terms: Normal
- 3-5 flagged terms: Worth investigating
- 6+ flagged terms: Strong AI signal
- Any "extreme frequency" phrase: Immediate flag
```

### Caveats

- Single word matches prove nothing
- Academic/formal writing naturally uses some flagged terms
- Non-native speakers may use these patterns innocently
- Always require multiple corroborating signals
