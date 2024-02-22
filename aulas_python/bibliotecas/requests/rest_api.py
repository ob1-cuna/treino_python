import requests
import json
import csv

url = 'https://restcountries.com/v3.1/name/'

print("Digite o nome do pais:")
pais = input("> ")

def resultado(nome):
    name =  url + f"{pais}"
    info = requests.get(name)
    tt = json.loads(info.text)[0]

    return [
        tt['name']['common'],
        tt['flags']['png'],
        tt['region'],
        tt['subregion'],
        tt['population'],
        tt['timezones'][0],
        list(tt['name']['nativeName'].values())[0]['common']
    ]

def criar_tabela():
    detalhes = resultado(pais)
    cabecalho = ["Pais", "Bandeira", "Regiao", "Sub Regiao", "Populacao", "Fuso-Horario", "Nome Local"]
    
    with open('GFG.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)
        writer.writerow(detalhes)

criar_tabela()
