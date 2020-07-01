# def file_name_label():
#     a = upload_image()
#

# def profile_photo():
#     a = file_name_label()
#


# def card_maker():
#     x = 100
#     y = 50
#     for col in range(2):
#         arr = ["green", "blue","purple","orange"]
#         for row in range(4):
#             color = random.choice(arr)
#             rectangle = root.create_rectangle(x, y, x + CARD_SIDE, y + CARD_SIDE, fill=color, outline=color)
#             arr.remove(color)
#             x += 250
#         x = 100
#         y += 250
#
# def background_of_cards():
#     root.delete("all")
#     x = 100
#     y = 50
#     for col in range(2):
#         for row in range(5):
#             rectangle = canvas.create_rectangle(x, y, x + CARD_SIDE, y + CARD_SIDE, fill="white", outline="black")
#             x += 250
#         x = 100
#         y += 250
#


# def make_canvas(width, height, title=None):

# objects = {}
# top = tkinter.Tk()
# top.minsize(width=width, height=height)
# if title:
#     top.title(title)
# canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
# canvas.pack()
# canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
# canvas.yview_scroll(8, 'units')  # otherwise it's clipped off
#
# return canvas

# canvas: Canvas = make_canvas(1000, 1000, "Match - up")

# canvas.pack()
#
#
# card_maker(canvas)
# figure_maker(canvas)

# canvas.delete("all")
# filename = PIL.ImageTk.PhotoImage(PIL.Image.open("ball.jpg"))
# image = canvas.create_image(100, 100, image=filename)
# background_of_cards(canvas)
# button = tkinter.Button(canvas,
#                         text="QUIT",
#                         fg="red",
#                         command=quit)
# button.pack(side=tkinter.LEFT)
# slogan = Button(canvas, text="start game", command=background_of_cards(canvas))
# slogan.pack()
