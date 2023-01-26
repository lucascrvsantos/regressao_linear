from interface import Interface

class Regressao(Interface):
    def __init__(self):
        Interface.__init__(self)
        self.lines = []

    def calcular(self) -> list:
        print(self.x_points, self.y_points)
        n = len(self.x_points)
        somatorio_x = sum(self.x_points)
        somatorio_y = sum(self.y_points)
        produto = []
        x_square = []
        for i in range(len(self.x_points)):
            product = self.x_points[i] * self.y_points[i]
            produto.append(product)
        print('end')
        for x in self.x_points:
            square = x**2
            x_square.append(square)
        numerador_a = (n * sum(produto)) - (somatorio_x * somatorio_y)
        denominador_a = (n*sum(x_square)) - (somatorio_x**2)
        a = numerador_a / denominador_a
        b = (somatorio_y / len(self.y_points)) - (a * (somatorio_x / len(self.x_points)))
        self.obter_reta(a, b)

    def obter_reta(self, a, b,):
        if self.lines:
            self.canvas.delete(self.lines[0])
            self.lines.remove(self.lines[0])
        xmin = min(self.x_points)
        xmax = max(self.x_points)
        fmin = a * xmin + b
        fmax = a * xmax + b
        Interface.desenhar(self, 'line', [xmin, fmin, xmax, fmax])
        Interface.update(self, a, b)