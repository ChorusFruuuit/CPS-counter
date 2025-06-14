from tkinter import *
import time

APP_WIDTH = 400 # px
APP_HEIGHT = 200 # px

win = Tk()
# canvas = Canvas(win, width=APP_WIDTH, height=APP_HEIGHT, bg='#FFFFFF')

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_offset = screen_width / 2 - APP_WIDTH / 2
y_offset = screen_height / 2 - APP_HEIGHT / 2

windowGeometry = f'{APP_WIDTH}x{APP_HEIGHT}+{int(x_offset)}+{int(y_offset)}'
win.geometry(windowGeometry)

# line1 = canvas.create_line(0, APP_HEIGHT / 2, APP_WIDTH, APP_HEIGHT / 2, fill='#000000')
# line2 = canvas.create_line(APP_WIDTH / 2, 0, APP_WIDTH / 2, APP_HEIGHT, fill='#000000')

clicks = []
disp = Label(win, text='CPS: 0')

disp.pack()
win.update()
disp.place(x = APP_WIDTH / 2 - disp.winfo_width() / 2, y = APP_HEIGHT / 2 - disp.winfo_height() / 2)

def upadte_display(display: Label):

    while True:
        if len(clicks) == 0:
            break
        if time.time() - clicks[0] >= 1:
            del clicks[0]
        else:
            break

    cps = len(clicks)
    win.update()
    disp.configure(text=f'CPS: {cps}')
    w = display.winfo_width()
    h = display.winfo_height()
    display.place(x = APP_WIDTH / 2 - w / 2, y = APP_HEIGHT / 2 - h / 2)

    if cps > 0:
        win.after(10, lambda: upadte_display(disp))

def onClick(event=None):
    prev_cps = len(clicks)
    clicks.append(time.time())
    if prev_cps == 0:
        upadte_display(disp)

win.bind('<Button-1>', onClick)

if __name__ == '__main__':
    win.resizable(0, 0)
    win.title('CPS counter')
    # canvas.pack()
    win.mainloop()