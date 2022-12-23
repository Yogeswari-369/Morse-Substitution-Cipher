import tkinter
from tkinter import IntVar, END, DISABLED, NORMAL
from tkinter import messagebox
from playsound import playsound
from PIL import ImageTk, Image


root = tkinter.Tk()
root.title('Morse Code Translator')


button_font = ('SimSun', 10)
root_color = "black"
frame_color = "white"
button_color = "#c0c0c0"
text_color = "#f8f8ff"
root.config(bg=root_color)


def convert():
    if language.get() == 1:
        get_morse()
    elif language.get() == 2:
        get_english()

        
def get_morse():
    morse_code = ""
    text = input_text.get("1.0", END)
    text = text.split()
    for letter in text:
        for ch in letter:
            ch=ch.upper()
            if ch in english_to_morse.keys():
                morse_char = english_to_morse[ch]
                morse_code += morse_char
                morse_code += " "
                morse_code += " "
            else:
                morse_code=""
                messagebox.showerror(title="Incorrect", message="Choose correct option")
                break        
    output_text.insert("1.0", morse_code)

    
              
        
def get_english():
    english = ""
    text = input_text.get("1.0", END)
    text=text.split("  ")
    flag=1
    for letter in text[:-1]:
        for ch in letter:
            if ch=='.' or ch=='-':
                flag=1
            else:
                flag=0
                break
        if flag:
            english_char = morse_to_english[letter]
            english += english_char
            english += ""
        else:
            english=""
            messagebox.showerror(title="Incorrect", message="Choose correct option")
            break
    
    output_text.insert("1.0", english)


def clear():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)



def play():
    if language.get() == 1:
        text = output_text.get("1.0", END)
    elif language.get() == 2:
        text = input_text.get("1.0", END)

    #Play the tones (., -, " " , |)
    for value in text:
        if value == ".":
            playsound('C:\\Users\\YOGESWARI\\OneDrive\\Documents\\MP3file\\dit.mp3')
            root.after(100)
        elif value == "-":
            playsound('C:\\Users\\YOGESWARI\\OneDrive\\Documents\\MP3file\\dah.mp3')
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(700)



def show_guide():
    global morse
    global guide
    guide = tkinter.Toplevel()
    guide.title("Morse Guide")
    guide.geometry('350x350+'+ str(root.winfo_x()+500) + "+" + str(root.winfo_y()))
    guide.config(bg=root_color)


    morse = ImageTk.PhotoImage(Image.open('C:\\Users\\YOGESWARI\\OneDrive\\Documents\\morse_chart.jpg'))
    label = tkinter.Label(guide, image=morse, bg=frame_color)
    label.pack(padx=10, pady=10, ipadx=5, ipady=5)
    close_button = tkinter.Button(guide, text="Close", font=button_font, bg=button_color, command=hide_guide)
    close_button.pack(padx=10, ipadx=50)
    guide_button.config(state=DISABLED)


def hide_guide():
    guide_button.config(state=NORMAL)
    guide.destroy()





english_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
            'U': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 
            'Y': '-.--', 'Z': '--..', '1': '.----',
            '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7':  '--...', '8': '---..', '9': '----.', 
            '0': '-----', ' ':' ', '|':'|', "":"" }

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])



input_frame = tkinter.LabelFrame(root, bg=frame_color)
output_frame = tkinter.LabelFrame(root, bg=frame_color)
input_frame.pack(padx=16, pady=(16,8))
output_frame.pack(padx=16, pady=(8,16))


input_text = tkinter.Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame, text="English --> Morse Code", variable=language, value=1, font=button_font, bg=frame_color)
english_button = tkinter.Radiobutton(input_frame, text="Morse Code --> English", variable=language, value=2, font=button_font, bg=frame_color)
guide_button = tkinter.Button(input_frame, text="Guide", font=button_font, bg=button_color, command=show_guide)

morse_button.grid(row=0, column=0, pady=(15,0))
english_button.grid(row=1, column=0)
guide_button.grid(row=2, column=0, sticky="WE", padx=10)


output_text = tkinter.Text(output_frame, height=8, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

convert_button = tkinter.Button(output_frame, text="Convert", font=button_font, bg=button_color, command=convert)
play_button = tkinter.Button(output_frame, text="Play Morse", font=button_font, bg=button_color, command=play)
clear_button = tkinter.Button(output_frame, text="Clear", font=button_font, bg=button_color, command=clear)
quit_button = tkinter.Button(output_frame, text="Quit", font=button_font, bg="red", command=root.destroy)
convert_button.grid(row=0, column=0, padx=10, ipadx=50) 
play_button.grid(row=1, column=0, padx=10, sticky="WE")
clear_button.grid(row=2, column=0, padx=10, sticky="WE")
quit_button.grid(row=3, column=0)


root.mainloop()

