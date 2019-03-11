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
        self.register_frame = Frame(root, relief=GROOVE)
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
        # self.input_frame.forget()
        # self.buttons_frame.forget()
        # window
        nb = ttk.Notebook(root)
        self.main_frame = Frame(nb)
        nb.add(self.main_frame, text="Add")
        self.find_frame = Frame(nb)
        nb.add(self.find_frame, text="Find")
        self.change_frame = Frame(nb)
        nb.add(self.change_frame, text="Change")
        nb.pack()
        # Menu

        self.main_menu = Menu(root)
        self.menu = Menu(self.main_menu, tearoff=0)
        self.menu.add_command(label='Save')
        self.main_menu.add_cascade(label="File", menu=self.menu)
        self.main_menu.add_cascade(label="Help")
        self.main_menu.add_cascade(label="About")
        root.config(menu=self.main_menu)
        # Buttom frame
        self.main_button = Frame(self.main_frame, relief=GROOVE)
        self.add_lesson = Button(self.main_button, text="Add lessons", width=25, height=5,
                                 command=lambda *args: self.active("1"))
        self.add_work = Button(self.main_button, text="Add work", width=25, height=5,
                               command=lambda *args: self.active("2"))
        self.add_akce = Button(self.main_button, text="Add presentation", width=25, height=5,
                               command=lambda *args: self.active("3"))
        self.add_lesson.grid(row=1, column=1, padx=50, pady=30)
        self.add_work.grid(row=2, column=1, padx=50, pady=30)
        self.add_akce.grid(row=3, column=1, padx=50, pady=30)
        self.main_button.grid(row=1, column=1, rowspan=3)
        # lessom_frame
        self.lesson_frame = LabelFrame(self.main_frame, text='Lesson', relief=GROOVE)
        self.lesson_from = Label(self.lesson_frame, text="From:")
        self.lesson_from_value = ttk.Combobox(self.lesson_frame)
        self.lesson_from_value['values'] = ('15:00', '16:00', '17:00', '18:00')
        self.lesson_to = Label(self.lesson_frame, text="To:")
        self.lesson_to_value = ttk.Combobox(self.lesson_frame)
        self.lesson_to_value['values'] = ('18:00', '19:00')
        self.lesson_day = Label(self.lesson_frame, text="Day:")
        self.lesson_day_value = Spinbox(self.lesson_frame, from_=0, to=31)
        self.lesson_month = Label(self.lesson_frame, text="Month:")
        self.lesson_month_value = Spinbox(self.lesson_frame, from_=0, to=12)
        self.lesson_year = Label(self.lesson_frame, text="Year:")
        self.lesson_year_value = ttk.Combobox(self.lesson_frame)
        self.lesson_year_value['values'] = ('2018', '2019', '2020', '2021', '2022')
        self.lesson_year_value.current(1)
        self.lesson_car = Label(self.lesson_frame, text="Use personal car:")
        self.lesson_car_check = Checkbutton(self.lesson_frame)
        self.lesson_save_bt = Button(self.lesson_frame, text="Save", command=lambda *args: self.save("1"))
        self.lesson_delete_bt = Button(self.lesson_frame, text="Clear all", command=lambda *args: self.clear("1"))
        self.lesson_from.grid(row=1, column=1)
        self.lesson_from_value.grid(row=1, column=2)
        self.lesson_to.grid(row=2, column=1)
        self.lesson_to_value.grid(row=2, column=2)
        self.lesson_day.grid(row=1, column=3)
        self.lesson_day_value.grid(row=1, column=4)
        self.lesson_month.grid(row=2, column=3)
        self.lesson_month_value.grid(row=2, column=4)
        self.lesson_year.grid(row=1, column=5)
        self.lesson_year_value.grid(row=1, column=8)
        self.lesson_car.grid(row=2, column=5)
        self.lesson_car_check.grid(row=2, column=8, sticky=W)
        self.lesson_save_bt.grid(row=1, column=9)
        self.lesson_delete_bt.grid(row=2, column=9)
        self.lesson_frame.grid(row=1, column=2, sticky=W)
        for lessons in self.lesson_frame.winfo_children():
            lessons.configure(state='disable')
        # work_frame
        self.break_check = IntVar()
        self.work_frame = LabelFrame(self.main_frame, text="Work", relief=GROOVE)
        self.work_from = Label(self.work_frame, text="From:")
        self.work_from_value = ttk.Combobox(self.work_frame)
        self.work_from_value['values'] = ('15:00', '16:00', '17:00', '18:00')
        self.work_to = Label(self.work_frame, text="To:")
        self.work_to_value = ttk.Combobox(self.work_frame)
        self.work_to_value['values'] = ('18:00', '19:00')
        self.work_day = Label(self.work_frame, text="Day:")
        self.work_day_value = Spinbox(self.work_frame, from_=0, to=31)
        self.work_month = Label(self.work_frame, text="Month:")
        self.work_month_value = Spinbox(self.work_frame, from_=0, to=12)
        self.work_year = Label(self.work_frame, text="Year:")
        self.work_year_value = ttk.Combobox(self.work_frame)
        self.work_year_value['values'] = ('2018', '2019', '2020', '2021', '2022')
        self.work_year_value.current(1)
        self.work_break = Label(self.work_frame, text="Break time:")
        self.work_break_check = Checkbutton(self.work_frame, variable=self.break_check, command=self.active_check)
        self.work_break_value = Entry(self.work_frame, width=10, state='disable')
        self.work_break_note = Label(self.work_frame, text="(minutes)")
        self.work_save_bt = Button(self.work_frame, text="Save", command=lambda *args: self.save("2"))
        self.work_delete_bt = Button(self.work_frame, text="Clear all", command=lambda *args: self.clear("2"))
        self.work_from.grid(row=3, column=1)
        self.work_from_value.grid(row=3, column=2)
        self.work_to.grid(row=4, column=1)
        self.work_to_value.grid(row=4, column=2)
        self.work_day.grid(row=3, column=3)
        self.work_day_value.grid(row=3, column=4)
        self.work_month.grid(row=4, column=3)
        self.work_month_value.grid(row=4, column=4)
        self.work_year.grid(row=3, column=5)
        self.work_year_value.grid(row=3, column=8)
        self.work_break.grid(row=4, column=5)
        self.work_break_check.grid(row=4, column=8, sticky=W)
        self.work_break_value.grid(row=4, column=8)
        self.work_break_note.grid(row=4, column=8, sticky=E)
        self.work_save_bt.grid(row=3, column=9)
        self.work_delete_bt.grid(row=4, column=9)
        self.work_frame.grid(row=2, column=2, sticky=W)
        for lessons in self.work_frame.winfo_children():
            lessons.configure(state='disable')
        # presentation_frame
        self.presentation_frame = LabelFrame(self.main_frame, text='Presentation', relief=GROOVE)
        self.presentation_from = Label(self.presentation_frame, text="From:")
        self.presentation_from_value = ttk.Combobox(self.presentation_frame)
        self.presentation_from_value['values'] = ('07:00', '08:00', '09:00', '10:00')
        self.presentation_to = Label(self.presentation_frame, text="To:")
        self.presentation_to_value = ttk.Combobox(self.presentation_frame)
        self.presentation_to_value['values'] = ('18:00', '19:00', '20:00')
        self.presentation_day = Label(self.presentation_frame, text="Day:")
        self.presentation_day_value = Spinbox(self.presentation_frame, from_=0, to=31)
        self.presentation_month = Label(self.presentation_frame, text="Month:")
        self.presentation_month_value = Spinbox(self.presentation_frame, from_=0, to=12)
        self.presentation_year = Label(self.presentation_frame, text="Year:")
        self.presentation_year_value = ttk.Combobox(self.presentation_frame)
        self.presentation_year_value['values'] = ('2018', '2019', '2020', '2021', '2022')
        self.presentation_year_value.current(1)
        self.presentation_name = Label(self.presentation_frame, text="Title:")
        self.presentation_name_input = Entry(self.presentation_frame)
        self.presentation_save_bt = Button(self.presentation_frame, text="Save", command=lambda *args: self.save("3"))
        self.presentation_delete_bt = Button(self.presentation_frame, text="Clear all",
                                             command=lambda *args: self.clear("3"))
        self.presentation_from.grid(row=5, column=1)
        self.presentation_from_value.grid(row=5, column=2)
        self.presentation_to.grid(row=6, column=1)
        self.presentation_to_value.grid(row=6, column=2)
        self.presentation_day.grid(row=5, column=3)
        self.presentation_day_value.grid(row=5, column=4)
        self.presentation_month.grid(row=6, column=3)
        self.presentation_month_value.grid(row=6, column=4)
        self.presentation_year.grid(row=5, column=5)
        self.presentation_year_value.grid(row=5, column=8)
        self.presentation_name.grid(row=6, column=5)
        self.presentation_name_input.grid(row=6, column=8, sticky=W)
        self.presentation_save_bt.grid(row=5, column=9)
        self.presentation_delete_bt.grid(row=6, column=9)
        self.presentation_frame.grid(row=3, column=2, sticky=W)
        for presentation in self.presentation_frame.winfo_children():
            presentation.configure(state='disable')

        # self.input_frame = Frame(root, relief=GROOVE)
        # self.input_frame.pack(fill=BOTH, expand=1, padx=80, pady=10)
        # self.buttons_frame = Frame(root, relief=GROOVE)
        # self.buttons_frame.pack(fill=BOTH, expand=1, padx=80, pady=20)
        # self.username = Label(self.input_frame, text="Username:")
        # self.password = Label(self.input_frame, text="Password:")
        # self.username_input = Entry(self.input_frame, width=40)
        # self.password_input = Entry(self.input_frame, width=40)
        # self.login = Button(self.buttons_frame, text="Login", height=2, width=20, command=self.verification)
        # self.register = Button(self.buttons_frame, text="Register", height=2, width=20, command=self.registration)
        # self.auto_login = Checkbutton(self.buttons_frame, text="Auto login")
        # self.username.pack(padx=2, pady=2)
        # self.username_input.pack(padx=2, pady=2)
        # self.password.pack(padx=2, pady=2)
        # self.password_input.pack(padx=2, pady=2)
        # self.login.grid(row=1, column=2, sticky=W + E + N + S, padx=5, pady=10)
        # self.register.grid(row=2, column=2, sticky=W + E + N + S, padx=5, pady=10)
        # self.auto_login.grid(row=1, column=1, rowspan=2, sticky=W + E + N + S, padx=2, pady=2)


root = Tk()
app = MyApp(root)
root.mainloop()
