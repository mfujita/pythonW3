import PySimpleGUI as sg
import matplotlib.pyplot as plt

layout=[
    [sg.Text('x1 ', font=('Arial', 20)), sg.InputText(k='-x1-')],
    [sg.Text('x2 ', font=('Arial', 20)), sg.InputText(k='-x2-')],
    [sg.Button('Plot', font=('Arial', 20))]
]
window=sg.Window('Plotter', layout)
X=[]
Y=[]

while True:
    event, values=window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Plot':
        xinicial=int(values['-x1-'])
        xFinal=int(values['-x2-'])
        x = xinicial
        while x <= xFinal:
            X.append(x)
            Y.append(0.25*x**3-0.3*x**2+0.8*x-10)
            x+=1
        plt.plot(X,Y)
        plt.show()
        X.clear()
        Y.clear()
window.close()