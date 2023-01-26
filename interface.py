import tkinter as tk
import tkinter.font as font

class Interface:
    def __init__(self):
        self.x_points = []
        self.y_points = []
        self.root = tk.Tk()
        self.root.title('Regressão Linear')
        fonnt = font.Font(self.root, size=20)
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.btn_calcular = tk.Button(self.root, text='Calcular')
        self.label = tk.Label(self.root, text='f(x) = ax + b', font=fonnt)
        self.label.pack(anchor='center')
        self.canvas.pack()
        self.btn_calcular.pack(anchor='center')

    def obter_ponto(self, xc, yc):
        r = 10
        self.canvas.create_oval(xc, yc, xc + r, yc - r, fill='black')
        self.x_points.append(xc)
        self.y_points.append(yc)

    def desenhar(self, option, coords):
        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        if option == 'line':
            line = self.canvas.create_line(x1, y1, x2, y2)
            self.lines.append(line)

    def apagar(self):
        self.canvas.delete('all')
        while self.x_points:
            self.x_points.remove(self.x_points[0])
        while self.y_points:
            self.y_points.remove(self.y_points[0])
        self.label['text'] = f'f(x) = ax + b'

    def update(self, a, b):
        if a < 0:
            self.label['text'] = f'f(x) = {format(-a, ".2f")}x + {format(b, ".2f")}'
        elif a < 0 and b < 0:
            self.label['text'] = f'f(x) = {format(-a, ".2f")}x {format(b, ".2f")}'
        elif a > 0 and b < 0:
            self.label['text'] = f'f(x) = -{format(a, ".2f")}x {format(b, ".2f")}'
        else:
            self.label['text'] = f'f(x) = -{format(a, ".2f")}x + {format(b, ".2f")}'

    def run(self):
        self.root.mainloop()