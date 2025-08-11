from typing import Optional

import self


class User:
    """Represents a basic user in the Habit Quest system."""
    def __init__(self, name: str):
        """Initialize a user with a name, XP, and level."""
        self.__name = name
        self.__xp = 0
        self.__level = 1
    def get_name(self) -> str:
        """Return the user's name."""
        return self.__name
    def get_xp(self) -> int:
        """Return the user's current XP."""
        return self.__xp
    def get_level(self) -> int:
        """Return the user's current level."""
        return self.__level
    def add_xp(self, amount: int) -> None:
        """Add XP and handle level up if needed."""
        if amount > 0:
            self.__xp += amount
            while self.__xp >= self.__level * 100:
                self.__xp -= self.__level * 100
                self.__level += 1
    def reset_progress(self) -> None:
        """Reset XP and level (e.g., for a new game)."""
        self.__xp = 0
        self.__level = 1

class Player(User):
    """A player character, extended from User, with avatar or streaks."""
    def __init__(self, name: str, avatar: Optional[str] = None):
        """Initialize a player with optional avatar."""
        super().__init__(name)
        self.__avatar = avatar or "🧑"
    def get_avatar(self) -> str:
        """Return the player's avatar."""
        return self.__avatar
    def set_avatar(self, avatar: str) -> None:
        """Set a new avatar."""
        self.__avatar = avatar

class Habit:
    """Represents a single daily habit."""
    def __init__(self, title: str):
        """Initialize a habit with a title and completion status."""
        self.__title = title
        self.__completed = False
    def get_title(self) -> str:
        """Return the habit's title."""
        return self.__title
    def is_completed(self) -> bool:
        """Return True if the habit is completed, else False."""
        return self.__completed
    def complete(self) -> None:
        """Mark the habit as complete."""
        self.__completed = True
    def reset(self) -> None:
        """Reset the habit's completion status."""
    self.__completed = False