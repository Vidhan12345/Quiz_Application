from tkinter import *
import tkinter as tk
from tkinter import messagebox

win = Tk()
win.title("Quiz Application")
win.maxsize(width=1000, height=700)
win.minsize(width=1000, height=700)
win.configure(bg="#333333")

question_list = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
        "correct_option": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        "correct_option": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Claude Monet"],
        "correct_option": "A"
    },
    {
        "question": "Who is not the member of Straw hats?",
        "options": ["A. Brook", "B. Franky", "C. Carrot", "D. Cat burglar Nami"],
        "correct_option": "C"
    }
]

num_questions = 0  # Define num_questions as a global variable
current_question_index = 0
score = 0

def register():
    name = name_entry.get()
    password = password_entry.get()

    # Validate input
    if not name or not password:
        messagebox.showerror("Error", "Please enter your name and password.")
        return

    # Perform registration logic
    messagebox.showinfo("Registration Successful", "You have been registered for the quiz.")

    # Show the section for creating a custom quiz
    show_create_quiz_section()


def show_create_quiz_section():
    # Hide the registration widgets
    name_label.pack_forget()
    name_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    register_button.pack_forget()

    # Show the create quiz widgets
    default_quiz_button.pack()
    num_questions_label.pack(pady=20)
    num_questions_entry.pack()
    num_questions_button.pack()


def create_quiz():
    global num_questions  # Make num_questions accessible inside create_quiz function

    num_questions = num_questions_entry.get()
    if num_questions.isdigit() and int(num_questions) > 0:
        num_questions = int(num_questions)
        num_questions_label.config(text=f"Enter Question ({num_questions} remaining):")
        show_question_section()
    else:
        messagebox.showerror("Error", "Please enter a valid number of questions.")


def add_question():
    global num_questions  # Make num_questions accessible inside add_question function

    question = question_entry.get()
    option_a = option_a_entry.get()
    option_b = option_b_entry.get()
    option_c = option_c_entry.get()
    option_d = option_d_entry.get()
    correct_option = correct_option_entry.get()

    # Validate input
    if not question or not option_a or not option_b or not option_c or not option_d or not correct_option:
        messagebox.showerror("Error", "Please enter the question, all options, and the correct option.")
        return

    question_list.append({"question": question, "options": [option_a, option_b, option_c, option_d], "correct_option": correct_option})  # Append the question, options, and correct option to the list
    question_entry.delete(0, END)  # Clear the question entry field
    option_a_entry.delete(0, END)  # Clear the option A entry field
    option_b_entry.delete(0, END)  # Clear the option B entry field
    option_c_entry.delete(0, END)  # Clear the option C entry field
    option_d_entry.delete(0, END)  # Clear the option D entry field
    correct_option_entry.delete(0, END)  # Clear the correct option entry field

    messagebox.showinfo("Question Added", "Question has been added to the quiz.")

    num_questions -= 1
    if num_questions == 0:
        # All questions have been added, show the quiz creation complete message
        messagebox.showinfo("Quiz Creation Complete", "Quiz creation is complete. You can now start the quiz.")
        start_quiz()
    else:
        # Prompt the user for the next question
        num_questions_label.config(text=f"Enter Question ({num_questions} remaining):")


def show_question_section():
    # Hide the create quiz widgets
    default_quiz_button.pack_forget()
    num_questions_label.pack_forget()
    num_questions_entry.pack_forget()
    num_questions_button.pack_forget()

    # Show the question entry widgets
    question_label.pack()
    question_entry.pack()
    option_a_label.pack()
    option_a_entry.pack()
    option_b_label.pack()
    option_b_entry.pack()
    option_c_label.pack()
    option_c_entry.pack()
    option_d_label.pack()
    option_d_entry.pack()
    correct_option_label.pack()
    correct_option_entry.pack()
    question_button.pack()


def start_quiz():
    global current_question_index, score

    # Hide the question entry widgets
    question_label.pack_forget()
    question_entry.pack_forget()
    option_a_label.pack_forget()
    option_a_entry.pack_forget()
    option_b_label.pack_forget()
    option_b_entry.pack_forget()
    option_c_label.pack_forget()
    option_c_entry.pack_forget()
    option_d_label.pack_forget()
    option_d_entry.pack_forget()
    correct_option_label.pack_forget()
    correct_option_entry.pack_forget()
    question_button.pack_forget()

    # Display the first question
    current_question_index = 0
    score = 0
    display_question()


def display_question():
    global current_question_index

    question_data = question_list[current_question_index]
    question = question_data['question']
    options = question_data['options']

    # Create the question label
    question_text = f"Question {current_question_index + 1}: {question}"
    question_label = tk.Label(win, text=question_text)
    question_label.pack()

    # Create the option buttons
    for i, option in enumerate(options):
        option_text = f"Option {chr(ord('A') + i)}: {option}"
        option_button = tk.Button(win, text=option_text, command=lambda i=i: check_answer(i))
        option_button.pack()


def check_answer(selected_option_index):
    global current_question_index, score

    question_data = question_list[current_question_index]
    correct_option_index = ord(question_data['correct_option']) - ord('A')

    if selected_option_index == correct_option_index:
        score += 1

    current_question_index += 1

    if current_question_index == len(question_list):
        # All questions have been answered, show the final score
        messagebox.showinfo("Quiz Complete", f"You have completed the quiz!\nYour score: {score}/{len(question_list)}")
        win.destroy()
    else:
        # Display the next question
        for widget in win.winfo_children():
            widget.destroy()
        display_question()


# Create GUI elements
Login_label = tk.Label(win, text="Login",bg='#333333',fg="#FF3399",font=("Arial",25))

name_label = tk.Label(win, text="Username:",bg='#333333',fg="#FFFFFF",font=("Arial",16))
name_entry = tk.Entry(win,font=("Arial",16))

password_label = tk.Label(win, text="Password:",bg='#333333',fg="#FFFFFF",font=("Arial",16))
password_entry = tk.Entry(win, show="*",font=("Arial",16))

register_button = tk.Button(win, text="Register", command=register,bg='#FF3399',fg="#FFFFFF",font=("Arial",16))

default_quiz_button = tk.Button(win, text="Start Default Quiz", command=start_quiz,font=("Arial",16))

num_questions_label = tk.Label(win, text="Enter the number of additional questions:")
num_questions_entry = tk.Entry(win)
num_questions_button = tk.Button(win, text="Next", command=create_quiz)

question_label = tk.Label(win, text="Enter Question:")
question_entry = tk.Entry(win)
option_a_label = tk.Label(win, text="Option A:")
option_a_entry = tk.Entry(win)
option_b_label = tk.Label(win, text="Option B:")
option_b_entry = tk.Entry(win)
option_c_label = tk.Label(win, text="Option C:")
option_c_entry = tk.Entry(win)
option_d_label = tk.Label(win, text="Option D:")
option_d_entry = tk.Entry(win)
correct_option_label = tk.Label(win, text="Correct Option:")
correct_option_entry = tk.Entry(win)

question_button = tk.Button(win, text="Add", command=add_question)

# Show the registration widgets initially
Login_label.pack(pady=(210,10))
name_label.pack(pady=(10,10))
name_entry.pack(pady=10)
password_label.pack()
password_entry.pack(pady=(10))
register_button.pack()

win.mainloop()
