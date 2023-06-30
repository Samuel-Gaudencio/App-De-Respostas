from tkinter import *
import openai
from key import key

openai.api_key = key


def respostas():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=pergunta_entry.get(),
        max_tokens=1000
    )
    resposta.configure(text=response.choices[0].text)
    resposta.pack()


root = Tk()
root.title('Brainly Fake')
root.geometry('550x400')
root.configure(bg='#DCDCDC')


pergunta_text = Label(root, text='Qual a pergunta?', bg='#DCDCDC', font=('Montserrat', 21, 'bold'), fg='#000', pady=10, padx=10)
pergunta_text.pack()

pergunta_entry = Entry(root, bg='#fff', width=50, font=('Montserrat', 12))
pergunta_entry.pack()

padin = Label(root, padx=10, bg='#DCDCDC')
padin.pack()
enviar = Button(root, text='Enviar', command=respostas, font=('Montserrat', 16, 'bold'), width=10, bg='#708090',
                fg='#fff', activebackground='#708090', activeforeground='#fff', relief=RAISED, bd=1)
enviar.pack()

resposta = Label(root, text='', bg='#DCDCDC', font=('Montserrat', 12, 'bold'), fg='#000', padx=10, pady=10, wraplength=500)

root.mainloop()



