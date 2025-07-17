
import tkinter as tk
from tkinter import ttk


# main window light mode
class LightModeStyle(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system
        self.BACKGROUND_COLOR = "#2b2b2b"
        self.BODY_COLOR = "#b1b3b5"
        self.PRIMARY_COLOR = "#434345"
        self.SECONDARY_COLOR = "#ffffff"

        self.theme_use("clam")

        # custom style classes
        # general style classes
        self.configure("BodyFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.BODY_COLOR)

        self.configure("SectionFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.SECONDARY_COLOR)

        self.configure("FrameDescriptionLabel.TLabel",
                       font=("Arial", 14, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("DescriptionLabelSmaller.TLabel",
                       font=("Arial", 13, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("AppButton.TButton",
                       bordercolor=self.SECONDARY_COLOR,
                       borderwidth=0,
                       background=self.SECONDARY_COLOR)

        self.configure("Image.TLabel",
                       background=self.SECONDARY_COLOR)

        # specific style classes
        self.configure("DateTimeLabel.TLabel",
                       font=("Arial", 15, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareInfoHeading.TLabel",
                       font=("Arial", 13, "underline", "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareComponentInfo.TLabel",
                       font=("Arial", 13),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)


# main window dark mode
class DarkModeStyle(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system
        self.BACKGROUND_COLOR = "#2b2b2b"
        self.PRIMARY_COLOR = "#dddcde"
        self.SECONDARY_COLOR = "#434345"

        self.theme_use("clam")

        # custom style classes
        # general style classes
        self.configure("BodyFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.PRIMARY_COLOR)

        self.configure("SectionFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.SECONDARY_COLOR)

        self.configure("FrameDescriptionLabel.TLabel",
                       font=("Arial", 14, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("DescriptionLabelSmaller.TLabel",
                       font=("Arial", 13, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR,)

        self.configure("AppButton.TButton",
                       bordercolor=self.SECONDARY_COLOR,
                       borderwidth=0,
                       background=self.SECONDARY_COLOR)

        self.configure("Image.TLabel",
                       background=self.SECONDARY_COLOR)

        # specific style classes
        self.configure("DateTimeLabel.TLabel",
                       font=("Arial", 15, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareInfoHeading.TLabel",
                       font=("Arial", 13, "underline", "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareComponentInfo.TLabel",
                       font=("Arial", 13),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)
