# Model-Specific Fingerprints

Each AI model has distinctive linguistic patterns - "fingerprints" that persist even when prompted to write differently.

## Why Fingerprints Exist

**Root cause**: Deterministic training and fine-tuning processes create consistent patterns.

**Key finding**: LLMs have unique and consistent linguistic markers that:
- Persist across different prompts and topics
- Remain stable when instructed to "write like a human"
- Are highly consistent due to fixed model weights

## ChatGPT / GPT-4 Patterns

### Vocabulary Fingerprint

**Signature words**:
- "delve" (most discussed GPT tell)
- "tapestry" (especially "rich tapestry of...")
- "nuanced"
- "multifaceted"
- "crucial"
- "comprehensive"

**Signature phrases**:
- "It's not about X; it's about Y"
- "Let's dive into..."
- "It's important to note that..."
- "Without further ado..."

### Structural Fingerprint

**Characteristics**:
- Low-variance, formal phrasing
- Heavy use of tricolon structures
- Em dash overuse
- Correlative conjunctions ("not only...but also")
- Explicit topic sentences

**Example GPT structure**:
```
[Topic sentence stating main point]
[Supporting detail 1]
[Supporting detail 2]
[Concluding transition to next paragraph]
```

### Tone Fingerprint

- Helpful, eager-to-please tone
- Excessive qualification and hedging
- Professional formality even in casual contexts
- Tendency to provide comprehensive coverage

### Formatting Fingerprint

- Bullet points and numbered lists
- Section headers even for short responses
- Bold key terms
- Markdown formatting in text responses

## Claude (Anthropic) Patterns

### Vocabulary Fingerprint

**Less likely to use**:
- "delve" (trained to avoid)
- "tapestry"
- Many GPT-overused terms

**Characteristic patterns**:
- Extended analogies and metaphors
- Thoughtful qualifications
- Acknowledgment of limitations
- "That said..." transitions

### Structural Fingerprint

**Characteristics**:
- Analytical, methodical structure
- Symmetrical sentence flow
- Numbered explanations when appropriate
- Clear logical progression

**Example Claude structure**:
```
[Nuanced opening acknowledging complexity]
[Point 1 with careful qualification]
[Point 2 with consideration of counterarguments]
[Balanced conclusion with caveats]
```

### Tone Fingerprint

- More conversational than GPT
- Willing to express uncertainty
- Acknowledges when questions are complex
- Less eager-to-please, more thoughtful
- "That's a great question" (in default mode)

### Distinguishing Features

Claude tends to:
- Sound more human "out of the box"
- Use fewer formulaic phrases
- Provide more balanced perspectives
- Acknowledge limitations explicitly

## Gemini (Google) Patterns

### Vocabulary Fingerprint

**Characteristic patterns**:
- Conversational or fact-dense synthesis
- Integration of current information
- Practical, applied framing

### Structural Fingerprint

**Characteristics**:
- More varied structure than GPT
- Better at matching casual registers
- Integrates real-time information when available
- Practical guide persona

### Tone Fingerprint

- Better at humor and sarcasm
- More emotional undertones
- Conversational transitions
- Less formally structured

### Distinguishing Features

Gemini tends to:
- Reference current events and recent data
- Use more conversational language
- Be less rigidly structured
- Show more tonal variation

## Open Source Models

### LLaMA Patterns

**Characteristics**:
- Distinct syntactic fingerprints from each fine-tune
- Patterns differ even within the same family
- Generally more varied than commercial models

### Mistral Patterns

**Characteristics**:
- Efficient, concise responses
- Less verbose than GPT/Claude
- Different balance of formality

### Fine-Tuning Effects

Key insight: Fine-tuning creates distinct fingerprints even from same base model.

Models fine-tuned for:
- Code: More structured, technical patterns
- Chat: More conversational patterns
- Instruction-following: More explicit structure

## Cross-Model Detection

### Universal AI Patterns

Some patterns appear across most AI models:

1. **Uniform sentence length** (low burstiness)
2. **Hedging language clusters**
3. **Perfect grammar** (no minor human errors)
4. **Lack of personal anecdotes**
5. **Absence of colloquialisms/idioms**
6. **Over-organization**

### Model-Agnostic Signals

These work regardless of which AI generated the text:

- Structural uniformity
- Low perplexity scores
- Repetitive syntactic templates
- Consistent formality level
- Absence of first-person experience

## Detection Implications

### Model Identification

If you need to identify WHICH model generated text:

1. Check for model-specific vocabulary
2. Analyze structural patterns
3. Assess tone characteristics
4. Look for formatting fingerprints

### Model-Agnostic Detection

If you only need to know IF text is AI-generated:

1. Focus on universal patterns
2. Use ensemble methods trained on multiple models
3. Check for structural uniformity + vocabulary signals

### Evolving Fingerprints

**Challenge**: Each model update changes fingerprints slightly.

**GPT-3.5 vs GPT-4**: Different vocabulary preferences, structure patterns.

**Implication**: Detection systems need continuous updates.

## Fingerprint Persistence

### Research Finding

Fingerprints persist even when:
- Prompted to "write like a human"
- Given specific style instructions
- Asked to mimic particular authors
- Instructed to vary sentence length

### Why They Persist

1. Model weights are fixed
2. Training patterns are deeply embedded
3. Probability distributions remain consistent
4. Fine-tuning doesn't fully override base patterns

### Limitations

Fingerprints can be obscured by:
- Heavy human editing
- AI paraphrasing tools
- Multiple rounds of revision
- Translation and back-translation

## Practical Application

### Detection Workflow

```
1. Check universal AI patterns first
   → If strong signals, classify as AI

2. If inconclusive, check model-specific patterns
   → May identify which model

3. Consider context
   → Some models more common in certain domains

4. Apply ensemble scoring
   → Weight universal + model-specific signals
```

### Confidence Levels

| Signal Type | Confidence |
|-------------|-----------|
| Multiple universal patterns | High |
| Model-specific vocabulary cluster | Medium-High |
| Single model-specific term | Low |
| Structural pattern alone | Medium |
| Tone assessment alone | Low |

### Caveats

- Model fingerprints evolve with updates
- Heavy editing obscures fingerprints
- Some humans write in AI-like patterns
- Always require corroborating evidence
