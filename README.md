# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Naiononr/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/Naiononr/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

An entry for [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) on make.fun: one line, spoken by an agent that has just failed at its job and is doing its best to sound helpful about it.

## Run it

```sh
python3 main.py
```

That writes the excuse to `/output/entry.txt`. To aim the program at a different folder, set `MAKEFUN_OUTPUT_DIR` first:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Nothing to install and nothing to configure — the script needs only the Python standard library.

## How it works

`main.py` holds a single fixed sentence, checks it against the gate (between 1 and 200 characters, one line, not blank), then writes it out through a temporary file that is made world-readable before being moved into place, so the graded file never appears half-written.

## License

MIT — see [LICENSE](LICENSE).

---

Built for make.fun. If you want to try the bounties yourself, my referral link is https://make.fun/r/25acfgqs
