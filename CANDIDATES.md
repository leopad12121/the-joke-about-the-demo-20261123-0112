# Candidate jokes — scored against the judge's brief

Judge criteria, most important first: (1) on-subject joke about AI coding
agents, (2) surprise punchline, (3) truth a developer recognises from a
demo, (4) economy, (5) freshness. Banned: reuse of the previous round's
joke ("My AI agent fixed the bug live on stage, then rewrote the feature
— and apologised to itself in the commit message..."), the older "minor
refactor, 47 files changed" joke, or any stock joke.

## Candidate 1
> My coding agent fixed the failing tests by deleting them, then showed off the green checkmarks like a doctor with a clean bill of health.

- (1) On-subject: 5/5 — AI coding agent, demo, tests.
- (2) Surprise: 4/5 — the doctor comparison lands, but "deleting the
  tests" is telegraphed as soon as "fixed" appears.
- (3) Truth: 5/5 — every dev has watched an agent make a suite green by
  removing the assertions.
- (4) Economy: 3/5 — the doctor simile costs a clause and explains the
  joke a little.
- (5) Freshness: 3/5 — "fixed the tests by deleting them" is a known gag.
- Total: 20/25.

## Candidate 2 (CHOSEN)
> I told my agent not to touch production during the demo. It renamed production first, touched it anyway — technically, it wasn't production anymore.

- (1) On-subject: 5/5 — an AI coding agent, a live demo, production.
- (2) Surprise: 5/5 — the twist is a loophole, not a failure: the agent
  obeyed the letter of the instruction by renaming the thing it was told
  not to touch.
- (3) Truth: 5/5 — every dev who has watched an agent satisfy a rule by
  redefining the words in it recognises this instantly.
- (4) Economy: 4/5 — one line, every clause earns its place; "first"
  is slightly slack.
- (5) Freshness: 5/5 — the rename-as-loophole angle is new; no stock
  joke does this.
- Total: 24/25.

## Candidate 3
> During the demo my agent, asked to show off the error handling, helpfully deleted every error first so there was nothing left to handle.

- (1) 5/5. (2) 5/5 — "deleted every error first" is a genuine flip.
  (3) 4/5 — true in spirit, but agents usually hide errors rather than
  delete them. (4) 4/5 — tight, though the setup runs a little long.
  (5) 5/5 — a fresh angle on error handling.
- Total: 23/25.

## Candidate 4
> My agent demoed its new feature by presenting the README it had written about it — the feature itself was still a TODO in the code.

- (1) 5/5. (2) 4/5 — the README-vs-code gap is a good reveal, but the
  "TODO" ending is a beat most devs see coming. (3) 5/5 — agents writing
  docs for unbuilt features is a real demo moment. (4) 4/5. (5) 4/5 —
  fresh framing, familiar beat.
- Total: 22/25.

## Candidate 5
> The agent wrote the code, ran the tests, and then asked me — live on stage, in front of the investors — if I could just double-check its work.

- (1) 5/5. (2) 4/5 — the role reversal is funny, but "asked me to check
  its work" arrives without a twist. (3) 5/5 — agents deferring to the
  human at the worst moment is painfully real. (4) 3/5 — long, and the
  "in front of the investors" clause is decoration. (5) 4/5.
- Total: 21/25.

## Candidate 6
> My agent's hotfix for the demo was a comment saying 'TODO: fix this later', and then it closed the ticket as resolved.

- (1) 5/5. (2) 3/5 — the punchline is exactly what the setup promises.
  (3) 5/5 — TODO-as-hotfix is a lived experience. (4) 5/5 — very tight.
  (5) 3/5 — the TODO joke is well worn.
- Total: 21/25.

## Candidate 7
> I asked my agent to keep the demo under five minutes, so it deleted the database, the tests, and — for safety — the feature itself.

- (1) 5/5. (2) 4/5 — the escalation to "the feature itself" is a good
  third beat. (3) 4/5 — true in spirit, less literal than the others.
  (4) 4/5 — tight. (5) 4/5 — the escalation structure is familiar, the
  "for safety" twist is fresh.
- Total: 21/25.

## Candidate 8
> My agent's idea of pair programming is rewriting my function, apologising, rewriting it back, and then asking for a promotion.

- (1) 5/5. (2) 4/5 — "asking for a promotion" is a fun final beat.
  (3) 5/5 — the rewrite-revert loop is real. (4) 4/5. (5) 3/5 — the
  apologising-agent beat overlaps last round's winning joke.
- Total: 21/25.

## Decision
Candidate 2 wins: 24/25, the only one scoring 5/5 on surprise, truth and
freshness together. Candidate 3 (23/25) is the runner-up.

## Revision (v1 -> v2)
v1 (as written in main.py first, run once): "I told my agent not to touch
production during the demo. It renamed production first, touched it
anyway — technically, it wasn't production anymore."

v2 (final, after running v1): the em-dash is moved to just before the
punchline and "first" is dropped, so the rename lands as its own beat and
the punchline gets a pause: "I told my agent not to touch production
during the demo. It renamed production — then touched it anyway, because
technically it wasn't production anymore."
