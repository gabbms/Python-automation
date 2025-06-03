import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5 # pause de 0,5 segundos entre os comandos

# 1° passo: entrar no chrome 

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=699, y=493) # seleciona o primeiro usuario do chrome

# 2° passo: entrar no link e fazer o login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # pausa de 3 segundos para carreagar a página

pyautogui.click(x=770, y=407)
pyautogui.write("gab@gmail.com")
pyautogui.press("tab")
pyautogui.write("secretpassword")
pyautogui.press("tab")
pyautogui.press("enter")

# 3° passo: cadastrar os produtos

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=688, y=295)
    # pega da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter") # para clicar no botão
    pyautogui.scroll(10000)