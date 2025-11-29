class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def score_as_string(self):
        if self.score == 0:
            return "Love"
        elif self.score == 1:
            return "Fifteen"
        elif self.score == 2:
            return "Thirty"
        elif self.score == 3:
            return "Forty"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score += 1
        else:
            self.player2.score += 1

    def get_score(self):
        if self.player1.score == self.player2.score:
            if self.player1.score < 3:
                score = self.player1.score_as_string() + "-All"
            else:
                score = "Deuce"
        elif self.player1.score >= 4 or self.player2.score >= 4:
            if self.score_difference() == 1:
                score = "Advantage " + self.leading_player().name
            else:
                score = "Win for " + self.leading_player().name
        else:
            score = self.player1.score_as_string() + "-" + self.player2.score_as_string()

        return score

    def leading_player(self):
        if self.player1.score > self.player2.score:
            return self.player1
        return self.player2

    def score_difference(self):
        return abs(self.player1.score - self.player2.score)
