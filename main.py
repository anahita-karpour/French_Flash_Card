import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
global_word = {}
flip_timer = None
data_dict = [] #.to_dic(orient="records") always produces a list of dictionaries, not a dictionary itself

#__________Read from french_words.csv______
def read_words():
    global data_dict
    words_to_learn = "./data/words_to_learn.csv"

    try:
        dataframe = pandas.read_csv(words_to_learn)
    except FileNotFoundError:
        dataframe = pandas.read_csv("./data/french_words.csv")  # dataframe

    # don't use finally here: finally implies "cleanup that must always happen regardless of outcome
    data_dict = dataframe.to_dict(orient="records")
    return data_dict


#___________Pick a random word/translation ____________
def random_word_generator():
    global data_dict

    # if dataframe is not None and not dataframe.empty:
    if data_dict: # false for both None and empty list[]
        a_word = random.choice(data_dict)

        print(a_word)
        return a_word
    return None

#__________________Put the randomly generated word on the flashcard_________
def next_flash_card():
    global global_word, flip_timer

    if flip_timer is not None:
        window.after_cancel(flip_timer) # cancel any pending flip from the previous card

    global_word = random_word_generator()
    if global_word is not None:
        #print(global_word)
        canvas.itemconfig(card_image, image = front_image)
        canvas.itemconfig(card_title, text="French", fill = "black")
        canvas.itemconfig(card_word, text=global_word.get("French"), fill="black")
        #Schedule card flip
        flip_timer = window.after(3000, flip_card)
    else:
        canvas.itemconfig(card_title, text="Done!", fill="black")
        canvas.itemconfig(card_word, text="You've learned all the words!", fill="black")
        check_button.config(state="disabled")
        cross_button.config(state="disabled")

def is_known():
    global global_word, data_dict
    # if dataframe is not None:
    if data_dict:
        if global_word in data_dict:
            #convert the dataframe to dic and remove the word
            data_dict.remove(global_word)

        #convert the dic to dataframe and saved into words_to_learn.csv file
        df = pandas.DataFrame(data_dict)
        df.to_csv("./data/words_to_learn.csv", index=False)
        # move on to the next word
        next_flash_card()

#__________________Flip Cards____________________________________
def flip_card():
    # card image should change to the card_back.png
    canvas.itemconfig(card_image, image = back_image)
    # change card_title color to white and text to "English"
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=global_word.get("English"), fill="white")

#------------------------------------------------UI SETUP -------------------------------------------------#
#____________Window________________
window = Tk()
window.title("French Flash Card")
window.config(padx=50, pady=50, width=900, height=625, bg=BACKGROUND_COLOR)
# window.after(3000, flip_card)

#_______Canvas___________________
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Canvas image
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=front_image) #center= half width, half height

canvas.grid(row=0, column=0, columnspan=2)

# Canvas text
card_title = canvas.create_text(400, 150, text ="", font=("Arial", 40, "italic"))
                                        #these positions are relative to the canvas
                                        # so 400 is halfway along the width and 150 is a bit towards the top.
card_word= canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
                                        #positioned at exactly the centre of the canvas



#_______Window Widgets - buttons_______________
check_image = PhotoImage(file="./images/right.png")
check_button = Button(image = check_image, highlightthickness=0 ,command= is_known)
check_button.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
check_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image = cross_image, highlightthickness=0, command = next_flash_card)
cross_button.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
cross_button.grid(row=1, column=0)

read_words()
next_flash_card()

#keept he window open and listening
window.mainloop()
