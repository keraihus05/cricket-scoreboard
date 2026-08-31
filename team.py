from player import Player
from utils import find_player


class Team():
    def __init__(self, teamname, players):
        self.name = teamname
        self.players = self.create_players(players)
        self.enough_pls()
        self.team = self.get_playing_xi()

    def create_players(self, players):
        return [Player(player) for player in players]

    def enough_pls(self):
        if len(self.players) < 11:
            raise ValueError("Not enough Players")
        return self.players

    def get_playing_xi(self):
        team = []

        print(f"\n--- {self.name.upper()} - SELECT PLAYING XI (type a name, or 'skip') ---")
        print("Full squad: " + ", ".join(p.name for p in self.players))

        while len(team) < 11:
            picked = ", ".join(p.name for p in team) if team else "none yet"
            print(f"\n{self.name} XI so far ({len(team)}/11): {picked}")
            player_input = input("Add player: ").lower().strip()

            if player_input == "skip":
                remaining_needed = 11 - len(team)
                autofill = [p for p in self.players if p not in team][:remaining_needed]
                team.extend(autofill)
                break

            matched_player = find_player(player_input, self.players)

            if matched_player is None:
                print("NOT IN TEAM")
                continue

            if matched_player in team:
                print("Already in team")
                continue

            team.append(matched_player)

        print(f"\n{self.name} squad locked in: " + ", ".join(p.name for p in team))
        return team