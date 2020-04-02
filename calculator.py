import tkinter


def add_text(new_text, calculation) -> None:
    "Adds the value of a button to the entry field."
    text = calculation.get()
    calculation.set(text + new_text)


def solve(calculation) -> None:
    "Calculates calculation and sets entry field to the result."
    text = calculation.get()
    if text:
        calculation.set(str(eval(text)))


def delete(calculation) -> None:
    "Sets the entry field to ''."
    calculation.set("")


def remove(calculation) -> None:
    "Removes the last character in the entry field."
    text = calculation.get()
    calculation.set(text[:-1])


# main (only) gui
# adds buttons and entry
root = tkinter.Tk()
root.title("Rechner")
root.iconphoto(False, tkinter.PhotoImage(file="icon.png"))
root.geometry("320x450")
root.resizable(False, False)
calculation = tkinter.StringVar()
calculation_entry = tkinter.Entry(
    master=root, width=54, textvariable=calculation, state="disabled")
calculation_entry.grid(row=0, column=0, columnspan=5, ipady=5)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="1", command=lambda: add_text("1", calculation)).grid(row=1, column=0)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="2", command=lambda: add_text("2", calculation)).grid(row=1, column=1)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="3", command=lambda: add_text("3", calculation)).grid(row=1, column=2)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="4", command=lambda: add_text("4", calculation)).grid(row=2, column=0)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="5", command=lambda: add_text("5", calculation)).grid(row=2, column=1)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="6", command=lambda: add_text("6", calculation)).grid(row=2, column=2)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="7", command=lambda: add_text("7", calculation)).grid(row=3, column=0)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="8", command=lambda: add_text("8", calculation)).grid(row=3, column=1)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="9", command=lambda: add_text("9", calculation)).grid(row=3, column=2)
tkinter.Button(master=root, height=5, width=10, background="black", foreground="white",
               text="0", command=lambda: add_text("0", calculation)).grid(row=4, column=1)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text=".", command=lambda: add_text(".", calculation)).grid(row=4, column=0)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="*", command=lambda: add_text("*", calculation)).grid(row=1, column=3)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="/", command=lambda: add_text("/", calculation)).grid(row=2, column=3)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="+", command=lambda: add_text("+", calculation)).grid(row=3, column=3)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="-", command=lambda: add_text("-", calculation)).grid(row=4, column=3)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="(", command=lambda: add_text("(", calculation)).grid(row=5, column=0)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text=")", command=lambda: add_text(")", calculation)).grid(row=5, column=1)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="C", command=lambda: delete(calculation)).grid(row=4, column=2)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="<-", command=lambda: remove(calculation)).grid(row=5, column=2)
tkinter.Button(master=root, height=5, width=10, background="gray", foreground="white",
               text="=", command=lambda: solve(calculation)).grid(row=5, column=3)
root.mainloop()
