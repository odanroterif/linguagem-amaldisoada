from tkinter import *

window = Tk()

window.title("ta ruim, com C# é melhor")
window.geometry("800x620")
window.resizable(False,False)
window ['bg'] = "#4B0082"
#--------------------------------
name = Label(window, text = "nome", font = "Arial35", bg= "#4B0082",fg="white")
name_field = Entry(window,font = "Arial 11 bold")
button = Button (window, text = "clique aqui se acha que C# é muito melhor")
name.pack(pady=50)
name_field.pack(pady=50)
button.pack()

window.mainloop()
