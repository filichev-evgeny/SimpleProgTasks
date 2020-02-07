from tkinter import   
offset=0
i=0
j=0
def HELLO:
    global i,j,offseti
    label=Label(window,text="ПРИВЕТ" font=('Arial Bold',i+j+offseti))
    label.grid(row=i,column=j)
    i==1
    j+=1
    if j>10
        j=0
        i=offseti+1
        offseti+=1
    window.after(50,HELLO)
    window = Tk()  
    window.attributes('-fullscreen', True)
    window.title("Кто читает заголовки тот няша")  
    window.after-idle(HELLO)
    window.mainloop()