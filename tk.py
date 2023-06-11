import tkinter as tk
from tkinter import ttk
import time
from functools import partial
import sympy as sp
from sympy.plotting import plot
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Доставлены библиотеки для всех задач


class Menu:


    @classmethod
    def close_menu(cls):
        for btn in cls.btns:
            btn.destroy()


    @classmethod
    def open_menu(cls):
        cls.btns = []
        root.title("Меню")
        calc = tk.Button(text="Калькулятор", command=cls.calculator)
        calc.place(width=700, height=80, y=50, x=50)
        exp = tk.Button(text="Аналитические выражения", command=cls.analytic_expressions)
        exp.place(width=700, height=80, y=150, x=50)
        graphs = tk.Button(text="Построение графиков", command=cls.graphs)
        graphs.place(width=700, height=80, y=250, x=50)
        cls.btns.append(calc)
        cls.btns.append(exp)
        cls.btns.append(graphs)

    
    @classmethod
    def calculator(cls):
        cls.close_menu()
        Calculator().open_calculator()

    
    @classmethod
    def analytic_expressions(cls):
        cls.close_menu()
        AnalyticsExpressions.open_analytics()

    
    @classmethod
    def graphs(cls):
        cls.close_menu()
        GraphBuilder.open_graph()


class Calculator:
    first = 0
    second = 0
    state = "+"


    @classmethod
    def close_calc(cls):
        for btn in cls.buttons:
            btn.destroy()
        Menu.open_menu()


    @classmethod
    def open_calculator(cls):
        cls.buttons = []
        root.title("Калькулятор")
        back_btn = tk.Button(text="Назад", command=cls.close_calc)
        back_btn.place(x=10, y=10, width=40, height=20)
        cls.buttons.append(back_btn)
        box = tk.Entry()
        box.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.05)
        cls.buttons.append(box)
        btns = [
            "7", "8", "9",
            "4", "5", "6",
            "1", "2", "3",
            "+", "0", "-",
             "*", "=", "/"
        ]
        pos_x = 80
        pos_y = 150
        k = 0
        for btn in btns:
            
            if k == 3:
                k = 0
                pos_x = 80
                pos_y += 100
            b = tk.Button(text=btn, command=partial(cls.button_handler, btn, box))
            b.place(width=200, height=80, x=pos_x, y=pos_y)
            cls.buttons.append(b)
            pos_x += 220
            k += 1
        c = tk.Button(text="C", command=partial(cls.button_handler, "C", box))
        c.place(height=80, width=40, x=740, y=40)
        cls.buttons.append(c)


    @classmethod
    def button_handler(cls, n: str, box: tk.Entry):
        if n.isdigit():
            print(n)
            box.insert(len(box.get()), n)
        else:
            if n == "+":
                cls.first = int(box.get())
                cls.state = "+"
                box.delete(0, last="end")
            if n == "-":
                cls.first = int(box.get())
                cls.state = "-"
                box.delete(0, last="end")
            if n == "/":
                cls.first = int(box.get())
                cls.state = "/"
                box.delete(0, last="end")
            if n == "*":
                cls.first = int(box.get())
                cls.state = "*"
                box.delete(0, last="end")
            if n == "=":
                cls.second = int(box.get())
                box.delete(0, last="end")
                if cls.state == "+":
                    box.insert(0, cls.first + cls.second)
                if cls.state == "-":
                    box.insert(0, cls.first - cls.second)
                if cls.state == "/":
                    box.insert(0, cls.first / cls.second)
                if cls.state == "*":
                    box.insert(0, cls.first * cls.second)
                cls.state="+"
                cls.first = 0
                second = 0
            if n == "C":
                box.delete(0, last="end")
                cls.state = "+"
                cls.first = 0
                cls.second = 0


class AnalyticsExpressions:

    answer_label = None

    @classmethod
    def open_analytics(cls):
        cls.buttons = []
        back_btn = tk.Button(text="Назад", command=cls.close_analytics)
        back_btn.place(x=10, y=10, width=40, height=20)
        cls.buttons.append(back_btn)
        root.title("Аналитические выражения")
        entry_box = tk.Entry()
        entry_box.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.05)
        cls.buttons.append(entry_box)
        eq_button = tk.Button(text="=", command=partial(cls.f, entry_box))
        eq_button.place(width=40, height=80, x=740, y=40)
        cls.buttons.append(eq_button)


    @classmethod
    def close_analytics(cls):
        for btn in cls.buttons:
            btn.destroy()
        if cls.answer_label is not None:
            cls.answer_label.destroy()
        Menu.open_menu()
        

    @classmethod
    def f(cls, entry):
        a = entry.get()
        cls.make_expression(a)


    @classmethod
    def make_expression(cls, s):
        transformations = (standard_transformations + (implicit_multiplication_application,))
        s = s.replace("=", "-").replace("^", "**")
        f = sp.parse_expr(s, transformations=transformations)
        sq = sp.solve(f)
        cls.print_answer(sq)
    

    @classmethod
    def print_answer(cls, answer):
        if cls.answer_label is not None:
            cls.answer_label.destroy()
        label = tk.Label(text=f"Ответ: {answer}", font=50)
        label.place(relx=0.2, rely=0.2)
        cls.answer_label = label


class GraphBuilder:
    @classmethod
    def open_graph(cls):
        cls.buttons = []
        back_btn = tk.Button(text="Назад", command=cls.close_graph)
        back_btn.place(x=10, y=10, width=40, height=20)
        cls.buttons.append(back_btn)
        root.title("Построение графиков")
        entry_box = tk.Entry()
        entry_box.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.05)
        cls.buttons.append(entry_box)
        x_from_label = tk.Label(text="X от:")
        x_from_label.place(x=80, y=150)
        x_to_label = tk.Label(text="X до:")
        x_to_label.place(x=180, y=150)
        cls.buttons.append(x_from_label)
        cls.buttons.append(x_to_label)
        x_from_box = tk.Entry()
        x_from_box.place(x=120, y=135, height=50, width=50)
        x_to_box = tk.Entry()
        x_to_box.place(x=220, y=135, height=50, width=50)
        x_from_box.insert("end", "-10")
        x_to_box.insert("end", "10")
        cls.buttons.append(x_from_box)
        cls.buttons.append(x_to_box)
        eq_button = tk.Button(text="=", command=partial(cls.f, entry_box, x_from_box, x_to_box))
        eq_button.place(width=40, height=80, x=740, y=40)
        cls.buttons.append(eq_button)
        

    
    @classmethod
    def f(cls, entry, from_box, to_box):
        a = entry.get()
        from_x =from_box.get()
        to_x = to_box.get()
        cls.make_graph(a, from_x, to_x)


    @classmethod
    def make_graph(cls, s, from_x, to_x):
        print(s)
        exp = sp.sympify(s)
        x = sp.Symbol('x')
        p = plot(exp, (x, from_x, to_x), show=False)
        fig, ax = plt.subplots()
        backend = p.backend(p)
        backend.ax = ax
        backend._process_series(backend.parent._series, ax, backend.parent)
        backend.ax.spines['right'].set_color('none')
        backend.ax.spines['bottom'].set_position('zero')
        backend.ax.spines['top'].set_color('none')
        plt.close(backend.fig)
        canvas = FigureCanvasTkAgg(fig)
        canvas.draw()
        cls.buttons.append(canvas.get_tk_widget())
        canvas.get_tk_widget().place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)


    @classmethod
    def close_graph(cls):
        for btn in cls.buttons:
            btn.destroy()
        Menu.open_menu()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    root.resizable(width=False, height=False)
    Menu.open_menu()
    root.mainloop()
