class Settings():
    """Класс для хранения настроек игры."""
    def __init__(self):
        # настройки экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (200, 200, 200)
        # скорость коробля
        self.speed_ship = 1.3
        # настройки пули
        self.bullet_speed_factor = 0.2
        self.bullet_bg_color = 255, 255, 255
        self.bullet_maximum = 5
        # Настройки пришельца
        self.alien_bg_color = (255, 255, 255)
        self.alien_speed_factor = 0.02
        self.alien_speed_direchions = -1