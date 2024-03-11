*__Observação importante:__ Esse exemplo aprendi com o Lira da Hashtag Treinamentos.*
<h1>Automatizando Tarefas</h1>
<p>Esse projeto é para automatizar uma tarefa de cadastro de produtos, no banco de dados da empresa. </p>
<p></p>

<h3>Passo-a-passo da automação:</h3>
<br/>
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
<br/>
<p>Do 12° passo até o 15° foi repetido para todos os campos que precisassem ser preenchidos com informações da nossa base de dados.</p>
<br/>
<p>16° Pedimos para o Python pressionar a tecla enter para enviar os dados que seriam cadastrados no banco de dados da empresa.</p>
<p>17° Depois de preenchido o primeiro cadastro, pedimos para o mouse rolar o Scroll do mouse(aquela bolinha que tem no meio do mouse para subir ou descer a página) para o começo da página e repetir todo o processo, até cadastrar todos os itens da nossa base de dados.</p>
<br/>

*Dicas: O editor de código que estou usando é o visual Studio, a extensão que utilizei para compilar/rodar o código Python foi "Python" e "Python Debugger". Para ler o arquivo .csv, usei a extensão "Rainbow CSV".*

<br/>
<p>Observaram que utilizei muito as palavras: "clicar", "pressionar" e "digitar"? Então, é que no Python funciona exatamente assim.</p>
<br/>

<p>Quando quero que o Python digite alguma coisa, basta digitar o código:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/fe636165-d695-4b5c-98a6-0858281693fc)

<br/>
<p>Quando quero que o Python pressione alguma tecla, basta digitar o código:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/661992be-44bf-44ee-b3e9-f267cdd24e5f)

<br/>
<p>Quando quero que o Python clique em algum lugar com o mouse, basta digitar o código:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/8b2545f4-49ee-4330-b969-ead2d4bdc26d)

<br/>

<p>Para achar a posição exata do mouse, utilizamos:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/302657cc-9047-4747-b300-b6ec8e8e3f48)

<br/>

<p>E para visualizar essa informação, precisamos mostrar no terminal com o código:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/612a019d-f3cb-49ce-b852-7255b7715757)

<br/>

<p>Logo, usaremos a combinação dos dois códigos para mostrar a informação que queremos no terminal:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/96c8134e-2764-4f8f-a2fc-ab7b01eda043)

<br/>

<p>O pyautogui, nada mais é que uma biblioteca de automação que fornece métodos para controlar mouse e teclado.Essa biblioteca precisa ser instalada através do terminal, usando:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/95056649-bb34-4302-ac02-acac572540e3)

 <br/>
 
<p>Agora que já alinhamos as partes importantes, bora codar??!</p>

<br/>

<p>A primeira coisa que precisamos fazer é importar o pyautogui:</p>


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/eb04d378-656d-4ed5-8e7b-c1400d108f56)

 <br/>
 
<p>Agora que importamos o pyautogui, vamos poder usá-lo para o que precisarmos e nesse momento, precisamos que ele abra o Chrome:</p>


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/a8d392ae-fef2-4d6c-b7d5-958ec072189b)

<br/>

<p>A automação faz tudo muito rápido, a velocidade da internet ou do computador não interferem em nada, então, mesmo que não carregue a página que ele precisa para colocar as informações, ele vai digitar onde estiver. Por isso, é recomendável estipular um tempo para que o Python execute cada comando pyautogui. Para isso utilizamos o .PAUSE:</p>


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/fb3337a1-19f9-420c-a48c-30f6c64118b7)

<br/>

<p>Agora, todos os comandos pyautogui que vierem abaixo desse código vão levar essa quantidade de segundos para rodar. Nesse exemplo, foi utilizado um segundo, mas podem colocar 0.5 para carregar mais rápido ou mais segundos, para garantir que não dê nenhum erro ao executar a automação futuramente. </p>

<br/>

<p>Agora que ele abriu o Chrome, precisamos informar qual o link do site que ele precisa digitar e pressionar a tecla "enter" para ir pro destino informado. </p>

<br/>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/b0cb9474-6599-4727-8dfb-056b77940341) 
<p>Poderíamos deixar assim nesse exemplo, porque o link só será utilizado essa vez. Mas, se o link fosse utilizado mais de uma vez na automação, o ideal seria utilizar assim:</p>
<br/>


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/f93d0b9f-e6c7-44bf-a336-7ca4dca21959) 
<p>Dessa forma, fazemos o link virar uma variável e se precisar alterar o endereço da url, basta mudar diretamente na váriavel e quando precisar utilizá-lo, basta chamar a variável "link".</p>
  
  <br/>
  
<p>Como, para entrar na internet geralmente leva mais tempo para carregar as informações, podemos fazer com que nesse momento específico da automação o Python insera as informações demorando mais tempo. Assim, garantimos que o Chrome esteje aberto para que a automação insira o link que ele deve pesquisar. Para isso, utilizamos a biblioteca "time" que já vem instalada no Python. Primeiro importamos essa biblioteca, podemos colocá-la embaixo da importação que fizemos do pyautogui no começo da automação.</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/bf26d498-66e4-42ef-8ec7-e17fe1f9645c)

<br/>

<p>Logo após, antes da variável "link", chamamos a biblioteca time para pausar a automação no tempo que eu especificar:</p>


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/58795ce9-ce70-4bca-be31-2134a05b7b3d)
<p>Neste exemplo especifiquei 10 segundos, assim ele vai conseguir abrir o Chrome, carregar a página e adicionar o link sem margem de erros. Lembrando que tudo depende da velocidade do seu computador, para o meu preciso de 10s, mas pode colocar menos segundos também.</p>

 <br/>
 
 <p>Como vai abrir outro link, vou seguir a mesma linha de raciocínio e deixar mais 10 segundos para conseguir carregar a url informada:</p>
 
 
 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/0daa9f9a-32b4-410c-8a81-14d4c3f2155f)
 
 <br/>
 
<p>Vai abrir na página de Login. Agora, para fazer com que o Python clique na opção "E-mail", vou precisar usar o mouse. Nesse exemplo, vou deixar o mouse em cima da caixa de texto, como no exemplo abaixo:</p>
 
![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/ead2f485-76d2-4509-affa-fde36ab20438)

<br/>

<p>Mas antes de colocar o mouse na caixa de texto, vamos precisar digitar o comando:</p>


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/2af39ae9-2aa0-46e7-991d-dfe28d62460a)

<br/>

<p>Para verificar qual posição que o mouse está, compile a automação, apertando a seta no canto superior direito da tela no Visual Studio Code(Vscode):</p>


 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/23071274-ee48-4987-bc92-79183ab16168)
 
<br/>

<p>Pedimos para encontrar a posição do mouse, mas observe que não deu nem tempo de chegar na posição que queríamos. Por isso, mais uma vez vamos usar o time, assim vamos conseguir minimizar a tela do VScode e entrar na tela do login.</p>


 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/52f8e5e7-d0fc-4da3-8dfd-3df7c7381d37)
 
<br/>

<p>Agora sim você pode compilar a automação e deixar o mouse na posição que desejar.</p>


 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/aec30e47-609e-4141-a991-bafa93717579)  
<p>No meu caso apareceu x=439, y=371, copiei e colei do terminal e já pedi para o pyautogui clicar nessa posição. Depois que ele clicar, deve-]se pedir para ele digitar o email, passar para o próximo campo e digitar a senha:</p>

 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/91c550e9-cc4a-446f-9955-9189a7a1a57b)
 
<br/>

<p>Para apertar em logar é possível, fazer com três opções. A primeira opção é pressionando a tecla "enter" com o pyautogui.press("enter"), a segunda é apertando a tecla "Tab" e em seguida "enter" com pyautogui.press("tab") e pyautogui.press("enter") e a terceira que é pegando a posição do mouse e em seguida apertando enter:</p>


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/c9af69c7-dc50-4c79-b500-f0e746418a3a)
<p>Acrescentei um time de 5 segundos, para o Python esperar antes de fazer a próxima ação.</p>

<br/>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/83a5a6dd-7dba-46a4-8c36-39c157a96944)







