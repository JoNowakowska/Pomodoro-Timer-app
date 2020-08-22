import tkinter as tk
from tkinter import ttk
from collections import deque

class Settings(ttk.Frame):

    def __init__(self, parent, controller, shift_function):
        super().__init__(parent)

        self['style'] = 'Background.TFrame'

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(2, weight = 1)

        self.controller = controller
        self.settings_frame = ttk.Frame(self, padding = '30 15 30 15')
        self.settings_frame.grid(sticky = 'EW', padx=10, pady=10)
        self.settings_frame.columnconfigure(0, weight = 1)
        self.settings_frame['style'] = 'Background.TFrame'

        self.pomodoro_label = ttk.Label(
            self.settings_frame,
            text= "Pomodoro: ",
            style = 'LightText.TLabel'
        )

        self.pomodoro_label.grid(row=0, column=0, sticky='W')

        self.pomodoro_spinbox = tk.Spinbox(
            self.settings_frame,
            textvariable = controller.pomodoro,
            from_ = 0,
            to=120,
            increment = 1,
            width = 10,
            justify = 'center'
        )

        self.pomodoro_spinbox.focus()
        self.pomodoro_spinbox.grid(row=0, column=1, sticky='EW')

        self.short_break_label = ttk.Label(
            self.settings_frame,
            text= "Short break: ",
            style = 'LightText.TLabel'
        )

        self.short_break_label.grid(row=1, column=0, sticky='W')

        self.short_break_spinbox = tk.Spinbox(
            self.settings_frame,
            textvariable = controller.short_break,
            from_ = 0,
            to=120,
            increment = 1,
            width = 10,
            justify = 'center'
        )

        self.short_break_spinbox.grid(row=1, column=1, sticky='EW')

        self.long_break_label = ttk.Label(
            self.settings_frame,
            text= "Long break: ",
            style = 'LightText.TLabel'
        )

        self.long_break_label.grid(row=2, column=0, sticky='W')

        self.long_break_spinbox = tk.Spinbox(
            self.settings_frame,
            textvariable = controller.long_break,
            from_ = 0,
            to=120,
            increment = 1,
            width = 10,
            justify = 'center'
        )

        self.long_break_spinbox.grid(row=2, column=1, sticky='EW')


        self.back_button = ttk.Button(self.settings_frame, text = ' <- Back to the Pomodoro Timer', command = shift_function, cursor = 'hand2', style = 'PomodoroButton.TButton')
        self.back_button.grid(row = 3, column = 0, columnspan=2, sticky='EW')
        self.back_button.columnconfigure(0, weight = 1)

        for child in self.settings_frame.winfo_children():
            child.grid_configure(padx = 5, pady = 5)
