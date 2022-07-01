from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.image import Image
#from kivymd.uix.textfield import MDTextFieldRound
from kivy.uix.button import Button
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from datetime import datetime
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition, ScreenManager
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.button import MDRectangleFlatIconButton
#from kivymd.uix.textfield import MDTextFieldRect
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.input.providers.mouse import MouseMotionEvent
from kivymd.uix.menu import MDDropdownMenu

#####################  SQL imports  ################################
import sqlite3
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#os.remove('trainer.db')
engine = create_engine('sqlite:///trainer.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
#################################  SQL Shit ####################################
# [{email: "nabil", password: "1", name: "mns"} ]

class User(Base):
    __tablename__ = "user"
    email = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    name = Column(String)
    age = Column(String)
    weight = Column(String)
    gender = Column(String)
    jp = Column(String)
    
    def __init__(self, email, password, name='', age='',weight='', gender='', jp=''):
        self.email = email
        self.password = password
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
        self.jp = jp

Base.metadata.create_all(engine)

############################################################################



##############################################################################


logged_in_user = None

class LoginScreen(Screen):
    

    def loginBtn(self):
        email = ObjectProperty(None)
        password = ObjectProperty(None)
        email_input = self.email.text
        password_input = self.password.text
        print(email_input)
        print(password_input)
        valid = session.query(User).filter(User.email == email_input, User.password == password_input).count()
        if valid == 0 or (email_input == '' or password_input == ''):
        #if valid == 0:
            print("Invalid email or password")
        else:
            result = session.query(User).filter(User.email == email_input, User.password == password_input)
            for user in result:
                print(f"Welcome {user.name}!")
                global logged_in_user
                logged_in_user = user.email       
                self.manager.current="main"

        #self.manager.current="main"
        #result = session.query(User).filter(User.email == email_input).all()
        
class SignUpScreen(Screen):
    def registerBtn(self):
        email_input = self.email.text
        password_input = self.password.text
        password_confirmation_input = self.password_confirmation.text
        username_input = self.username.text
        age_input = self.age.text
        weight_input = self.weight.text
        gender_input = self.gender.text
        jp_input = self.jp.text
        
        if password_confirmation_input != password_input:
            print("Password unmatch!!")
        else:
            data = User(email_input, password_input, username_input, age_input,weight_input, gender_input, jp_input)
            session.add(data)
            session.commit()
class MainScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass
class GraphScreen(Screen):
    pass

class NotificationScreen(Screen):
    pass

class UserProfileScreen(Screen):
    
    # we need to get the user value from the database
    # current_user= session.query(User).filter()

    

    def on_pre_enter(self):
        self.callback()

    def callback(self):
        global logged_in_user
        result = session.query(User).filter(User.email == logged_in_user)
        for user in result:
            self.username_label.text = user.name
            self.age_label.text = user.age
            self.weight_label.text=user.weight
            self.gender_label.text=user.gender
            self.jp_label.text = user.jp


        

class EditUserProfileScreen(Screen):

    def on_pre_enter(self):
        self.callback()

    def callback(self):
        global logged_in_user
        result = session.query(User).filter(User.email == logged_in_user)
        for user in result:
            self.chg_username.text = user.name
            self.chg_age.text = user.age
            self.chg_weight.text=user.weight
            self.chg_gender.text = user.gender
            self.chg_jp.text = user.jp
    
    def savechanges(self):
        username_input = self.chg_username.text
        age_input = self.chg_age.text
        weight_input = self.chg_weight.text
        gender_input = self.chg_gender.text
        jp_input = self.chg_jp.text
        session.update(User.email == logged_in_user).values()

        



sm=ScreenManager()
#sm.add_widget(MDScreen(name="md"))
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(SignUpScreen(name="signup"))
sm.add_widget(MainScreen(name="main"))
sm.add_widget(SettingsScreen(name="settings"))
sm.add_widget(GraphScreen(name="graph"))
sm.add_widget(NotificationScreen(name="notify"))
sm.add_widget(UserProfileScreen(name="userprofile"))
sm.add_widget(EditUserProfileScreen(name="edituserprofile"))
#class ScreenManager(ScreenManager):
 #   pass


#class ProfileCard(FloatLayout, FakeRectangleElevationBehaviour):
 #   pass

#class MovementAnalysis(ProfileCard):
 #   pass



Window.size = (320,550)

#GUI= Builder.load_file("main.kv") #Make Sure this is after all clas definitions!

class MainApp(MDApp):

    def build(self):
        #builder = Builder.load_file("main.kv")
        #return #builder
        pass


if __name__ == '__main__':
    MainApp().run()


