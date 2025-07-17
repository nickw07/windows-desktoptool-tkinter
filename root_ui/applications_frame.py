
import tkinter as tk
from tkinter import ttk

from tkinter import filedialog, messagebox

import time
import pyautogui

from applications.app_calculator import Calculator
from applications.app_pwdgenerator import Pwdgenerator


class ApplicationsFrame(ttk.Frame):
    def __init__(self, container, parent_window, **kwargs):
        super().__init__(container, **kwargs)

        # root reference
        self.parent_window = parent_window

        # frame functionality - Open Calculator/Password generator/Screenshot
        # 1
        self.calculator_app_icon = tk.PhotoImage(file=r"graphics/applications-frame/calculator-64x64px.png")
        calculator_app_button = ttk.Button(self,
                                           image=self.calculator_app_icon,
                                           command=self.start_calculator,
                                           style="AppButton.TButton")
        calculator_app_button.place(x=20, y=20)

        calculator_app_label = ttk.Label(self,
                                         text="Calculator",
                                         style="FrameDescriptionLabel.TLabel")
        calculator_app_label.place(x=105, y=50)

        # 2
        self.password_generator_app_icon = tk.PhotoImage(file=r"graphics/applications-frame/pwdgenerator-64x64px.png")
        password_generator_app_button = ttk.Button(self,
                                                   image=self.password_generator_app_icon,
                                                   command=self.start_password_generator,
                                                   style="AppButton.TButton")
        password_generator_app_button.place(x=285, y=20)

        password_generator_app_label = ttk.Label(self,
                                                 text="Key Generator",
                                                 style="FrameDescriptionLabel.TLabel")
        password_generator_app_label.place(x=370, y=50)

        # 3
        self.take_screenshot_app_icon = tk.PhotoImage(file=r"graphics/applications-frame/screenshot-64x64px.png")
        take_screenshot_app_button = ttk.Button(self,
                                                image=self.take_screenshot_app_icon,
                                                command=self.take_screenshot,
                                                style="AppButton.TButton")
        take_screenshot_app_button.place(x=600, y=20)

        take_screenshot_app_label = ttk.Label(self,
                                              text="Screenshot",
                                              style="FrameDescriptionLabel.TLabel")
        take_screenshot_app_label.place(x=685, y=50)

    def start_calculator(self):
        # toplevel window
        calculator = Calculator(self.parent_window)
        calculator.grab_set()

    def start_password_generator(self):
        # toplevel window
        password_generator = Pwdgenerator(self.parent_window)
        password_generator.grab_set()

    def take_screenshot(self):
        self.parent_window.iconify()
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        self.parent_window.deiconify()

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if file_path:
            screenshot.save(file_path)
            messagebox.showinfo("Screenshot was taken!", f"Screenshot saved in {file_path}.")
        else:
            messagebox.showerror("Screenshot was not taken!", message="Screenshot not saved.")