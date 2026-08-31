from team import Team
from match import Match
from squads import SQUADS


def choose_team(prompt, taken=None):
    taken = taken or []

    while True:
        query = input(prompt).strip().lower()

        matches = [name for name in SQUADS if name.lower() == query]

        if not matches:
            matches = [name for name in SQUADS if query in name.lower()]

        if len(matches) == 1:
            name = matches[0]
            if name in taken:
                print(f"{name} has already been picked.")
                continue
            return name

        if len(matches) > 1:
            print(f"'{query}' matches multiple teams ({', '.join(matches)}) - be more specific.")
            continue

        print("Team not found.")


print("Available teams: " + ", ".join(SQUADS.keys()))
team_a_name = choose_team("Team A: ")
team_b_name = choose_team("Team B: ", taken=[team_a_name])

team_a = Team(teamname=team_a_name, players=SQUADS[team_a_name])
team_b = Team(teamname=team_b_name, players=SQUADS[team_b_name])

match = Match(team_a, team_b)

while not match.game_over:
    match.play_match()