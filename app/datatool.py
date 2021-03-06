# Transformação dos dados.
# Após pegar ler a tabela fornecida, separei as colunas e utilizei como lista para inserir no banco de dados.
# CPF e CNPJ foram trasformados em células apenas com os números e as vírgulas foram transformadas em pontos.
# Os valores 'NULL' continuaram assim.

import pandas as pd

class DataTool:

  def __init__(self, initialData):
    self.initialData = pd.read_table(initialData, header = None)

  def transformData(self):
    data_list = self.splitColumns(self.initialData)

    for i in range(0, len(data_list)):
      data_list[i][0] = self.idTransform (data_list[i][0])
      for ii in range(1, len(data_list[i])):
        if data_list[i][ii] == 'NULL':
          data_list[i][ii] = 'NULL'
        else:
          data_list[i][4] = self.decimalTransform (data_list[i][4])
          data_list[i][5] = self.decimalTransform (data_list[i][5])
          data_list[i][6] = self.idTransform (data_list[i][6])
          data_list[i][7] = self.idTransform (data_list[i][7])
    return data_list

  def splitColumns(self, value):
    data_list=[]
    for i in range(1, len(value)):
      data_list.append(value[0][i].split())
    return data_list
  
  def idTransform (self, value):
    if(value == 'NULL'):
      return "NULL"
    else:
      return ''.join([str(digits_num) for digits_num in value if digits_num.isdigit()])

  def decimalTransform (self, value):
    return value.replace(',', '.')

data = DataTool("base_teste.txt")

print(data.transformData())