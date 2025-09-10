import tkinter as tk
from tkinter import ttk

# 기본 설정
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("800x400")
root.configure(bg="black")

# 전역 변수
seconds = 0
total_seconds = 0
running = False

# 라벨
lbl = tk.Label(root, font=("Arial", 60, "bold"), bg="black", fg="cyan")
lbl.pack(pady=30)

# 진행률 바
progress = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
progress.pack(pady=10)

# 시간 포맷 함수 (HH:MM:SS)
def format_time(sec):
    hours = sec // 3600
    minutes = (sec % 3600) // 60
    seconds = sec % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# 카운트다운 함수
def countdown():
    global seconds, running
    if running and seconds >= 0:
        lbl.config(text=f"{format_time(seconds)} left")
        update_progress()
        seconds -= 1
        root.after(1000, countdown)
    elif seconds < 0:
        lbl.config(text="Times Up!")
        progress['value'] = 100

# 진행률 업데이트
def update_progress():
    if total_seconds > 0:
        percent = ((total_seconds - seconds) / total_seconds) * 100
        progress['value'] = percent
    else:
        progress['value'] = 0

# 시간 추가 함수 (누적)
def add_time(sec):
    global seconds, total_seconds, running
    if not running:
        seconds += sec
        total_seconds = seconds
        lbl.config(text=f"{format_time(seconds)} remaining")
        update_progress()

# 시작 함수
def start():
    global running
    if seconds > 0:
        running = True
        countdown()

# 멈춤 함수
def pause():
    global running
    running = False
    lbl.config(text=f"{format_time(seconds)} Paused")

# 초기화 함수
def reset():
    global seconds, total_seconds, running
    running = False
    seconds = 0
    total_seconds = 0
    lbl.config(text="00:00:00 initialized")
    progress['value'] = 0

# 종료 함수
def exit_app():
    root.destroy()

# 시간 추가 버튼 프레임
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="+1분", font=("Arial", 16), command=lambda: add_time(60)).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="+5분", font=("Arial", 16), command=lambda: add_time(300)).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="+10분", font=("Arial", 16), command=lambda: add_time(600)).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="+30분", font=("Arial", 16), command=lambda: add_time(1800)).grid(row=0, column=3, padx=10)
tk.Button(btn_frame, text="+1시간", font=("Arial", 16), command=lambda: add_time(3600)).grid(row=0, column=4, padx=10)

# 제어 버튼 프레임
control_frame = tk.Frame(root, bg="black")
control_frame.pack(pady=20)

tk.Button(control_frame, text="Start", font=("Arial", 20), bg="green", fg="white", command=start).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="Stop", font=("Arial", 20), bg="orange", fg="white", command=pause).grid(row=0, column=1, padx=10)
tk.Button(control_frame, text="Init", font=("Arial", 20), bg="blue", fg="white", command=reset).grid(row=0, column=2, padx=10)
tk.Button(control_frame, text="End", font=("Arial", 20), bg="red", fg="white", command=exit_app).grid(row=0, column=3, padx=10)

# 실행
root.mainloop()