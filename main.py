from tkinter import *
import sqlite3


class MyApp:
    db_name = 'users_data'

    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])


    def verification(self):
        login = self.username_input.get()
        password = self.password_input.get()
        if len(login) == 0:
            print('too short')
        elif len(password) == 0:
            print('too short')
        else:
            self.username_input.delete(0, END)
            self.password_input.delete(0, END)
            query = 'SELECT Login,Password FROM Users'
            db_rows = self.run_query(query)
            print(db_rows)
            for row in db_rows:
                if login in row[0] and password in row[1]:
                    print("ok")
                else:
                    print('error')





    def auto_login(self):
        pass

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def validation(self):
        return len(self.register_login_input.get()) != 0 and len(self.register_password_input.get()) != 0 and len(
            self.register_name_input.get()) != 0 and len(self.register_surname_input.get()) != 0

    def adding(self):
        if self.validation():
            if self.register_login_input.get() == 'admin':
                self.isAdmin = TRUE
            else:
                self.isAdmin = FALSE
            query = 'INSERT INTO Users VALUES (?,?,?,?,?)'
            parameters = (
                self.register_login_input.get(), self.register_password_input.get(), self.register_name_input.get(),
                self.register_surname_input.get(), self.isAdmin)
            self.run_query(query, parameters)
            self.register_login_input.delete(0, END)
            self.register_password_input.delete(0, END)
            self.register_name_input.delete(0, END)
            self.register_surname_input.delete(0, END)

    def registration_back(self):
        self.register_frame.forget()
        self.input_frame.pack(fill=BOTH, expand=1, padx=80, pady=10)
        self.buttons_frame.pack(fill=BOTH, expand=1, padx=80, pady=20)

    # noinspection PyAttributeOutsideInit
    def registration(self):
        self.input_frame.forget()
        self.buttons_frame.forget()
        self.register_frame = Frame(root, relief=GROOVE)
        self.register_name = Label(self.register_frame, text="Name:")
        self.register_name_input = Entry(self.register_frame)
        self.register_surname = Label(self.register_frame, text="Surname:")
        self.register_surname_input = Entry(self.register_frame)
        self.register_login = Label(self.register_frame, text="Login:")
        self.register_login_input = Entry(self.register_frame)
        self.register_password = Label(self.register_frame, text="Password:")
        self.register_password_input = Entry(self.register_frame)
        self.register_save = Button(self.register_frame, text="Save", command=self.adding)
        self.register_back = Button(self.register_frame, text="Back", command=self.registration_back)
        self.register_surname.grid(row=2, column=1, pady=5)
        self.register_surname_input.grid(row=2, column=2, pady=5)
        self.register_name.grid(row=1, column=1, pady=5)
        self.register_name_input.grid(row=1, column=2, pady=5)
        self.register_login.grid(row=3, column=1, pady=5)
        self.register_login_input.grid(row=3, column=2, pady=5)
        self.register_password.grid(row=4, column=1, pady=5)
        self.register_password_input.grid(row=4, column=2, pady=5)
        self.register_save.grid(row=5, column=2, pady=5)
        self.register_back.grid(row=5, column=1, pady=5)
        self.register_frame.pack(fill=BOTH, expand=1, padx=80, pady=10)

    def __init__(self, root):
        root.title("OS salary")
        self.input_frame = Frame(root, relief=GROOVE)
        self.input_frame.pack(fill=BOTH, expand=1, padx=80, pady=10)
        self.buttons_frame = Frame(root, relief=GROOVE)
        self.buttons_frame.pack(fill=BOTH, expand=1, padx=80, pady=20)
        self.username = Label(self.input_frame, text="Username:")
        self.password = Label(self.input_frame, text="Password:")
        self.username_input = Entry(self.input_frame, width=40)
        self.password_input = Entry(self.input_frame, width=40)
        self.login = Button(self.buttons_frame, text="Login", height=2, width=20, command=self.verification)
        self.register = Button(self.buttons_frame, text="Register", height=2, width=20, command=self.registration)
        self.auto_login = Checkbutton(self.buttons_frame, text="Auto login")
        self.username.pack(padx=2, pady=2)
        self.username_input.pack(padx=2, pady=2)
        self.password.pack(padx=2, pady=2)
        self.password_input.pack(padx=2, pady=2)
        self.login.grid(row=1, column=2, sticky=W + E + N + S, padx=5, pady=10)
        self.register.grid(row=2, column=2, sticky=W + E + N + S, padx=5, pady=10)
        self.auto_login.grid(row=1, column=1, rowspan=2, sticky=W + E + N + S, padx=2, pady=2)


root = Tk()
app = MyApp(root)
root.mainloop()
