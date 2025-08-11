import random

class GameManager:
    """Manages transitions, stat tracking and game state"""
    def __init__(self, gui):
        self.gui = gui
        self.player = None
        self.day = 1
        self.max_days = 5

    def start_game(self, name):
        """Starts the game by setting the day to 1 and updating stats"""
        from player import Player
        self.player = Player(name)
        self.current_day = 1
        self.gui.show_game_screen()
        self.gui.update_stats(self.player)

    def perform_task(self):
        """Increases stats and handles task completion"""
        result = random.choice(['win', 'lose'])
        if result == 'win':
            self.player.add_experience(10)
            self.player.update_health(5)
            self.gui.show_task_result("Success! +10 XP, +5 HP")
        else:
            self.player.add_experience(5)
            self.player.update_health(-10)
            self.gui.show_task_result("Failed! +5 XP, -10 HP")
        self.gui.update_stats(self.player)
        self.next_day()

    def next_day(self):
        """Updates stat labels from player data"""
        self.current_day += 1
        if self.player.health <= 0 or self.current_day > self.max_days:
            self.end_game()
        else:
            self.gui.update_day(self.current_day)

    def end_game(self):
        """Ends the game by updating stats"""
        self.gui.show_game_over(self.player)