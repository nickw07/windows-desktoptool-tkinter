
import tkinter as tk
from tkinter import ttk

import math

import pyperclip

from applications.app_styles import CalculatorLightModeStyle, CalculatorDarkModeStyle

from root.theme_manager import ThemeManager


class Calculator(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # GUI placement and setup
        self.root_x = parent.winfo_x()
        self.root_y = parent.winfo_y()

        self.geometry(f"+{self.root_x}+{self.root_y}")
        self.resizable(False, False)

        self.title("Calculator")
        self.iconbitmap(r"../graphics/window-icon-32x32px.ico")

        # start in correct mode
        if ThemeManager.is_dark_mode():
            self.style = CalculatorDarkModeStyle()
            self.configure(background=self.style.BACKGROUND_COLOR)
        else:
            self.style = CalculatorLightModeStyle()
            self.configure(background=self.style.BACKGROUND_COLOR)

        # GUI separation by frames
        equation_frame = EquationFrame(self,
                                       style="BodyFrameCalc.TFrame")
        equation_frame.pack()

        button_frame = ButtonFrame(self,
                                   equation_frame.equation_display_entry,
                                   equation_frame.equation_var,
                                   style="BodyFrameCalc.TFrame")
        button_frame.pack(padx=5, pady=5)


class EquationFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.equation_var = tk.StringVar(value="0")

        # current expression
        self.equation_display_entry = ttk.Entry(self,
                                                textvariable=self.equation_var,
                                                font=("Arial", 16, "bold"),
                                                width=34,
                                                state="readonly",
                                                justify=tk.CENTER,
                                                style="EquationDisplayEntryCalc.TEntry")
        self.equation_display_entry.grid(row=0, column=0, pady=10)


class GeneralMethods:
    def __init__(self, equation_var, equation_text, copy_entry_button):

        self.equation_var = equation_var
        self.equation_text = equation_text

        # widget transfer
        self.copy_entry_button = copy_entry_button

        self.ERROR_SUFFIX = "Error"

    # auxiliary methods
    def handle_error(self, arithmetic_error=False, syntax_error=False, value_error=False):
        # error reaction

        if arithmetic_error:
            self.equation_var.set(f"Arithmetic {self.ERROR_SUFFIX}")
            self.equation_text = ""

        elif syntax_error:
            self.equation_var.set(f"Syntax {self.ERROR_SUFFIX}")
            self.equation_text = ""

        elif value_error:
            self.equation_var.set(f"Value {self.ERROR_SUFFIX}")
            self.equation_text = ""

    @staticmethod
    def round_result(result):
        return str(round(result, 5))

    @staticmethod
    def remove_leading_zeros_expression_start(number):
        while number.startswith("0"):
            number = number[1:]
        return number


class ButtonFrame(ttk.Frame):
    def __init__(self, container, equation_display_entry, equation_var, **kwargs):
        super().__init__(container, **kwargs)

        self.equation_var = equation_var
        self.equation_text = ""

        # widget transfer
        self.equation_display_entry = equation_display_entry

        self.SUPERSCRIPT_TWO = chr(0xB2)
        self.SQRT_SIGN = chr(0x221A)

        # creating button widgets
        # first row
        open_parentheses_button = ttk.Button(self,
                                             text="(",
                                             command=lambda: self.button_press("("),
                                             style="OperationButtonCalc.TButton")
        open_parentheses_button.grid(row=0, column=0, padx=2, pady=2)

        close_parentheses_button = ttk.Button(self,
                                              text=")",
                                              command=lambda: self.button_press(")"),
                                              style="OperationButtonCalc.TButton")
        close_parentheses_button.grid(row=0, column=1, padx=2, pady=2)

        switch_sign_button = ttk.Button(self,
                                        text="- / +",
                                        command=self.switch_mathematical_sign_of_expression,
                                        style="OperationButtonCalc.TButton")
        switch_sign_button.grid(row=0, column=2, padx=2, pady=2)

        self.copy_entry_button = ttk.Button(self,
                                            text="Copy Entry!",
                                            command=self.copy_result,
                                            style="OperationButtonCalc.TButton")
        self.copy_entry_button.grid(row=0, column=3, sticky=tk.EW, columnspan=2, padx=2, pady=2)

        # second row
        button_1 = ttk.Button(self,
                              text="1",
                              command=lambda: self.button_press(1),
                              style="BaseOptionButtonCalc.TButton")
        button_1.grid(row=1, column=0, padx=2, pady=2)

        button_2 = ttk.Button(self,
                              text="2",
                              command=lambda: self.button_press(2),
                              style="BaseOptionButtonCalc.TButton")
        button_2.grid(row=1, column=1, padx=2, pady=2)

        button_3 = ttk.Button(self,
                              text="3",
                              command=lambda: self.button_press(3),
                              style="BaseOptionButtonCalc.TButton")
        button_3.grid(row=1, column=2, padx=2, pady=2)

        delete_button = ttk.Button(self,
                                   text="DEL",
                                   command=self.delete_last,
                                   style="OperationButtonCalc.TButton")
        delete_button.grid(row=1, column=3, padx=2, pady=2)

        all_clear_button = ttk.Button(self,
                                      text="AC",
                                      command=self.all_clear,
                                      style="OperationButtonCalc.TButton")
        all_clear_button.grid(row=1, column=4, sticky=tk.EW, columnspan=2, padx=2, pady=2)

        # third row
        button_4 = ttk.Button(self,
                              text="4",
                              command=lambda: self.button_press(4),
                              style="BaseOptionButtonCalc.TButton")
        button_4.grid(row=2, column=0, padx=2, pady=2)

        button_5 = ttk.Button(self,
                              text="5",
                              command=lambda: self.button_press(5),
                              style="BaseOptionButtonCalc.TButton")
        button_5.grid(row=2, column=1, padx=2, pady=2)

        button_6 = ttk.Button(self,
                              text="6",
                              command=lambda: self.button_press(6),
                              style="BaseOptionButtonCalc.TButton")
        button_6.grid(row=2, column=2, padx=2, pady=2)

        plus_button = ttk.Button(self,
                                 text="+",
                                 command=lambda: self.button_press("+"),
                                 style="OperationButtonCalc.TButton")
        plus_button.grid(row=2, column=3, padx=2, pady=2)

        minus_button = ttk.Button(self,
                                  text="-",
                                  command=lambda: self.button_press("-"),
                                  style="OperationButtonCalc.TButton")
        minus_button.grid(row=2, column=4, padx=2, pady=2)

        # fourth row
        button_7 = ttk.Button(self,
                              text="7",
                              command=lambda: self.button_press(7),
                              style="BaseOptionButtonCalc.TButton")
        button_7.grid(row=3, column=0, padx=2, pady=2)

        button_8 = ttk.Button(self,
                              text="8",
                              command=lambda: self.button_press(8),
                              style="BaseOptionButtonCalc.TButton")
        button_8.grid(row=3, column=1, padx=2, pady=2)

        button_9 = ttk.Button(self,
                              text="9",
                              command=lambda: self.button_press(9),
                              style="BaseOptionButtonCalc.TButton")
        button_9.grid(row=3, column=2, padx=2, pady=2)

        multiply_button = ttk.Button(self,
                                     text="*",
                                     command=lambda: self.button_press("*"),
                                     style="OperationButtonCalc.TButton")
        multiply_button.grid(row=3, column=3, padx=2, pady=2)

        divide_button = ttk.Button(self,
                                   text="/",
                                   command=lambda: self.button_press("/"),
                                   style="OperationButtonCalc.TButton")
        divide_button.grid(row=3, column=4, padx=2, pady=2)

        # fifth row
        button_0 = ttk.Button(self,
                              text="0",
                              command=lambda: self.button_press(0),
                              style="BaseOptionButtonCalc.TButton")
        button_0.grid(row=4, column=0, padx=2, pady=2)

        decimal_button = ttk.Button(self,
                                    text=".",
                                    command=lambda: self.button_press("."),
                                    style="BaseOptionButtonCalc.TButton")
        decimal_button.grid(row=4, column=1, padx=2, pady=2)

        equals_button = ttk.Button(self,
                                   text="=",
                                   command=self.perform_action,
                                   style="EqualsButtonCalc.TButton")
        equals_button.grid(row=4, column=2, padx=2, pady=2)

        square_button = ttk.Button(self,
                                   text=f"x {self.SUPERSCRIPT_TWO}",
                                   command=self.square_of_expression,
                                   style="OperationButtonCalc.TButton")
        square_button.grid(row=4, column=3, padx=2, pady=2)

        sqrt_button = ttk.Button(self,
                                 text=self.SQRT_SIGN,
                                 command=self.sqrt_of_expression,
                                 style="OperationButtonCalc.TButton")
        sqrt_button.grid(row=4, column=4, padx=2, pady=2)

        # scrollbar
        equation_display_entry_scrollbar = ttk.Scrollbar(self,
                                                         orient=tk.HORIZONTAL,
                                                         command=self.equation_display_entry.xview)
        equation_display_entry_scrollbar.grid(row=5, column=0, sticky=tk.EW, columnspan=5, padx=2, pady=5)
        self.equation_display_entry.configure(xscrollcommand=equation_display_entry_scrollbar.set)

        self.general_methods = GeneralMethods(self.equation_var, self.equation_text, self.copy_entry_button)

    def button_press(self, pressed_button):

        self.equation_text += str(pressed_button)

        self.equation_var.set(self.equation_text)

    def perform_action(self):

        try:
            # check for ** or //
            if "**" in self.equation_text or "//" in self.equation_text:
                self.general_methods.handle_error(syntax_error=True)

            self.calculation_of_expression()

        except ZeroDivisionError:
            self.general_methods.handle_error(arithmetic_error=True)
        except SyntaxError:
            self.general_methods.handle_error(syntax_error=True)
        except ValueError:
            self.general_methods.handle_error(value_error=True)
        except TypeError:
            self.general_methods.handle_error(value_error=True)
        except Exception as E:
            print(E)

    def calculation_of_expression(self):

        self.equation_text = self.equation_var.get()
        self.equation_text = self.general_methods.remove_leading_zeros_expression_start(self.equation_text)

        result = eval(str(self.equation_text))
        result = self.general_methods.round_result(result)

        self.equation_var.set(result)
        self.equation_text = result

    def square_of_expression(self):

        try:
            self.equation_text = self.equation_var.get()

            # operation
            result = (float(self.equation_text) * float(self.equation_text))
            result = self.general_methods.round_result(result)

            self.equation_var.set(result)
            self.equation_text = result

        except ValueError:
            self.general_methods.handle_error(value_error=True)
        except Exception as E:
            print(E)

    def sqrt_of_expression(self):

        try:
            self.equation_text = self.equation_var.get()

            # operation
            result = math.sqrt(float(self.equation_text))
            result = self.general_methods.round_result(result)

            self.equation_var.set(result)
            self.equation_text = result

        except ValueError:
            self.general_methods.handle_error(value_error=True)
        except Exception as E:
            print(E)

    def switch_mathematical_sign_of_expression(self):

        self.equation_text = self.equation_var.get()

        try:

            if self.equation_text[0] != "-":
                equation_text_reversed = self.equation_text[::-1]
                equation_text_reversed += "-"
                self.equation_text = equation_text_reversed[::-1]

                self.equation_var.set(self.equation_text)

            else:
                equation_text_reversed = self.equation_text[::-1]
                equation_text_reversed = equation_text_reversed[:-1]
                self.equation_text = equation_text_reversed[::-1]

                self.equation_var.set(self.equation_text)

        except IndexError:
            self.general_methods.handle_error(syntax_error=True)

    def delete_last(self):

        if self.general_methods.ERROR_SUFFIX in self.equation_var.get():
            self.equation_var.set("")
            self.equation_text = self.equation_var.get()
        else:
            self.equation_var.set(self.equation_var.get()[:-1])
            self.equation_text = self.equation_var.get()

    def all_clear(self):

        self.equation_text = ""
        self.equation_var.set("")

    def copy_result(self):
        result = self.equation_var.get()
        if result.startswith("Arithmetic") or result.startswith("Syntax") or result.startswith("Value"):
            pyperclip.copy("")
        else:
            pyperclip.copy(result)
