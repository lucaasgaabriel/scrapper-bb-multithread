from unidecode import unidecode
import requests

def get_municipios():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    response = requests.get(url)

    if response.status_code == 200:
        municipios = response.json()
        nomes_municipios = []
        
        for municipio in municipios:
            nome_municipio = municipio['nome']
            nomes_municipios.append(unidecode(nome_municipio))

    return nomes_municipios

