from settings import SoundsSettings


class Sounds:
    def play_explosion_sound(self):
        SoundsSettings.explosion_fx.play()

    def play_laser_sound(self):
        SoundsSettings.laser_sound.play()

    def play_small_explosion_sound(self):
        SoundsSettings.small_explosion_sound.play()

    def play_game_over_sound(self):
        SoundsSettings.game_over_sound.play()

    def play_win_game_sound(self):
        SoundsSettings.win_game_sound.play()


