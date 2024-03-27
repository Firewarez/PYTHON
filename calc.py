import requests
from tkinter import *
import requests

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    cotacao_gbp = requisicao_dic['GBPBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Btc: {cotacao_btc}
    Libra {cotacao_gbp}'''

    texto_cotacoes["text"] = texto


janela = Tk()
janela.title("Cotação Atual das Moedas by Arthur")
janela.maxsize(1360, 768)
janela.resizable(False, False)

def numero1():
    valor1 = float()

f_1 = Frame(janela, width=100, height=100, bg="blue")
f_1.grid(row=2, column=0)

#Texto do app
texto_oritentacao = Label(janela, text="Clique no botão para exibir a cotação das moedas", font=('Arial', 20),)
texto_oritentacao.grid(row=0, column=0, padx=5, pady=5)

#Botões Do app
botao1 = Button(janela, text="1",font=('Arial', 15), command= pegar_cotacoes)
botao1.grid(row=2, column=4, padx=5, pady=5)

botao2 = Button(janela, text="2",font=('Arial', 15), command= pegar_cotacoes)
botao2.grid(row=2, column=1, padx=5, pady=5)

botao3 = Button(janela, text="3",font=('Arial', 15), command= pegar_cotacoes)
botao3.grid(row=2, column=2, padx=5, pady=5)

botao = Button(janela, text="Buscar cotações",font=('Arial', 15), command= pegar_cotacoes)
botao.grid(row=1, column=0, padx=5, pady=5)


#Apresentar os valores
texto_cotacoes = Label(janela, text="",font=('Arial', 15))
texto_cotacoes.grid(row=5, column=0)


janela.mainloop()