import tkinter as tk
import random

window = tk.Tk()
window.minsize(height=300, width=600)
window.config(pady=20,padx=20)
window.title('Typing Speed Test')

words = ["An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state. Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission.", "Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. The Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large supermarkets.", "Two common terms used to describe a salesperson are 'Farmer' and 'Hunter'. The reality is that most professional salespeople have a little of both. A hunter is often associated with aggressive personalities who use aggressive sales technique.", "A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing. This can be accomplished using one or both thumbs.", "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference in typing speed between touch typists and self-taught hybrid typists. According to the study, 'The number of fingers does not determine typing speed... People using self-taught typing strategies were found to be as fast as trained typists... instead of the number of fingers, there are other factors that predict typing speed.", "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. They can also be used as a tool by those learning to read, learning to speak a non-native language, or in an environment where the audio is difficult to hear or is intentionally muted.", "A freelancer or freelance worker, is a term commonly used for a person who is self-employed and is not necessarily committed to a particular employer long-term. Freelance workers are sometimes represented by a company or a temporary agency that resells freelance labor to clients; others work independently or use professional associations or websites to get work."]

time = 0

# Functons.

def start_game():
    global time
    time=0
    global words
    game_window=tk.Toplevel()

    game_window.minsize(height=500, width=200)
    game_window.title('Typing Speed Test')
    game_window.config(bg='lightblue')

    # Display the random text here.
    text_display = tk.Text(game_window, height=2, width=30, font=('Times', 20))

    original_text = random.choice(words).lower()
    text_display.insert('1.0', original_text)

    text_display.config(state='disabled')  # read-only
    text_display.pack(pady=20,padx=20)

    timer_label = tk.Label(window, text="", font=('Helvetica', 20), fg='white')
    timer_label.pack(pady=20)

    # Take the user input.

    user_input = tk.Entry(game_window,font=('Times',20),bg='white',fg='black',width=30)
    user_input.pack(ipady=10)

    # Set the timer.
    def update_timer():
        global time
        time +=1
        minutes = int(time/60)
        seconds = time % 60
        hours = int(minutes/60)
        minutes = minutes % 60

        # Update the label with the current count
        label.config(text=f"Time: {hours} h : {minutes} m : {seconds} s")
        timer_label.config(text=f"Time: {hours} h : {minutes} m : {seconds} s")
        # Schedule this function to run again in 1 second (1000ms)
        game_window.after(1000, update_timer)


    label = tk.Label(game_window, font=("Helvetica", 20),bg='white',fg='black')
    label.pack(pady=30)

    # Start the timer loop
    update_timer()

    result_label = tk.Label(window, text="", font=('Helvetica', 20), fg='white')
    result_label.pack(pady=20)



    # Create button and restart the game.
    def restart_game():
        game_window.destroy()
        start_game()

    # Calculate the words per minute.
    def calculate_wpm():
        global time

        typed_text = user_input.get()

        correct_chars = 0

        for i in range(min(len(typed_text), len(original_text))):
            if typed_text[i] == original_text[i]:
                correct_chars += 1

        minutes = time / 60

        if minutes > 0:
            wpm = (correct_chars / 5) / minutes
        else:
            wpm = 0

        result_label.config(text=f"WPM: {int(wpm)}")

        game_window.destroy()



    start_again_button = tk.Button(game_window,text='Start Again',command=restart_game)
    start_again_button.pack(padx=20,pady=30)

    done_button = tk.Button(game_window,text="Done",command=calculate_wpm)
    done_button.pack()




# Label and Button.

label1 = tk.Label(text="Test Your Typing Speed Here",fg='white',font=('sans serif',25),pady=30,cursor="hand2")
label1.pack()

start_button = tk.Button(window, text="Start", font=('Times', 20),
                         bg='green', fg='black', padx=20, pady=10,
                         command=start_game)

start_button.pack(pady=20)


window.mainloop()

