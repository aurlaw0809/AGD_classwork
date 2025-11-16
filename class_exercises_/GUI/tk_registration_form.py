import tkinter as tk
from tkinter import ttk

from class_exercises_.GUI.tkinter_examples import MainFrame

class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Registration Form')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.top_frame = tk.Frame(self)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nw")

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.grid(row=1, column=0, sticky="nw")

        self.bottom_frame.right_frame = tk.Frame(self)
        self.bottom_frame.right_frame.grid(row=1, column=1, sticky="nw", padx=10, pady=5)
        self.bottom_frame.right_frame.columnconfigure(0, weight=1)

        self.bottom_frame.left_frame = tk.Frame(self)
        self.bottom_frame.left_frame.grid(row=1, column=0, sticky="nw", padx=10, pady=5)
        self.bottom_frame.left_frame.columnconfigure(0, weight=1)

        #create left side
        self.registration_frame_title = RegistrationFormFrameTitle(self.top_frame)
        self.submit_button_frame = SubmitBoxFrame(self)
        self.registration_frame = RegistrationFormFrame(self.bottom_frame.left_frame)

        #position left side
        self.registration_frame_title.grid(row=0, column=0, sticky='w')
        self.registration_frame.grid(row=0, column=0, sticky='nw')
        self.submit_button_frame.grid(row=2, column=0, sticky='w', padx=10, pady=10)

        #right side
        self.entry_box_frame = EntryBoxFrame(self.bottom_frame.right_frame)
        self.gender_choice_frame = GenderChoiceFrame(self.bottom_frame.right_frame)
        self.country_choice_frame = CountryChoiceFrame(self.bottom_frame.right_frame)
        self.programming_choice_frame = ProgramingChoiceFrame(self.bottom_frame.right_frame)

        #position right side
        self.entry_box_frame.grid(row=0, column=0, sticky="nw")
        self.gender_choice_frame.grid(row=1, column=0, sticky="nw")
        self.country_choice_frame.grid(row=2, column=0, sticky="nw")
        self.programming_choice_frame.grid(row=3, column=0, sticky="nw")


class RegistrationFormFrameTitle(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.title = tk.Label(self,
                              text="Registration Form",
                              justify="left",
                              anchor="w",
                              font=("Arial", 28))

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'we'}
        self.title.grid(row=0, column=0, **settings)
        self.columnconfigure(0, weight=1)

#registration left side labels
class RegistrationFormFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #labels
        self.name_label = tk.Label(self, text="Full name", justify="left", anchor="w")
        self.email_label = tk.Label(self, text="Email", justify="left", anchor="w")
        self.gender_label = tk.Label(self, text="Gender", justify="left", anchor="w")
        self.country_label = tk.Label(self, text="Country", justify="left", anchor="w")
        self.programming_label = tk.Label(self, text="Programming", justify="left", anchor="w")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky':"w"}

        self.name_label.grid(row=0,
                             column=0,
                             **settings)

        self.email_label.grid(row=1,
                              column=0,
                              **settings)

        self.gender_label.grid(row=2,
                               column=0,
                               **settings)

        self.country_label.grid(row=3,
                                column=0,
                                **settings)

        self.programming_label.grid(row=4,
                                    column=0,
                                    **settings)

#email and name entry buttons
class EntryBoxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)

        self.name = tk.Entry(self, width=40, justify="left")
        self.email = tk.Entry(self, width=40, justify="left")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 5, 'sticky': 'w'}

        self.name.grid(row=0,
                       column=0,
                       **settings)

        self.email.grid(row=1,
                        column=0,
                        **settings)

#gender choice buttons
class GenderChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)

        # Gender choices
        self.options = ['Male', 'Female']

        # Create a tk variable which will hold the value of the selected gender
        self.gender_choice = tk.StringVar()
        self.gender_choice.set(self.options[0])

        # Create radio buttons (list comprehension)
        self.gender_options = [tk.Radiobutton(self, text=gender,
                                             value=gender,
                                             variable=self.gender_choice,
                                             # command=self.change_color
                                             )
                              for gender in self.options]

        self.place_widgets()

    def place_widgets(self):
        for item in self.gender_options:
            item.pack(side=tk.LEFT, anchor='w', padx=10, pady=5)

#country choice button combobox
class CountryChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)

        self.current_country = tk.StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.current_country, state='readonly', width=37)

        self.combobox['values'] = ('United Kingdom', 'UK', 'England', 'Ireland', 'Northern Ireland', 'Wales',
                                           'Scotland', 'Britain')
        self.combobox.set('select your country')

        self.current_value = self.combobox.get()

        self.place_widgets()

    def place_widgets(self):
        self.combobox.grid(row=0, column=0, padx=10, pady=5, sticky='w')

#programming check box
class ProgramingChoiceFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1)

        self.java_check = ttk.Checkbutton(self, text="Java")

        self.python_check = ttk.Checkbutton(self, text="Python")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx':10, 'pady': 5, 'sticky': 'w'}
        self.java_check.grid(row=0, column=0, **settings)
        self.python_check.grid(row=0, column=1, **settings)

class SubmitBoxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # submit button
        self.submit = tk.Button(self,
                                text="Submit",
                                bg="gray67",
                                fg="gray1",
                                activebackground="red",
                                activeforeground="white"
                                )

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}

        self.submit.grid(row=0,
                         column=0,
                         **settings)

if __name__ == '__main__':

    registration_form = RegistrationForm()
    registration_form.geometry('500x500+100+100')
    registration_form.mainloop()