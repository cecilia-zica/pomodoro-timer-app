from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps= 0
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    start_button.config(state="disabled")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text= "Long Break", fg=RED)
    #If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text= "Break", fg=PINK)
    else:
    #If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✓"
        check_mark.config(text= marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=200, height=226)
window.config(padx= 100, pady=50, bg= YELLOW)

canvas = Canvas(width=200, height=226, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=tomato_img)

timer_text = canvas.create_text(102, 135, text="00:00", fill= "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column= 2, row= 2)

timer_label = Label(text= "Timer", fg= GREEN, font=(FONT_NAME, 40, "bold"), bg= YELLOW)
timer_label.grid(column= 2, row= 1)

start_button = Button(text="Start", font=(FONT_NAME,13), command= start_timer)
start_button.grid(column= 1, row= 3)

reset_button = Button(text="Reset", font=(FONT_NAME,13), highlightthickness= 0, command= reset_timer)
reset_button.grid(column= 3, row= 3)

check_mark = Label(text= "", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 30, "bold"))
check_mark.grid(column= 2, row=3)

window.mainloop()

