class FootballScorer:
    """
    Calculates the points of two teams based on their scores.

    ...

    Attributes
    ----------
    name_team_1 : str
        a string with name of the first team
    name_team_2 : str
        a string with the name of the second team
    score_team_1 : int
        an integer with the score of the first team
    score_team_2 : int
        an integer with the score of the second team
    points_team_1 : int
        an integer with the points of the first team
    points_team_2 : int
        an integer with the points of the second team

    Methods
    -------
    check_points():
        Checks if the scores of the teams are valid (not negative)
    input_names_scores():
        Inputs the names and scores of the teams
    calculate_points():
        Calculates the points of the teams based on their scores
    """

    def __init__(self, name_team_1=None, name_team_2=None, score_team_1=None, score_team_2=None):
        """
        Constructs all the necessary attributes for the football scorer object.

        Parameters
        ----------
            name_team_1 : str
                name of the first team
            name_team_2 : str
                name of the second team
            score_team_1 : int
                score of the first team
            score_team_2 : int
                score of the second team
        """
        self.name_team_1 = name_team_1
        self.name_team_2 = name_team_2
        self.score_team_1 = score_team_1
        self.score_team_2 = score_team_2
        self.points_team_1, self.points_team_2 = None, None
        if None in (self.name_team_1, self.name_team_2):
            self.input_names_scores()
        self.check_points()

    def check_points(self):
        """
        Checks if the scores of the teams are valid (not negative)
        """
        if (self.score_team_1 or self.score_team_2) < 0:
            raise ValueError("Invalid Score")

    def input_names_scores(self):
        """
        Inputs the names and scores of the teams
        """
        self.name_team_1 = input("Enter name of team 1: ")
        self.name_team_2 = input("Enter name of team 2: ")
        self.score_team_1 = int(input(f"Enter score of {self.name_team_1}: "))
        self.score_team_2 = int(input(f"Enter score of {self.name_team_2}: "))

    def calculate_points(self):
        """
        Calculates the points of the teams based on their scores
        """
        if self.score_team_1 > self.score_team_2:
            self.points_team_1, self.points_team_2 = 3, 0
        elif self.score_team_1 < self.score_team_2:
            self.points_team_1, self.points_team_2 = 0, 3
        else:
            self.points_team_1, self.points_team_2 = 1, 1

    def __str__(self):
        """
        Returns the scores and points of the teams in a formatted string
        """
        return (f"Team 1: Score: {self.score_team_1}, Points: {self.points_team_1}\n"
                f"Team 2: Score: {self.score_team_2}, Points: {self.points_team_2}")


if __name__ == '__main__':
    # This will call the function input_names_scores() in the object initialization
    fs = FootballScorer()
    # and then calculate_points()
    fs.calculate_points()
    # and then print using the reserved method __str__()
    print(fs)
    # This will directly input the names and scores in the object initialization
    fs2 = FootballScorer('t1', 't2', 1, 2)
    fs2.calculate_points()
    print(fs2)
