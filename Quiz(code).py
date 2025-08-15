from tkinter import *
import random

# === QUESTION BANK ===
question_bank = {
    "How long ago did dinosaurs die out ?": ['65 million years ago', '130 million years ago', '160 million years ago', '225 million years ago'],
    "Which animals dominated the earth after dinosaurs ?": ['Mammoths', 'Mammals', 'Reptiles', 'Apes'],
    "Which is the largest snake on the earth at over 10.5 m on average ?": ['Indian Python', 'Reticulated Python', 'Anaconda', 'GlassViper'],
    "Which is the largest fish found with a weight of about 30 tonnes ?": ['Tiger Shark', 'Whale Shark', 'Basking Shark', 'Greenland Shark'],
    "Which one is the smallest ocean in the world ?": ['Indian', 'Pacific', 'Atlantic', 'Arctic'],
    "Which country gifted the 'Statue of Liberty' to USA in 1886 ?": ['France', 'Canada', 'Brazil', 'England'],
    "Dead sea is located between which two countries ?": ['Jordan and Sudan', 'Turkey and UAE', 'Jordan and Israel', 'UAE and Egypt'],
    "On which date is world wide web day celebrated every year ?": ['August 6', 'August 1', 'September 1', 'July 1'],
    "What is baking soda ?": ['Potassium Chloride', 'Potassium Carbonate', 'Potassium Hydroxide', 'Sodium Bicarbonate'],
    "Plants receive Nutrients mainly from ?": ['Chlorophyll', 'Atmosphere', 'Light', 'Soil'],
}

# === ANSWER KEY ===
answer_bank = {
    "How long ago did dinosaurs die out ?": "65 million years ago",
    "Which animals dominated the earth after dinosaurs ?": "Mammals",
    "Which is the largest snake on the earth at over 10.5 m on average ?": "Reticulated Python",
    "Which is the largest fish found with a weight of about 30 tonnes ?": "Whale Shark",
    "Which one is the smallest ocean in the world ?": "Arctic",
    "Which country gifted the 'Statue of Liberty' to USA in 1886 ?": "France",
    "Dead sea is located between which two countries ?": "Jordan and Israel",
    "On which date is world wide web day celebrated every year ?": "August 1",
    "What is baking soda ?": "Sodium Bicarbonate",
    "Plants receive Nutrients mainly from ?": "Soil",
}

# === QUIZ VARIABLES ===
selected_questions = dict(random.sample(list(question_bank.items()), k=random.randint(5, 10)))
question_list = list(selected_questions.keys())
current_question_index = 0
user_score = 0
attempted_questions = 0

# To keep track of user answers per question (index-based)
user_answers = [None] * len(question_list)

# === FUNCTIONS ===
def start_quiz():
    start_button.forget()
    button_frame.pack(pady=20)
    prev_button.pack(side=LEFT, padx=10)
    next_button.pack(side=LEFT, padx=10)
    quit_button.pack(side=LEFT, padx=10)
    show_question()

def show_question():
    clear_frame()
    global current_question_index

    if current_question_index < len(question_list):
        q = question_list[current_question_index]
        Label(f1, text=f"Question {current_question_index + 1}: {q}", font="calibre 20 normal", padx=15, pady=10, wraplength=750, justify=LEFT).pack(anchor=NW)
        
        # Set user_ans to previously selected answer or None
        if user_answers[current_question_index] is not None:
            user_ans.set(user_answers[current_question_index])
        else:
            user_ans.set('None')

        for opt in selected_questions[q]:
            Radiobutton(f1, text=opt, variable=user_ans, value=opt, font="calibre 16 normal", padx=20).pack(anchor=NW)

    update_buttons()

def update_buttons():
    # Disable Prev button if on first question
    if current_question_index == 0:
        prev_button.config(state=DISABLED)
    else:
        prev_button.config(state=NORMAL)

    # Disable Next button if on last question
    if current_question_index == len(question_list) - 1:
        next_button.config(text="Submit")
    else:
        next_button.config(text="Next Question")

def save_answer():
    global attempted_questions, user_score
    selected = user_ans.get()
    if selected != 'None':
        # If this question was not answered before, increment attempted_questions
        if user_answers[current_question_index] is None:
            attempted_questions += 1
        user_answers[current_question_index] = selected
    else:
        # If changing answer to None, decrement attempted if previously answered
        if user_answers[current_question_index] is not None:
            attempted_questions -= 1
        user_answers[current_question_index] = None

def next_question():
    global current_question_index
    save_answer()

    # If last question, show results
    if current_question_index == len(question_list) - 1:
        calculate_score()
        show_result()
    else:
        current_question_index += 1
        show_question()

def prev_question():
    global current_question_index
    save_answer()
    if current_question_index > 0:
        current_question_index -= 1
        show_question()

def calculate_score():
    global user_score
    user_score = 0
    for idx, q in enumerate(question_list):
        if user_answers[idx] == answer_bank[q]:
            user_score += 1

def show_result():
    clear_frame()
    button_frame.forget()

    total = len(question_list)
    wrong = attempted_questions - user_score
    skipped = total - attempted_questions

    result_text = f"Your Score: {user_score} / {total}\n"
    result_text += f"Attempted: {attempted_questions}\nCorrect: {user_score}\nWrong: {wrong}\nSkipped: {skipped}"

    Label(f1, text=result_text, font="calibre 20 bold", pady=20).pack()
    Label(f1, text="Thanks for Participating!😊", font="calibre 18 italic").pack()

def quit_quiz():
    save_answer()
    calculate_score()
    show_result()

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

root = Tk()
root.title("Quiz App")
root.geometry("850x520")
root.minsize(800, 500)

# Initialize tkinter variables AFTER root is created
user_ans = StringVar()
user_ans.set('None')

Label(root, text="Quiz App", font="calibre 40 bold", relief=SUNKEN, background="lightgreen", padx=10, pady=5).pack()
Label(root, text="", font="calibre 20 bold").pack()

start_button = Button(root, text="Start Quiz", command=start_quiz, font="calibre 20 bold", background="orange")
start_button.pack()

f1 = Frame(root)
f1.pack(side=TOP, fill=X)

# Buttons (hidden at start)
button_frame = Frame(root)

prev_button = Button(
    button_frame,
    text="Previous Question",
    command=prev_question,
    font="calibre 20 bold",
    background="#D3D3D3",  # Light Gray
    width=15
)

next_button = Button(
    button_frame,
    text="Next Question",
    command=next_question,
    font="calibre 20 bold",
    background="#87CEEB",  # SkyBlue
    width=15
)

quit_button = Button(
    button_frame,
    text="Quit",
    command=quit_quiz,
    font="calibre 20 bold",
    background="#FF6961",  # Light Coral
    width=10
)

root.mainloop()
