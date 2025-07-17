

# light dark mode management
class ThemeManager:
    current_mode = "light"

    @classmethod
    def switch_mode(cls):
        if cls.current_mode == "light":
            cls.current_mode = "dark"
        else:
            cls.current_mode = "light"

    @classmethod
    def is_dark_mode(cls):
        return cls.current_mode == "dark"
