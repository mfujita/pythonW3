import xlsxwriter
import xlsxwriter.worksheet

vendas = [
    ['Produto 1', 'Codigo 1', 'Quantidade 1', 'PrecoCompra 1'],
    ['Produto 2', 'Codigo 2', 'Quantidade 2', 'PrecoCompra 2'],
    ['Produto 3', 'Codigo 3', 'Quantidade 3', 'PrecoCompra 3'],
    ['Produto 4', 'Codigo 4', 'Quantidade 4', 'PrecoCompra 4'],
    ['Produto 5', 'Codigo 5', 'Quantidade 5', 'PrecoCompra 5'],
    ['Produto 6', 'Codigo 6', 'Quantidade 6', 'PrecoCompra 6'],
]

planilha=xlsxwriter.Workbook('Relatorio.xlsx')
aba=planilha.add_worksheet('Agosto')

for i in range(len(vendas)):
    produto=vendas[i][0]
    codigo=vendas[i][1]
    qtde=vendas[i][2]
    precoCompra=vendas[i][3]
    aba.write(f"A{i+1}", produto)
    aba.write(f"B{i+1}", codigo)
    aba.write(f"C{i+1}", qtde)
    aba.write(f"D{i+1}", precoCompra)

    aba.set_column('A:B',40)

planilha.close()