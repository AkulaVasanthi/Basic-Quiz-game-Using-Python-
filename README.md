# Basic-Quiz-game-Using-Python's-Tkinter GUI library

# Tkinter Quiz App
A simple interactive Quiz Application built with Python's Tkinter GUI library.  
The app presents randomly selected multiple-choice questionsand also tracks the user's score and displays the final result.

# Features
- Randomly selects between 5 to 10 questions from a question bank.
- Displays one question at a time with multiple-choice options.
- Tracks the number of attempted, correct, wrong, and skipped questions.
- Shows the final score with detailed statistics.
- Simple and clean user interface using Tkinter.

# Requirements
- Python 3.x
- Tkinter (usually included with Python standard library)

# How to Run
Run the Python script: python quiz_app.py

# Process
1) Click Start Quiz to begin.
2) Select an answer and click Next Question.
3) Click Quit anytime to end the quiz and view results

# Code Overview
question_bank: A dictionary containing questions and their multiple-choice options.

answer_bank: A dictionary with the correct answer for each question.

Random selection of questions to create a varied quiz experience every time.

User interactions handled via Tkinter widgets: Label, Radiobutton, Button, and Frame.

Score and quiz progress tracked with global variables.

