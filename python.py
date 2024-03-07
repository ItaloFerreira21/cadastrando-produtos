import time
import pyautogui
import pandas
pyautogui.PAUSE = 1

# PASSO 1: ABRIR O NAVEGADOR
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

# PASSO 2: ENTAR NO SITE
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write (link)
pyautogui.press ("enter")
time.sleep (2)

# PASSO 3: FAZER LOGUIN NO SISTEMA DA EMPRESA
pyautogui.click (x=399, y=407)
pyautogui.write ("email-da-empresa@gmail.com")
pyautogui.press ("tab")
pyautogui.write ("senha-da-empresa")
pyautogui.press ("tab")
pyautogui.press ("enter")
time.sleep (1.5)

# PASSO 4: IMPORTAR A BASE DE DADOS
tabela = pandas.read_csv ("produtos.csv")
print (tabela)


# PASSO 5: CADASTRAR UM PRODUTO
for linha in tabela.index:
    pyautogui.click (x=513, y=294)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write (codigo)
    pyautogui.press ("tab")

    pyautogui.write (tabela.loc[linha, "marca"])
    pyautogui.press ("tab")

    pyautogui.write (tabela.loc[linha, "tipo"])
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "categoria"]))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press ("tab")

    pyautogui.write (str(tabela.loc[linha, "custo"]))
    pyautogui.press ("tab") 
# PASSO 6: REPETIR ATE ACABAR OS PRODUTOS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna (obs):
        pyautogui.write (obs)
    pyautogui.press ("tab")

    pyautogui.press ("enter")
    pyautogui.scroll (5000)