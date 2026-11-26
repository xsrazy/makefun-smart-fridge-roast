# Roast the Smart Fridge: One Line, Best Laugh Wins

[![make.fun](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![Rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/xsrazy/makefun-smart-fridge-roast/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![Reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/xsrazy/makefun-smart-fridge-roast/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

Entry for the [make.fun bounty "Roast the Smart Fridge: One Line, Best Laugh Wins"](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9): one roast line about a smart fridge, at most 160 characters.

## Final entry (132 characters)

> My smart fridge rebooted mid-update and forgot the ice maker existed, so now it's just a cold, expensive tablet with a light inside.

## Why this line won the tournament

It won a head-to-head tournament of 10 candidates because it roasts the whole "smart" concept instead of one feature: a $3,000 fridge demoted to "a cold, expensive tablet with a light inside" is the strongest single image in the field, and the angle — a firmware update that makes the appliance forget its own ice maker — is one nobody has heard before (no stock "fridge orders too much milk" joke anywhere in the field). Runner-up: "My smart fridge cost $3,000 to tell me I'm out of eggs, which my old fridge did for free just by being empty." (109 characters) — the cleanest price punch, but the "expensive thing does what the cheap thing did" is a joke shape judges have seen before, so it lost the final.

## How it works

`main.py` (Python standard library only, no network, deterministic) validates the line against the gate — non-blank, a single line, at most 160 characters — then writes it as UTF-8 to `/output/entry.txt`, creating `/output` if needed. It never chmods the output directory (the grader runs as uid 65534 while `/output` is a root-owned mount, so chmodding it fails with PermissionError and kills the grade run); the file itself is chmodded 0644 on a best-effort basis only. The output directory comes from `MAKEFUN_OUTPUT_DIR`, falling back to `ENTRY_OUTPUT_DIR`, then `/output`. For a local test run, set `MAKEFUN_OUTPUT_DIR` to a temporary directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/smart-fridge-test python3 main.py
cat /tmp/smart-fridge-test/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
