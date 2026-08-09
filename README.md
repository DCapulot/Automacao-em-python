# 🤖 Automação de Cadastro de Produtos (RPA em Python)

> 🎓 **Projeto desenvolvido 100% com os ensinamentos e metodologia do Grupo Hashtag Treinamentos!**

Este projeto de automação de processos (RPA - *Robotic Process Automation*) foi construído aplicando na prática todos os conceitos ensinados pela **Hashtag Treinamentos**. O objetivo principal é eliminar tarefas manuais e repetitivas por meio da leitura de uma base de dados externa e do cadastramento automático de produtos em um sistema web.

---

## 🎯 O que aprendi com o Grupo Hashtag Treinamentos

Neste projeto, apliquei as técnicas e lógicas ensinadas pela Hashtag para:
- **Captura de Coordenadas:** Mapear a posição exata $X$ e $Y$ do ponteiro do mouse na tela utilizando `pyautogui.position()` para garantir cliques precisos nos campos.
- **Automação de Navegador e Telas:** Abrir programas, acessar links e realizar o login automatizado no sistema da Hashtag.
- **Manipulação e Leitura de Dados:** Importar e estruturar dados de arquivos `.csv` utilizando a biblioteca `pandas`.
- **Lógica e Tratamento de Dados:** Tratar valores nulos/vazios (`NaN`) dentro do loop para evitar erros ao preencher o campo de observações.
- **Automação em Loop com Sincronização:** Cadastrar dezenas de itens de forma sequencial utilizando laços de repetição, pausas de segurança (`pyautogui.PAUSE` / `time.sleep`) e rolagem automática de página (`pyautogui.scroll`).

---

## 📌 Etapas da Automação

1. **Abertura do Navegador:** O script aciona o menu do sistema, abre o Google Chrome e navega até a URL do sistema de cadastro.
2. **Login no Sistema:** Preenchimento automático de e-mail e senha, seguido do envio do formulário
