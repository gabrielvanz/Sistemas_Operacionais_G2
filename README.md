<h1 align="center" style="color: green">Trabalho G2 - Sistemas Operacionais</h1>

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/gabrielvanz/RealityStone_Gabriel_Compass/blob/develop/LICENSE)

<h2>Sobre o projeto</h2>

> Este projeto é referente a G2 de Sistemas Operacionais, lecionado pelo professor Fernando Posser.
  <br>É utilizado o banco de dados PostgreSQL e a linguagem Python, que são a base para  o funcionamento do Adminer, uma ferramenta de gerenciamento de banco de dados.


<h2>Integrantes do grupo</h2>

- Bruno Benevenuto

- Gabriel Gomes

- Gabriel Vanz

- Gilberto Calonego

- Henrique Wommer

<br>

<h2>Tecnologias utilizadas</h2>

<p align="center" color=""><a href="https://www.python.org/" title="Python"><img height="70" width="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"></a>
<a href="https://www.docker.com/" title="Docker"><img height="70" width="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"></a>
<a href="https://code.visualstudio.com/" title="Visual Studio Code"><img height="70" width="70" src="https://img.icons8.com/color/344/visual-studio-code-2019.png"></a>
<a href="https://git-scm.com/" title="Git"><img height="70" width="70" src="https://camo.githubusercontent.com/fbfcb9e3dc648adc93bef37c718db16c52f617ad055a26de6dc3c21865c3321d/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f6769742d73636d2f6769742d73636d2d69636f6e2e737667"> </a>
<a href="https://github.com/" title="GitHub"> <img height="70" width="70" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></a>
<a href="https://www.canva.com/" title="Canva"> <img height="70" width="70" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/canva/canva-original.svg"></a></p> 

<br>

<h2>Pré-requisitos</h2>

```bash
Para Linux
• Docker              ->   20.10 ou superior

Para Windows
• Docker Desktop      ->   4.14.1 ou superior

```
<br>

<h2>Como clonar o repositório com Git</h2>
1- Abra o Git Bash

2- Escolha local em que deseja ter o diretório clonado com seguinte comando

```bash
$ git init
```

3- Digite ```git clone``` e cole a URL deste repositório

```bash
$ git clone https://github.com/gabrielvanz/Sistemas_Operacionais_G2.git
```

<br>

<h2>Executando</h2>

1- Abra a pasta em que foi clonado o repositório

2- Digite o comando para executar os arquivos python + yaml

```bash
docker-compose up -d
```
3- Pressione **Enter**

<br>

<h2>Abrir o Adminer</h2>

1- Abra o navegador e utilize o link abaixo

```bash
localhost:8080
```

2- Passe nos campos os respectivos valores:
```bash
Motor de base de dados  => PostgreSQL
Servidor                => database
Nome de utilizador      => docker
Senha                   => docker
Base de dados           => exampledb
```
3- Clique em **Entrar**

<br>

<h2>Relacionados</h2>

> https://www.canva.com/design/DAFSZ5ui-2I/iIbvgNh31DVjFUMESIZGZg/view?utm_content=DAFSZ5ui-2I&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


<h2>Referências</h2>

> https://github.com/irtiza07/postgres-python-docker <br>https://hub.docker.com/_/postgres <br>https://hub.docker.com/_/adminer
