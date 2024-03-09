#Passo a passo do projeto
#Passo 1: entrar no sistema da empresa usando python;
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login -- sistema provisório;
    # pip install pyautogui -> instalar a bliblioteca para automação de tarefas no terminal
import pyautogui #chamando a biblioteca de automação para fazer a tarefa que quisermos
import time

#Vou pausar a automoção por causa da internet
pyautogui.PAUSE = 1

#Passo 1.1: Abrir o navegador(Chrome)-tecla Windows do teclado-pesquisar chrome e apertar entra
pyautogui.press("win") #Pedindo para pressionar a tecla Windows do teclado
pyautogui.write("chrome") #Pedindo para escrever o texto chrome
pyautogui.press("enter") #apertar a tecla enter

#Vou pausar a automoção por causa da internet e falar pra nesse caso esperar 10s antes de digitar o link
#Mas primeiro devo importar a biblioteca que já vem instalada no python, "time"
time.sleep(10) #pausa aí python
 
#entrar no site
#Para não precisar ficar digitando o site varias vezes no código,vamos criar a variavel link
link= "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #lê-se link recebe esse texto todo
pyautogui.write(link)#Pedindo para digitar o site, neste caso a variavel link
pyautogui.press("enter")

#Aqui vou colocar um tempo por causa da internet
time.sleep(10)

#Passo 2: Fazer Login usando python;
pyautogui.click(x=439, y=371) #Aqui peço para clicar na posição que encontrei do mouse no posicaoMouse.py
pyautogui.write("daiane@programandoempython.com")

#Escrever a senha
pyautogui.press("tab") #pressionando a tecla tab
pyautogui.write("muDarSenHa")
 
#clicando no botão logar, nesse caso vai direto se clicar em enter, caso não, modelo abaixo
#pyautogui.press("enter") #pressionando enter
pyautogui.click(x=668, y=533)
time.sleep(5) #coloquei tempo só por garantia que a automação vai ter tempo de carregar a outra página

#Passo 3: Importar a base de dados para fazer o cadastro;
#pip install pandas numpy openpyxl --- biblioteca completa do pandas --- bibli. que trabalha com base de dados
import pandas #importando pandas
#lendo base de dados 
tabela = pandas.read_csv("produtos.csv") #pedindo para ler o arquivo csv, tabelas separadas por virgula
#print(tabela) --- Caso queira ver a tabela no terminal

#Passo 4: cadastrar 1 produto;
#Para cada linha da minha tabela
for linha in tabela.index: #o pandas chama cada linha de indice por isso fica index

    #Clicar no 1° campo
    pyautogui.click(x=807, y=255)

    #Digitar o nome do campo 
    #apertar tab para ir para o próximo campo
    codigo = tabela.loc[linha,"codigo"] #localizar na tabela essa linha e essa coluna. linha é a var q coloquei no for
    pyautogui.write(codigo) #digitando valor exato da variavel que esta na base de dados
    pyautogui.press("tab")

    #Digitar o nome do campo 
    #apertar tab para ir para o próximo campo
    #localizar na tabela essa linha e essa coluna. linha é a var q coloquei no for
    pyautogui.write(tabela.loc[linha,"marca"]) #digitando valor exato da variavel que esta na base de dados
    pyautogui.press("tab")

    #Digitar o nome do campo 
    #apertar tab para ir para o próximo campo
    #localizar na tabela essa linha e essa coluna. linha é a var q coloquei no for
    pyautogui.write(tabela.loc[linha,"tipo"]) #digitando valor exato da variavel que esta na base de dados
    pyautogui.press("tab")

    #Digitar o nome do campo 
    #apertar tab para ir para o próximo campo
    #localizar na tabela essa linha e essa coluna. linha é a var q coloquei no for
    #p/ transformar nro da tabela em texto, basta usar str(), ele significa texto
    pyautogui.write(str(tabela.loc[linha,"categoria"])) #digitando valor exato da variavel que esta na base de dados
    pyautogui.press("tab")

    #Digitar o nome do campo 
    #apertar tab para ir para o próximo campo
    #localizar na tabela essa linha e essa coluna. linha é a var q coloquei no for
    #p/ transformar nro da tabela em texto, basta usar str(), ele significa texto
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"])) #digitando valor exato da variavel que esta na base de dados
    pyautogui.press("tab")

    #Digitar o nome do campo 
    #apertar tab para ir para o próximo campo
    #localizar na tabela essa linha e essa coluna. linha é a var q coloquei no for
    #p/ transformar nro da tabela em texto, basta usar str(), ele significa texto
    pyautogui.write(str(tabela.loc[linha,"custo"])) #digitando valor exato da variavel que esta na base de dados
    pyautogui.press("tab")

    #Digitar o nome do campo 
    #apertar tab para ir para o próximo campo
    #localizar na tabela essa linha e essa coluna. linha é a var q coloquei no for
    #Como em algumas linhas terão valores e outras não precisa abrir uma condição
    obs = tabela.loc[linha,"obs"] #colocando obs em uma variável
    if not pandas.isna(obs):#insa significa está vazio. se a obsnão estiver vazia digiti-a, senão table
        pyautogui.write(obs) #digitando valor exato da variavel que esta na base de dados
    pyautogui.press("tab")
    
    #Apertar Enviar --- Como já saiu do campo obs, basta apertar enter
    pyautogui.press("enter")
    pyautogui.scroll(15000) #fazendo com que a roda do mouse gire até voltar p/ inicio da tela


#Passo 5: Repetir o processo de cadastro até acabar.
