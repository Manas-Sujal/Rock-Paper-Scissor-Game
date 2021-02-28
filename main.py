from tkinter import *
import tkinter.messagebox
import random


global options, OpponentChoice

options = ["Rock", "Paper", "Scissor"]


def rock():
    OpponentChoice = random.choice(options)
    if OpponentChoice == "Rock":
        tkinter.messagebox.showinfo("Tie", "The Computer Choose Rock, Its a Tie")
    if OpponentChoice == "Paper":
        tkinter.messagebox.showinfo("Lost", "The Computer Choose Paper, You Lost")
    if OpponentChoice == "Scissors":
        tkinter.messagebox.showinfo("Win", "The Computer Choose Scissor, You Win")

def scissor():
    OpponentChoice = random.choice(options)
    if OpponentChoice == "Rock":
        tkinter.messagebox.showinfo("Lost", "The Computer Choose Rock, You Lost")
    if OpponentChoice == "Paper":
        tkinter.messagebox.showinfo("Win", "The Computer Choose Paper, You Win")
    if OpponentChoice == "Scissors":
        tkinter.messagebox.showinfo("Tie", "The Computer Choose Scissor, Its a Tie")

def paper():
    OpponentChoice = random.choice(options)
    if OpponentChoice == "Rock":
        tkinter.messagebox.showinfo("Win", "The Computer Choose Rock, You Win")
    if OpponentChoice == "Paper":
        tkinter.messagebox.showinfo("Tie", "The Computer Choose Paper, Its a Tie")
    if OpponentChoice == "Scissors":
        tkinter.messagebox.showinfo("Lost", "The Computer Choose Scissor, You Lost")


def start():
    global screen2
    screen2 = Tk()
    screen2.geometry("600x600")
    screen2.title("Rock, Paper and Scissors")
    Label(screen2, text="Rock, Paper and Scissors", bg="gray"
          , width="300", height="3", font=("Brush MT Script", 13)).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Your Choice : "
          , width="300", height="3", font=("Brush MT Script", 13)).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Rock : ", command = rock
          , width="15", height="3", font=("Brush MT Script", 13)).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Paper : ", command = paper
           , width="15", height="3", font=("Brush MT Script", 13)).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Scissors : ", command = scissor
           , width="15", height="3", font=("Brush MT Script", 13)).pack()

    screen2.mainloop()

start()