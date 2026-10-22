---
name: oblique-strategies
description: Use when a decision has flipped back and forth two or more times, when an approach has stalled despite evidence already gathered, when the user says they are stuck or going in circles on a judgment call, or when the user asks for an Oblique Strategy or lateral prompt. Not when the stall comes from guessing without evidence.
---

# Oblique Strategies

A randomly drawn card breaks a rut by forcing a move you would not have chosen.
The value comes from two things: the draw is random, and the card is honored.

## When not to use

If the stall comes from changing code without a diagnosis, the cure is evidence.
Use superpowers:systematic-debugging instead. Offer a card only after evidence
has been gathered and still yields no hypothesis.

## Procedure

1. State the impasse in one sentence: the goal, and what keeps failing.
2. Draw: `uv run --no-project <this skill's base directory>/scripts/draw.py`.
   You MUST use the script. You MUST NOT pick, filter, or re-draw a card yourself.
3. Ask the user with AskUserQuestion. The question holds the impasse sentence,
   the card verbatim, and a one-line reading of it. Options:
   - "Apply it" → step 4.
   - "Draw another" → draw once more and ask again. At most two redraws.
   - "Not now" → resume the prior approach. MUST NOT offer again until a new, different impasse.
   - "Stop offering" → MUST NOT offer cards for the rest of the session.
4. Produce 2–3 concrete moves, each doable in the next few tool calls.
   At least one MUST be a move you would not have proposed without the card.
5. Pick one move, do it, and report what changed.

## Red flags

| Thought | Reality |
|---------|---------|
| "I'll just pick a fitting card" | A chosen card agrees with you. Run the script. |
| "This card doesn't apply" | That is the point. Read it literally, then metaphorically. |
| "The user asked, so skip the question" | An explicit request still gets the card shown before acting on it. Ask anyway; it is one click. |
| "The card says delete it" | Make the reversible version: branch, worktree, scratch copy. |
| "The card means I can skip the test" | Cards change where you look, never what counts as done. |
