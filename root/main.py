
import tkinter as tk
from tkinter import ttk

from main_styles import LightModeStyle

from root_ui.heading_frame import HeadingFrame
from root_ui.system_frame import SystemFrame
from root_ui.quickaccess_frames import QuickAccessFirst, QuickAccessSecond
from root_ui.applications_frame import ApplicationsFrame


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # GUI placement and setup
        self.WIDTH = 900
        self.HEIGHT = 600

        self.MONITOR_CENTER_X = int(self.winfo_screenwidth() / 2 - (int(self.WIDTH) / 2))
        self.MONITOR_CENTER_Y = int(self.winfo_screenheight() / 2 - (int(self.HEIGHT) / 2))

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.MONITOR_CENTER_X}+{self.MONITOR_CENTER_Y}")
        self.resizable(False, False)

        self.title("Desktop Tool")
        self.iconbitmap(r"../graphics/window-icon-32x32px.ico")

        self.style = LightModeStyle(self)
        self.configure(background=self.style.BACKGROUND_COLOR)

        # GUI separation by frames
        self.body_frame = BodyFrame(self,
                                    width=860,
                                    height=560,
                                    style="BodyFrame.TFrame")
        self.body_frame.place(x=20, y=20)

        heading_frame = HeadingFrame(self.body_frame,
                                     width=840,
                                     height=50,
                                     style="SectionFrame.TFrame")
        heading_frame.place(x=10, y=10)
        heading_frame.show_time()

        system_info_frame = SystemFrame(self.body_frame,
                                        width=625,
                                        height=350,
                                        style="SectionFrame.TFrame")
        system_info_frame.place(x=10, y=70)

        # frame raising
        self.frames = {}

        quick_access_first_page_frame = QuickAccessFirst(self.body_frame,
                                                         self,
                                                         width=205,
                                                         height=350,
                                                         style="SectionFrame.TFrame")
        quick_access_first_page_frame.place(x=645, y=70)

        quick_access_second_page_frame = QuickAccessSecond(self.body_frame,
                                                           self,
                                                           width=205,
                                                           height=350,
                                                           style="SectionFrame.TFrame")
        quick_access_second_page_frame.place(x=645, y=70)

        self.frames[QuickAccessFirst] = quick_access_first_page_frame
        self.frames[QuickAccessSecond] = quick_access_second_page_frame

        self.change_window(QuickAccessFirst)

        applications_frame = ApplicationsFrame(self.body_frame,
                                               self,
                                               width=840,
                                               height=120,
                                               style="SectionFrame.TFrame")
        applications_frame.place(x=10, y=430)

    def change_window(self, container):
        frame = self.frames[container]
        frame.tkraise()


class BodyFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
