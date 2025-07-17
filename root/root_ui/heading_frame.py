
import tkinter as tk
from tkinter import ttk

import datetime

import subprocess

from root.theme_manager import ThemeManager

from root.main_styles import LightModeStyle, DarkModeStyle


class HeadingFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.date_var = tk.StringVar(value="date")
        self.time_var = tk.StringVar(value="time")

        self.button_mode = True

        # displaying date and time
        date_label = ttk.Label(self,
                               textvariable=self.date_var,
                               style="DateTimeLabel.TLabel")
        date_label.place(x=10, y=10)

        time_label = ttk.Label(self,
                               textvariable=self.time_var,
                               style="DateTimeLabel.TLabel")
        time_label.place(x=390, y=10)

        # additional functionalities
        self.switch_mode_button_icon = tk.PhotoImage(file=r"../graphics/heading-frame/switch-32x32px.png")
        switch_mode_button = ttk.Button(self,
                                        image=self.switch_mode_button_icon,
                                        command=self.switch_mode,
                                        style="AppButton.TButton")
        switch_mode_button.place(x=700, y=3)

        self.lock_screen_button_icon = tk.PhotoImage(file=r"../graphics/heading-frame/lock-32x32px.png")
        lock_screen_button = ttk.Button(self,
                                        image=self.lock_screen_button_icon,
                                        command=self.lock_screen,
                                        style="AppButton.TButton")
        lock_screen_button.place(x=745, y=3)

        self.close_app_button_icon = tk.PhotoImage(file=r"../graphics/heading-frame/close-32x32px.png")
        close_app_button = ttk.Button(self,
                                      image=self.close_app_button_icon,
                                      command=self.close_app,
                                      style="AppButton.TButton")
        close_app_button.place(x=790, y=3)

    def show_time(self):
        # get current date and time
        date_current = datetime.date.today()
        date_string = date_current.strftime("%B %d, %Y")
        self.date_var.set(date_string)

        time_current = datetime.datetime.now()
        time_string = time_current.strftime("%H:%M")  # :%S if seconds are required
        self.time_var.set(time_string)

        self.after(1000, self.show_time)

    def switch_mode(self):
        # switching between dark & light mode

        ThemeManager.switch_mode()

        if ThemeManager.is_dark_mode():
            DarkModeStyle()
        else:
            LightModeStyle()

    @staticmethod
    def lock_screen():
        try:
            # bring user to lock screen -> re-enter password
            subprocess.run("rundll32.exe user32.dll,LockWorkStation")
        except Exception as E:
            print(f"{E} - Work Station could not be closed")

    def close_app(self):
        # destroy root window
        self.winfo_toplevel().destroy()
