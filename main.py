from tkinter import *
import math 
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
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(texto_tiempo, text="00:00")
    label_tiempo.config(text="Tiempo")
    label_check.config(text="")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_tiempo():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    
    if reps % 8 == 0:
        cuenta_atras(long_break)
        label_tiempo.config(text="Descanso largo", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        cuenta_atras(short_break)
        label_tiempo.config(text="Descanso corto", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
    else:
        cuenta_atras(work_sec)
        label_tiempo.config(text="Trabaja", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)


    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def cuenta_atras(cuenta):
    minutos = math.floor(cuenta / 60)
    segundos = cuenta % 60
    if segundos < 10:
        segundos = f"0{segundos}"

    canvas.itemconfig(texto_tiempo, text=f"{minutos}:{segundos}")
    if cuenta > 0:
        global timer
        timer = window.after(1000, cuenta_atras, cuenta - 1)
    else:
        start_tiempo()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅"
        label_check.config(text=mark)
            




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
texto_tiempo = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



label_tiempo = Label(text="TIEMPO", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_tiempo.grid(column=1, row=0)

label_check = Label(fg=GREEN, font=(FONT_NAME, 18, "bold"), bg=YELLOW)
label_check.grid(column=1, row=4)

#botones
boton_start = Button(text="Start", highlightthickness=0, command=start_tiempo)
boton_start.grid(column=0, row=2)

boton_start = Button(text="Reset", highlightthickness=0, command=reset)
boton_start.grid(column=2, row=2)

window.mainloop()