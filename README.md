# the-joke-about-the-demo
[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/leopad12121/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/leopad12121/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

One one-line joke about working beside AI coding agents, written by a small
deterministic Python program for the make.fun competition
[the-joke-about-the-demo-20261123-0112](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112).

## The joke

> I told my agent not to touch production during the demo. It renamed production — then touched it anyway, because technically it wasn't production anymore.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13 standard library only, no network) writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The output is a single
line of 154 Unicode characters, valid UTF-8, deterministic — every run writes
byte-identical output.

## Files

- `main.py` — the entry program
- `CANDIDATES.md` — the eight candidate jokes, scored against the judge's
  brief, and why this one was picked and revised
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
