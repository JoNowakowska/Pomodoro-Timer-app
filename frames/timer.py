import tkinter as tk
from tkinter import ttk
from collections import deque


class Timer(ttk.Frame):

    def __init__(self, parent, controller, shift_function):
        super().__init__(parent)

        self['style'] = 'Background.TFrame'

        self.controller = controller
        self.current_description = tk.StringVar(value = controller.schedule[0])
        self.current_time = tk.StringVar()
        self.pomodoro = int(controller.pomodoro.get())
        self.current_time.set(f'{self.pomodoro:02d}:00') 
        self.time_running = False
        self._timer_decrement_job = None
        self.columnconfigure(0, weight = 1)


        description_and_settings_frame = ttk.Frame(self)
        description_and_settings_frame.grid(row=0, column=0, sticky='NEWS')
        description_and_settings_frame.columnconfigure((0,1), weight = 1)

        description_and_settings_frame['style'] = 'Background.TFrame'

        timer_frame = ttk.Frame(self, height = '100')
        timer_frame.grid(row=1, column=0, pady=(10,0), sticky='NEWS')
        timer_frame['style'] = 'Timer.TFrame'

        buttons_frame = ttk.Frame(self, padding = 10)
        buttons_frame.grid(row=2, column = 0, sticky = 'EW')
        buttons_frame.columnconfigure((0,1,2), weight = 1)
        buttons_frame['style'] = 'Background.TFrame'

        self.description_label = ttk.Label(description_and_settings_frame, textvariable = self.current_description)
        self.description_label.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky = 'W')
        self.description_label['style'] = 'LightText.TLabel'

        self.settings_button = ttk.Button(description_and_settings_frame, text = 'Settings', command = shift_function, cursor = 'hand2', style = 'PomodoroButton.TButton')
        self.settings_button.grid(row=0, column=2, sticky = 'E', padx=(0,10), pady=(10,0))

        self.time_label = ttk.Label(timer_frame, textvariable=self.current_time)
        self.time_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        self.time_label['style'] = 'TimerText.TLabel'

        self.start_button = ttk.Button(buttons_frame, text='Start', command = self.start_timer, cursor = 'hand2', style = 'PomodoroButton.TButton')
        self.start_button.grid(row=0, column=0, sticky = 'EW')

        self.stop_button = ttk.Button(buttons_frame, text='Stop', command = self.stop_timer, state='disabled', cursor = 'hand2', style = 'PomodoroButton.TButton')
        self.stop_button.grid(row = 0, column = 1, padx=5, sticky = 'EW')

        self.reset_button = ttk.Button(buttons_frame, text = "Reset", command = self.reset_timer, cursor = 'hand2', style = 'PomodoroButton.TButton')
        self.reset_button.grid(row=0, column=2, sticky = 'EW')

    def start_timer(self):
        self.time_running = True
        self.count_down()
        self.stop_button['state'] = 'enabled'
        self.start_button['state'] = 'disabled'

    def stop_timer(self):
        self.time_running = False
        self.start_button['state'] = 'enabled'
        self.stop_button['state'] = 'disabled'
        
        if self._timer_decrement_job:
            self.after_cancel(self._timer_decrement_job)
            self._timer_decrement_job = None

    def reset_timer(self):
        self.stop_timer()
        self.controller.schedule = deque(self.controller.schedule_descriptions)
        self.current_description.set(self.controller.schedule[0])
        self.pomodoro = int(self.controller.pomodoro.get())
        self.current_time.set(f'{self.pomodoro:02d}:00')

    def count_down(self):
        current_time = self.current_time.get()
        minutes, seconds = current_time.split(':')
        minutes = int(minutes)
        seconds = int(seconds)

        if self.time_running and self.current_time.get() != '00:00':
            if seconds > 0:
                seconds = seconds - 1          
            else:
                seconds = 59
                minutes = minutes - 1
            self.current_time.set('{:02d}:{:02d}'.format(minutes, seconds))
            self._timer_decrement_job = self.after(1000, self.count_down)
        
        elif self.time_running and self.current_time.get() == '00:00':
            self.controller.schedule.rotate(-1)
            next_up = self.controller.schedule[0]
            self.current_description.set(next_up)

            if next_up == 'Pomodoro':
                self.pomodoro = int(self.controller.pomodoro.get())
                self.current_time.set(f'{self.pomodoro:02d}:00')    
            elif next_up == 'Short break':
                self.short_break = int(self.controller.short_break.get())
                self.current_time.set(f'{self.short_break:02d}:00')
            elif next_up == 'Long time':
                self.long_break = int(self.controller.long_break.get())
                self.current_time.set(f'{self.long_break:00}:00')
            
            self._timer_decrement_job = self.after(1000, self.count_down)