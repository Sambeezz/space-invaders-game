class GameStats: 
    def __init__(self, polly):
        self.settings = polly.settings
        self.reset_stats()
        self.high_score = 0 
        
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0 