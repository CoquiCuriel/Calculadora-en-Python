from tkinter import *

root = Tk()
root.configure(background='#333333')
root.title('Calculadora')
root.geometry('386x168')

#configura el ancho de las columnas a todo el espacio disponible
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

#funciones

def press(num):
    equation.set(equation.get()+str(num))  

def equalpress():
    try:
        total = str(eval(equation.get()))
        #el calculo lo realiza la funcion 'eval'
        equation.set(total)
    except:
        equation.set('error')

def clear():
    equation.set('')


#barra de pantalla
equation = StringVar()
expression_entry = Entry(root, textvariable=equation)
expression_entry.grid(row=0, columnspan=4, sticky='nswe')
#columnspan indica que ocupe 4 columnas, sticky indica que ocupe todo el espacio disponible

#botones
btn7 = Button(root, text=' 7 ', fg='#fff', background='#666', command=lambda:press(7))
btn7.grid(row=1, column=0, sticky='nswe')

btn8 = Button(root, text=' 8 ', fg='#fff', background='#666', command=lambda:press(8))
btn8.grid(row=1, column=1, sticky='nswe')

btn9 = Button(root, text=' 9 ', fg='#fff', background='#666', command=lambda:press(9))
btn9.grid(row=1, column=2, sticky='nswe')

btndiv = Button(root, text=' / ', fg='#fff', background='#fe9727', command=lambda:press('/'))
btndiv.grid(row=1, column=3, sticky='nswe')

btn4 = Button(root, text=' 4 ', fg='#fff', background='#666', command=lambda:press(4))
btn4.grid(row=2, column=0, sticky='nswe')

btn5 = Button(root, text=' 5 ', fg='#fff', background='#666', command=lambda:press(5))
btn5.grid(row=2, column=1, sticky='nswe')

btn6 = Button(root, text=' 6 ', fg='#fff', background='#666', command=lambda:press(6))
btn6.grid(row=2, column=2, sticky='nswe')

btnmul = Button(root, text=' * ', fg='#fff', background='#fe9727', command=lambda:press('*'))
btnmul.grid(row=2, column=3, sticky='nswe')

btn1 = Button(root, text=' 1 ', fg='#fff', background='#666', command=lambda:press(1))
btn1.grid(row=3, column=0, sticky='nswe')

btn2 = Button(root, text=' 2 ', fg='#fff', background='#666', command=lambda:press(2))
btn2.grid(row=3, column=1, sticky='nswe')

btn3 = Button(root, text=' 3 ', fg='#fff', background='#666', command=lambda:press(3))
btn3.grid(row=3, column=2, sticky='nswe')

btnresta = Button(root, text=' - ', fg='#fff', background='#fe9727', command=lambda:press('-'))
btnresta.grid(row=3, column=3, sticky='nswe')

btn0 = Button(root, text=' 0 ', fg='#fff', background='#666', command=lambda:press(0))
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2)

decimal = Button(root, text=' . ', fg='#fff', background='#666', command=lambda:press('.'))
decimal.grid(row=4, column=2, sticky='nswe')

btnsuma = Button(root, text=' + ', fg='#fff', background='#fe9727', command=lambda:press('+'))
btnsuma.grid(row=4, column=3, sticky='nswe')

btnequal = Button(root, text=' = ', fg='#fff', background='#fe9727', command=equalpress)
btnequal.grid(row=5, column=3, sticky='nswe')

btnClear = Button(root, text=' clear ', fg='#fff', background='#999', command=clear)
btnClear.grid(row=5, column=2, sticky='nswe')

root.mainloop()