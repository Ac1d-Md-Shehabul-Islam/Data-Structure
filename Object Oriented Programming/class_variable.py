class Player:
    
    team_score = 0                  #class variable
    
    def __init__(self,name,score):
        self.name = name
        self.run = score
        
    def hit_four(self):
        self.run +=4
        Player.team_score +=4
        
    def hit_six(self):
        self.run +=6
        Player.team_score +=6
        
    def get_team_score(self):
        print("Total run:",Player.team_score)
        
    def get_player_score(self):
        print(self.name, "score is:", self.run  )
        
#============================================================================


a = Player('Sakib',0)
b = Player('Tamim',0)
b.hit_six()
a.hit_four()
a.hit_six()
a.get_team_score()
a.get_player_score()
