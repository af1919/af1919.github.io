#Day 28, we are the best at this!!
from tkinter import *
import time





# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    a = 900
    minutes,seconds = divmod(a,60)
    canvas.itemconfig(f"{minutes:02d}:{seconds:02d}")
    window.after(1) 


# ---------------------------- TIMER MECHANISM ------------------------------- #  

def start_clock():
    global current_seconds
    total_minutes = 15
    current_seconds = total_minutes * 60
    update_clock()

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def update_clock():
    global current_seconds
    if current_seconds > 0:
        minutes, seconds = divmod(current_seconds, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        canvas.itemconfig(timer_text, text=time_str)
        current_seconds -= 1
        window.after(1000, update_clock)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)
text = '✔'
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

photo = PhotoImage(file='/Users/abelfanta/Downloads/pomodoro-start/tomato.png')
canvas.create_image(100,112,anchor='center',image=photo)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=4,row=3)

label = Label(text='TIMER',font=(FONT_NAME,30,'bold'),fg='#9bdeac',bg=YELLOW,highlightthickness=0,activebackground=GREEN)
label.grid(column=4,row=0)

button = Button(text='Start',command=start_clock)
button.grid(column=1,row=4)

button_1 = Button(text='Reset',command=reset_timer)
button_1.grid(column=6,row=4)


















window.mainloop()