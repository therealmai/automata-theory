#Jomar Leano BSCS-3
import tkinter as tk
from tkinter import messagebox

class MyGUI:
    
    def __init__(self):
        
        self.root = tk.Tk()
        
        # Set the size of the app
        app_width = 800
        app_height = 600
        
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        #Exercise 3
        self.textboxFrame2 = tk.Frame(self.root)
        
        self.label = tk.Label(self.root, text="Exercise 3", font=('Arial', 18), anchor='w', justify="left")
        self.label.pack(padx=20, pady=20)
        
        self.label1 = tk.Label(self.root, text="Write a program that accepts the language L = { anbncn / n ≥ 0 }: the program yields the result ‘Y’ if the argument string w Є { a,b,c } is in L, and ‘N’ if it is not. For example, input “aabbcc” yields output “YES”, since aabbcc Є L, and input “bbaaccc” yields output “NO”, since bbaaccc Є L.", font=('Arial', 14), anchor='w', justify="left", wraplength=700)
        self.label1.pack(padx=20, anchor="w")
        
        self.textboxFrame1 = tk.Frame(self.root)
        self.textboxFrame1.columnconfigure(0, weight=1)
        self.textboxFrame1.columnconfigure(1, weight=1)
        self.textboxFrame1.columnconfigure(2, weight=1)
        self.textboxFrame1.columnconfigure(3, weight=1)
        self.textboxFrame1.rowconfigure(0, weight=1)
        self.textboxFrame1.rowconfigure(1, weight=1)
        
        self.textbox2 = tk.Text(self.textboxFrame1, height=3, font=("Arial", 16))
        self.textbox2.grid(row = 0, columnspan=2, sticky = tk.W+tk.E)
        
        # button 1
        self.button = tk.Button(self.textboxFrame1, text="Enter", font=("Arial",12), command=self.check_L)
        self.button.grid(row=1,column=0)
        
        #button 2
        self.button = tk.Button(self.textboxFrame1, text="Clear", font=("Arial",12), command=self.clearWords1)
        self.button.grid(row=1,column=1)
        
        
        self.textboxFrame1.pack(padx=20)
        
        # Calculate the x and y coordinates of the top-left corner of the app
        x = (screen_width // 2) - (app_width // 2)
        y = (screen_height // 2) - (app_height // 2)
        
        # Set the position of the app
        self.root.geometry(f"{app_width}x{app_height}+{x}+{y}")
        self.root.title("Automata Exercise")
        
        self.root.mainloop()
    
    def check_L(self):
        stringInput = self.textbox2.get('1.0', tk.END)
        print(stringInput)
        if stringInput =="\n":
            messagebox.showinfo(title="Error", message="No text inputted")
        else:
            a_count = 0
            b_count = 0
            c_count = 0
            for i in range(len(stringInput)):
                if stringInput[i] == 'a':
                    a_count += 1
                elif stringInput[i] == 'b':
                    b_count += 1
                elif stringInput[i] == 'c':
                    c_count += 1
            print(a_count)
            print(b_count)
            print(c_count)
            
            if a_count == b_count and b_count == c_count:
                messagebox.showinfo(title="Error", message="Yes")
                return 'YES'
            else:
                messagebox.showinfo(title="Error", message="No")
                return 'NO'
             
    
    def clearWords1(self):
        self.textbox2.delete('1.0', tk.END)
        
MyGUI()