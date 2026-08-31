
# Cricket Scoreboard

A terminal-based cricket scorer written in Python. Pick two teams, set the
playing XIs, and score the match ball-by-ball straight from the command line.

## Features

- Pick any two teams from a built-in set of squads (or add your own)
- Select a playing XI by name, with partial/surname matching (e.g. typing
  `azam` finds Babar Azam) - or type `skip` at any point to auto-fill the
  rest of the XI
- Choose your opening striker and non-striker at the start of each innings,
  and pick the next batter live as wickets fall
- Full ball-by-ball scoring: runs, wickets (with dismissal type), and extras
  (wides, no-balls, byes, leg byes, penalties)
- Automatic over/bowler management, including a cap on overs per bowler
- A tidy, live-updating scoreboard after every ball
- Automatic run-chase tracking and match result in the second innings

## Requirements

- Python 3.9+
- No external dependencies - everything runs from the standard library

## Getting Started

```bash
git clone <your-repo-url>
cd <repo-folder>
python3 main.py
```

## How to Play

When you run `main.py` you'll be walked through:

1. **Pick two teams** - type a team name (or part of one) from the list shown
2. **Pick each playing XI** - type player names one at a time, or `skip` to
   auto-fill whoever's left
3. **Choose the match format** - overs per innings (e.g. `10`, `20`, `50`)
4. **Choose who bats first**
5. **Pick openers and a bowler** for each innings

From there, you'll be prompted for `CURRENT BALL:` after every delivery.
Accepted inputs:

| Input | Meaning |
|---|---|
| `0`-`6` | Runs scored off the bat |
| `wicket` / `w` / `out` | A dismissal (you'll be asked how) |
| `lbw`, `caught`, `stumped`, `bowled`, `hitwicket`, `runout`, `obstructingthefield`, `retiredhurt` | A dismissal, with the method already specified |
| `wide`, `noball` / `nb`, `bye`, `leg bye`, `penalty` | An extra (you'll be asked how many runs) |
| `exit` / `quit` / `break` / `end` | Ends the match early |

When a wicket falls, you'll be asked who's out (matched against the two
batters at the crease) and who's coming in next - both support partial name
matching too.

## Project Structure

```
main.py     - entry point: team selection and the game loop
match.py    - Match class: coin toss, format, and running both innings
innings.py  - Innings class: ball-by-ball scoring logic and the scoreboard
team.py     - Team class: building a playing XI from a squad
player.py   - Player class: per-player batting/bowling stats
squads.py   - built-in squad data (add your own teams here)
utils.py    - shared name-matching helper (supports surname-only input)
```

## Adding Your Own Teams

Open `squads.py` and add a new entry to the `SQUADS` dictionary:

```python
"My Team": [
    "Player One",
    "Player Two",
    # ... at least 11 players
],
```

It'll show up automatically in the team picker next time you run the game.

## Possible Future Improvements

- Save/load match state so a game can be resumed
- Export a full scorecard at the end of the match
- Support for tied matches / DLS-style adjustments


