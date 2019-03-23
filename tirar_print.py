import pyautogui
from Tkinter import *
import os
import pytesseract as pyt
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.imagem=pyautogui.screenshot()
        # dvd self.imagem_legenda=self.imagem.crop((214,720,752,831))
        #netflix self.imagem_legenda=self.imagem.crop((248,730,711,796))
        self.imagem_legenda=self.imagem.crop((248,730,711,796))
        self.legenda=Entry(self)
        self.legenda.insert(0,self.pega_legenda())
        self.legenda.pack()
        self.pack()
        self.nome=Entry(self)
        self.nome.pack()
        self.sair=Button(self)
        self.sair["text"]="Sair"
        self.sair["command"]=self.ss
        self.sair.pack()
    def ss(self):
        
        imagem_cortada=self.imagem.crop((67,369,893,796))
        #netflix imagem_cortada=imagem.crop((67,369,893,796))
        #dvd imagem_cortada=imagem.crop((85,200,840,842))
        diretorio='/home/lucas/Pictures/baralho_ingles/'+self.nome.get()
        os.mkdir(diretorio)
        imagem_cortada.save(diretorio+"/imagem.jpg",'jpeg')
        self.imagem_legenda.save(diretorio+"/legenda.jpg",'jpeg')
        self.quit()
    def pega_legenda(self):
        return pyt.image_to_string(self.imagem_legenda)

        
	
root=Tk()
app=App(root)
app.mainloop()
root.destroy()
