import requests
import pandas as pd

def extrair_populacao_ibge():
    # URL da API para Tabela 4714, Variável 93 (População), Localidade N6 (Todos os municípios)
    url = "https://servicodados.ibge.gov.br/api/v3/agregados/4714/periodos/2022/variaveis/93?localidades=N6[all]"
    
    print("Consumindo API SIDRA/IBGE...")
    response = requests.get(url)
    data = response.json()
    
    # O IBGE retorna uma estrutura de lista aninhada, precisamos "achatar" os dados
    resultados = data[0]['resultados'][0]['series']
    
    lista_populacao = []
    for item in resultados:
        lista_populacao.append({
            'id_municipio': item['localidade']['id'],
            'nome_municipio': item['localidade']['nome'],
            'populacao': int(item['serie']['2022'])
        })
    
    df_ibge = pd.DataFrame(lista_populacao)
    df_ibge.to_csv('populacao_ibge_2022.csv', index=False)
    print("Dados do IBGE salvos com sucesso!")
    return df_ibge

df_pop = extrair_populacao_ibge()