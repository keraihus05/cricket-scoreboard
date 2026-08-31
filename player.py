class Player():
    def __init__(self, name):
        self.name = name

        #Batting Attributes
        self.runs = 0
        self.balls_faced = 0
        self.out = False

        #Bowling Attributes
        self.wickets = 0
        self.overs_bowled = 0
        self.runs_conc = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


    