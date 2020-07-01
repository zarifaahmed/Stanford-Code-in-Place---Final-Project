import tkinter
from tkinter import *
from tkinter import filedialog
import PIL
from PIL import ImageTk, Image
import random
from random import choice

FILE_NAME = "color.txt"
root = Tk()
root.title = ("Code in Place Profile")
name = Entry(root, bg="blue", fg="white", width="40")
name.place(x=127, y=24)
surname = Entry(root, bg="blue", fg="white", width="40")
surname.place(x=127, y=70)
password = Entry(root, bg="blue", fg="white", width="40")
password.place(x=127, y=115)


def main():
    root.minsize(width="500", height="500")
    root.configure(bg="white")
    image_upload_btn()
    information_labels()
    button = tkinter.Button(root, text='Sign in', padx="70", bg="white", command=submit_infos_btn).place(x=127, y=230)
    root.mainloop()


def information_labels():
    name_label = Label(root, bg="white", text="Enter name").place(x=127, y=2)
    surname_label = Label(root, bg="white", text="Enter surname").place(x=127, y=45)
    password_label = Label(root, bg="white", text="Enter password").place(x=127, y=90)


def submit_infos_btn():
    user_name = name.get()
    user_sname = surname.get()
    user_pass = password.get()
    arr_name = [user_name, user_pass, user_sname]
    clear_frame()
    global name_check
    global password_check

    root.minsize(width="500", height="500")
    log_in_label = Label(root, bg="white", text="Please log in your account").place(x=127, y=2)

    name_label = Label(root, bg="white", text="Name").place(x=127, y=30)
    name_check = Entry(root, bg="blue", fg="white", width="40")
    name_check.place(x=127, y=55)
    password_label = Label(root, bg="white", text="Password").place(x=127, y=75)
    password_check = Entry(root, bg="blue", fg="white", width="40")
    password_check.place(x=127, y=100)
    button = tkinter.Button(root, text='Log in', padx="100", bg="white", command=lambda: log_in(arr_name)).place(x=127,
                                                                                                                 y=150)


def log_in(arr_name):
    password_checker = password_check.get()
    name_checker = name_check.get()
    if arr_name[0] == name_checker and arr_name[1] == password_checker:
        clear_frame()
        entrance_game_page(arr_name)
    else:
        welcome_label = Label(root, bg="white", text="Something is wrong. Enter right name and password").place(x=127,
                                                                                                                y=5)


def entrance_game_page(arr_name):
    root.minsize(width="500", height="500")
    welcome_label = Label(root, bg="white", text="WELCOME TO GAME  " + arr_name[0] + " " + arr_name[2] + "!").place(x=100,
                                                                                                                  y=10)
    my_image_label = Label(image=my_image).place(x=100, y=40)
    button = tkinter.Button(root, text='Show games', padx="108", bg="white",
                            command=lambda: game_starter(arr_name)).place(x=100, y=350)


def game_starter(arr_name):
    clear_frame()
    root.minsize(width="500", height="500")
    welcome_label = Label(root, bg="white", text= arr_name[0] + " " + arr_name[2] ).place(
        x=100, y=10)
    my_image_label = Label(image=my_image).place(x=100, y=40)
    button = tkinter.Button(root, text='Calculation Game', padx="108", bg="yellow",
                            command=lambda: calc_game(arr_name)).place(x=100, y=350)
    button = tkinter.Button(root, text='Color Game', padx="108", bg="purple",
                            command=lambda: color_game(arr_name)).place(x=100, y=400)
    button = tkinter.Button(root,text="QUIT", padx="108",bg="gray", command=quit).place(x=100, y=450)

def color_game(arr_name):
    clear_frame()
    root.minsize(width="1000", height="1000")
    welcome_label = Label(root, bg="white", text=" " + arr_name[0] + " " + arr_name[2]).place(x=100, y=10)
    my_image_label = Label(image=my_image).place(x=100, y=40)
    color_game_process(arr_name)


def color_game_process(arr_name):
    global color_entry
    color_list = load_colors()
    box_color = random.choice(color_list)
    canvas = Canvas(root, width=450, height=210, bg=str(box_color))
    canvas.place(x=400, y=40)
    name_label = Label(root, bg="white", text="Which color is this?").place(x=400, y=270)
    color_entry = Entry(root, bg="white", fg=box_color, width="40")
    color_entry.place(x=400, y=290)
    button = tkinter.Button(root, text='Check it', padx="100", bg="white",
                            command=lambda: color_control(box_color, arr_name)).place(x=400, y=350)
    button2 = tkinter.Button(root, text='Leave game', padx="100", bg="white",
                             command=lambda: game_starter(arr_name)).place(x=400, y=390)


def color_control(box_color, arr_name):
    random_color = color_entry.get()
    if random_color == box_color:
        name_label = Label(root, bg="white", text="Correct answer").place(x=400, y=320)
        color_game_process(arr_name)
    else:
        name_label = Label(root, bg="white", text="Wrong answer").place(x=400, y=320)


def load_colors():
    color_list = []
    for line in open(FILE_NAME):
        color_list.append(line.strip())
    return color_list


def calc_game(arr_name):
    clear_frame()
    root.minsize(width="1000", height="1000")
    welcome_label = Label(root, bg="white", text=" " + arr_name[0] + " " + arr_name[2]).place(x=100, y=10)
    my_image_label = Label(image=my_image).place(x=100, y=40)
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    words = ["addition","subtraction","multiplication"]
    movement = random.choice(words)
    num1_label = Label(root, bg="white", text=str(num1)).place(x=450, y=100)
    num2_label = Label(root, bg="white", text=str(num2)).place(x=450, y=150)
    name_label = Label(root, bg="white", text="Calculate " + movement + " of this numbers").place(x=450, y=200)
    num_entry = Entry(root, bg="white", fg="black", width="40")
    num_entry.place(x=450, y=250)

    button_minus = tkinter.Button(root, text='Check addition ', padx="50", bg="white",
                                  command=lambda: calc_pl(num1, num2, num_entry, arr_name)).place(x=700, y=100)
    button_minus = tkinter.Button(root, text='Check subtraction ', padx="50", bg="white",
                                  command=lambda: calc_min(num1, num2, num_entry, arr_name)).place(x=700, y=150)
    button_multiply = tkinter.Button(root, text='Check multiplication ', padx="50", bg="white",
                                     command=lambda: calc_mul(num1, num2, num_entry, arr_name)).place(x=700, y=200)
    button_divide = tkinter.Button(root, text='Check division ', padx="50", bg="white",
                                   command=lambda: calc_div(num1, num2, num_entry, arr_name)).place(x=700, y=250)
    button2 = tkinter.Button(root, text='Leave game', padx="50", bg="white",
                             command=lambda: game_starter(arr_name)).place(x=700, y=300)


def calc_pl(num1, num2, num_entry, arr_name):
    result = num1 + num2
    result_num = num_entry.get()
    print(result_num)
    print(result)
    if int(result_num) == int(result):
        name_label = Label(root, bg="white", text="Correct answer").place(x=400, y=350)
        button2 = tkinter.Button(root, text='New game', padx="100", bg="white",
                                 command=lambda: calc_game(arr_name)).place(x=400, y=370)
    else:
        name_label = Label(root, bg="white", text="Wrong answer").place(x=400, y=320)


def calc_min(num1, num2, num_entry, arr_name):
    result = num1 - num2
    result_num = num_entry.get()
    print(result_num)
    print(result)
    if int(result_num) == int(result):
        name_label = Label(root, bg="white", text="Correct answer").place(x=400, y=350)
        button2 = tkinter.Button(root, text='New game', padx="100", bg="white",
                                 command=lambda: calc_game(arr_name)).place(x=400, y=370)
    else:
        name_label = Label(root, bg="white", text="Wrong answer").place(x=400, y=320)


def calc_mul(num1, num2, num_entry, arr_name):
    result = num1 * num2
    result_num = num_entry.get()
    print(result_num)
    print(result)
    if int(result_num) == int(result):
        name_label = Label(root, bg="white", text="Correct answer").place(x=400, y=350)
        button2 = tkinter.Button(root, text='New game', padx="100", bg="white",
                                 command=lambda: calc_game(arr_name)).place(x=400, y=370)
    else:
        name_label = Label(root, bg="white", text="Wrong answer").place(x=400, y=320)


def calc_div(num1, num2, num_entry, arr_name):
    result = int(num1 / num2)
    result_num = num_entry.get()
    print(result_num)
    print(result)
    if int(result_num) == int(result):
        name_label = Label(root, bg="white", text="Correct answer").place(x=400, y=350)
        button2 = tkinter.Button(root, text='New game', padx="100", bg="white",
                                 command=lambda: calc_game(arr_name)).place(x=400, y=370)
    else:
        name_label = Label(root, bg="white", text="Wrong answer").place(x=400, y=320)


#

def clear_frame():
    # destroy all widgets from frame
    for widget in root.winfo_children():
        widget.destroy()


def image_upload_btn():
    button = tkinter.Button(root, text='Choose Image', padx="50", bg="white", command=upload_image).place(x=127, y=150)


def upload_image():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/FinalProject",
                                               title="Select file",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img_name_label = Label(root, bg="blue", fg="white", text=root.filename).place(x=127, y=180)

    my_image = ImageTk.PhotoImage(Image.open(root.filename))


if __name__ == '__main__':
    main()
