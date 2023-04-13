import webbrowser
from kivy.app import App
from kivymd.uix.chip import MDChip
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,  Screen, SlideTransition
from kivy.properties import ObjectProperty,ListProperty,BooleanProperty,StringProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior #
from kivy.uix.recyclegridlayout import RecycleGridLayout #
from kivy.uix.behaviors import FocusBehavior #
from kivy.uix.recycleview.layout import LayoutSelectionBehavior #
import sqlite3
from kivymd.uix.screen import Screen
from kivy.config import Config
Config.set('graphics', 'resizable', True)
import os
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.filemanager import MDFileManager
import urllib



class filemanager(Screen):
    pass

class SecondWindow(Screen):
    def welcome(self):
        pass

class FirstWindow(Screen):
    email = ObjectProperty()
    password = ObjectProperty()

    """def login(self, email, password):
        app = App.get_running_app(MDApp)

        app.username = email
        app.password = password
        if email == "hello" and password == "1234":
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'

            app.config.read(app.get_application_config())
            app.config.write()"""

    def login(self):
        con = sqlite3.connect("login.db")
        cur = con.cursor()
        cur.execute("""INSERT INTO data_value(email,password) VALUES(?,?))""",(self.email.text, self.password.text)
                    )
        con.commit()
        con.close()
    def submit(self,email,password):

        con = sqlite3.connect("login.db")
        cur = con.cursor()
        #statement = f"SELECT * FROM customer WHERE email ='{email}' AND password='{password}';"

        cur.execute("select email,password from data_value where email=(?) and password = (?)",(email,password))
        exists = cur.fetchall()
        if exists:
            sm.current = "screen_two"
        else:
            print("false")


class ThirdWindow(Screen):
    num = ObjectProperty()
    sch = ObjectProperty()
    ph = ObjectProperty()
    email = ObjectProperty()
    addr = ObjectProperty()
    amount = ObjectProperty()
    def get_h(self):
        pass
    def submit(self):
        con = sqlite3.connect('first_db.db')
        cur = con.cursor()
        cur.execute("""INSERT INTO customer(num,sch,ph,email,addr,amount)  VALUES(?,?,?,?,?,?)""",(self.num.text, self.sch.text, self.ph.text, self.email.text, self.addr.text,self.amount.text)
                    )
        con.commit()
        con.close()

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)



class  FourthWindow(Screen):

   data_items = ListProperty([])
   data_text = ListProperty([])
   sch =ObjectProperty()

   def __init__(self,**kwargs,):
       super(FourthWindow, self).__init__(**kwargs)
       self.get_use()

   def search_data(self):
       con = sqlite3.connect('first_db.db')
       cur = con.cursor()
       cur.execute("SELECT  FROM  customer", (self.sch))
       row = cur.fetchall()

       for r in row:
           print(r)

   def get_use(self):
        con = sqlite3.connect('first_db.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM customer ")
        row = cur.fetchall()

        for r in row:
            for j in r:
                self.data_items.append(j)

class FifthWindow(Screen):
        pass


class WindowManager(Screen):
    pass


Kv = Builder.load_file("login.kv")

sm = ScreenManager()

sm.add_widget(FirstWindow(name="screen_one"))

sm.add_widget(SecondWindow(name="screen_two"))

sm.add_widget(ThirdWindow(name="screen_three"))

sm.add_widget(FourthWindow(name ="screen_four"))

sm.add_widget(FifthWindow(name = "screen_five"))


class Mainapp(MDApp):
    email = StringProperty(None)
    password = StringProperty(None)
    con = sqlite3.connect("")
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        con = sqlite3.connect('first_db.db')
        c = con.cursor()
        #create A table
        c.execute("""CREATE TABLE if not exists customer(
              num text,
              sch text,
              ph text,
              email text,
              addr  text,
              amount text)
        """)
        con.commit()
        con.close()

        #email validation from method

        con = sqlite3.connect("login.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE if not exists data_value(
                email text,
                password text)
        """)
        con.commit()
        con.close()

        return sm



if __name__ == "__main__":

    Mainapp().run()
