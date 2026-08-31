from utils import find_player

dismissals = ['out', 'wicket', 'w', 'lbw', 'caught', 'stumped', 'runout', 'hitwicket', 'obstructingthefield', 'retiredhurt']
extras = ['wide', 'noball', 'bye', 'leg bye', 'penalty', 'nb']
bowler_dismissals = ['lbw', 'caught', 'stumped', 'cnb', 'bowled', 'hitwicket']
field_dismissals = ['runout', 'obstructingthefield', 'retiredhurt']

class Innings():
    def __init__(self, bat_team, bowl_team, match_overs, chasing_total = None):
        self.bat_team = bat_team
        self.bowl_team = bowl_team
        self.match_overs = match_overs
        self.bowler = ''
        self.chase = chasing_total
        self.innings_finished = False
        self.batters_used = []
        self.start_innings()


    def start_innings(self):
        self.runs, self.wickets, self.bowled, self.overs = 0, 0, 0, 0
        self.striker, self.non_striker = self.choose_openers()
        self.bowler = self.get_bowler()
        return self.runs, self.wickets, self.bowled, self.overs

    def choose_openers(self):
        print(f"\n--- {self.bat_team.name.upper()} INNINGS - CHOOSE OPENERS ---")
        striker = self.select_batter("Striker: ")
        non_striker = self.select_batter("Non-striker: ")
        print(f"\nOpening pair: {striker.name} (striker) & {non_striker.name} (non-striker)")
        return striker, non_striker

    def select_batter(self, prompt):
        available = [p for p in self.bat_team.team if p not in self.batters_used]
        print("Available batters: " + ", ".join(p.name for p in available))

        while True:
            query = input(prompt).lower().strip()
            matched_player = find_player(query, available)

            if matched_player is None:
                print("Not available to bat (not in team, already batted, or already selected).")
                continue

            self.batters_used.append(matched_player)
            return matched_player

    def score_update(self, current_ball):
        current_ball = str(current_ball)
        current_ball=current_ball.lower().replace(" ", "")

        if current_ball.isdigit():
            runs = int(current_ball)
            self.score_runs(runs)
            return self.scoreboard()

        elif current_ball in dismissals:
            self.record_wicket(current_ball)
            return self.scoreboard()

        elif current_ball in extras:
            extra_type = current_ball
            self.score_extras(extra_type, runs=int(input('How many extra runs?: ')))
            return self.scoreboard()

        return "Incorrect input"

    def score_runs(self, runs):
        if runs in range(0, 7):
            self.runs += runs
            self.striker.runs += runs
            self.striker.balls_faced += 1
            self.bowled += 1
            self.bowler.runs_conc += runs
            self.change_strike(runs=runs)
            self.check_over()
            self.innings_over()
            return 
        return "THIS MANY RUNS NOT POSSIBLE"

    def record_wicket(self, method):
        self.wickets += 1
        if method in ['wicket', 'w', 'out']:
            method = self.get_wicket_method()
        if method in bowler_dismissals:
            self.bowler.wickets += 1
        self.bowled += 1
        self.striker.balls_faced += 1
        self.next_batter()
        self.check_over()
        self.innings_over()

    def get_wicket_method(self):
        while True:
            method = input("How Out?").lower().replace(" ", "")

            if method in bowler_dismissals or method in field_dismissals:
                return method

            print("INVALID DISMISSAL TYPE")

    def score_extras(self, extra_type, runs):
        self.bowler.runs_conc += runs
        if extra_type.lower() == 'wide':
            self.runs += runs + 1
            self.change_strike(runs=runs)

        elif extra_type in ['noball', 'nb']:
            self.runs += runs + 1
            self.striker.balls_faced += 1
            self.change_strike(runs=runs)

        elif extra_type.lower() in ['bye', 'legbye']: 
            self.runs += runs
            self.bowled += 1
            self.change_strike(runs=runs)

        elif extra_type.lower() == 'penalty':
            self.runs += runs

    def check_over(self):
        if self.bowled == 6:
            self.bowled = 0
            self.overs += 1
            self.change_strike()
            self.bowler.overs_bowled += 1
            print(f"\n--- END OF OVER {self.overs} ---")
            print(self.scoreboard())
            if self.wickets < 10 and not self.innings_over_check():
                self.get_bowler()

    def innings_over_check(self):
        # peek at whether the innings is already done, without setting state,
        # so check_over doesn't ask for a new bowler needlessly
        if self.wickets == 10:
            return True
        if self.overs == self.match_overs:
            return True
        if self.chase is not None and self.runs >= self.chase:
            return True
        return False

    def change_strike(self, runs=0):
        if runs % 2 != 0:
            self.striker, self.non_striker = self.non_striker, self.striker
            return self.striker, self.non_striker
        return self.striker, self.non_striker

    def next_batter(self):
        while True:
            query = input("Who's out? ").lower().strip()
            who_out = find_player(query, [self.striker, self.non_striker])

            if who_out is None:
                print("That's not one of the two batters at the crease. Try again.")
                continue
            break

        who_out.out = True

        if self.wickets == 10:
            return None

        new_batter = self.select_batter("Next batter: ")

        if who_out is self.striker:
            self.striker = new_batter
        else:
            self.non_striker = new_batter

        print(f"\n{who_out.name} is out! {new_batter.name} comes to the crease.")
        return new_batter

    def innings_over(self):
        if self.wickets == 10:
            self.innings_finished = True
        elif self.overs == self.match_overs:
            self.innings_finished = True
        elif self.chase is not None and self.runs >= self.chase:
            self.innings_finished = True
        return 

    def get_bowler(self):
        max_overs = self.match_overs // 5
        print("Bowling side: " + ", ".join(
            f"{p.name} ({p.overs_bowled}/{max_overs} overs)" for p in self.bowl_team.team
        ))

        while True:
            query = input("BOWLER'S NAME: ").lower().strip()
            matched_player = find_player(query, self.bowl_team.team)

            if matched_player is None:
                print("Not in bowling team.")
                continue

            if self.bowler != '' and matched_player.name == self.bowler.name:
                print("BOWLER JUST BOWLED!!")
                continue

            if matched_player.overs_bowled == self.match_overs // 5:
                print("NO MORE OVERS LEFT!")
                continue

            self.bowler = matched_player
            return self.bowler

    def balls_remaining(self):
        total_balls = self.match_overs * 6
        bowled_balls = self.overs * 6 + self.bowled
        return max(total_balls - bowled_balls, 0)

    def scoreboard(self):
        width = 42
        run_rate = self.runs / self.overs if self.overs > 0 else 0

        lines = []
        lines.append("=" * width)
        lines.append(f"{self.bat_team.name.upper():^{width}}")
        lines.append("=" * width)
        lines.append(f" {self.runs}/{self.wickets}   ({self.overs}.{self.bowled} overs)   RR {run_rate:.2f}")
        lines.append("-" * width)
        lines.append(f" {self.striker.name + '*':<28}{self.striker.runs:>4} ({self.striker.balls_faced})")
        lines.append(f" {self.non_striker.name:<28}{self.non_striker.runs:>4} ({self.non_striker.balls_faced})")

        if self.bowler:
            lines.append("-" * width)
            lines.append(f" Bowler: {self.bowler.name}  {self.bowler.wickets}-{self.bowler.runs_conc}")

        if self.chase is not None:
            lines.append("-" * width)
            runs_needed = max(self.chase - self.runs, 0)
            lines.append(f" NEED {runs_needed} FROM {self.balls_remaining()} BALLS")

        lines.append("=" * width)
        return "\n".join(lines)