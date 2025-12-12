---
name: ai-writing-detection
description: Comprehensive AI writing detection patterns and methodology. Provides vocabulary lists, structural patterns, model-specific fingerprints, and false positive prevention guidance. Use when analyzing text for AI authorship or understanding detection patterns.
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch
---

# AI Writing Detection Reference

Expert-level knowledge base for detecting AI-generated text, compiled from academic research, commercial detection tools, and empirical analysis.

## Quick Reference: High-Confidence Signals

These indicators strongly suggest AI authorship when found together:

### Vocabulary Red Flags
**High-signal words** (50-700x more common in AI text):
- "delve", "tapestry", "nuanced", "multifaceted", "underscore"
- "intricate interplay", "played a crucial role", "complex and multifaceted"
- "paramount", "pivotal", "meticulous", "holistic", "robust"

**Overused phrases**:
- "It's important to note that..."
- "In today's fast-paced world..."
- "At its core..."
- "Without further ado..."
- "Let me explain..."

See [reference/vocabulary-patterns.md](reference/vocabulary-patterns.md) for complete lists.

### Structural Red Flags
- **Uniform sentence lengths**: 12-18 words consistently (low burstiness)
- **Tricolon structures**: "research, collaboration, and problem-solving"
- **Em dash overuse**: AI uses em dashes more than typical human writing
- **Perfect paragraph uniformity**: All paragraphs same approximate length
- **Template conclusions**: "In summary...", "In conclusion..."

See [reference/structural-patterns.md](reference/structural-patterns.md) for details.

### Tone Red Flags
- Passive and detached voice throughout
- Absence of first-person pronouns where expected
- Consistent formality with no stylistic variation
- Over-politeness and excessive hedging

## Detection Methodology

### Multi-Layer Analysis Approach

**Layer 1: Vocabulary Pattern Matching**
- Scan for overused AI words/phrases
- Count frequency of flagged terms
- Look for clusters of high-signal vocabulary

**Layer 2: Structural Analysis**
- Observe sentence length variation (uniform = AI signal)
- Check paragraph uniformity
- Identify repetitive syntactic templates
- Note formatting patterns (excessive headers, bullet points)

**Layer 3: Stylometric Observation**
- Pronoun usage patterns (missing first-person?)
- Tone consistency (too uniform = AI signal)
- Punctuation patterns (em dash overuse?)

**Layer 4: Coherence Check**
- Do paragraphs build a coherent argument?
- Are concepts repeated with different words?
- Do transitions actually connect ideas?

**Layer 5: Confidence Scoring**
- Weight multiple signals together
- Require corroborating evidence (3+ signals minimum)
- Apply context-specific adjustments

## Model-Specific Patterns

Different AI models have distinct "fingerprints":

| Model | Key Tells |
|-------|-----------|
| ChatGPT/GPT-4 | "delve", "tapestry", tricolons, em dashes |
| Claude | Analytical structure, extended analogies, cautious qualifications |
| Gemini | Conversational synthesis, fact-dense paragraphs |

See [reference/model-fingerprints.md](reference/model-fingerprints.md) for detailed model patterns.

## False Positive Prevention

**Critical requirements**:
- Minimum 200 words for reliable analysis
- Never flag on single indicators alone
- Use ensemble scoring (multiple signals required)

**High false-positive risk groups**:
- Non-native English speakers (61% false positive rate in research)
- Technical/formal writing
- Neurodivergent writers
- Content using grammar correction tools

See [reference/false-positive-prevention.md](reference/false-positive-prevention.md) for detailed guidance.

## Analysis Output Format

Structure findings as:

```
**Overall Assessment**: [Likely AI / Possibly AI / Likely Human / Inconclusive]
**Confidence**: [Low / Medium / High]

**Summary**: 2-3 sentence overview

**Evidence Found**:
- [Category]: [Specific indicator] - "[Quote from text]"
- [Category]: [Specific indicator] - "[Quote from text]"

**Mitigating Factors**: [Elements suggesting human authorship]

**Caveats**: [Limitations, alternative explanations]
```

## Key Principles

1. **No certainty claims** - AI detection is probabilistic
2. **Multiple signals required** - Single indicators prove nothing
3. **Context matters** - Academic writing differs from blogs
4. **Stakes awareness** - False accusations cause real harm
5. **Evolving field** - Detection methods require constant updates

## Reference Files

- [vocabulary-patterns.md](reference/vocabulary-patterns.md) - Complete word/phrase lists with frequencies
- [structural-patterns.md](reference/structural-patterns.md) - Sentence, paragraph, and discourse patterns
- [model-fingerprints.md](reference/model-fingerprints.md) - GPT, Claude, Gemini specific tells
- [false-positive-prevention.md](reference/false-positive-prevention.md) - Avoiding false accusations

## Sources

This knowledge base synthesizes research from:
- Stanford HAI (DetectGPT, bias studies)
- GPTZero, Originality.ai, Turnitin, Pangram methodologies
- Academic papers on stylometry and discourse analysis
- Empirical studies on detection accuracy and limitations
