from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
import json
from tkinter import filedialog
from tkinter import messagebox
import shutil

window = Tk()

def upload_file():
    filename = filedialog.askopenfilename()
    destination_filename = r"C:\Users\Erika\Documents\UFSC\POO II\sistema_eleicoes\imports"
    try:
        shutil.copy(filename, destination_filename)
        messagebox.showinfo("Sucesso!", "Upload feito com sucesso!") 
    except():
        messagebox.showerror("Erro!", "Houve um erro ao fazer o upload do seu arquivo, tente novamente mais tarde") 
        

def open_popup_example_file():
    top= Toplevel(window)
    top.geometry("300x300")
    top.title("Exemplo de arquivo para importação")
    Label(top, text= "EXEMPLO DE ARQUIVO PARA IMPORTAÇÃO COM SUCESSO:", wraplength=290).place(x=10,y=80)
    database_json_filename = r'C:\Users\Erika\Documents\UFSC\POO II\sistema_eleicoes\json\exemplo_eleicoes.json'
    with open(database_json_filename, 'r') as inside:
        data = json.load(inside)
        Label(top, text=str(data), wraplength=290).place(x=10, y=120)
  
def plot(): 
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    y = [i**2 for i in range(101)] 
    plot1 = fig.add_subplot(111) 
    plot1.plot(y) 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
window.title('Sistema de Eleições') 
window.geometry("500x500") 
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     text = "Ver Gráfico")
plot_button.pack() 
import_button = Button(master = window,
                    bg='#31B404',
                    command=upload_file,
                     height = 2,  
                     text = "Importar Gráfico")
import_button.pack() 
example_graph_import_button = Button(master = window,
                    bg='#FFFF00',
                    command=open_popup_example_file,
                     height = 2,  
                     text = "Ver exemplo de arquivo para importar")
example_graph_import_button.pack() 

window.mainloop() 