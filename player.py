"""Holds information about the player's stats and includes methods for adjusting them throughout gameplay."""

class Player:
    """Representing the player."""

    def __init__(self, name: str):
        """Starts the player with default stats"""
        self.name = name
        self.health = 100
        self.experience = 0
        self.score = 0

    def complete_habit(self) -> None:
        """Completes a habit. Increases energy and focus, also tracks completed habits."""
        self.completed_habits += 1
        self.focus = min(100, self.focus + 5)
        self.energy = max(0, self.energy - 10)
        self.total_actions += 1

    def skip_habit(self) -> None:
        """Skips a habit. Decreases energy and focus."""
        self.focus = max(0, self.focus - 10)
        self.energy = max(0, self.energy -5)
        self.total_actions += 1

    def game_is_over(self) -> bool:
        """Game is over based off player stats"""
        return self.energy <=0 or self.focus <= 0

    def reset(self) -> None:
        """Resets all of the player's stats back to default values"""
        self.energy = 100
        self.focus = 100
        self.completed_habit = 0
        self.total_actions = 0