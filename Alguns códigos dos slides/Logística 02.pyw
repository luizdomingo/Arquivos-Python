def salvar_dados():
    f = open('encomenda.txt', 'a')
    f.write('Destino: ')
    f.write(f'{destino.get()}\n')
    f.write('Descrição: ')
    f.write(f'{descrição.get()}\n')
    f.write('Endereço: ')
    f.write(f'{endereço.get("1.0", END)}\n')
    destino.delete(0, END)
    descrição.delete(0, END)
    endereço.delete('1.0', END)
    f.close()


from tkinter import *

app = Tk()
app.title('Head-Ex Logística e Transportes')
Label(app, text="Destino: ").pack()
Radiobutton(app, text='Cambridge, MA').pack()
Radiobutton(app, text='Cambridge, UK').pack()
Radiobutton(app, text='Seattle, WA').pack()

Label(app, text="Descrição: ").pack()
descrição = Entry(app)
descrição.pack()
Label(app, text="Endereço: ").pack()
endereço = Text(app)
endereço.pack()
Button(app, text="Salvar", command=salvar_dados).pack()
app.mainloop()
