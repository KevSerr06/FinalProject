
import tkinter as tk
from gui import HabitQuestApp
from models import Player

def main() -> None:
    """Start the application."""
    window = tk.Tk()
    player = Player(name="Player One", avatar="🧙")
    app = HabitQuestApp(window, player)
    window.mainloop()

if __name__ == "__main__":
    main()