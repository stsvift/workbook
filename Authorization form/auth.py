import hashlib
from customtkinter import CTk, CTkLabel as Label, CTkEntry as Entry, CTkButton as Button, CTkToplevel as Toplevel, CTkCheckBox as Checkbutton
from tkinter import messagebox, IntVar

# Создание графического интерфейса
root = CTk()
root.title("Регистрация/Авторизация")

def register():
    def register_user():
        username = reg_username_entry.get()
        password = reg_password_entry.get()

        # Проверяем, не существует ли уже пользователь с таким именем
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, _ = line.strip().split(":")
                if username == stored_username:
                    messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует")
                    return

        # Хеширование пароля
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Записываем нового пользователя
        with open("users.txt", "a") as file:
            file.write(f"{username}:{hashed_password}\n")

        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        register_window.destroy()

    register_window = Toplevel(root)
    register_window.title("Регистрация")

    Label(register_window, text="Имя пользователя:").grid(row=0, column=0, pady=10)
    reg_username_entry = Entry(register_window)
    reg_username_entry.grid(row=0, column=1, pady=10)

    Label(register_window, text="Пароль:").grid(row=1, column=0, pady=10)
    reg_password_entry = Entry(register_window, show="*")
    reg_password_entry.grid(row=1, column=1, pady=10)

    # Чекбокс для отображения пароля
    show_password_var = IntVar()
    show_password = Checkbutton(register_window, text="Показать пароль", variable=show_password_var)
    show_password.grid(row=2, column=0, columnspan=2, pady=10)
    def toggle_password():
        if show_password_var.get():
            reg_password_entry.configure(show="")
        else:
            reg_password_entry.configure(show="*")
    show_password_var.trace_add("write", lambda *args: toggle_password())

    Button(register_window, text="Зарегистрироваться", command=register_user, fg_color="#9d00ff", hover_color="#7800c2").grid(row=3, column=0, columnspan=2, pady=10)

def login():
    username = login_username_entry.get()
    password = login_password_entry.get()

    # Хеширование введенного пароля для сравнения с хранимым
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and hashed_password == stored_password:
                messagebox.showinfo("Успех", "Авторизация прошла успешно!")
                return
        messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")

# Авторизация
Label(root, text="Авторизация").grid(row=0, column=0, columnspan=2, pady=10)
Label(root, text="Имя пользователя:").grid(row=1, column=0, pady=10)
login_username_entry = Entry(root)
login_username_entry.grid(row=1, column=1, pady=10)
Label(root, text="Пароль:").grid(row=2, column=0, pady=10)
login_password_entry = Entry(root, show="*")
login_password_entry.grid(row=2, column=1, pady=10)

# Чекбокс для отображения пароля при авторизации
show_password_var = IntVar()
show_password = Checkbutton(root, text="Показать пароль", variable=show_password_var)
show_password.grid(row=3, column=0, columnspan=2, pady=10)
def toggle_password():
    if show_password_var.get():
        login_password_entry.configure(show="")
    else:
        login_password_entry.configure(show="*")
show_password_var.trace_add("write", lambda *args: toggle_password())

Button(root, text="Войти", command=login, fg_color="#9d00ff", hover_color="#7800c2").grid(row=4, column=0, columnspan=2, pady=10)

# Регистрация
Label(root, text="Еще не зарегистрированы?").grid(row=5, column=0, columnspan=2, pady=10)
register_button = Button(root, text="Зарегистрироваться", command=register, fg_color="#9d00ff", hover_color="#7800c2")
register_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()