"""Saves and loads player stats from a local file."""

import os
FILE_NAME = "player_stats.txt"

def save_stats(player) -> None:
    """Saves player stats to a local file."""
    with open(FILE_NAME, "w") as file:
        file.write(f"{player.name}\n")
        file.write(f"{player.energy}\n")
        file.write(f"{player.focus}\n")
        file.write(f"{player.completed_habit}\n")
        file.write(f"{player.total_actions}\n")

def load_stats() -> dict:
    """Loads player stats from a local file if it exists."""
    if not os.path.isfile(FILE_NAME):
        return None
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    if len(lines) < 5:
        return None

    return{
        "name": lines[0].strip(),
        "energy": int(lines[1]),
        "focus": int(lines[2]),
        "completed_habit": int(lines[3]),
        "total_actions": int(lines[4]),
    }