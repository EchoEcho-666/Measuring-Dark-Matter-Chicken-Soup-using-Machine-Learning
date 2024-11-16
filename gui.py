import time
import threading
import customtkinter as ctk

from customtkinter import filedialog

from PIL import Image

 

ctk.set_appearance_mode("Light")        
 

ctk.set_default_color_theme("green")


#Customize
mainFont = ("Montserrat", 24)

windowText = "placeholder"

mainTitleText = "title"

 

class program(ctk.CTk):
    
    def __init__(self, *args, **kwargs):
 
        
        super().__init__(*args, **kwargs)

        self.title(windowText)

        self.geometry("1400x1000")

        self.label = ctk.CTkLabel(self, text=mainTitleText, font=mainFont)
        self.label.place(relx=0.5, rely=0.05, anchor="center")

        self.ready = ctk.CTkLabel(self, text="", font=mainFont)
        self.ready.place(relx=0.5, rely=0.8, anchor="center")





        self.pic1 = ctk.CTkLabel(self, text="", font=mainFont)
        self.pic1.place(relx=0.2, rely=0.7, anchor="center")

        self.pic2 = ctk.CTkLabel(self, text="", font=mainFont)
        self.pic2.place(relx=0.8, rely=0.7, anchor="center")

        


        def generate():
            if self.ready.cget('text') == "Ready":

                result = ctk.CTkToplevel(self)

                result.title("Result")

                result.test = ctk.CTkLabel(result, text="a", font=mainFont)
                result.test.place(relx=0.5, rely=0.5, anchor="center")
        

        self.button = ctk.CTkButton(self, text="Generate Result", font=mainFont, command=lambda : generate())
        self.button.place(relx=0.5, rely=0.9, anchor="center")

        





        self.selectText1 = ctk.CTkLabel(self, text="No file selected", font=mainFont)
        self.selectText1.place(relx=0.2, rely=0.3, anchor="w")

        self.selectText2 = ctk.CTkLabel(self, text="No file selected", font=mainFont)
        self.selectText2.place(relx=0.2, rely=0.4, anchor="w")



        self.selectButton1 = ctk.CTkButton(self, text="Select file", font=mainFont, command=lambda : select_file(self.selectText1))
        self.selectButton1.place(relx=0.1, rely=0.3, anchor="center")

        self.selectButton2 = ctk.CTkButton(self, text="Select file", font=mainFont, command=lambda : select_file(self.selectText2))
        self.selectButton2.place(relx=0.1, rely=0.4, anchor="center")


        def select_file(thing):

            filetypes = [("Pictures", ".png .jpg .jpeg")
                         ]
            
            file = filedialog.askopenfilename(filetypes=filetypes)
        

            if file != "":

                thing.configure(text=file)

                if thing == self.selectText1:
                    img = ctk.CTkImage(light_image=Image.open(file), size=(400,400))


                    self.pic1.configure(image=img)
                else:
                    img = ctk.CTkImage(light_image=Image.open(file), size=(400,400))


                    self.pic2.configure(image=img)
                
            else:
                thing.configure(text="No file selected")




            if self.selectText1.cget('text') != "No file selected" and self.selectText2.cget('text') != "No file selected":
    

                self.ready.configure(text="Ready")

            else:
                
                self.ready.configure(text="")




 
 
if __name__ == "__main__":

    
    program().mainloop()  
