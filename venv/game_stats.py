class Game_Stas():
    """Ведет статистику игры."""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.stats_reset()
        self.activ_game = False
    def stats_reset(self):
        """Обнавляет статистику в игре"""
        self.ship_quantity = self.ai_settings.speed_quantity