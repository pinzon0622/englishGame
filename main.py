import os
import tkinter as tk
from tkinter import ttk, messagebox
from questionsData import questions



def show_question():
    question = questions[0]
    question_label.config(text=question["question"])
    for i, option in enumerate(question["options"]):
        option_buttons[i].config(text=option, command=lambda: check_answer(option))
    next_button.config(state="disabled")

def check_answer(answer):
    question = questions[0]
    if answer == question["answer"]:
        messagebox.showinfo("Correct", "You got it right!")
    else:
        messagebox.showerror("Incorrect", "You got it wrong!")
        print("The correct answer is", question["answer"])
        print("You selected", answer)
    next_button.config(state="normal")

def next_question():
    pass

root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text="Question goes here")
question_label.pack()



option_buttons = []
for i in range(4):
    button = tk.Button(root, text="Option " + str(i + 1))
    button.pack()
    option_buttons.append(button)

next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack()

show_question()

root.mainloop()
