
import tkinter as tk
from tkinter import ttk

import random
import string

import pyperclip

from applications.app_styles import PwdgenLightModeStyle, PwdgenDarkModeStyle

from root.theme_manager import ThemeManager


class Pwdgenerator(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # GUI placement and setup
        self.root_x = parent.winfo_x()
        self.root_y = parent.winfo_y()

        self.geometry(f"+{self.root_x}+{self.root_y}")
        self.resizable(False, False)

        self.title("Random password generator")
        self.iconbitmap(r"../graphics/window-icon-32x32px.ico")

        # start in correct mode
        if ThemeManager.is_dark_mode():
            self.style = PwdgenDarkModeStyle()
            self.configure(background=self.style.BACKGROUND_COLOR)
        else:
            self.style = PwdgenLightModeStyle()
            self.configure(background=self.style.BACKGROUND_COLOR)

        # GUI separation by frames
        input_info_label = ttk.Label(self,
                                     text="Create a random password",
                                     style="InfoLabelRPG.TLabel")
        input_info_label.grid(row=0, column=0, padx=10, pady=10)

        input_frame = InputFrame(self,
                                 style="BodyFrameRPG.TFrame")
        input_frame.grid(row=1, column=0)

        divider = ttk.Separator(self,
                                style="SeparatorRPG.TSeparator")
        divider.grid(row=2, column=0, sticky=tk.EW, pady=5)

        output_info_label = ttk.Label(self,
                                      text="Your random password is:",
                                      style="InfoLabelRPG.TLabel")
        output_info_label.grid(row=3, column=0, padx=5, pady=10)

        output_frame = OutputFrame(self,
                                   input_frame.password_var,
                                   input_frame.ERROR,
                                   style="BodyFrameRPG.TFrame")
        output_frame.grid(row=4, column=0)


class InputFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        # creation parameters
        self.length_var = tk.IntVar(value=8)

        self.using_lowercase = tk.BooleanVar()
        self.using_uppercase = tk.BooleanVar()
        self.using_digits = tk.BooleanVar()
        self.using_punctuation = tk.BooleanVar()

        self.password_var = tk.StringVar()

        # symbol access
        self.LOWERCASE_LETTERS = string.ascii_lowercase
        self.UPPERCASE_LETTERS = string.ascii_uppercase
        self.DIGITS = string.digits
        self.PUNCTUATION = string.punctuation

        self.ERROR = "Select characters"

        # pwd specification - length/characters
        # 1
        length_label = ttk.Label(self,
                                 text="Length:",
                                 style="SpecificationInfoLabelRPG.TLabel")
        length_label.grid(row=0, column=0, sticky=tk.W, padx=12, pady=10)

        length_scale = ttk.Scale(self,
                                 length=100,
                                 from_=8,
                                 to=75,
                                 variable=self.length_var,
                                 command=self.update_value)
        length_scale.grid(row=0, column=1, sticky=tk.EW, columnspan=3, padx=12, pady=10)

        display_length_label = ttk.Label(self,
                                         textvariable=self.length_var,
                                         style="SpecificationInfoLabelRPG.TLabel")
        display_length_label.grid(row=0, column=4)

        # 2
        include_info_label = ttk.Label(self,
                                       text="Include:",
                                       style="SpecificationInfoLabelRPG.TLabel")
        include_info_label.grid(row=1, column=0, padx=12, pady=10)

        uppercase_letters_checkbutton = ttk.Checkbutton(self,
                                                        text="ABC",
                                                        variable=self.using_uppercase,
                                                        style="OptionCheckbuttonRPG.TCheckbutton")
        uppercase_letters_checkbutton.grid(row=1, column=1, padx=10)

        lowercase_letters_checkbutton = ttk.Checkbutton(self,
                                                        text="abc",
                                                        variable=self.using_lowercase,
                                                        style="OptionCheckbuttonRPG.TCheckbutton")
        lowercase_letters_checkbutton.grid(row=1, column=2, padx=10)

        digits_checkbutton = ttk.Checkbutton(self,
                                             text="123",
                                             variable=self.using_digits,
                                             style="OptionCheckbuttonRPG.TCheckbutton")
        digits_checkbutton.grid(row=1, column=3, padx=10)

        punctuation_checkbutton = ttk.Checkbutton(self,
                                                  text="#!'",
                                                  variable=self.using_punctuation,
                                                  style="OptionCheckbuttonRPG.TCheckbutton")
        punctuation_checkbutton.grid(row=1, column=4, padx=10)

        generate_pwd_button = ttk.Button(self,
                                         text="Generate password",
                                         command=self.generate_password,
                                         style="PerformActionButtonRPG.TButton")
        generate_pwd_button.grid(row=2, column=0, sticky=tk.EW, columnspan=5, padx=12, pady=10)

    def update_value(self, value):
        # even numbers on scale
        self.length_var.set(int(float(value)))

    def generate_password(self):
        characters = ""

        pwd_length = self.length_var.get()
        lowercase = self.using_lowercase.get()
        uppercase = self.using_uppercase.get()
        digits = self.using_digits.get()
        punctuation = self.using_punctuation.get()

        if lowercase:
            characters += self.LOWERCASE_LETTERS
        if uppercase:
            characters += self.UPPERCASE_LETTERS
        if digits:
            characters += self.DIGITS
        if punctuation:
            characters += self.PUNCTUATION

        if not characters:
            self.password_var.set(f"{self.ERROR}")
            return None
        else:
            # password creation
            password = "".join(random.choices(characters, k=pwd_length))
            self.password_var.set(password)


class OutputFrame(ttk.Frame):
    def __init__(self, container: tk.Toplevel, password_var: tk.StringVar, error: str, **kwargs):
        super().__init__(container, **kwargs)

        # value transfer
        self.password_var = password_var

        self.ERROR = error

        # displaying result
        self.result_entry = ttk.Entry(self,
                                      font=("Arial", 13),
                                      state="readonly",
                                      textvariable=self.password_var,
                                      width=41,
                                      style="ResultEntryRPG.TEntry")
        self.result_entry.grid(row=0, column=0, sticky=tk.EW, padx=12)

        self.result_entry_scrollbar = ttk.Scrollbar(self,
                                                    orient=tk.HORIZONTAL,
                                                    command=self.result_entry.xview)
        self.result_entry_scrollbar.grid(row=1, column=0, sticky=tk.EW, padx=12, pady=7)
        self.result_entry.configure(xscrollcommand=self.result_entry_scrollbar.set)

        copy_result_button = ttk.Button(self,
                                        text="Copy result!",
                                        command=self.copy_password,
                                        style="PerformActionButtonRPG.TButton")
        copy_result_button.grid(row=2, column=0, sticky=tk.EW, padx=12, pady=10)

    def copy_password(self):
        if self.password_var.get() != self.ERROR:
            password = self.password_var.get()
            pyperclip.copy(password)
