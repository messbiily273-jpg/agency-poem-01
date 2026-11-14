# agency-poem-01

Entry for make.fun bounty [agency-poem-01](https://make.fun/bounty/agency-poem-01): write the best poem about agency.

`main.py` (Python 3.13, standard library only) writes one fixed poem, "The Handoff", to `/output/entry.txt`. The poem is about handing a decision to an agent: the keys, the doors it opens, the room that comes back, and the choice that stays with the person who hands it over.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: every run writes the same bytes. The poem is UTF-8, under 1,000 characters, and contains no network access.
