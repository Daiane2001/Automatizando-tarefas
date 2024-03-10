*__Observação importante:__ Esse exemplo aprendi com o Lira da Hashtag Treinamentos.*
<h1>Automatizando Tarefas</h1>
<p>Esse projeto é para automatizar uma tarefa de cadastro de produtos, no banco de dados da empresa. </p>
<p></p>

<h3>Passo-a-passo da automação:</h3>
<p>1° Pedimos para o Python pressionar a tecla "Windows" do teclado.</p>
<p>2° Pedimos para digitar Chrome (Pode ser qualquer navegador do seu interesse).</p>
<p>3° Pedimos para pressionar a tecla enter no Chrome.</p>
<p>4° Pedimos para digitar no Chrome, o site que utilizamos para o login do usuário que irá cadastrar os produtos no sistema da empresa.</p>
<p>5° Pedimos para pressionar a tecla enter do teclado.</p>
<p>6° Pedimos para o Python clicar na posição exata em que estava a opção de e-mail. (Para isso encontramos a posição do mouse, vou explicar a seguir).</p>
<p>7° Pedimos para o Python digitar o e-mail.</p>
<p>8° Pedimos para o Python pressionar a opção "Tab" do teclado, para mudar para a opção senha.</p>
<p>9° Pedimos para o Python digitar a senha.</p>
<p>10° Pedimos para o Python pressionar a tecla "Tab" do teclado, para mudar para a opção enter.</p>
<p>11° Pedimos para o Python clicar na opção exata do primeiro item a ser cadastrado (também encontrando a posição do Mouse).<p>
<p>12° Pedimos para o Python digitar a informação que estava na nossa base de dados. </p>
<p>13° Pedimos para o Python pressionar a tecla "Tab" do teclado para passar para o próximo campo.</p>
<p>14° Pedimos para o Python digitar a informação que estava na nossa base de dados. </p>
<p>15° Pedimos para o Python pressionar a tecla "Tab" do teclado para passar para o próximo campo.</p>
<p></p>
<p></p>
<p></p>
<p>Do 12° passo até o 15° foi repetido para todos os campos que precisassem ser preenchidos com informações da nossa base de dados.</p>
<p></p>
<p></p>
<p></p>
<p>16° Pedimos para o Python pressionar a tecla enter para enviar os dados que seriam cadastrados no banco de dados da empresa.</p>
<p>17° Depois de preenchido o primeiro cadastro, pedimos para o mouse rolar o Scroll do mouse(aquela bolinha que tem no meio do mouse para subir ou descer a página) para o começo da página e repetir todo o processo, até cadastrar todos os itens da nossa base de dados.</p>
<p></p>
*Dicas: O editor de código que estou usando é o visual Studio, a extensão que utilizei para compilar/rodar o código Python foi "Python" e "Python Debugger". Para ler o arquivo .csv, usei a extensão "Rainbow CSV".*
<p></p>
<p>Observaram que utilizei muito as palavras "clicar", "pressionar" e "digitar"? Então, é que no Python funciona exatamente assim.</p>
<p></p>
<p>Quando quero que o Python digite alguma coisa, basta digitar o código:</p>
pyautogui.write("Texto que quero que ele digite")
<p></p>
<p>Quando quero que o Python pressione alguma tecla, basta digitar o código;</p>
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("Win")
<p></p>
<p>Quando quero que o Python clique em algum lugar com o mouse, basta digitar:</p>
pyautogui.click()
<p></p>
<p>Para achar a posição exata do mouse, utilizamos:</p>
pyautogui.position()
<p></p>
<p>E para visualizar essa informação, precisamos mostrar no terminal com o código:</p>
print()
<p></p>
<p>Logo, usaremos a combinação dos dois códigos para mostrar a informação que queremos no terminal:</p>
print(pyautogui.position())
<p></p>
<p>O pyautogui, nada mais é que uma biblioteca de automação que fornece métodos para controlar mouse e teclado.Essa biblioteca precisa ser instalada através do terminal, usando:</p>
pip install pyautogui
 <p></p>
<p>Agora que já alinhamos as partes importantes, bora codar??!</p>
<p></p>
<p>A primeira coisa que precisamos fazer é importar o pyautogui:</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/eb04d378-656d-4ed5-8e7b-c1400d108f56)
 <p></p>
<p>Agora que importamos o pyautogui, vamos poder usá-lo para o que precisarmos e nesse momento, precisamos que ele abra o Chrome:</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/a8d392ae-fef2-4d6c-b7d5-958ec072189b)
<p>A automação faz tudo muito rápido, a velocidade da internet ou do computador não interferem em nada, então, mesmo que não carregue a página que ele precisa para colocar as informações, ele vai digitar onde estiver. Por isso, é recomendável estipular um tempo para que o Python execute cada comando pyautogui. Para isso utilizamos o .PAUSE:</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/fb3337a1-19f9-420c-a48c-30f6c64118b7)
<p>Agora, todos os comandos pyautogui que vierem abaixo desse código vão levar essa quantidade de segundos para rodar. Nesse exemplo, foi utilizado um segundo, mas podem colocar 0.5 para carregar mais rápido ou mais segundos, para garantir que não dê nenhum erro ao executar a automação futuramente. </p>
<p></p>

<p>Agora que ele abriu o Chrome, precisamos informar qual o link do site que ele precisa digitar e pressionar a tecla "enter" para ir pro destino informado. </p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/b0cb9474-6599-4727-8dfb-056b77940341) 
<p>Poderíamos deixar assim nesse exemplo, porque o link só será utilizado essa vez. Mas, se o link fosse utilizado mais de uma vez na automação, o ideal seria utilizar assim:</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/f93d0b9f-e6c7-44bf-a336-7ca4dca21959) 
<p>Dessa forma, fazemos o link virar uma variável e se precisar alterar o endereço da url, basta mudar diretamente na váriavel e quando precisar utilizá-lo, basta chamar a variável "link".</p>
  <p></p>
<p>Como, para entrar na internet geralmente leva mais tempo para carregar as informações, podemos fazer com que nesse momento específico da automação o Python insera as informações demorando mais tempo. Assim, garantimos que o Chrome esteje aberto para que a automação insira o link que ele deve pesquisar. Para isso, utilizamos a biblioteca "time" que já vem instalada no Python. Primeiro importamos essa biblioteca, podemos colocá-la embaixo da importação que fizemos do pyautogui no começo da automação.</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/bf26d498-66e4-42ef-8ec7-e17fe1f9645c)
<p>Logo após, antes da variável "link", chamamos a biblioteca time para pausar a automação no tempo que eu especificar.</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/58795ce9-ce70-4bca-be31-2134a05b7b3d)
<p>Neste exemplo especifiquei 10 segundos, assim ele vai conseguir abrir o Chrome, carregar a página e adicionar o link sem margem de erros. Lembrando que tudo depende da velocidade do seu computador, para o meu preciso de 10s, mas pode colocar menos segundos também.</p>
 <p></p>
 <p>Como vai abrir outro link, vou seguir a mesma linha de raciocínio e deixar mais 10 segundos para conseguir carregar a url informada.</p>
 <p></p>
 
 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/0daa9f9a-32b4-410c-8a81-14d4c3f2155f)
 <p></p>
<p>Vai abrir na página de Login. Agora, para fazer com que o Python clique na opção "E-mail", vou precisar usar o mouse. Nesse exemplo, vou deixar o mouse em cima da caixa de texto, como no exemplo abaixo.</p>
<p></p>
 
![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/ead2f485-76d2-4509-affa-fde36ab20438)
<p>Mas antes de colocar o mouse na caixa de texto, vamos precisar digitar o comando:</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/2af39ae9-2aa0-46e7-991d-dfe28d62460a)
<p></p>
<p>Para verificar qual posição que o mouse está, compile a automação, apertando a seta no canto superior direito da tela no Visual Studio Code(Vscode):</p>
<p></p>

 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/23071274-ee48-4987-bc92-79183ab16168)
<p></p> 
<p>Pedimos para encontrar a posição do mouse, mas observe que não deu nem tempo de chegar na posição que queríamos. Por isso, mais uma vez vamos usar o time, assim vamos conseguir minimizar a tela do VScode e entrar na tela do login.</p>
<p></p>

 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/52f8e5e7-d0fc-4da3-8dfd-3df7c7381d37)
<p>Agora sim você pode compilar a automação e deixar o mouse na posição que desejar.</p>
<p></p>

 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/aec30e47-609e-4141-a991-bafa93717579)  
<p>No meu caso apareceu x=439, y=371, copiei e colei do terminal e já pedi para o pyautogui clicar nessa posição. Depois que ele clicar, deve-]se pedir para ele digitar o email, passar para o próximo campo e digitar a senha:</p>
<p></p>

 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/91c550e9-cc4a-446f-9955-9189a7a1a57b)
<p></p>
<p>Para apertar em logar é possível, fazer com três opções. A primeira opção é pressionando a tecla "enter" com o pyautogui.press("enter"), a segunda é apertando a tecla "Tab" e em seguida "enter" com pyautogui.press("tab") e pyautogui.press("enter") e a terceira que é pegando a posição do mouse e em seguida apertando enter:</p>
<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/c9af69c7-dc50-4c79-b500-f0e746418a3a)
<p>Acrescentei um tempo de 5 segundos para a próxima página ter tempo de carregar.</p>

<p></p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/c5f38069-db75-4e9c-9b52-60acc7ca7d2f)




