import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = ""

    # 체크박스 상태 확인
    if use_uppercase.get():
        characters += string.ascii_letters  # 대소문자 모두
    else:
        characters += string.ascii_lowercase  # 소문자만

    if use_digits.get():
        characters += string.digits

    if use_special.get():
        characters += string.punctuation

    if not characters:  # 아무 옵션도 선택하지 않은 경우
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "옵션을 선택하세요!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    root.update()  # 클립보드 갱신
    status_var.set("클립보드에 복사됨!")

# 메인 윈도우
root = tk.Tk()
root.title("패스워드 생성기")

# 길이 입력
tk.Label(root, text="패스워드 길이:").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")  # 기본값 12자리

# 옵션 체크박스
use_uppercase = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="영문 대소문자 섞기 (해제시 소문자만)", variable=use_uppercase).pack(anchor="w")
tk.Checkbutton(root, text="숫자 포함", variable=use_digits).pack(anchor="w")
tk.Checkbutton(root, text="특수문자 포함", variable=use_special).pack(anchor="w")

# 결과 표시 (Entry로 변경 → 마우스로 복사 가능)
result_entry = tk.Entry(root, font=("Arial", 14), fg="blue", width=30)
result_entry.pack(pady=10)

# 버튼
tk.Button(root, text="패스워드 생성", command=generate_password).pack()
tk.Button(root, text="클립보드에 복사", command=copy_to_clipboard).pack(pady=5)

# 상태 표시
status_var = tk.StringVar()
tk.Label(root, textvariable=status_var, fg="green").pack()

root.mainloop()
