from tkinter import *
import pygame
import math
# ---------------------------- CONSTANTS ------------------------------- #

CHECKMARK = '✓'

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer = ''

# ---------------------------- AUDIO ------------------------------- #
pygame.mixer.init()


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    time_stamp_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count = long
        timer_label.config(text='Break', fg=PINK)
        pygame.mixer.music.load('assets/Bb2.aiff')
        pygame.mixer.music.play()
    elif reps % 2 == 0:
        count = short
        timer_label.config(text='Break', fg=YELLOW)
        pygame.mixer.music.load('assets/Db1.aiff')
        pygame.mixer.music.play()
    else:
        count = work
        timer_label.config(text='Work', fg=RED)
        pygame.mixer.music.load('assets/C1.aiff')
        pygame.mixer.music.play()
    countdown(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        time_stamp = ''
        for _ in range(math.floor(reps/2)):
            time_stamp += CHECKMARK
            time_stamp_label.config(text=time_stamp)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=GREEN, width=200, height=230)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)

tomato_pic = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_pic)

timer_text = canvas.create_text(
    100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer', font=(FONT_NAME, 50), bg=GREEN, fg=PINK)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

time_stamp_label = Label(bg=GREEN, font=(FONT_NAME, 20), fg=RED)
time_stamp_label.grid(column=1, row=3)

window.mainloop()
