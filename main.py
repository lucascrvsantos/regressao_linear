#from regressao import Regressao
from excel import Values
from regressao import Regressao

values = Values('excel/data/Regressao.csv')
app = Regressao()

x_values, y_values = values.obter_valores()
for i in range(len(x_values)):
    print(int(x_values[i]), int(y_values[i]))
    app.obter_ponto(int(x_values[i]), int(y_values[i]))

app.btn_calcular['command'] = app.calcular

app.run()