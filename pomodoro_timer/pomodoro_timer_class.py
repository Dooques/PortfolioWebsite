from tkinter import *
import pygame
import math
from PIL import ImageTk, Image


class PomodoroTimer:
    def __init__(self):
        # Constants
        self.WORK_MIN = 25
        self.SHORT_BREAK_MIN = 5
        self.LONG_BREAK_MIN = 20
        self.reps = 0
        self.timer = ''
        self.CHECKMARK = '✓'
        self.PINK = "#e2979c"
        self.RED = "#e7305b"
        self.GREEN = "#9bdeac"
        self.YELLOW = "#f7f5dd"
        self.FONT_NAME = "Courier"

        # Inits
        pygame.mixer.init()
        self.window = Tk()
        self.window.title('Pomodoro')
        path = 'pomodoro_timer/tomato.png'

        self.window.config(padx=100, pady=50, bg=self.GREEN, width=200, height=230)
        # TKinter Setup
        self.canvas = Canvas(width=200, height=224, bg=self.GREEN, highlightthickness=0)

        self.tomato_pic = ImageTk.PhotoImage(Image.open(path))
        self.canvas.create_image(100, 112, image=self.tomato_pic)

        self.timer_text = self.canvas.create_text(
            100, 130, text='00:00', fill='white', font=(self.FONT_NAME, 35, 'bold'))
        self.canvas.grid(column=1, row=1)

        self.timer_label = Label(text='Timer', font=(self.FONT_NAME, 50), bg=self.GREEN, fg=self.PINK)
        self.timer_label.grid(column=1, row=0)

        self.start_button = Button(text='Start', bg=self.YELLOW, command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(text='Reset', bg=self.YELLOW, command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        self.time_stamp_label = Label(bg=self.GREEN, font=(self.FONT_NAME, 20), fg=self.RED)
        self.time_stamp_label.grid(column=1, row=3)

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text='00:00')
        self.timer_label.config(text='Timer')
        self.time_stamp_label.config(text='')
        self.reps = 0

    def start_timer(self):
        self.reps += 1
        work = self.WORK_MIN * 60
        short = self.SHORT_BREAK_MIN * 60
        long = self.LONG_BREAK_MIN * 60
        if self.reps % 8 == 0:
            count = long
            self.timer_label.config(text='Break', fg=self.PINK)
            pygame.mixer.music.load('pomodoro_timer/assets/Bb2.aiff')
            pygame.mixer.music.play()
        elif self.reps % 2 == 0:
            count = short
            self.timer_label.config(text='Break', fg=self.YELLOW)
            pygame.mixer.music.load('pomodoro_timer/assets/Db1.aiff')
            pygame.mixer.music.play()
        else:
            count = work
            self.timer_label.config(text='Work', fg=self.RED)
            pygame.mixer.music.load('pomodoro_timer/assets/C1.aiff')
            pygame.mixer.music.play()
        self.countdown(count)

    def countdown(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_min < 10:
            count_min = f'0{count_min}'
        if count_sec < 10:
            count_sec = f'0{count_sec}'
        self.canvas.itemconfig(self.timer_text, text=f'{count_min}:{count_sec}')
        if count > 0:
            self.timer = self.window.after(1000, self.countdown, count - 1)
        else:
            self.start_timer()
            time_stamp = ''
            for _ in range(math.floor(self.reps/2)):
                time_stamp += self.CHECKMARK
                self.time_stamp_label.config(text=time_stamp)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    pomodoro = PomodoroTimer()
    pomodoro.run()
