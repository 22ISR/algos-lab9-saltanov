import tkinter as tk
import math
root = tk.Tk()
root.title("Калькулятор")
root.geometry("800x500")

def on_button_click(value):
    if value == "=":
        try:
            result = eval(textbox.get("1.0", tk.END))
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, result)
    
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль")
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Ошибка: Деление на ноль")
        except Exception as e:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Error")

    elif value == "Clear":
        textbox.delete("1.0", tk.END)

    elif value == "√":
        try:
            root = eval(textbox.get("1.0", tk.END))
            sqrt_math = math.sqrt(root)
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, sqrt_math)

        except Exception as e:
            textbox.delete("1.0", tk.END)
            textbox.insert(tk.END, "Error")


    else:
        print(value)
        textbox.insert(tk.END, value + "")






label = tk.Label(root, text="Калькулятор", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=20, pady=20)

buttonFrame = tk.Frame(root)
buttonFrame.pack(fill="x")
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)

btn17 = tk.Button(buttonFrame, text="(", font=("Arial", 18), command=lambda v="(": on_button_click(v))
btn18 = tk.Button(buttonFrame, text=")", font=("Arial", 18), command=lambda v=")": on_button_click(v))
btn19 = tk.Button(buttonFrame, text=".", font=("Arial", 18), command=lambda v=".": on_button_click(v))
btn20 = tk.Button(buttonFrame, text="√", font=("Arial", 18), command=lambda v="√": on_button_click(v))
btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 18), command=lambda v="1": on_button_click(v))
btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 18), command=lambda v="2": on_button_click(v))
btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 18), command=lambda v="3": on_button_click(v))
btn4 = tk.Button(buttonFrame, text="-", font=("Arial", 18), command=lambda v="-": on_button_click(v))
btn5 = tk.Button(buttonFrame, text="4", font=("Arial", 18), command=lambda v="4": on_button_click(v))
btn6 = tk.Button(buttonFrame, text="5", font=("Arial", 18), command=lambda v="5": on_button_click(v))
btn7 = tk.Button(buttonFrame, text="6", font=("Arial", 18), command=lambda v="6": on_button_click(v))
btn8 = tk.Button(buttonFrame, text="+", font=("Arial", 18), command=lambda v="+": on_button_click(v))
btn9 = tk.Button(buttonFrame, text="7", font=("Arial", 18), command=lambda v="7": on_button_click(v))
btn10 = tk.Button(buttonFrame, text="8", font=("Arial", 18), command=lambda v="8": on_button_click(v))
btn11 = tk.Button(buttonFrame, text="9", font=("Arial", 18), command=lambda v="9": on_button_click(v))
btn12 = tk.Button(buttonFrame, text="*", font=("Arial", 18), command=lambda v="*": on_button_click(v))
btn13 = tk.Button(buttonFrame, text="Clear", font=("Arial", 18), command=lambda v="Clear": on_button_click(v))
btn14 = tk.Button(buttonFrame, text="0", font=("Arial", 18), command=lambda v="0": on_button_click(v))
btn15 = tk.Button(buttonFrame, text="=", font=("Arial", 18), command=lambda v="=": on_button_click(v))
btn16 = tk.Button(buttonFrame, text="/", font=("Arial", 18), command=lambda v="/": on_button_click(v))

btn17.grid(row=0, column=0, sticky="we")
btn18.grid(row=0, column=1, sticky="we")
btn19.grid(row=0, column=2, sticky="we")
btn20.grid(row=0, column=3, sticky="we")
btn1.grid(row=1, column=0, sticky="we")
btn2.grid(row=1, column=1, sticky="we")
btn3.grid(row=1, column=2, sticky="we")
btn4.grid(row=1, column=3, sticky="we")
btn5.grid(row=2, column=0, sticky="we")
btn6.grid(row=2, column=1, sticky="we")
btn7.grid(row=2, column=2, sticky="we")
btn8.grid(row=2, column=3, sticky="we")
btn9.grid(row=3, column=0, sticky="we")
btn10.grid(row=3, column=1, sticky="we")
btn11.grid(row=3, column=2, sticky="we")
btn12.grid(row=3, column=3, sticky="we")
btn13.grid(row=4, column=0, sticky="we")
btn14.grid(row=4, column=1, sticky="we")
btn15.grid(row=4, column=2, sticky="we")
btn16.grid(row=4, column=3, sticky="we")

root.mainloop()
