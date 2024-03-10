*Observação importante: Esse exemplo aprendi com o Lira da Hashtag Treinamentos.*

Automatizando Tarefas
Esse projeto, é para automatizar uma tarefa de cadastro de produtos no banco de dados da empresa. 
A base de dados que utilizamos é um arquivo .csv, que nada mais é que, colunas separadas por vírgulas.

Passo-a-passo da automação:
1° Pedimos para o Python pressionar a tecla "Windows" do teclado.
2° Pedimos para digitar Chrome (Pode ser qualquer navegador do seu interesse).
3° Pedimos para pressionar a tecla enter no Chrome.
4° Pedimos para digitar no Chrome, o site que utilizamos para o login do usuário que irá cadastrar os produtos no sistema da empresa.
5° Pedimos para pressionar a tecla enter do teclado.
6° Pedimos para o Python clicar na posição exata em que estava a opção de e-mail. (Para isso encontramos a posição do mouse, vou explicar a seguir).
7° Pedimos para o Python digitar o e-mail.
8° Pedimos para o Python pressionar a opção "Tab" do teclado, para mudar para a opção senha.
9° Pedimos para o Python digitar a senha.
10° Pedimos para o Python pressionar a tecla "Tab" do teclado, para mudar para a opção enter.
11° Pedimos para o Python clicar na opção exata do primeiro item a ser cadastrado (também encontrando a posição do Mouse).
12° Pedimos para o Python digitar a informação que estava na nossa base de dados.
13° Pedimos para o Python pressionar a tecla "Tab" do teclado para passar para o próximo campo.
14° Pedimos para o Python digitar a informação que estava na nossa base de dados. 
15° Pedimos para o Python pressionar a tecla "Tab" do teclado para passar para o próximo campo.

Do 12° passo até o 15° foi repetido para todos os campos que precisassem ser preenchidos com informações da nossa base de dados.

16° Pedimos para o Python pressionar a tecla enter para enviar os dados que seriam cadastrados no banco de dados da empresa.
17° Depois de preenchido o primeiro cadastro, pedimos para o mouse rolar o Scroll do mouse(aquela bolinha que tem no meio do mouse para subir ou descer a página) para o começo da página e repetir todo o processo, até cadastrar todos os itens da nossa base de dados.

*Dicas: O editor de código que estou usando é o visual Studio, a extensão que utilizei para compilar/rodar o código Python foi "Python" e "Python Debugger". Para ler o arquivo .csv, usei a extensão "Rainbow CSV".*

Observaram que utilizei muito as palavras "clicar", "pressionar" e "digitar"? Então, é que no Python funciona exatamente assim.

Quando quero que o Python digite alguma coisa, basta digitar o código:
pyautogui.write("Texto que quero que ele digite")

Quando quero que o Python pressione alguma tecla, basta digitar o código;
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("Win")

Quando quero que o Python clique em algum lugar com o mouse, basta digitar:
pyautogui.click()

Para achar a posição exata do mouse, utilizamos:
pyautogui.position()

E para visualizar essa informação, precisamos mostrar no terminal com o código:
print()

Logo, usaremos a combinação dos dois códigos para mostrar a informação que queremos no terminal:
print(pyautogui.position())

O pyautogui, nada mais é que uma biblioteca de automação que fornece métodos para controlar mouse e teclado.
Essa biblioteca precisa ser instalada através do terminal, usando :
pip install pyautogui
 
Agora que já alinhamos as partes importantes, bora codar??!

A primeira coisa que precisamos fazer é importar o pyautogui:
![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/eb04d378-656d-4ed5-8e7b-c1400d108f56)
 
Agora vamos que importamos o pyautogui, vamos poder usá-lo para o que precisarmos e nesse momento, precisamos que ele abra o chrome:
![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/64a3344e-547b-45a7-a949-1ec9bf28295f)
Como a automação faz tudo muito rápido, mesmo que a internet esteje lenta ou o seu computador esteje quase parando, mesmo que não carregue a página que ele precisa para colocar as informações, ele vai digitar onde estiver mesmo. Por isso, é recomendável estipular um tempo para que o Python execute cada comando pyautogui. Para estipular esse tempo, é nescessário importar a biblioteca time, que já vem instalada no Python.
![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/23a9ae59-22db-4b09-8410-66a1a90b778c)  
Agora, todos os comandos pyautogui que vierem abaixo desse código vão levar essa quantidade de segundos para rodar, nesse exemplo foi utilizado 1 segundo, mas podem colocar 0.5 para carregar mais rápido ou mais segundos pq sua internet ou computador estão muito lentos.


Agora que ele abriu o Chrome, precisamos informar qual o link do site que ele precisa digitar e pressionar a tecla "enter" para ir pro destino informado. 
![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/b0cb9474-6599-4727-8dfb-056b77940341) 
Poderíamos deixar assim nesse exemplo, porque o link só será utilizado essa vez. Mas, se o link fosse utilizado mais de uma vez na automação, o ideal seria utilizar assim:
![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/f93d0b9f-e6c7-44bf-a336-7ca4dca21959) 
Dessa forma, fazemos o link virar uma variável e se precisar alterar o endereço da url, basta mudar diretamente na váriavel e quando precisar utilizá-lo, basta chamar a variável.






