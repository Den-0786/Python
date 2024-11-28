from tkinter import *
from PIL import Image, ImageTk
import math
import winsound

#------------------------- CONSTANTS ----------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

reps = 0
timer = None
is_paused = False
time_left = 0

# ----------------------- TIMER RESET ---------------------------- #
def reset_timer():
    global time_left, is_paused
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_marks.config(text="")
    global reps
    reps = 0
    is_paused = False
    time_left = 0
# -------------------- PAUSE BUTTON ------------------------------#
def pause_timer():
    global is_paused, timer
    if is_paused:
        return  # Prevent re-entering if already paused
    window.after_cancel(timer)
    is_paused = True
    pause_button.config(text="Paused")
    
# -------------------- RESUME BUTTON ------------------------------#
def resume_timer():
    global is_paused, timer
    if not is_paused:
        return  # Prevent re-entering if already running
    is_paused = False
    pause_button.config(text="Pause")
    count_down(time_left)

# ---------------------- TIMER MECHANISM ----------------------------#
def start_timer():
    global time_left
    global reps
    reps +=1
    
    work_sec = WORK_MIN * 60
    work_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        time_left = long_break_sec
        title_label.config(text="Long Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        time_left = work_break_sec
        title_label.config(text="Short Break", fg=PINK, bg=YELLOW)
    else:
        time_left =  work_sec
        title_label.config(text="Work in session", fg=GREEN, bg=YELLOW)
    
    count_down(time_left)

# --------------------- COUNTDOWN MECHANISM ---------------------------- #
def count_down(count):
    global time_left, timer, is_paused
    
    time_left = count
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0 and not is_paused:
        global timer
        timer =  window.after(1000, count_down, count - 1)
        
    elif count == 0:
        winsound.Beep(440, 1000)
        start_timer()
        mark = ""
        
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark = "\u2713"
        check_marks.config(text= mark)
        
# --------------------- UI SETUP -------------------------------------- #

window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)


# Creating the image window
canvas = Canvas(window, width= 200, height=224)
img = Image.open("Tkinter/tomato.jpeg")
tk_img = ImageTk.PhotoImage(img)
canvas.create_image(100, 112, image=tk_img)
timer_count = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid()

# Creating the timer label
title_label = Label(window, text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN)
canvas.create_window(100, -20, window=title_label)


#Creating the start buttons
start_button = Button(window, text="Start", font=(FONT_NAME, 10, "bold"), fg=PINK, command=start_timer)
canvas.create_window(28, 210, window=start_button)

#Creating the reset 
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), fg=PINK, command=reset_timer)
canvas.create_window(175, 210, window=reset_button)

# Creating a pause button
pause_button = Button(text="Pause", font=(FONT_NAME, 9), fg=PINK, command=pause_timer)
canvas.create_window(175, 20, window=pause_button)

#Creating a resume button
resume_button = Button(window, text="Resume", font=(FONT_NAME, 9), fg=PINK, command=resume_timer)
canvas.create_window(27, 20, window= resume_button)


# Creating the checkbutton 
check_marks = Label(font=(FONT_NAME, 15), fg=GREEN)
canvas.create_window(100, 225, window=check_marks)


window.mainloop()