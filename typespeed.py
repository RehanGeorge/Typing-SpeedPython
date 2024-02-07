import tkinter as tk
from time import time
import random

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump",
]

# Initialize Tkinter window
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("800x400")


# Function to choose a random sentence
def choose_sentence():
    global sentence, start_time
    sentence = random.choice(sentences)
    sentence_label.config(text=sentence)
    start_time = time()


# Function to start the timer
def start_timer(event):
    global start_time
    start_time = time()
    print(start_time)


# Function to stop the timer and calculate typing speed
def stop_timer(event):
    end_time = time()
    time_taken = round(end_time - start_time, 2)
    words_per_minute = round((len(sentence.split()) / time_taken) * 60)
    result_label.config(
        text=f"Your typing speed is {words_per_minute} words per minute"
    )


# Label to display the chosen sentence
sentence_label = tk.Label(window, text="", font=("Arial", 12))
sentence_label.pack()

# Text entry field
entry_field = tk.Entry(window, font=("Arial", 12))
entry_field.pack()
entry_field.bind("<Return>", stop_timer)

# Label to display the result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

# Button to start the test
start_button = tk.Button(window, text="Start", command=choose_sentence)
start_button.pack()

# Run the Tkinter event loop
window.mainloop()
