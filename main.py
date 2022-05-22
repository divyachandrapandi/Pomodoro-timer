from tkinter import *
import math

# TODO = POMODORO TECHNIQUE FOR EFFICIENT WORK FLOW
#  4 TIMES { WORK FOR 25 MIN + 5MIN SHORT BREAK }
#  LONG BREAK TIMES FOR 20 MIN

# ---------------------------- CONSTANTS ------------------------------- #
VIOLET = "#251D3A"
BLUE = "#2A2550"
ORANGE = "#7FB5FF"
YELLOW = "#E04D01"
SANDAL = "#F9D923"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
# TODO - 9 TIMER RESET
#  to stop timer, we need to break the loop, so after cancel
#  to make the timer start from beginning, initialize the reps to zero
#  create a timer variable (global) and pass it to after cancel
def timer_reset():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    timer_label.config(text="Timer")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# TODO - 4 timer function passed as command to start_button
# TODO - 6 reps is the count of each timeout. Intializing it as zero, we have increment it with one
#  if condition for work, break pattern
#  config label above (timer label) accordingly
def timer_start():
    global reps
    reps += 1
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=ORANGE)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short break", fg=YELLOW)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=ORANGE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# TODO -3  countdown
#  In tkinter we cannot pass a loop since we already have a mainloop which runs to detect any change on window
#  create a function which uses after method that itself a loop which pass millisecond as sleep time,
#  function, its argument

def count_down(count):
    count_min = math.floor(count / 60)  # floor--> 4.8 to 4 --> gives 4 min
    count_sec = count % 60  # modulo give remaining seconds
    # TODO -5 Dynamic typing
    """The dynamic typing explained : the count_sec variable holds integer value but since we need to pass 0 using
     f-string does not change the data type of count_sec at the same time we can concatenate the zero as string in 
     text for itemconfig in canvas"""
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(50, count_down, count - 1)
    # TODO - 7 to make the timer continue the next count down, we need to call timer_start in a loop
    #  after count > 0, we need to start the start_timer() function again
    # TODO - 8 to add checkmark after each work session
    #  create a empty string as marks,
    #  logic --> for every half of reps, one work session completed
    #  now add checkmarks in a loop of range of half-reps using config method
    else:
        timer_start()
        marks = ""
        working_session = math.floor(reps / 2)
        for _ in range(working_session):
            marks += "✔"
            checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer Project")
window.config(padx=100, pady=50, bg=BLUE)
# TODO - 1 SET CANVAS
#  Canvas is a widget which allows to lay another widget on top of it
#  Canvas has create method to create image, text
#  To add image uses separate variable tomato_image
#  To add text on centre of canvas image
#  DO NOT FORGET TO PACK
#  add padx, pady value and change some bg
#  highlightthickness is zero to merge window, canvas bg color
canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

# TODO - 2 SET UP LABEL, BUTTONS
#  Label for Timer title
#  Button for Start, reset
#  Label for Checkmarks
#  fg (foreground color) is used to color them
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=SANDAL, font=(FONT_NAME, 20, "bold"), bg=BLUE)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=timer_start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(row=2, column=2)

checkmark = Label(bg=BLUE, fg=ORANGE, font=(FONT_NAME, 14, 'bold'))
checkmark.grid(row=2, column=1)

window.mainloop()
