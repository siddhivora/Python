import re

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import itertools
import pymysql
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.garden import Graph, MeshLinePlot
from kivy.animation import Animation

db = pymysql.connect(host="localhost",
                    user = "user1",
                    passwd = "user1",
                    db = "db1")
mycursor = db.cursor()

radio_value = ''

from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class CustomPopup(Popup):
    pass
#make general funtion to scan integer from string
#class scan_string(self, value):
#    int(re.search(r'\d+', value).group())

#class Ball(Widget):
#    anim = Animation(x=100, y=100)
#    anim.start()
#    pass
#class AnimWid(Widget):
#    pass
class PatientScreen(Screen):    
    global radio_value
    
    male = ObjectProperty(True)
    female = ObjectProperty(False)
    mixed = ObjectProperty(False)
    
    def insert_radio_value(self):
        if self.ids["male1"].active:
            radio_value = 'Male'            
        elif self.ids["female1"].active:
            radio_value = 'Female'
        elif self.ids["mixed1"].active:
            radio_value = 'Other'
        
    def patient_ID(self):
        
        mycursor.execute("SELECT * FROM patient_info")
        mycursor.fetchall()
        count = mycursor.rowcount       
        value = str(count + 1)  
        return value
    
    def inputNumber(self):
        while True:
            try:
                userInput = int(weight1.value)       
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                return userInput 
                break 
    
    def search_db(self):    
        self.ids["male1"].active = False
        self.ids["female1"].active = False
        self.ids["mixed1"].active = False
        val = self.ids["fname"].text
        #sql = "SELECT height, weight, gender, age, smoker FROM patient_info WHERE name ='%s'"%(val)
        sql0 = "SELECT id FROM patient_info WHERE name ='%s'"%(val)
        sql = "SELECT height FROM patient_info WHERE name ='%s'"%(val)
        sql1 = "SELECT weight FROM patient_info WHERE name ='%s'"%(val)
        sql2 = "SELECT gender FROM patient_info WHERE name ='%s'"%(val)
        sql3 = "SELECT age FROM patient_info WHERE name ='%s'"%(val)
        sql4 = "SELECT smoker FROM patient_info WHERE name ='%s'"%(val)
        
        mycursor.execute(sql0)
        sql0 = mycursor.fetchall()
        sql0 = str(sql0)
        sql0 = (re.search(r'\d+', sql0).group())
        self.ids["pid"].text = sql0
        
        mycursor.execute(sql)
        sql = mycursor.fetchall()
        sql = str(sql)
        sql = (re.search(r'\d+', sql).group())
        self.ids["height"].text = sql
        #sql = ( ", ".join(sql) )
        #sql1 = sql[1]
        #sql = int(re.search(r'\d+', sql).group())
        mycursor.execute(sql1)
        sql1 = mycursor.fetchall()
        sql1 = str(sql1)
        sql1 = (re.search(r'\d+', sql1).group())
        self.ids["weight"].text = sql1
        
        mycursor.execute(sql2)
        sql2 = mycursor.fetchall()
        sql2 = str(sql2)
        sql2 = (re.search(r'\w+', sql2).group())        
        if sql2 == 'Male':
            self.ids["male1"].active = True
        elif sql2 == 'Female':
            self.ids["female1"].active = True
        elif sql2 == 'Other':
            self.ids["mixed1"].active = True
        
        mycursor.execute(sql3)
        sql3 = mycursor.fetchall()
        sql3 = str(sql3)
        sql3 = (re.search(r'\d+', sql3).group())
        self.ids["dob"].text = sql3
        
        mycursor.execute(sql4)
        sql4 = mycursor.fetchall()
        sql4 = str(sql4)
        sql4 = (re.search(r'\w+', sql4).group())
        self.ids["smoker"].text = sql4
        
#        print (sql,sql1,sql2,sql3,sql4)
        
        
       
        
      
    def storevalue(self):
        if self.ids["male1"].active:
            radio_value = 'Male'            
        elif self.ids["female1"].active:
            radio_value = 'Female'
        elif self.ids["mixed1"].active:
            radio_value = 'Other'
        sql = "INSERT INTO patient_info (name, height, weight, gender, age, smoker) VALUE(%s, %s, %s, %s, %s, %s)"
        val = (self.ids["fname"].text, self.ids["height"].text, self.ids["weight"].text, radio_value, self.ids["dob"].text, self.ids["smoker"].text)
        mycursor.execute(sql, val)        
        db.commit()
            
    def open_popup(self):        
        popup_1 = CustomPopup()
        val = ('','','','','','')
        (self.ids["fname"].text, self.ids["height"].text, self.ids["weight"].text, radio_value, self.ids["dob"].text, self.ids["smoker"].text) = val        
        popup_1.open()
    
    def new_patient(self):
        mycursor.execute("SELECT * FROM patient_info")
        mycursor.fetchall()
        count = mycursor.rowcount
        value = str(count + 1)
        self.ids["pid"].text = value
        val = ('','','','','')
        (self.ids["fname"].text, self.ids["height"].text, self.ids["weight"].text, self.ids["dob"].text, self.ids["smoker"].text) = val      
        self.ids["male1"].active = False
        self.ids["female1"].active = False
        self.ids["mixed1"].active = False
        
class SpirometryScreen(Screen):
    def fev1_test(self):
        value = 0
        return str(value)
    
    def fev1_predict(self):
        value = 0
        return str(value)
    
    def fvc_test(self):
        value = 0
        return str(value)
    
    def fvc_predict(self):
        value = 0
        return str(value)
    
    def fev1_fvc_test(self):
        value = 0
        return str(value)
    
    def fev1_fvc_predict(self):
        value = 0
        return str(value)
    
    def diagnosis(self):
        value = self.ids["fev1_fvc"].text
#        if value < 0.7:
#            self.ids["dresult"].text = 'COPD is diagnosed.'
#        elif value >= 0.7 and value < 1:
#            self.ids["dresult"].text = 'Congrachulations!! You are healthy.'
#        else:
#            self.ids["dresult"].text = 'There is something wrong. Please re-test.'
    

class ClassificationScreen(Screen):
#    value = 0
#    if value = 0:
#        self.id["bal_1"]
    pass

class TreatmentScreen(Screen):
    pass

class TutorialScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(PatientScreen(name='patient'))
sm.add_widget(SpirometryScreen(name='spirometry'))
sm.add_widget(ClassificationScreen(name='classification'))
sm.add_widget(TreatmentScreen(name='treatment'))
sm.add_widget(TutorialScreen(name='tutorial'))

print mycursor.rowcount

class MyApp(App):
    def build(self):
        return sm

MyApp().run()