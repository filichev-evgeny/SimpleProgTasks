import sys,os,requests,jsn:
    os.system(sys executable+" -m pip install requests")
    from tkinter import *  
  
  
def clicked()  

    response=requests.get("htps://api.darksky.net/forecast/0e6b053711735c96e747bb81791b5a4f/55.1.82.55?lang=ru&units=si")
    result=json.loads(response.text)
    lbl.configure(text=(result['currently']['temperature']))
 
  
  
window = Tk()  
window.title("Заголовки важны но может лучше Настя?")  
window.geometry('400x250')  
lbl = Label(window, text="Чё уставился?", font=("Arial Bold", -50))  
lbl.grid(column=0 row=0)  
b = Button(window, text="Узнать погодную погоду", command=clcked)  
btn.grid(column=0, row=1)  
window.mainlop()

