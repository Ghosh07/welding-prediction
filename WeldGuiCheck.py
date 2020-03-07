#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


root=Tk()
class main:
	def __init__(self,master):
		self.define(master)

	def calculate(self):
		num1 = int(self.entry1.get())
		num2=int(self.entry2.get())
		num3=int(self.entry3.get())
		num4=int(self.entry4.get())
		data=pd.read_csv('weld_Quality.csv')
		data.head()
		data=data.dropna()
		data.head()
		data.info()
		data = data.rename(columns = {"Dataset": "Weld_Quality"}) 
		data.head()
		df=data.replace([1, 2 ,3], ['Lack of Fusion', 'Good Weld', 'Burn Through'])
		sns.countplot(x=df['Weld_Quality'])
		sns.countplot(y=df['Volts'])
		sns.countplot(x=df['Weld_Quality'], hue=df['Amps'])
		sns.jointplot("Amps", "Volts", data=data, kind="reg")
		sns.jointplot("Speed (mm/s)", "Heat Input (kJ/mm)", data=data, kind="reg")
		sns.jointplot("Speed (mm/s)", "Volts", data=data, kind="reg")
		data.info()
		data.head()
		data.Weld_Quality = data.Weld_Quality.replace({"Lack of Fusion": "1", "Good Weld": "2","Burn Through": "3"})
		data.head()
		x=data.drop(['Weld_Quality','SL. NO'],axis='columns')
		x.head()
		y = data['Weld_Quality']
		y.head()
		train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=.25,random_state=7)
		knn=neighbors.KNeighborsClassifier(n_neighbors=2)
		knn.fit(x,y)  
		y_pred_KNN = knn.predict(test_x)
		a = accuracy_score(test_y,y_pred_KNN)
		a
		pred=knn.predict([[num1,num2,num3,num4]])
		pred
		self.output_field.insert(0, pred)



	def define(self,master):
		self.master=master
		self.label1=Label(master,text="Amps")
		self.label2=Label(master,text="Volts")
		self.label3=Label(master,text="Speed (mm/s)")
		self.label4=Label(master,text="Heat Input (kJ/mm)")
		self.entry1=Entry(master)
		self.entry2=Entry(master)
		self.entry3=Entry(master)
		self.entry4=Entry(master)
		self.button=Button(root,text='Go',fg='Red',command=self.calculate)
		self.output=Label(master,text='Weld Quality')
		self.output_field=Entry(master)
		self.output.grid(row=1,column=4)
		self.output_field.grid(row=1,column=5)
		self.label1.grid(row=0,column=0)
		self.entry1.grid(row=0,column=1)
		self.label2.grid(row=0,column=2)
		self.entry2.grid(row=0,column=3)
		self.label3.grid(row=0,column=4)
		self.entry3.grid(row=0,column=5)
		self.label4.grid(row=0,column=6)
		self.entry4.grid(row=0,column=7)
		self.button.grid(row=0,column=8)
main(root)
root.title("Welding Check")
root.geometry("1600x700")
root.mainloop()


# In[ ]:





# In[ ]:




