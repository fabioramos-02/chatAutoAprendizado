# -*- coding: utf-8 -*-

from tkinter import *
from extract import chatbot_response

def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        Chat.config(state=NORMAL)
        Chat.insert(END, "Você: " + msg + '\n\n')
        Chat.config(foreground="#000000", font=("Arial", 12))

        res = chatbot_response(msg)
        Chat.insert(END, "Bot: " + res + '\n\n')

        Chat.config(state=DISABLED)
        Chat.yview(END)

base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

Chat = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", )
Chat.config(state=DISABLED)

scrollbar = Scrollbar(base, command=Chat.yview)
Chat['yscrollcommand'] = scrollbar.set

SendButton = Button(base, font=("Verdana", 10, 'bold'), text="Enviar", width="12", height=5,
                    bd=0, bg="#666", activebackground="#333", fg='#ffffff',
                    command=send)

EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

scrollbar.place(x=376, y=6, height=386)
Chat.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=6, y=401, height=90, width=265)
SendButton.place(x=275, y=401, height=90)

base.mainloop()
