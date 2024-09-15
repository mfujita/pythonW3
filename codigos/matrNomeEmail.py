import random
import xlsxwriter

nomes=[
    ["Elizabete Estrada Jimenes"],
    ["Beto Jardel Abreu de Menezes"],
    ["Elisângela Branco Marinho"],
    ["Maria Chaves de Molina"],
    ["Hilda Camacho"],
    ["Bella Thaíssa Bittencourt Góis"],
    ["Carla Daniela Flores Quintana"],
    ["Demian Barreto"],
    ["Ediane Kelly Leon de Britto"],
    ["Solange Campos Queirós"],
    ["Elano Bonilha Gomes"],
    ["Bernadete Franco Saraiva"],
    ["Ezequiel Valter Branco Neto"],
    ["Andre Esteves Salgado"],
    ["Flavia Barreto de Delvalle"],
    ["Gian Pablo de Casanova"],
    ["Anakin Kim Bonilha Marinho de Machado"],
    ["Vitoria Garcia de Lira"],
    ["Irene Josiane Ferreira de Menezes"],
    ["Estêvão Bittencourt Camacho"],
    ["Paulina Vera Flores Rivera de Gimenes"],
    ["Hellen Maria Burgos de Junqueira"],
    ["Maximiano Ávila Medina"],
    ["Everton Olavo Barros"],
    ["Diogo Oliveira Filho"],
    ["Flavio Cesar Castro"],
    ["Victor Hugo Oliveira Do Nascimento"],
    ["Diogo Álvaro Ferreira Moncorvo"],
    ["Cristina Lexa Araújo Da Fonseca"],
    ["Marcio Da Costa Batista"],
    ["Roberto De Souza Rocha"],
    ["Matheus Wallace Mendonça Da Cruz"],
    ["Agenor Apolinário Dos Santos Neto"],
    ["Marcelo Pires Vieira"],
    ["Marlon Brandon Coelho Couto Silva"],
    ["Gustavo Da Hungria Neves"],
    ["Clériton Sávio Santos Silva"],
    ["Daniel Garcia Felicione Napoleão"],
    ["Matheus Brasileiro Aguiar"],
    ["Mayra Corrêa Aygadoux"],
    ["Doroth Helena De Sousa Alves"],
    ["Leandro Roque De Oliveira"],
    ["Claucirlei Jovêncio De Souza"],
    ["Filipe Cavaleiro De Macedo Da Silva Faria"],
    ["Jheison Failde De Souza"],
    ["Ana Maria Braga"],
    ["Josefina das Dores Socorro"],
    ["Hildebrando Martinelli Castro"],
    ["Esperidião Amin Alencar"],
    ["Antonio Vasquez Solto Filho"],
    ["Estevan Rodrigues Souza"],
    ["Lara Castro Santos"],
    ["Brenda Lima Rocha"],
    ["Beatrice Araujo Oliveira"],
    ["Sofia Rodrigues Almeida"],
    ["Leila Santos Rodrigues Pilares"],
    ["Mateus Dias Azevedo Guimarães"],
    ["Giovanna Castro Silva"],
    ["Amanda Oliveira Castro Coelho"],
    ["Leonor Costa Lima Carneiro"],
    ["Vitor Santos Cunha Da Silva"],
    ["Luis Santos Barbosa"],
    ["Mariana Melo Pereira Teixeira"],
    ["Alex Almeida Carvalho Junior"],
    ["Laura Mariana Cardoso Andrade"],
    ["Leticia Castro Cardoso Imaculada"],
    ["Tomas Pinto Gonçalves De Azevedo"],
    ["Emilly Araujo Sousa"],
    ["Danilo Melo Barros Cavalcante"],
    ["Gabrielle Melo Martins Barbosa"],
    ["Mariana Sousa Vilares Astolfe"],
    ["Stenico Santana Garcia"],
    ["Anna Dias Alves Botafogo"],
    ["Luan Barros Cardoso Oliveira"],
    ["Isabela Correia Tavares"],
    ["Marcos Barbosa Castro Neves"],
    ["Lara Azevedo Costa Duarte"],
    ["Giovana Carvalho Rodrigues Oliveira"],
    ["Kauã Kock Brito"],
    ["Julieta Costa Rocha"],
    ["Melissa Alessandra Barros"],
    ["Otavio Ribeiro Santos"],
    ["Breno Pinto Novaes"],
    ["Douglas Pereira Almeida"],
    ["Miguel Gomes Cardoso Alvares"],
    ["Ariadne Vieira Nogueira"],
    ["Eleni Magalhães Peres"],
    ["Regina Ferreira Xavier Rezende"],
    ["Ana Caroline Dutra De Melo"],
    ["Sara Casagrande Barichelo"],
    ["Leticia Ramos Queiroz Vasconcelos"],
    ["Moacir Clemente Ribeiro Filho"],
    ["Isabele Leite Barreto Martins"],
    ["Luiza Abdala Amorim Favoreto"],
    ["Rodrigo de Paula Lucano"],
    ["Vinicius Martins Santana Santigo"],
    ["Juliane Sofia Azeredo Camargo"],
    ["Eloá Soares Guerreiro Bonifácio"],
    ["Carlos Eduardo Medeiros Paes"],
    ["Natan Pazonini Francischini"],
    ["Eriston Araujo Feliciano"],
    ["Nelson Pascoal Aguiar"],
    ["Raquel Gusmão Pacheco"],
    ["Reginaldo Antenor Terranobre"]
]

dominios = ['gmail.com','yahoo.com.br','outlook.com','hotmail.com','rocketmail.com','protonmailcom','zoho.com']

maiorNome = 0
for linha in nomes:
    if len(linha[0]) > maiorNome:
        maiorNome = len(linha[0])

def eliminaAcentos(texto):
    return texto.replace("á","a").replace("â","a").replace("ã","a").replace("ê","e").replace("é","e").replace("í","i").replace("ó","o").replace("ô","o").replace("ú","u")

listaNumero = [] 
def geraNumeroSemRepeticao():
    while len(listaNumero) < len(nomes):
        aleatorio = random.randint(100,300)
        if aleatorio not in listaNumero:
            listaNumero.append(aleatorio)

    for i in range(len(listaNumero)):
        print(listaNumero[i],end=' ')
    
geraNumeroSemRepeticao()


# for coluna in nomes:
#     campo = coluna[0].split()
#     nome = campo[0]
#     nome = eliminaAcentos(nome)
#     sobrenome=campo[len(campo)-1]
#     sobrenome = eliminaAcentos(sobrenome)
#     dom=random.randint(0,len(dominios))-1
#     print(f'<tr><td>{coluna[0]:<{maiorNome}}' + "</td><td>" + nome.lower()+"."+sobrenome.lower()+"@"+dominios[dom]+ "</td></tr>")

listaEmail=[]
def geraEmail():
    for nome in nomes:
        campo=nomes[i][0].split()
        nome=campo[0]
        nome=eliminaAcentos(nome)
        sobrenome=campo[len(campo)-1]
        sobrenome=eliminaAcentos(sobrenome)
        dom=random.randint(0,len(dominios))-1
        listaEmail.append(nome.lower()+"."+sobrenome.lower()+"@"+dominios[dom])


# for i in range(len(nomes)):
#     campo=nomes[i][0].split()
#     nome=campo[0]
#     nome=eliminaAcentos(nome)
#     sobrenome=campo[len(campo)-1]
#     sobrenome=eliminaAcentos(sobrenome)
#     dom=random.randint(0,len(dominios))-1
#     print(f'<tr><td>{listaNumero[i]}</td> <td>{nomes[i][0]:<{maiorNome}}' + "</td><td>" + nome.lower()+"."+sobrenome.lower()+"@"+dominios[dom]+ "</td></tr>")

workbook = xlsxwriter.Workbook('first.xlsx')
aba = workbook.add_worksheet('planilha1')

for i in range(len(nomes)):
    campo=nomes[i][0].split()
    nome=campo[0]
    nome=eliminaAcentos(nome)
    sobrenome=campo[len(campo)-1]
    sobrenome=eliminaAcentos(sobrenome)
    dom=random.randint(0,len(dominios))-1
    email=nome.lower()+"."+sobrenome.lower()+"@"+dominios[dom]
    aba.write(f"A{i+1}",listaNumero[i])
    aba.write(f"B{i+1}",nomes[i][0])
    aba.write(f"C{i+1}",email)

    aba.set_column('B:C',50)
    aba.set_column('C:D',40)

workbook.close()

