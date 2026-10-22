# oblique-strategies

A Claude Code plugin. When work stalls on a judgment call, Claude draws a random
lateral-thinking card and asks you whether to apply it.

## Behavior

- Triggers when a decision flips back and forth, an approach stalls despite evidence,
  you say you're stuck, or you ask for an Oblique Strategy.
- Does not trigger when the stall comes from guessing without evidence.
  That case belongs to systematic debugging.
- The card comes from `scripts/draw.py`, never from the model.
  A model asked for a "random" card picks one that agrees with it.
- You approve every card: apply it, draw another (max two), not now, or stop offering.

## Install

```
/plugin marketplace add lxcode/oblique-strategies
/plugin install oblique-strategies@oblique-strategies
```

Requires [uv](https://docs.astral.sh/uv/).

## Decks

`skills/oblique-strategies/decks/engineering.txt` is an original deck and ships with the plugin.

The Eno/Schmidt deck is copyrighted and not included.
To use it, transcribe your own copy into `~/.config/oblique-strategies/eno.txt`
(or `$XDG_CONFIG_HOME/oblique-strategies/eno.txt`), one card per line.
The script prefers it when present. That location survives plugin updates.

## Development

```
uvx ruff check . && uvx ruff format --check . && uvx ty check skills/oblique-strategies/scripts
```
