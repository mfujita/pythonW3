# Intro
# How does Django Work?
# Django utiliza MVT (Model View Template)
# Model → Os dados a serem apresentados, geralmente de uma banco de dados.
# View → O manipulador de requisição que retorna um modelo e conteúdo relevantes - baseado na requisição do usuário
# Template → Um arquivo de texto (como HTML) contendo a aparência (layout) da web page com a lógica de como mostrar os dados.

# Model
# O Model fornece dados do banco de dados.
# No Djando, a informação é entregue com um ORM (Object Relational Mapping) que é a técnica projetada para facilitar o trabalho com banco de dados.
# A forma mais comum de extrair dados de um banco de dados é o SQL. Um problema com SQL é que você precisar ter um bom entendimento sobre a estrutura de  banco de dados para trabalhar com ela.
# Django com ORM torna mais fácil comunicar com o banco de dados sem ter que escrever instruções SQL complexas.
# Os modelos são geralmente localizados em um arquivo chamado models.py.

# View
# Uma view é uma função que toma como requisições HTTP como argumentos, importa model(s) relevantes, procura quais informações enviam para o template e retorna o resultado.
# Os views geralmente são localizados no arquivo chamado views.py.

# Template
# Um template é um arquivo o qual você descrevee como o resultado deve ser representado.
# Templates são geralmente arquivos .html com código HTMLdescrevendo o layout da web page, mas pode ser em outros formatos de arquivos para apresentar outro resoltado, mas vamos nos concentrar nos arquivos .html.
# Django usa HTML padrão para descrever o layout, mas usa tags Django para adicionar lógica.
# <h1>Minha página</h1>
# <p>Meu nome é {{ primeiroNome }}. </p>
# O template de uma aplicação é localizado um diretório chamado templates.

# URL
# Djando fornece uma forma de navegar pelas diferentes páginas em um website.
# Quando um usuário requisita uma URL, Djando decide qual view será enviada.
# Isto é feito pelo arquivo chamado urls.py

# So, What is Going On?
# Quando você tem Djando instalado e criado sua primeira sua primeira aplicação web e o navegador requerer a URL, basicamente o que acontece é:
'''
1. Djando recebe a URL, verifica o arquivo urls.py e chama a view que combina com a URL.
2. A View, localizada em views.py, verifica o modelo relevante.
3. Os models são importados pelo arquivo models.py
4. O view então envia o dado para um template específico no diretório template.
5. Os templates contém tags HTML e Djando e com os dados ele retorna o conteúdo HTML de volta para o navegador.
'''

# Django pode fazer mais do que isto, mas basicamenteo que você aprende neste tutorial são os passos básicos de uma aplicação web com Djando.