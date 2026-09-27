# 🤖 Automação de Cadastro de Produtos (RPA em Python)

> 🎓 **Projeto desenvolvido 100% com os ensinamentos e metodologia do Grupo Hashtag Treinamentos!**

Este projeto de automação de processos (RPA - *Robotic Process Automation*) foi construído aplicando na prática todos os conceitos ensinados pela **Hashtag Treinamentos**. O objetivo principal é eliminar tarefas manuais e repetitivas por meio da leitura de uma base de dados externa e do cadastramento automático de produtos em um sistema web.

---

## ⚠️ Aviso importante antes de executar

Este script utiliza **coordenadas de clique fixas na tela** (`pyautogui.click(x=..., y=...)`), capturadas na resolução de tela e no navegador do desenvolvedor original.

Isso significa que **a automação só vai clicar nos lugares certos se a sua tela, o zoom do navegador e a posição da janela forem iguais** aos usados na gravação original. Se algo estiver diferente, o script vai clicar no lugar errado.

Para recalibrar as coordenadas para a sua tela, use o script `cordenada.py` (veja a seção [Recalibrando as coordenadas](#-recalibrando-as-coordenadas)).

---

## 🎯 O que aprendi com o Grupo Hashtag Treinamentos

Neste projeto, apliquei as técnicas e lógicas ensinadas pela Hashtag para:

- **Captura de Coordenadas:** Mapear a posição exata X e Y do ponteiro do mouse na tela utilizando `pyautogui.position()` para garantir cliques precisos nos campos.
- **Automação de Navegador e Telas:** Abrir programas, acessar links e realizar o login automatizado no sistema da Hashtag.
- **Manipulação e Leitura de Dados:** Importar e estruturar dados de arquivos `.csv` utilizando a biblioteca `pandas`.
- **Lógica e Tratamento de Dados:** Tratar valores nulos/vazios (`NaN`) dentro do loop para evitar erros ao preencher o campo de observações.
- **Automação em Loop com Sincronização:** Cadastrar dezenas de itens de forma sequencial utilizando laços de repetição, pausas de segurança (`pyautogui.PAUSE` / `time.sleep`) e rolagem automática de página (`pyautogui.scroll`).

---

## 📌 Etapas da Automação

1. **Abertura do Navegador:** O script pressiona a tecla Windows, digita "chrome", abre o Google Chrome e navega até a URL do sistema de cadastro.
2. **Login no Sistema:** Clica no campo de e-mail, preenche e-mail e senha (alternando com `Tab`) e envia o formulário com `Enter`.
3. **Leitura da Base de Dados:** Lê o arquivo `produtos.csv` com `pandas`, carregando as colunas `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo` e `obs`.
4. **Cadastro em Loop:** Para cada linha da planilha, o script:
   - Clica no botão de novo cadastro;
   - Preenche código, marca, tipo, categoria, preço unitário e custo (alternando com `Tab`);
   - Preenche o campo de observações **somente se não estiver vazio** (evita escrever "nan" no formulário);
   - Envia o cadastro com `Enter`;
   - Rola a página para o próximo item com `pyautogui.scroll()`.
5. O processo se repete automaticamente até que todos os produtos da planilha tenham sido cadastrados.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **[Python](https://www.python.org/)**
- **[Pandas](https://pandas.pydata.org/):** Leitura e estruturação dos dados do `produtos.csv`.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Controle automatizado de mouse e teclado.

---

## 📂 Estrutura de Arquivos

```
Automacao-em-python/
├── automacao_de_tarefas.py   # Script principal da automação
├── coordenada.py              # Utilitário para capturar coordenadas do mouse
├── produtos.csv                # Base de dados com os produtos a cadastrar
└── README.md
```

> 📝 Os nomes `automacao_de_tarefas.py` e `coordenada.py` acima já estão corrigidos (sem espaço e sem erro de digitação). Se o arquivo no seu repositório ainda estiver como `automaycão de tarefas.py` ou `cordenada.py`, renomeie-os para evitar problemas ao rodar comandos no terminal.

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/DCapulot/Automacao-em-python.git
```

### 2. Entre na pasta do projeto

```bash
cd Automacao-em-python
```

### 3. Instale as bibliotecas necessárias

```bash
pip install pandas pyautogui
```

### 4. Recalibre as coordenadas para a sua tela

Veja a seção [Recalibrando as coordenadas](#-recalibrando-as-coordenadas) abaixo antes de rodar o script principal — isso evita cliques no lugar errado.

### 5. Configure suas credenciais

Abra o `automacao_de_tarefas.py` e substitua o e-mail e a senha de exemplo pelos seus dados de login, ou (recomendado) adapte o script para ler essas informações de variáveis de ambiente em vez de deixá-las escritas no código.

### 6. Execute o script

```bash
python "automacao_de_tarefas.py"
```

> ⚠️ Não mexa no mouse ou teclado enquanto o script estiver rodando — como ele controla o cursor diretamente, qualquer interferência pode desalinhar os cliques.

---

## 🎯 Recalibrando as coordenadas

Use o `coordenada.py` para descobrir a posição exata de um elemento na sua tela:

```bash
python coordenada.py
```

O script espera 5 segundos (tempo para você posicionar o mouse sobre o elemento desejado) e depois imprime as coordenadas X e Y no terminal. Use esses valores para atualizar as chamadas `pyautogui.click(x=..., y=...)` dentro do `automacao_de_tarefas.py`.

---

## 📚 Fonte / Créditos

Este projeto foi desenvolvido com base nos ensinamentos do **[Grupo Hashtag Treinamentos](https://www.hashtagtreinamentos.com/)**, referência em cursos de Python, Excel e Automação de Processos no Brasil.

---

## 👤 Autor

**David Capulot Corrêa**

Projeto desenvolvido para fins de estudo e prática de automação (RPA) com Python.
