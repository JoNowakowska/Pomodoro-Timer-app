import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Timer, Settings

COLOR_PRIMARY = '#2e3f4f'
COLOR_SECONDARY = '#293846'
COLOR_LIGHT_BACKGROUND = '#fff'
COLOR_LIGHT_TEXT = '#eee'
COLOR_DART_TEXT = '#8095a8'

class PomodoroTimer(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use('clam')
        self['background'] = COLOR_PRIMARY

        style.configure('Timer.TFrame', background = COLOR_LIGHT_BACKGROUND)
        style.configure('Background.TFrame', background = COLOR_PRIMARY)
        style.configure(
            'TimerText.TLabel',
            background = COLOR_LIGHT_BACKGROUND,
            foreground = COLOR_DART_TEXT,
            font = 'Courier 38'
        )

        style.configure(
            'LightText.TLabel',
            background = COLOR_PRIMARY,
            foreground = COLOR_LIGHT_TEXT,
        )


        style.configure(
            'PomodoroButton.TButton',
            background = COLOR_SECONDARY,
            foreground = COLOR_LIGHT_TEXT,
        )

        style.map(
            'PomodoroButton.TButton',
            background = [('active', COLOR_PRIMARY), ('disabled', COLOR_LIGHT_TEXT)]
        )

        self.title('Pomodoro Timer by Joanna')
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0,), weight=1)

        self.schedule_descriptions = ['Pomodoro', 'Short break', 'Pomodoro', 'Short break', 'Pomodoro', 'Long break', 'Pomodoro']
        self.schedule = deque(self.schedule_descriptions)

        self.pomodoro = tk.StringVar(value = '25')
        self.short_break = tk.StringVar(value = '05')
        self.long_break = tk.StringVar(value = '15')

        container = ttk.Frame(self)
        container.grid(column=0, row=0)

        timer_frame = Timer(container, self,  lambda: self.shift_frame(Settings))
        timer_frame.grid(column=0, row=1, sticky='NEWS')
    
        settings_frame = Settings(container, self,  lambda: self.shift_frame(Timer))
        settings_frame.grid(column=0, row=1, sticky='NEWS')

        self.frames = {}

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame

        self.shift_frame(Timer)

    def shift_frame(self, selected_frame):
        frame = self.frames[selected_frame]
        frame.tkraise()

app = PomodoroTimer()

app.mainloop()