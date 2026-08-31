# Cricket Scoreboard

A command-line cricket scoring application built in Python.

I built this project to improve my understanding of object-oriented programming and to get experience building a larger Python program with multiple classes interacting with one another. Rather than having all of the logic in one file, I wanted to structure the application around the different components of a cricket match, such as players, teams, innings and the match itself.

## What it does

The application allows you to run a limited-overs cricket match from the terminal, starting with team selection and finishing with the result.

Some of the main features include:

* Selecting two teams from the available squads
* Selecting the playing XI for each team
* Choosing the number of overs
* Selecting the opening batters and bowler
* Scoring the match ball-by-ball
* Handling runs from 0–6
* Handling wickets and different dismissal types
* Handling wides, no-balls, byes, leg byes and penalty runs
* Automatically managing strike rotation
* Managing overs and changing bowlers
* Keeping track of individual player statistics
* Managing a run chase during the second innings
* Automatically determining the result of the match

## Project structure

The project is split into several Python files, with each class responsible for a different part of the match.

```text
cricket-scoreboard/
│
├── main.py
├── match.py
├── innings.py
├── team.py
├── player.py
├── squads.py
├── utils.py
└── README.md
```

### `Player`

The `Player` class stores information about an individual player and keeps track of their batting and bowling statistics during the match.

### `Team`

The `Team` class is responsible for creating the players in a squad and selecting the playing XI and batting order.

### `Innings`

The `Innings` class contains most of the ball-by-ball scoring logic. It keeps track of the score, wickets, overs, current batters and bowler, as well as handling things such as strike rotation and extras.

### `Match`

The `Match` class manages the overall match. It brings the teams and innings together and handles things such as which team bats first, moving between innings and deciding the winner.

### `Squads`

This contains the player lists used to create the available teams. New teams can be added without having to change the main match logic.

### `Utils`

Contains helper functions used in different parts of the application, including player-name matching.

## Running the project

The project uses Python's standard library and does not require any external packages.

Clone the repository:

```bash
git clone https://github.com/keraihus05/cricket-scoreboard.git
cd cricket-scoreboard
```

Run the application with:

```bash
python3 main.py
```

## Using the scoreboard

The program guides you through setting up a match.

You first choose the two teams, select their playing XIs and decide how many overs the match will have. You then choose which team bats first and select the opening batters and bowler.

Once the innings begins, deliveries can be entered directly through the terminal.

For example:

```text
0 - 6       Runs scored
wide        Wide
noball      No-ball
bye          Bye
leg bye      Leg bye
wicket       Wicket
```

The program then updates the score and player statistics after each delivery.

Player names can also be entered using recognisable parts of their name rather than always requiring the full name.

## What I learned

The main purpose of this project was to move beyond smaller Python exercises and build something with several interacting components.

One of the biggest things I learned was how to manage state across different objects. A single delivery can change several things at once. For example, scoring an odd number of runs can change the striker, while a wicket can remove a player and bring in a new batter. An over can also trigger a change of bowler and the strike can change again.

As the project became more complicated, I had to think more carefully about which class should be responsible for each piece of logic. This helped me understand the practical side of object-oriented programming and the importance of keeping different parts of a program organised.

I also spent a lot of time handling edge cases and validating user input. Cricket has quite a few rules that interact with one another, so making sure that the program behaved correctly in different situations became an important part of the project.

## Future improvements

There are several things I would like to add in the future, including:

* Unit tests using `pytest`
* Saving and loading matches
* Exporting completed scorecards
* More detailed batting and bowling scorecards
* Support for tied matches and Super Overs
* More advanced match rules
* Storing previous match data
* Analysing player and team statistics
* Using historical cricket data to build a win-probability model

The last few ideas are particularly interesting to me because they would allow me to build on this project using statistics and machine learning, rather than just continuing to add features to the scoring system.

## Next steps

This project is mainly a programming project, but I see it as the starting point for a larger cricket data project.

The next stage would be to work with real ball-by-ball cricket data, analyse player and team performance, and eventually investigate whether statistical and machine-learning models can be used to estimate the probability of a team winning a match.

That would allow me to combine the programming skills developed here with my background in mathematics and statistics.
