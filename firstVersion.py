import tkinter
win = tkinter.Tk()
win.title("Mark's Memory Test")
win.geometry("1000x600")
str1 = "具体测试方法如下：" \
           "从4位数字开始，连续测10次，过关者，继续测试5位数，依次类推。" \
           "每次测试数字显示2秒后消失，请在5秒后在显示的输入框中输入记忆的数字，" \
         "5秒钟后进入下一个数字。"
def display():
    en.insert("insert", str1)

def newWin():
    win.destroy()
lb = tkinter.Label(win, text="Welcome to Number Memory Test", bg="orange", font=("Arial", 22))
lb.place(x=250, y=100)
en = tkinter.Text(win, width=30, height=6, font=("Arial", 20))
en.place(x=250,y=200)
bt1 = tkinter.Button(win, text="测试说明", bg="light green", font=("Arial", 28),command=display)
bt1.place(x=250, y=420)
bt = tkinter.Button(win, text="Start", bg="light green", font=("Arial", 28),command=newWin)
bt.place(x=590, y=420)

win.mainloop()