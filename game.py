import tkinter as tk

window = tk.Tk()

window.title("Моя програма")
window.geometry("400x250")


def exit_program():
    window.destroy()


label = tk.Label(
    window,
    text="Вітаю у моїй програмі!",
    font=("Arial", 18)
)

label.pack(pady=50)


exit_button = tk.Button(
    window,
    text="Вихід",
    font=("Arial", 14),
    command=exit_program
)

exit_button.pack()


window.mainloop()