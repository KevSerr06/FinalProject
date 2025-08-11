import tkinter as tk
from tkinter import messagebox
from models import Player, Habit

class HabitQuestApp:
    """Main GUI class for Habit Quest game."""

    def __init__(self, root: tk.Tk, player: Player):
        self.root = root
        self.root.title("Habit Quest")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.player = player
        self.habits = []

        #Setup frames
        self.start_frame = tk.Frame(self.root)
        self.game_frame = tk.Frame(self.root)
        self.end_frame = tk.Frame(self.root)

        for frame in (self.start_frame, self.game_frame, self.end_frame):
            frame.grid(row=0, column=0, sticky="nsew")
        self.setup_start_screen()
        self.setup_game_screen()
        self.setup_end_screen()
        self.show_frame(self.start_frame)

    def show_frame(self, frame: tk.Frame) -> None:
        """Raise the specified frame to the top"""
        frame.tkraise()

    #Start Screen
    def setup_start_screen(self) -> None:
        label = tk.Label(self.start_frame, text="🎯 Habit Quest", font=("Arial", 24))
        label.pack(pady=20)
        stats_button = tk.Button(self.start_frame, text="Game Stats", command=self.show_stats)
        stats_button.pack(pady=5)
        instructions_button = tk.Button(self.start_frame, text="Instructions", command=self.show_instructions)
        instructions_button.pack(pady=5)
        start_button = tk.Button(self.start_frame, text="Start Game", command=lambda: self.show_frame(self.game_frame))
        start_button.pack(pady=20)

    def show_stats(self) -> None:
        """Show player stats in a popup."""
        msg = f"Name: {self.player.get_name()}\nLevel: {self.player.get_level()}\nXP: {self.player.get_xp()}"
        messagebox.showinfo("Game Stats", msg)
    def show_instructions(self) -> None:
        """Show game instructions in a popup."""
        msg = "Complete daily habits to gain XP and level up!\nEach completed habit gives 10 XP.\nLevel up every 100 XP."
        messagebox.showinfo("Instructions", msg)

    #Game Screen
    def setup_game_screen(self) -> None:
        tk.Label(self.game_frame, text="Your Daily Habits", font=("Arial", 18)).pack(pady=10)
        self.habit_checkbuttons = []
        self.habit_vars = []

        #Placeholder habits
        sample_titles = ["Drink Water", "Read 10 Pages", "Exercise", "Study"]
        for title in sample_titles:
            habit = Habit(title)
            self.habits.append(habit)
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.game_frame, text=habit.get_title(), variable=var, font=("Arial", 12))
            cb.pack(anchor='w', padx=30)
            self.habit_checkbuttons.append(cb)
            self.habit_vars.append(var)
        self.stats_label = tk.Label(self.game_frame, text="", font=("Arial", 12))
        self.stats_label.pack(pady=10)
        self.update_game_stats()
        end_button = tk.Button(self.game_frame, text="End Day", command=self.end_game)
        end_button.pack(pady=20)

    def update_game_stats(self) -> None:
        """Update level and XP display in the game screen."""
        xp = self.player.get_xp()
        level = self.player.get_level()
        self.stats_label.config(text=f"Level: {level} XP: {xp}/100 Avatar: {self.player.get_avatar()}")

    def end_game(self) -> None:
        """Finish the game, award XP for completed habits, and go to the End Screen."""
        earned_xp = 0
        for i, var in enumerate(self.habit_vars):
            if var.get():
                earned_xp += 10
                self.habits[i].complete()
        self.player.add_xp(earned_xp)
        self.update_game_stats()
        self.show_frame(self.end_frame)

        #Saved earned XP for display
        self.daily_xp_earned = earned_xp

    #End Screen
    def setup_end_screen(self) -> None:
        label = tk.Label(self.end_frame, text=" GAME OVER ", font=("Arial", 24), fg="red")
        label.pack(pady=20)

        self.end_stats_label = tk.Label(self.end_frame, text="", font=("Arial", 14))
        self.end_stats_label.pack(pady=10)
        home_button = tk.Button(self.end_frame, text="Home", command=self.go_home)
        home_button.pack(pady=20)

    def go_home(self) -> None:
        """Return to start screen and update end stats."""
        summary = (
            f"XP earned today: {self.daily_xp_earned}\n"
            f"Total XP: {self.player.get_xp()}\n"
            f"Level: {self.player.get_level()}"
        )
        self.end_stats_label.config(text=summary)
        self.show_frame(self.start_frame)