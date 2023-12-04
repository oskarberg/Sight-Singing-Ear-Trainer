import tkinter as tk
import pygame
import random

# Initialize Pygame Mixer
pygame.mixer.init()

# Note Database
notes = {'1': 'C3', '2': 'D3', '3': 'E3', '4': 'F3', '5': 'G3', '6': 'A3', '7': 'B3', '8': 'C4'}
current_melody = []

# Function to Play Note
def play_note(note):
    pygame.mixer.Sound(f'Piano notes/{notes[note]}.mp3').play()


# Function to Play Melody
def play_melody():
    for note in current_melody:
        play_note(note)
        pygame.time.wait(1000)  # Wait for 500 milliseconds between notes

# Function to Generate Melody
def generate_melody_buttons(length=6):
    global current_melody
    current_melody = []
    last_note = None

    for _ in range(length):
        note = random.choice(list(notes.keys()))
        while note == last_note:  # Avoid consecutive repeats
            note = random.choice(list(notes.keys()))
        current_melody.append(note)
        last_note = note

    update_melody_buttons()

# Update the melody buttons display
def update_melody_buttons():
    for widget in melody_frame.winfo_children():
        widget.destroy()
    for note in current_melody:
        btn = tk.Button(melody_frame, text=note, command=lambda n=note: play_note(n))
        btn.pack(side='left', padx=5)

# GUI Setup
root = tk.Tk()
root.title("Sight Singing App")

# Set Window Size and Disable Resizing
root.geometry("600x300")
root.resizable(False, False)

# Melody Buttons Frame
melody_frame = tk.Frame(root)
melody_frame.pack(pady=20)

# Generate Melody Button
generate_button = tk.Button(root, text="Generate Melody", command=generate_melody_buttons)
generate_button.pack(pady=10)

# Play Melody Button
play_melody_button = tk.Button(root, text="Play Melody", command=play_melody)
play_melody_button.pack(pady=10)

# Play Root Note Button
play_root_note_button = tk.Button(root, text="Play Root Note (C3)", command=lambda: play_note('1'))
play_root_note_button.pack(pady=10)

# Main loop
root.mainloop()
