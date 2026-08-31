from innings import Innings

class Match():
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
        self.bat_team = self.get_bat_team()
        self.bowl_team = self.get_bowl_team()
        self.match_overs = self.get_match_overs()
        self.game_over = False

    def get_match_overs(self):
        return int(input("Match format(10, 20, 50) : "))
    

    def get_bat_team(self):
        while True:
            bat_team = input(
                f"Which team is batting first? "
                f"({self.team_a.name}/{self.team_b.name}): "
            ).lower().strip()

            if bat_team == self.team_a.name.lower():
                return self.team_a

            if bat_team == self.team_b.name.lower():
                return self.team_b

            print("Team not found.")

    def get_bowl_team(self):
        if self.bat_team == self.team_a:
            return self.team_b
        return self.team_a

    def team_win(self, inning):
        if inning.runs >= inning.chase:
            return f'{inning.bat_team.name} WINS BY {10 - inning.wickets} WICKETS'
        elif inning.wickets == 10:
            return f'{inning.bowl_team.name} WINS BY {inning.chase - inning.runs - 1} RUNS'

         

    def play_match(self):
        while not self.game_over:
            first_innings = Innings(bat_team=self.bat_team, bowl_team=self.bowl_team, match_overs=self.match_overs)
            while not first_innings.innings_finished:
                update = input("CURRENT BALL: ").lower()
                if update in ['break', 'exit', 'quit', 'end']:
                    self.game_over = True
                    return 
                print(first_innings.score_update(update))
            chasing_score = first_innings.runs + 1

            second_innings = Innings(bat_team=self.bowl_team, bowl_team=self.bat_team, match_overs=self.match_overs, chasing_total=chasing_score)
            while not second_innings.innings_finished:
                update = input("CURRENT BALL: ")
                if update in ['break', 'exit', 'quit', 'end']:
                    self.game_over = True
                    return 
                print(second_innings.score_update(update))
            print(self.team_win(second_innings))
            self.game_over = True


