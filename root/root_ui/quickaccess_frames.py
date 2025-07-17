
import tkinter as tk
from tkinter import ttk

import subprocess


class QuickAccessFirst(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        frame_description_label = ttk.Label(self,
                                            text="Quick Access (1)",
                                            style="FrameDescriptionLabel.TLabel")
        frame_description_label.place(x=25, y=12)

        # switch button
        self.switch_frame_button_icon = tk.PhotoImage(file=r"../graphics/quickaccess-frames/down-32x32px.png")
        switch_frame_button = ttk.Button(self,
                                         image=self.switch_frame_button_icon,
                                         command=lambda: controller.change_window(QuickAccessSecond),
                                         style="AppButton.TButton")
        switch_frame_button.place(x=155, y=300)

        # frame functionality - Opening Task Manager/Settings/Explorer
        # 1
        self.open_task_manager_button_icon = tk.PhotoImage(file=r"../graphics/quickaccess-frames/taskmanager-64x64px.png")
        open_task_manager_button = ttk.Button(self,
                                              image=self.open_task_manager_button_icon,
                                              command=self.open_task_manager,
                                              style="AppButton.TButton")
        open_task_manager_button.place(x=15, y=50)

        open_task_manager_label = ttk.Label(self,
                                            text="System",
                                            style="DescriptionLabelSmaller.TLabel")
        open_task_manager_label.place(x=100, y=80)

        # 2
        self.open_settings_button_icon = tk.PhotoImage(file=r"../graphics/quickaccess-frames/settings-64x64px.png")
        open_settings_button = ttk.Button(self,
                                          image=self.open_settings_button_icon,
                                          command=self.open_settings,
                                          style="AppButton.TButton")
        open_settings_button.place(x=15, y=135)

        open_settings_label = ttk.Label(self,
                                        text="Settings",
                                        style="DescriptionLabelSmaller.TLabel")
        open_settings_label.place(x=100, y=165)

        # 3
        self.open_explorer_button_icon = tk.PhotoImage(file=r"../graphics/quickaccess-frames/explorer-64x64px.png")
        open_explorer_button = ttk.Button(self,
                                          image=self.open_explorer_button_icon,
                                          command=self.open_explorer,
                                          style="AppButton.TButton")
        open_explorer_button.place(x=15, y=220)

        open_explorer_label = ttk.Label(self,
                                        text="Explorer",
                                        style="DescriptionLabelSmaller.TLabel")
        open_explorer_label.place(x=100, y=250)

    @staticmethod
    def open_task_manager():
        command = "taskmgr.exe"

        try:
            subprocess.call([command], shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")

    @staticmethod
    def open_settings():
        command = "start ms-settings:"

        try:
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")

    @staticmethod
    def open_explorer():
        explorer_path = "explorer.exe"
        command = f"start {explorer_path}"

        try:
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")


class QuickAccessSecond(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        frame_description_label = ttk.Label(self,
                                            text="Quick Access (2)",
                                            style="FrameDescriptionLabel.TLabel")
        frame_description_label.place(x=25, y=12)

        # switch button
        self.switch_frame_button_icon = tk.PhotoImage(file=r"../graphics/quickaccess-frames/up-32x32px.png")
        switch_frame_button = ttk.Button(self,
                                         image=self.switch_frame_button_icon,
                                         command=lambda: controller.change_window(QuickAccessFirst),
                                         style="AppButton.TButton")
        switch_frame_button.place(x=155, y=300)

        # frame functionality - Opening Notepad
        self.open_notepad_button_icon = tk.PhotoImage(file=r"../graphics/quickaccess-frames/notepad-64x64px.png")
        open_notepad_button = ttk.Button(self,
                                         image=self.open_notepad_button_icon,
                                         command=self.open_notepad,
                                         style="AppButton.TButton")
        open_notepad_button.place(x=15, y=50)

        open_notepad_label = ttk.Label(self,
                                       text="Notepad",
                                       style="DescriptionLabelSmaller.TLabel")
        open_notepad_label.place(x=100, y=80)

    @staticmethod
    def open_notepad():
        notepad_path = "notepad.exe"
        command = f"start {notepad_path}"

        try:
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")
