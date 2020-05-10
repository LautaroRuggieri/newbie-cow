#last version: 10 may 2020 (aprox. 2.5 months into programming)
#author: Lautaro Ruggieri (https://github.com/LautaroRuggieri)
#desc: bored, quarantined cow presents a basic mouse activity responder:
    #1-it draws a circle each time you left click, alternatig between red and blue color.
    #2-it draws a text if you double left click.
    #3-SHIFT + left click will turn on/off the 'tail mode'. tail mode draws a text after the mouse has 
    #  escaped a radius r>15 from where it was turned on or from the last message displayed.
    #4-the window notifies the user if tail mode has been activated or deactivated.
    #5-it detects if your mouse is gone from the canvas and politely asks you to come back.
    
    #it also a some 'hidden' feature in the form of commentaries, which makes the title of the
    # screen to display the mouse coords. Feel free to erase the '#' in the source code
    # and to chose the feature that takes place when you run it.
    


import tkinter as tk
import math

class Aplicacion:

    
    def __init__(self):
        #creo la ventana y un self.color para el metodo presion_mouse:
        self.ventana1=tk.Tk()
        self.color = 0
        
        #creo el canvas:
        self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background='black')
        self.canvas1.grid(column=0, row=2)
        
        #creo los eventos y el modulo que va a disparar cada evento:
        #self.canvas1.bind('<Motion>',          self.mover_mouse)
        self.canvas1.bind('<Button-1>',        self.presion_mouse       )
        self.canvas1.bind('<Enter>',           self.presencia_mouse     )
        self.canvas1.bind('<Leave>',           self.ausencia_mouse      )
        self.canvas1.bind('<Double-Button-1>', self.doblepresion_mouse  )
        self.canvas1.bind('<Shift Button-1>',  self.prender_mensaje_cola)
        self.canvas1.bind('<Motion>',          self.dibujar_mensaje_cola)
        self.mensaje_cola=False
        
        self.ventana1.mainloop()
        
    #def mover_mouse(self, evento):
    #   self.ventana1.title(str(evento.x) + ';' + str(evento.y))
    
    def presion_mouse(self, evento):   
        self.color = self.color + 1
        if self.color%2==0:
            self.ultimocirculo=self.canvas1.create_oval(evento.x-5,evento.y-5 , evento.x+5,evento.y+5, fill='red')
        else:
            self.ultimocirculo=self.canvas1.create_oval(evento.x-5,evento.y-5 , evento.x+5,evento.y+5, fill='blue')
            
        if self.color==10:
            self.color=0
    
    def presencia_mouse(self, evento):
        self.ventana1.title('Hey!')
    
    def ausencia_mouse(self, evento):
        self.ventana1.title('Come back, now.')
    
    def doblepresion_mouse(self, evento):
        self.canvas1.create_text(evento.x,evento.y , text='DOUBLE CLICK XD', fill='blue', font='Arial')
        self.canvas1.delete(self.ultimocirculo)
    
    def prender_mensaje_cola(self, evento):   #RECORDAR QUE SE ACTIVA Y DESACTIVA CON SHIFT+CLIC IZQ:   
        if not self.mensaje_cola:
            self.mensaje_cola=True
            self.ventana1.title('Tail mode ON')
            self.coordx=evento.x
            self.coordy=evento.y
            self.canvas1.create_text(evento.x,evento.y , text='TAIL MODE ACTIVATED!', fill='yellow')
        else:
            self.mensaje_cola=False
            self.ventana1.title('Tail mode OFF')
        
        
    def dibujar_mensaje_cola(self, evento):
        if self.mensaje_cola:
            r=math.sqrt((self.coordx-evento.x)**2 + (self.coordy-evento.y)**2)
            if r>15:
                self.canvas1.create_text(evento.x,evento.y , text='nice tail', fill='yellow')
                self.coordx=evento.x
                self.coordy=evento.y
                
            
            
    
app1=Aplicacion()
