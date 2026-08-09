import pyautogui
import time
import pandas

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("Win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click( x=358,y=85)

pyautogui.write("teste@gmail.com")
pyautogui.press("tab")

pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

#pip install panda openpyxl

time.sleep(4)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
        
    pyautogui.click(x=682, y=301)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
      pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
