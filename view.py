import tkinter as tk

class View:
    def __init__(self):
        self.listener = None
        self.window = tk.Tk() # Instanz des Hauptfensters
        self.window.resizable(False, False)
        self.window.title("Celsius/Fahrenheit Umrechnung")

        self.text_c = tk.StringVar() # 2 stringvariablen werden erzeugt, werden unten an die Labels gebunden
        self.text_f = tk.StringVar()

        self.heading = tk.Label(self.window, text="Celsius Fahrenheit Umrechnung", font="Arial 11 bold") #Headerzeile (Überschrift wird gesetzt und über 2 Spalten langgezogen)
        self.heading.grid(row=0, column=0, columnspan=2)

        self.entry = tk.Scale(self.window, command = lambda event: self.change(), from_=-273.15, to =400, orient = tk.HORIZONTAL)
        self.entry.grid(row=1, column = 0, columnspan=2, sticky = tk.W + tk.E)

        self.celsius = tk.Label(self.window, textvariable = self.text_c, font = "Helvetica 9 bold")     #beachte Eigenschaft textvariable
        self.celsius.grid(row =2, column = 0)

        self.fahrenheit = tk.Label(self.window, textvariable = self.text_f, font="Helvetica 9 bold")
        self.fahrenheit.grid(row=2, column=1)

    def set_listener(self, listener):
        self.listener = listener

    def change(self):
        if self.listener:
            self.listener(self.value)

    @property
    def value(self):
        return self.entry.get() # wir lesen den wert des scales (das wir entry benannt haben) aus

    def set_values(self, celsius, fahrenheit):
        self.text_c.set("{:.2f}° F ist \n {}° C".format(self.value, celsius)) # man bekommt den Wert und formatiert ihn
        self.text_f.set("{:.2f}° C ist \n {}° F".format(self.value, fahrenheit))

    def show(self):
        self.window.mainloop()