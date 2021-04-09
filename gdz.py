from bs4 import BeautifulSoup
import requests
from tkinter import Tk,Label,Button,Entry,Toplevel,PhotoImage
from PIL import Image, ImageTk
import os

class Algebra:
    def __init__(self, url, url_g):
        self.url = url
        self.url_g = url_g
        self.root = Tk()
        self.root['bg'] = '#808080'
        self.root.title('ГДЗ помощник')
        self.root.geometry('888x355')
        self.root.resizable(False,False)
        self.clicks = 0
        self.create_label_bg()

    def geometry(self):
        try:
            if self.clicks != 0:
                self.our_lable2.destroy()
            number = str(self.txt.get())
            alt_url = "ГДЗ по геометрии 9 класс  Мерзляк   упражнение - " + number + ", Решебник"
            url_get = self.url_g + number + '-nom/'
            response = requests.get(url_get)
            soup = BeautifulSoup(response.text, 'lxml')
            link_div = soup.html.find('img',alt=alt_url)
            result_url = link_div.attrs['src']
            result = 'https:'+result_url
            img = requests.get(result)
            img_option = open(number+'.jpg', 'wb')
            img_option.write(img.content)
            img_option.close()
            self.open_img_g()
        except:
            self.create_window()
    def create_window(self):
        self.window = Toplevel(self.root)
        self.window.geometry('310x90')
        self.window.title('ГДЗ помощник')
        self.window_lbl = Label(self.window, text='Номер не существует', bg='#c0c0c0', font=('Times New Roman', 20))
        self.window_lbl.grid(column=0, row=0, ipady=30, ipadx=30)
        self.window.mainloop()

    def open_img_g(self):
        number = str(self.txt.get())
        with Image.open(number+".jpg") as our_image2:
            our_image2 = our_image2.resize((642, 328), Image.ANTIALIAS)
            our_image2 = ImageTk.PhotoImage(our_image2)
            self.our_lable2 = Label(image=our_image2)
            self.our_lable2.image = our_image2
            self.our_lable2.place(x=239, y=7)
        os.remove(number+'.jpg')
        self.clicks = self.clicks+1

    def run(self):
        self.root.mainloop()
    
    def open_img(self):
        number = str(self.txt.get())
        with Image.open(number+".jpg") as our_image2:
            our_image2 = our_image2.resize((642, 328), Image.ANTIALIAS)
            our_image2 = ImageTk.PhotoImage(our_image2)
            self.our_lable2 = Label(image=our_image2)
            self.our_lable2.image = our_image2
            self.our_lable2.place(x=239, y=7) 
        os.remove(number+'.jpg')
        self.clicks = self.clicks+1
    def clear(self):
        self.our_lable2.destroy()

    def create_btn(self):
        self.btn2 = Button(self.root, text='Геометрия', font=('Times New Roman', 15), bd=2, bg='#EADEDB', activebackground='#F0EDE5', fg='black', relief='ridge', command=self.geometry)
        self.btn2.grid(column=1, row=3, padx=30, ipady=2, pady=20)
        self.btn3 = Button(self.root, text='Алгебра', font=('Times New Roman', 15),bd=2, bg='#EADEDB', activebackground='#F0EDE5', fg='black', relief='ridge', command=self.algebra)
        self.btn3.grid(column=1, row=4, padx=30, ipadx=11, ipady=2, pady=0)
        self.btn3 = Button(self.root, text='Очистить', font=('Times New Roman', 15),bd=2, bg='#EADEDB', activebackground='#F0EDE5', fg='black', relief='ridge', command=self.clear)
        self.btn3.grid(column=1, row=5, padx=30, ipadx=11, ipady=2, pady=50)

    def algebra(self):
        try:
            if self.clicks != 0:
                self.our_lable2.destroy()
            number = self.txt.get()
            alt = 'ГДЗ по алгебре 9 класс  Мерзляк   упражнение - '+number+', Решебник к учебнику 2019'
            url_get = self.url+number+'/'
            response = requests.get(url_get)
            soup = BeautifulSoup(response.text, 'lxml')
            link_div = soup.find('img', alt=alt)
            link_img = link_div.attrs['src']
            result = 'https:'+link_img
            img = requests.get(result)
            img_option = open(number+'.jpg', 'wb')
            img_option.write(img.content)
            img_option.close()
            self.open_img()
        except:
            self.create_window()

    def create_label_bg(self):
        self.bg_lbl_1 = Label(self.root, borderwidth=3, relief='solid', bg='#EADEDB', width=32, height=22)
        self.bg_lbl_1.place(x=3, y=4)
        self.bg_lbl_2 = Label(self.root, borderwidth=3, relief='solid', bg='#EADEDB', width=92, height=22)
        self.bg_lbl_2.place(x=236, y=4)

    def create_lbl(self):
        self.lbl = Label(self.root, text=('Где искать?'), font=("Times New Roman", 25), bd=3, fg='black', bg='#EADEDB')
        self.lbl.grid(column=1, row=0, stick='we', pady = 7, padx = 30)

    def create_entry(self):
        self.txt = Entry(self.root, width=20, font=('Times New Roman', 13))
        self.txt.grid(column=1, row=1, pady = 10,ipady=4)
        self.txt.focus()

def x(url, url_g):
    x = Algebra(url, url_g)
    x.create_lbl()
    x.create_entry()
    x.create_btn()
    x.run()

if __name__=='__main__':
    url_g = 'https://gdz.ru/class-9/geometria/merzlyak-polonskij/'
    url = 'https://gdz.ru/class-9/algebra/merzlyak/'
    x(url, url_g)