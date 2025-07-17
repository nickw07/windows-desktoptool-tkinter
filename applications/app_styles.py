
from tkinter import ttk


# calculator toplevel window light mode
class CalculatorLightModeStyle(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system
        self.BACKGROUND_COLOR = "#dddcde"
        self.PRIMARY_COLOR = "#4a4949"
        self.SECONDARY_COLOR = "#66696e"
        self.TERTIARY_COLOR = "#989b9e"
        self.ACCENT_COLOR = "#4361ee"
        self.new = "#5d6573"

        self.theme_use("clam")

        # custom style classes
        self.configure("BodyFrameCalc.TFrame",
                       background=self.BACKGROUND_COLOR)

        self.configure("EquationDisplayEntryCalc.TEntry",
                       bordercolor=self.TERTIARY_COLOR,
                       lightcolor=self.PRIMARY_COLOR,
                       darkcolor=self.PRIMARY_COLOR,
                       borderwitdh=1,
                       focusthickness=0,
                       foreground=self.BACKGROUND_COLOR,
                       background=self.BACKGROUND_COLOR,
                       fieldbackground=self.SECONDARY_COLOR)
        self.map("EquationDisplayEntryCalc.TEntry",
                 bordercolor=[("focus", self.PRIMARY_COLOR)],
                 lightcolor=[("focus", self.PRIMARY_COLOR)],
                 darkcolor=[("focus", self.PRIMARY_COLOR)])

        # number buttons
        self.configure("BaseOptionButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.BACKGROUND_COLOR,
                       width=7,
                       background=self.TERTIARY_COLOR)
        self.map("BaseOptionButtonCalc.TButton",
                 foreground=[("active", self.SECONDARY_COLOR)])

        # operation buttons (+-*/)
        self.configure("OperationButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.BACKGROUND_COLOR,
                       width=7,
                       background=self.SECONDARY_COLOR)
        self.map("OperationButtonCalc.TButton",
                 foreground=[("active", self.SECONDARY_COLOR)])

        # equals button and scrollbar
        self.configure("EqualsButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.BACKGROUND_COLOR,
                       width=7,
                       background=self.ACCENT_COLOR)
        self.map("EqualsButtonCalc.TButton",
                 foreground=[("active", self.PRIMARY_COLOR)])

        self.configure("TScrollbar",
                       bordercolor=self.SECONDARY_COLOR,
                       lightcolor=self.SECONDARY_COLOR,
                       darkcolor=self.SECONDARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       troughcolor=self.SECONDARY_COLOR,
                       arrowcolor=self.SECONDARY_COLOR)
        self.map("TScrollbar",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.TERTIARY_COLOR), ("!active", self.TERTIARY_COLOR)],
                 slider=[("active", self.TERTIARY_COLOR), ("!active", self.TERTIARY_COLOR)])


# calculator toplevel window dark mode
class CalculatorDarkModeStyle(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system
        self.BACKGROUND_COLOR = "#2b2b2b"
        self.PRIMARY_COLOR = "#dddcde"
        self.SECONDARY_COLOR = "#434345"
        self.TERTIARY_COLOR = "#6d6d6e"
        self.ACCENT_COLOR = "#6e48e0"

        self.theme_use("clam")

        # custom style classes
        self.configure("BodyFrameCalc.TFrame",
                       background=self.BACKGROUND_COLOR)

        self.configure("EquationDisplayEntryCalc.TEntry",
                       bordercolor=self.PRIMARY_COLOR,
                       lightcolor=self.PRIMARY_COLOR,
                       darkcolor=self.PRIMARY_COLOR,
                       borderwitdh=1,
                       focusthickness=0,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       fieldbackground=self.SECONDARY_COLOR)
        self.map("EquationDisplayEntryCalc.TEntry",
                 bordercolor=[("focus", self.PRIMARY_COLOR)],
                 lightcolor=[("focus", self.PRIMARY_COLOR)],
                 darkcolor=[("focus", self.PRIMARY_COLOR)])

        # number buttons
        self.configure("BaseOptionButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       width=7,
                       background=self.TERTIARY_COLOR)
        self.map("BaseOptionButtonCalc.TButton",
                 foreground=[("active", self.BACKGROUND_COLOR)])

        # operation buttons (+-*/)
        self.configure("OperationButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       width=7,
                       background=self.SECONDARY_COLOR)
        self.map("OperationButtonCalc.TButton",
                 foreground=[("active", self.BACKGROUND_COLOR)])

        # equals button and scrollbar
        self.configure("EqualsButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       width=7,
                       background=self.ACCENT_COLOR)
        self.map("EqualsButtonCalc.TButton",
                 foreground=[("active", self.BACKGROUND_COLOR)])

        self.configure("TScrollbar",
                       bordercolor=self.TERTIARY_COLOR,
                       lightcolor=self.TERTIARY_COLOR,
                       darkcolor=self.TERTIARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       troughcolor=self.PRIMARY_COLOR,
                       arrowcolor=self.PRIMARY_COLOR)
        self.map("TScrollbar",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])


# password generator toplevel window light mode
class PwdgenLightModeStyle(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system
        self.BACKGROUND_COLOR = "#dddcde"
        self.PRIMARY_COLOR = "#434345"
        self.SECONDARY_COLOR = "#ffffff"
        self.ACCENT_COLOR = "#4361ee"

        self.theme_use("clam")

        # custom style classes
        self.configure("BodyFrameRPG.TFrame",
                       background=self.BACKGROUND_COLOR)

        self.configure("InfoLabelRPG.TLabel",
                       font=("Arial", 16, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)

        self.configure("SpecificationInfoLabelRPG.TLabel",
                       font=("Arial", 14),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)

        self.configure("OptionCheckbuttonRPG.TCheckbutton",
                       focusthickness=5,
                       font=("Arial", 12),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)
        self.map("OptionCheckbuttonRPG.TCheckbutton",
                 foreground=[("active", self.PRIMARY_COLOR)],
                 background=[("active", self.SECONDARY_COLOR)],
                 indicatorbackground=[("selected", self.ACCENT_COLOR), ("!selected", self.PRIMARY_COLOR)],
                 indicatorcolor=[("selected", self.ACCENT_COLOR), ("!selected", self.PRIMARY_COLOR)])

        self.configure("PerformActionButtonRPG.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       font=("Arial", 14),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)
        self.map("PerformActionButtonRPG.TButton",
                 foreground=[("active", self.PRIMARY_COLOR)],
                 background=[("active", "#c9c9c9")])  # slightly darker color SECONDARY_COLOR

        self.configure("SeparatorRPG.TSeparator",
                       background=self.PRIMARY_COLOR)

        self.configure("ResultEntryRPG.TEntry",
                       bordercolor=self.PRIMARY_COLOR,
                       lightcolor=self.PRIMARY_COLOR,
                       darkcolor=self.PRIMARY_COLOR,
                       borderwitdh=1,
                       focusthickness=0,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       fieldbackground=self.SECONDARY_COLOR)
        self.map("ResultEntryRPG.TEntry",
                 bordercolor=[("focus", self.PRIMARY_COLOR)],
                 lightcolor=[("focus", self.PRIMARY_COLOR)],
                 darkcolor=[("focus", self.PRIMARY_COLOR)])

        # scrollbar and scale
        self.configure("TScrollbar",
                       bordercolor=self.ACCENT_COLOR,
                       lightcolor=self.ACCENT_COLOR,
                       darkcolor=self.ACCENT_COLOR,
                       background=self.BACKGROUND_COLOR,
                       troughcolor=self.PRIMARY_COLOR,
                       arrowcolor=self.PRIMARY_COLOR)
        self.map("TScrollbar",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])

        # TScale
        self.configure("TScale",
                       bordercolor=self.ACCENT_COLOR,
                       lightcolor=self.ACCENT_COLOR,
                       darkcolor=self.ACCENT_COLOR,
                       focuscolor=self.PRIMARY_COLOR,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)
        self.map("TScale",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])


# password generator toplevel window dark mode
class PwdgenDarkModeStyle(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system
        self.BACKGROUND_COLOR = "#2b2b2b"
        self.PRIMARY_COLOR = "#dddcde"
        self.SECONDARY_COLOR = "#434345"
        self.ACCENT_COLOR = "#6e48e0"

        self.theme_use("clam")

        # custom style classes
        self.configure("BodyFrameRPG.TFrame",
                       background=self.BACKGROUND_COLOR)

        self.configure("InfoLabelRPG.TLabel",
                       font=("Arial", 16, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)

        self.configure("SpecificationInfoLabelRPG.TLabel",
                       font=("Arial", 14),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)

        self.configure("OptionCheckbuttonRPG.TCheckbutton",
                       focusthickness=5,
                       font=("Arial", 12),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)
        self.map("OptionCheckbuttonRPG.TCheckbutton",
                 foreground=[("active", self.PRIMARY_COLOR)],
                 background=[("active", self.SECONDARY_COLOR)],
                 indicatorbackground=[("selected", self.ACCENT_COLOR), ("!selected", self.PRIMARY_COLOR)],
                 indicatorcolor=[("selected", self.ACCENT_COLOR), ("!selected", self.PRIMARY_COLOR)])

        self.configure("PerformActionButtonRPG.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       font=("Arial", 14),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)
        self.map("PerformActionButtonRPG.TButton",
                 foreground=[("active", self.PRIMARY_COLOR)],
                 background=[("active", "#6d6d6e")])  # slightly brighter color SECONDARY_COLOR

        self.configure("SeparatorRPG.TSeparator",
                       background=self.PRIMARY_COLOR)

        self.configure("ResultEntryRPG.TEntry",
                       bordercolor=self.PRIMARY_COLOR,
                       lightcolor=self.PRIMARY_COLOR,
                       darkcolor=self.PRIMARY_COLOR,
                       borderwitdh=1,
                       focusthickness=0,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       fieldbackground=self.SECONDARY_COLOR)
        self.map("ResultEntryRPG.TEntry",
                 bordercolor=[("focus", self.PRIMARY_COLOR)],
                 lightcolor=[("focus", self.PRIMARY_COLOR)],
                 darkcolor=[("focus", self.PRIMARY_COLOR)])

        # scrollbar and scale
        self.configure("TScrollbar",
                       bordercolor=self.ACCENT_COLOR,
                       lightcolor=self.ACCENT_COLOR,
                       darkcolor=self.ACCENT_COLOR,
                       background=self.BACKGROUND_COLOR,
                       troughcolor=self.PRIMARY_COLOR,
                       arrowcolor=self.PRIMARY_COLOR)
        self.map("TScrollbar",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])

        # TScale
        self.configure("TScale",
                       bordercolor=self.ACCENT_COLOR,
                       lightcolor=self.ACCENT_COLOR,
                       darkcolor=self.ACCENT_COLOR,
                       focuscolor=self.PRIMARY_COLOR,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)
        self.map("TScale",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])
