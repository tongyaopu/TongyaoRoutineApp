from typing import Optional, Tuple, Union
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
# myfont = ctk.CTkFont("UbuntuMono Nerd Font", size=20)
myfont = ("UbuntuMono Nerd Font", 24)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # configure window
        self.title("Tongyao Task")
        self.geometry("600x380")
 
         # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0) 
        self.grid_columnconfigure(1, weight=1) 
        self.grid_columnconfigure(2, weight=0)  
        self.grid_columnconfigure(3, weight=1) # second column today task
        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=0) # second column today task
        
        # session - yesterday's tasks
        self.yesterday = ctk.CTkFrame(self, width=100, corner_radius=0)
        self.yesterday.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.yesterday.grid_rowconfigure(6, weight=1)
        self.labelT1 = ctk.CTkLabel(self.yesterday, text="How did yesterday go?")
        self.labelT1.grid(row=0, column=0, padx=10, pady=20)
        self.checkbox1 = ctk.CTkCheckBox(self.yesterday, text="yesterday task1")
        self.checkbox2 = ctk.CTkCheckBox(self.yesterday, text="yesterday task2")
        self.checkbox3 = ctk.CTkCheckBox(self.yesterday, text="yesterday task3")
        self.checkbox1.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.checkbox2.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.checkbox3.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.labelN1 = ctk.CTkLabel(self.yesterday, text="Notes:")
        self.labelN1.grid(row=5, column=0, padx=20, pady=(10,0), sticky="sw")
        self.textN1 = ctk.CTkTextbox(self.yesterday, height=50) 
        self.textN1.grid(row=6, column=0, padx=20, pady=(0, 10), sticky="w") 
        # button
        # self.todaybutton = ctk.CTkButton(self.yesterday, text="Set goals!")
        # self.todaybutton.grid(row=6, column=0, padx=20, pady=10, sticky="e")

        # session - today's tasks
        # session title
        self.labelT = ctk.CTkLabel(self, text="Good Morning!\nWhat do you want to do today?")
        self.labelT.grid(row=0, column=2, pady=20)
        # labels
        self.label1 = ctk.CTkLabel(self, text="1. ")
        self.label1.grid(row=1, column=1, pady=10, sticky="e")
        self.label2 = ctk.CTkLabel(self, text="2. ")
        self.label2.grid(row=2, column=1, pady=10, sticky="e")
        self.label3 = ctk.CTkLabel(self, text="3. ")
        self.label3.grid(row=3, column=1, pady=10, sticky="e")
        self.labelN = ctk.CTkLabel(self, text="Notes")
        self.labelN.grid(row=4, column=1, pady=10, sticky="e")
        # textboxes
        self.entry1 = ctk.CTkEntry(self, placeholder_text="task 1")
        self.entry1.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.entry2 = ctk.CTkEntry(self, placeholder_text="task 2")
        self.entry2.grid(row=2, column=2, padx=10, pady=10, sticky="nsew") 
        self.entry3 = ctk.CTkEntry(self, placeholder_text="task 2")
        self.entry3.grid(row=3, column=2, padx=10, pady=10, sticky="nsew") 
        self.textN = ctk.CTkTextbox(self, height=50) 
        self.textN.grid(row=4, column=2, padx=10, pady=10, sticky="nsew") 
        # button
        self.todaybutton = ctk.CTkButton(self, text="Set goals!")
        self.todaybutton.grid(row=5, column=2, padx=0, pady=20, sticky="e")
# greetings = ctk.CTkLabel(
#     master=root, 
#     text="Good Morning!\nWhat do you want to do today?", 
#     font=myfont)
# greetings.pack()

# label_tsk1 = ctk.CTkLabel(
#     master=root,
#     text="1. ",
#     font=myfont
# )
# root.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()