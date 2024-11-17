import customtkinter as ctk
from PIL import Image, ImageTk

root = ctk.CTk()
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

mainFont = ("Montserrat", 24)
windowText = "Galaxy X, Y, and Z"
root.title(windowText)
root.geometry("1000x1000")

def load_gif(path):
    gif = Image.open(path)
    frames = []
    for _ in range(gif.n_frames):
        frames.append(ImageTk.PhotoImage(gif.copy().convert("RGBA")))
        gif.seek(_)  
    return frames

frames1 = load_gif("/Users/victor/Downloads/fwgifforgalaxy/fixed_x_animation.gif")
frames2 = load_gif("/Users/victor/Downloads/fwgifforgalaxy/fixed_y_animation.gif")
frames3 = load_gif("/Users/victor/Downloads/fwgifforgalaxy/fixed_z_animation.gif")

pic1 = ctk.CTkLabel(root, text="", font=mainFont)
pic1.place(relx=0.5, rely=0.5, anchor="center")

pic2 = ctk.CTkLabel(root, text="", font=mainFont)
pic2.place(relx=1.5, rely=0.5, anchor="center")

pic3 = ctk.CTkLabel(root, text="", font=mainFont)
pic3.place(relx=2.5, rely=0.5, anchor="center")

x = 0.5
stage = 1
frame_index1 = 0
frame_index2 = 0
frame_index3 = 0

def update_gif_labels():
    global frame_index1, frame_index2, frame_index3
    pic1.configure(image=frames1[frame_index1])
    pic2.configure(image=frames2[frame_index2])
    pic3.configure(image=frames3[frame_index3])
    frame_index1 = (frame_index1 + 1) % len(frames1)
    frame_index2 = (frame_index2 + 1) % len(frames2)
    frame_index3 = (frame_index3 + 1) % len(frames3)
    root.after(100, update_gif_labels)

def slide():
    global frame_index1, frame_index2, frame_index3

    global x, stage
    print(x)

    if stage == 1:
        if x >= -0.49:
            x -= 0.05
            pic1.place(relx=x)
            pic2.place(relx=x + 1)
            pic3.place(relx=x + 2)
            root.after(20, slide)
        else:
            stage = 2
            
    elif stage == 2:
        if x >= -1.49:
            x -= 0.05
            pic1.place(relx=x)
            pic2.place(relx=x + 1)
            pic3.place(relx=x + 2)
            root.after(20, slide)
        else:
            stage = 3

    frame_index1 = 0
    frame_index2 = 0
    frame_index3 = 0

def slideRight():
    global x, stage
    global frame_index1, frame_index2, frame_index3

    print(x)
    if stage == 3:
        if x <= -0.5:
            x += 0.05
            pic1.place(relx=x)
            pic2.place(relx=x + 1)
            pic3.place(relx=x + 2)
            root.after(20, slideRight)
        else:
            stage = 2
    elif stage == 2:
        if x <= 0.5:
            x += 0.05
            pic1.place(relx=x)
            pic2.place(relx=x + 1)
            pic3.place(relx=x + 2)
            root.after(20, slideRight)
        else:
            stage = 1

    frame_index1 = 0
    frame_index2 = 0
    frame_index3 = 0

update_gif_labels()

back = ctk.CTkButton(root, text="<", font=mainFont, command=slide)
forward = ctk.CTkButton(root, text=">", font=mainFont, command=slideRight)

back.place(relx=0.4, rely=0.9, anchor="center")
forward.place(relx=0.6, rely=0.9, anchor="center")


                

root.mainloop()
