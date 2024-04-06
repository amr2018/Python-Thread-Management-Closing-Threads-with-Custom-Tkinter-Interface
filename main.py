import customtkinter as ctk
import threading


run = True

def task():
    while run:
        print('Task running...')
        if not run:
            print('Task closed')
            return
        
def start_task():
    global run
    run = True
    threading.Thread(target=task).start()


def close_task():
    global run
    run = False

root = ctk.CTk()
root.geometry('500x60')

ctk.CTkButton(root, text='start task', command=start_task).place(x = 20, y = 10)
ctk.CTkButton(root, text='close task', command=close_task).place(x = 220, y = 10)

root.mainloop()