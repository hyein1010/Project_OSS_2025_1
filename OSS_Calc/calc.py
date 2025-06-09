import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""
        self.enable_check = tk.BooleanVar()

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 오답 체크박스
        check_frame = tk.Frame(root)
        check_frame.pack()
        tk.Checkbutton(check_frame, text="오답 풀이 기능", variable=self.enable_check).pack(anchor="w", padx=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            if self.enable_check.get() and '=' in self.expression:
                self.check_answer()
            else:
                try:
                    self.expression = str(eval(self.expression))
                except Exception:
                    self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def check_answer(self):
        try:
            left, right = self.expression.split("=")
            correct = eval(left.strip())
            user_answer = float(right.strip())

            if abs(correct - user_answer) < 1e-5:
                messagebox.showinfo("결과", "정답입니다!")
                self.expression = str(user_answer)
            else:
                messagebox.showwarning("결과", f"오답입니다.\n정답은 {correct}입니다.")
                self.expression = str(correct)
        except Exception as e:
            messagebox.showerror("오류", f"수식 오류: {e}")
            self.expression = ""


