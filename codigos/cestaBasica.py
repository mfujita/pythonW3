#Fonte https://www.lojamaximo.com.br/cestas-basicas/cesta-basica-casal-24kg

#import pandas as pd

# tabela = pd.read_csv("cestaBasica.csv", delimiter=";")
# print(tabela)

cestaBasica = [
["                      Achocolatado em Pó", "  PC 200G", "               Nescau"],
["                         Açúcar Refinado", "   PC 1KG", "            Caravelas"],
["                     Amaciante de Roupas", " FR 500ML", "                 Qboa"],
["                    Arroz Tipo 1 Premium", "   PC 5KG", "  Grão Maximo Premium"],
["               Biscoito Recheado Sabores", "  PC 120G", "              Triunfo"],
["          Biscoito Salgado Cream Cracker", "  PC 164G", "              Triunfo"],
["                Café Almofada Extraforte", "  PC 500G", "              Caboclo"],
["                  Mistura Creme de Leite", "  TP 200G", "               Mococa"],
["                            Creme Dental", "   FR 70G", "               Oral B"],
["                            Desinfetante", " FR 500ML", "              Minuano"],
["                              Detergente", " PR 500ML", "               Limpol"],
["                    Caixa PAP M1 Limpeza", "UN 15,85G", "              Benefit"],
["                            Caixa PAP M3", "UN 21,85G", "              Benefit"],
["                        Esponja Multiuso", "   PC 10G", "              Assolan"],
["                        Farinha de Trigo", "   PC 1KG", "               Corina"],
["Farofa de Mandioca Temperada Tradicional", "  PC 180G", "                 Mani"],
["           Feijão Carioca Tipo 1 Premium", "   PC 1KG", "  Grão Maximo Premium"],
["                             Fubá Mimoso", "  PC 500G", "                Sinhá"],
["                                Goiabada", "  PC 200G", "                Ploky"],
["                               Lã de Aço", "   PC 40G", "             Q Lustro"],
["                        Lava Roupa em Pó", "  CX 800G", "                Tixan"],
["              Leite Líquido UHT Integral", "   TP 1LT", "          Piracanjuba"],
["               Macarrão Espaguete Sêmola", "  PC 500G", "           Dona Benta"],
["                    Macarrão Instantâneo", "   PC 70G", "                 Apti"],
["                         Molho de Tomate", "  SH 300G", "                  Val"],
["                            Óleo de Soja", "PET 900ML", "                 Liza"],
["           Papel Higiênico Folha Simples", "  PC 200G", "             Personal"],
["             Filme Plástico Proteção Bag", "   UN 20G", "              Benefit"],
["                                Sabonete", "   PC 80G", "                Gipsy"],
["                        Sardinha em Óleo", "  LT 125G", "             Nautique"],
["                       Seleta de Legumes", "  LT 170G", "                 Ramy"],
["                                     Sal", "   PC 1KG", "           5 Estrelas"]]

maior1 = 0
maior2 = 0
maior3 = 0
for linha in cestaBasica:
    if len(linha[0]) > maior1:
        maior1 = len(linha[0])
    if len(linha[1]) > maior2:
        maior2 = len(linha[1])
    if len(linha[2]) > maior3:
        maior3 = len(linha[2])
    

for coluna in cestaBasica:
    col1=coluna[0].strip()
    col2=coluna[1].strip()
    col3=coluna[2].strip()
    print(f'<tr><td>{col1:<{maior1}}</td><td>{col2:<{maior2}}</td><td>{col3:<{maior3}}</td></tr>')