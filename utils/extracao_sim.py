import basedosdados as bd
import pandas as pd

# A consulta SQL que faz o trabalho pesado no servidor (agrupando por município e ano)
# Aqui filtramos para o ano de 2021 como exemplo
query_mortalidade = """
SELECT 
    ano, 
    sigla_uf, 
    id_municipio_residencia, 
    COUNT(*) as total_obitos
FROM `basedosdados.br_ms_sim.microdados`
WHERE ano = 2021
GROUP BY ano, sigla_uf, id_municipio_residencia
"""

# Extração: Carrega o resultado diretamente para um DataFrame Pandas
# NOTA: Será necessário um 'billing_project_id' do Google Cloud (gratuito)
print("A extrair dados do Base dos Dados...")
df_obitos = bd.read_sql(query=query_mortalidade, billing_project_id="a3bigdata")

# Transformação e Carga: Guardar o resultado limpo na pasta local
df_obitos.to_csv('dados_mortalidade_agrupados.csv', index=False)
print("Extração concluída com sucesso! Ficheiro guardado.")