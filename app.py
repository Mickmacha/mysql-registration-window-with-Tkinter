# -*- coding: utf-8 -*-
from tkinter.messagebox import *
import mysql.connector as mysql
import tkinter as tk

class Login():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Login Window")
        self.create_elements()
        self.root.mainloop()
        
    def create_elements(self):
        self.username = tk.Label(self.root, text="Username:", font=("Verdana", 14, "bold"))
        self.username.place(x=50, y=50)
        
        self.entry_username = tk.Entry(self.root, font=("Verdana", 14, "bold"))
        self.entry_username.place(x=160, y=50)
        
        self.password = tk.Label(self.root, text="Password:", font=("Verdana", 14, "bold"))
        self.password.place(x=50, y=90)
        
        self.entry_password = tk.Entry(self.root, font=("Verdana", 14, "bold"))
        self.entry_password.place(x=160, y=90)
        
        self.login_btn = tk.Button(self.root, text="Login", height=2, width=10, command=self.login_user)
        self.login_btn.place(x=50, y=160)
       
        self.new_user = tk.Label(self.root, text="New User?", font=("Verdana", 12, "bold"))
        self.new_user.place(x=150, y=140)
        
        self.register_btn = tk.Button(self.root, text="Sign Up", height=2, width=10, command=self.destroy_login)
        self.register_btn.place(x=150, y=160)
        
    def destroy_login(self):
        self.root.destroy()
        register = Register()
    
    def login_user(self):
        username = self.entry_username.get()
        userpassword= self.entry_password.get()
        
        if(username == "" or userpassword == ""):
            showinfo("OOPS!", "Your information cant be empty!")
            return
        mydb = mysql.connect(host ="localhost", 
                             user="root",
                             password="",
                             database = "tk_users"
                             )
        mycursor = mydb.cursor()
        sql=" select user, pass from user where user=%s and pass=%s"
        val = (username, userpassword)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        self.entry_username.delete(0,tk.END)
        self.entry_password.delete(0, tk.END)
        if result:
            showinfo("Success", "Youre logged in")
        else:
            showinfo("Failed", "No such user")

class Register():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Registration Window")
        self.create_elements()
        self.root.mainloop()
    def create_elements(self):
        self.username = tk.Label(self.root, text="Username:", font=("Verdana", 14, "bold"))
        self.username.place(x=50, y=50)
        
        self.entry_username = tk.Entry(self.root, font=("Verdana", 14, "bold"))
        self.entry_username.place(x=160, y=50)
        
        self.password = tk.Label(self.root, text="Password:", font=("Verdana", 14, "bold"))
        self.password.place(x=50, y=90)
        
        self.entry_password = tk.Entry(self.root, font=("Verdana", 14, "bold"))
        self.entry_password.place(x=160, y=90)
        
        self.name = tk.Label(self.root, text="Name:", font=("Verdana", 14, "bold"))
        self.name.place(x=50, y=130)
        
        self.entry_name = tk.Entry(self.root, font=("Verdana", 14, "bold"))
        self.entry_name.place(x=160, y=130)
        
        self.register_btn = tk.Button(self.root, text="Sign Up", height=2, width=10, command=self.register_user)
        self.register_btn.place(x=50, y=180)
        
        self.existing_user = tk.Label(self.root, text="Existing User?", font=("Verdana", 12, "bold"))
        self.existing_user.place(x=150, y=160)
        
        self.login_btn = tk.Button(self.root, text="Login", height=2, width=10, command=self.destroy_register)
        self.login_btn.place(x=150, y=180)
       
    def destroy_register(self):
        self.root.destroy()
        
    def register_user(self):
        username = self.entry_username.get()
        userpassword= self.entry_password.get()
        name = self.entry_name.get()
        
        if(username == "" or userpassword == ""):
            showinfo("OOPS!", "Your information cant be empty!")
            return
        mydb = mysql.connect(host ="localhost", 
                             user="root",
                             password="",
                             database = "tk_users"
                             )
        mycursor = mydb.cursor()
        mycursor.execute("select count(*) from user")
        result = mycursor.fetchone()
        old_count = result[0]
        
        sql="INSERT INTO user (user, pass, name) VALUE(%s, %s, %s)"
        val = (username, userpassword, name)
        mycursor.execute(sql, val)
        mydb.commit()
        
        mycursor.execute("select count(*) from user")
        result = mycursor.fetchone()
        new_count = result[0]
        
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
                
        if(old_count+1 == new_count):
            showinfo("Success", "Info saved successfully")
        else:
            showinfo("Failed", "info not saved")
            
if __name__ == '__main__':
    login = Login()
            
