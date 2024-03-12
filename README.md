*__Observação importante:__ Esse exemplo aprendi com o Lira da Hashtag Treinamentos.*
<h1>Automatizando Tarefas</h1>
<p>Esse projeto é para automatizar uma tarefa de cadastro de produtos, no banco de dados da empresa. </p>
<p></p>

<h3>Passo-a-passo da automação:</h3>
<br/>
<p><b>1°</b> Pedimos para o Python pressionar a tecla "Windows" do teclado.</p>
<p><b>2°</b> Pedimos para digitar Chrome (Pode ser qualquer navegador do seu interesse).</p>
<p><b>3°</b> Pedimos para pressionar a tecla enter no Chrome.</p>
<p><b>4°</b> Pedimos para digitar no Chrome, o site que utilizamos para o login do usuário que irá cadastrar os produtos no sistema da empresa.</p>
<p><b>5°</b> Pedimos para pressionar a tecla enter do teclado.</p>
<p><b>6°</b> Pedimos para o Python clicar na posição exata em que estava a opção de e-mail. (Para isso encontramos a posição do mouse, vou explicar a seguir).</p>
<p><b>7°</b> Pedimos para o Python digitar o e-mail.</p>
<p><b>8°</b> Pedimos para o Python pressionar a opção "Tab" do teclado, para mudar para a opção senha.</p>
<p><b>9°</b> Pedimos para o Python digitar a senha.</p>
<p><b>10°</b> Pedimos para o Python pressionar a tecla "Tab" do teclado, para mudar para a opção enter.</p>
<p><b>11°</b> Pedimos para o Python clicar na opção exata do primeiro item a ser cadastrado (também encontrando a posição do Mouse).<p>
<p><b>12°</b> Pedimos para o Python digitar a informação que estava na nossa base de dados. </p>
<p><b>13°</b> Pedimos para o Python pressionar a tecla "Tab" do teclado para passar para o próximo campo.</p>
<p><b>14°</b> Pedimos para o Python digitar a informação que estava na nossa base de dados. </p>
<p><b>15°</b> Pedimos para o Python pressionar a tecla "Tab" do teclado para passar para o próximo campo.</p>
<br/>
<p>Do 12° passo até o 15° foi repetido para todos os campos que precisassem ser preenchidos com informações da nossa base de dados.</p>
<br/>
<p><b>16°</b> Pedimos para o Python pressionar a tecla enter para enviar os dados que seriam cadastrados no banco de dados da empresa.</p>
<p><b>17°</b> Depois de preenchido o primeiro cadastro, pedimos para o mouse rolar o Scroll do mouse(aquela bolinha que tem no meio do mouse para subir ou descer a página) para o começo da página e repetir todo o processo, até cadastrar todos os itens da nossa base de dados.</p>
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

<p>Para verificar a posição em que o mouse está, compile a automação, apertando a seta no canto superior direito da tela no Visual Studio Code(Vscode):</p>


 ![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/23071274-ee48-4987-bc92-79183ab16168)
 
<br/>

<p>O pyautogui, nada mais é que uma biblioteca de automação, que fornece métodos para controlar mouse e teclado.Essa biblioteca precisa ser instalada através do terminal, usando:</p>

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


![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/53fb5a8f-e9ac-4f5e-9638-c07868f27de2)

<p>Poderíamos deixar assim nesse exemplo, porque o link só será utilizado essa vez. Mas, se o link fosse utilizado mais de uma vez na automação, o ideal seria utilizar assim:</p>


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

<p>Para verificar a posição em que o mouse está, compile a automação, apertando a seta no canto superior direito da tela no Visual Studio Code(Vscode):</p>


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
<p>Acrescentei um time de 5 segundos, para o Python esperar antes de fazer a próxima ação. Assim, vai dar tempo para o meu computador e a internet, abrirem a tela de formulário para cadastro de produtos e o Phython conseguir clicar na posição exata que está a primeira caixa de texto e começar a digitar as informações que estão na nossa base de dados.</p>

<br/>
 
<p>Como informei anteriormente, nessa parte também vamos precisar encontrar a posição do mouse. Então compile a automação, vá até a página do formulário de cadastro de produtos e deixe o mouse nessa posição:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/83a5a6dd-7dba-46a4-8c36-39c157a96944)
<p>Se você estiver feito o processo corretamente, no terminal vai aperecer a posição exata do mouse e você vai pegar essa informação e pedir para o Python clicar:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/58dbc80c-c2e5-476c-9d2c-3414c38d12fe)
<p>No meu caso, apareceu x=807, y=255, então pedi para o Python clicar nessa posição</p>

<br/>
 
<p>Nesse momento, antes de pedirmos para o Python pegar as informações que estão na nossa base de dados, arquivo "produtos.csv", precisamos fazer com que o Python entenda que precisa clicar nesse primeiro campo, digitar uma informação, apertar a tecla "Tab" para passar para o próximo campo, digitar outra informação, apertar a tecla "Tab" novamente e assim sucetivamente, até que a tecla "Tab" enteja na posição de enviar as informações.</p>

<br/>

<p>Ótimo! Com o Mouse na posição do primeiro campo, vamos usar os comandos pyautogui para digitar algo lá dentro da caixa e apertar a tecla "tab" para passar para o próximo campo:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/e80c4316-3aba-40b7-95f2-d3ade5ea8941)
<p>Digitamos o código e passamos para o próximo campo. Agora vamos fazer o mesmo processo com o pyautogui para digitar a informação e apertar a tecla "tab":</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/343ceb42-ecc1-4890-b634-5e462210160f)
<p>Esse mesmo processo vai ser repetido para todos os campos, fizemos juntos o código e a marca, agora repita esse processo para tipo, categoria, preço unitário, custo e observações.</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/cb7c4395-97cd-4292-b891-fa8ba02cdd45)
<p>Visualmente a automação deve estar assim: </p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/f2c5508b-de9b-4245-8969-3e3609c43393)

<p>Podemos observar que o pyautogui já colocou todas as informações que pedimos para ele inserir. Agora podemos enviar as informações através da tecla enter e cadastrar um novo produto.</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/0506725e-8703-494b-b11b-76c68685ad6c)

<br/>

<p>Observem que quando cadastramos o primeiro produto, ele vai mostrar na parte de baixo da tela:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/8136fc7a-7a04-4a76-a93c-969ab5b8727a)
<p>Interessante, mas como vamos cadastrar o próximo produto? Se você pensou em voltar para o inicio da tela, acertou. Mas como podemos fazer isso? Sabe aquela bolinha que tem no meio do mouse que nos faz navegar para cima e para baixo nas telas? Então, aqui no Python podemos fazer com que o mouse gire essa bolinha até o inicio da tela, essa bolinha se chama scroll, com o código:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/b7b07af1-a2d2-4d5d-9e4c-268ed25a12bf)

<p>Todas as vezes que precisarmos rodar a tela para cima ou para baixo podemos usar o scroll. Coloquei o valor de 15000 para garantir que o pyautogui vai girar o scroll até chegar no inicio da tela.</p>

<br/>
   
*Importante: Se você informar um valor positivo como no exemplo acima, o pyautogui vai girar o scroll para cima, se colocar um valor negativo, por exemplo "pyautogui.scroll(-150)", o pyautogui vai girar o scroll para baixo.*

<br/>

<p>Esse processo vai se repetir até acabar os produtos que temos que puxar da nossa base de dados. </p>

<br/>
 
<p>Certo, finalizamos o processo de cadastrar o primeiro produto. Você deve estar se perguntando sobre não termos pego diretamente as informações da nossa base de dados, mas não se preocupe, esse processo tivemos que fazer para dar um passo a passo para o pyautogui seguir, você não precisará fazer esse processo novamente.</p>

<br/>

<p>Agora sim vamos começar a pegar as informações da nossa base de dados. A primeira coisa que você precisará fazer, é instalar a biblioteca pandas no terminal. Ela é uma biblioteca para Ciências de Dados de código aberto (open source), e que providencia uma abordagem rápida e flexível. Para instalar, basta digitar no terminal: </p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/e4dc6e82-c4cb-41bb-8cbe-c9344cafabf7)
 
<p>É aconselhável instalar a biblioteca completa, como no exemplo acima, porque pode ocorrer, de uma determinada base de dados precisar ser trabalhada ou manuseada de forma diferente e instalando a biblioteca completa evitamos precisar fazer novas instalações.</p>

<br/>

<p>Depois de instalar a biblioteca, precisamos imortá-la:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/30767190-5ad0-4ece-bec2-f18a67ed52b7)

<br/>
  
<p>Ótimo,  agora vamos ler a nossa base de dados. Para isso, primeiro, precisaremos falar qual que é a base de dados que queremos ler. No nosso caso, vai ser um arquivo "csv", mas poderia ser "sql", "html", "excel" ou outro arquivo, basta inserir o comando abaixo: </p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/ec245955-155d-4fb3-bd03-7aa1c1aaf2b8)

<p>Nesse exemplo, criamos uma variável tabela para armazenar a nossa base de dados. Utlizamos a biblioteca pandas e pedimos para ler a nossa base de dados e informamos onde estava a nossa base de dados.</p>

<br/>
 
<p>Para que a nossa automação fique cadastrando cada linha que temos na nossa base de dados e só parar quando todas estiverem cadastradas, precisamos utilizar a estrutura de repetição for, que nos permite percorrer os itens de uma coleção e, para cada um deles, executar o bloco de código declarado no loop. No nosso caso, vamos declarar que para cada linha da nossa tabela, queremos pegar a informação correspondente a cada caixa de texto, mostrar na tela e logo após cadastrar. Vamos começar acrescentando o loop de repetição antes da linha que colocamos a posição do mouse para clicar no primeiro campo: </p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/0ef9e68e-4522-4608-b4bf-28ec8b816fb2)

<p>Agora precisamos voltar no primeiro campo e no lugar em colocamos uma informação aleatória, vamos pedir para o pyautogui localizar na tabela essa linha e essa coluna. O valor da linha vai ser mudada consecutivamente, então só precisamos colocar o valor exato da coluna que estamos utilizando nesse campo: </p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/e7f1c50a-ded7-4e9a-bb06-eaf7adee874c)
 
<p>Você pode fazer desse jeito acima ou também criar uma variável por fora e pedir para ela guardar o valor exato da base de dados e depois só chama-lá, como no exemplo abaixo:</p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/4d9af120-b1f6-4124-817a-37e2b3a499b1)

<p>Você pode escolher qual opção é melhor para o seu uso, só precisa lembrar que o valor da coluna deve ser escrita da mesma forma que estiver na base de dados. No nosso caso serão as seguintes informações: </p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/2805e7a2-469e-4dde-86da-07bd68ee5291)


<p>Observem acima que no campo da coluna "obs", nem todas as linhas possuem alguma informação. Neste caso vamos precisar fazer uma condição quando formos preencher este campo, mas para os outros campos podemos seguir a mesma linha de raciocínio que utilizamos no primeiro campo, falando para o pyautogui procurar na tabela a localização exata da linha e da coluna usada. </p>

<br/>

<p>Agora vamos aplicar a condição para o campo "obs", falando que se não tiver nenhum valor é pra seguir normalmente a automação.</p>

<p> Vamos começar declarando a variável "obs" e pedindo para ela guardar a localização da linha e da coluna utilizada. Depois vamos utilizar o comando if dizendo, se o valor da variável estiver vazio pressione a tecla "tab": </p>

![image](https://github.com/Daiane2001/Automatizando-tarefas/assets/62717387/4864fa7c-09a9-4500-8b38-54512c1c3a3d)
 
<p>Como informado na imagem, o pandas utiliza um método chamado isna(),para detectar se tem valores ausentes dentro do objeto que informamos, que no nosso caso é a variável "obs".</p>

<br/>

<p>Assim, concluimos a nossa automação. Espero ter te ajudado a compreender todos os códigos utilizados nesta aplicação e o funcionamento de cada um deles.</p>

<br/>

<h3>Atenciosamente, Daiane Santana de Oliveira.</h3>

<br/>

*Bibliografia:*

<ul>
<li><p>Lira da Hashtag Treinamentos.</p> </li>
<li><p>https://www.devmedia.com.br/for-python-estrutura-de-repeticao-for/38513</p></li>
<li><p>https://www.alura.com.br/artigos/pandas-o-que-e-para-que-serve-como-instalar</p></li>
<li><p>https://acervolima.com/funcao-pandas-isna-em-python/</p></li>
</ul>


