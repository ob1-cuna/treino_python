import json, requests, csv
from numerize import numerize 

url = 'https://restcountries.com/v3.1/name/'

def resultado(nome):
    name =  url + f"{nome}"
    info = requests.get(name)
    tt = json.loads(info.text)
    mylist = []
    sem_dado = 'NO DATA'
    for t in tt:
        valores = ['nome_pais_en','bandeira','regiao','subregiao','populacao','fuso-horario','nome_tativo', 'populacao_compact']
        items = [t.get('name', {}).get('common', sem_dado),
                 t.get('flags', {}).get('png', sem_dado),
                 t.get('region', sem_dado),
                 t.get('subregion', sem_dado),
                 t.get('population', sem_dado),
                 t.get('timezones', sem_dado)[0],
                 list(t.get('name',{}).get('nativeName', sem_dado).values())[0].get('common', sem_dado),
                 numerize.numerize(t.get('population'), 2),]
        mylist.append(dict(zip(valores,items)))
    return mylist

def criar_tabela(pais):
    detalhes = resultado(pais)
    cabecalho = ["Pais", "Bandeira", "Regiao", "Sub Regiao", "Populacao", "Fuso-Horario", "Nome Local"]
    filename = f"{pais}_results.csv"

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)
        for dado in detalhes:
            writer.writerow(dado.values())

def main():
    print("Digite nome do pais a pesquisar")
    nome_do_pais = input("> ")
    criar_tabela(nome_do_pais)

main()