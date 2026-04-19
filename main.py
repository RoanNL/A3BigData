import pandas as pd

print('Carregando arquivos chefia...')

# carregando CSVs
df_mort = pd.read_csv('./datasets/dados_mortalidade_agrupados.csv')
df_pop = pd.read_csv('./datasets/populacao_ibge_2022.csv')
df_ans = pd.read_csv('./datasets/beneficiarios.csv', encoding='latin1', sep=';', skiprows=3, skipfooter=2, engine='python')

print("Limpando e padronizando os IDs...")

# Limpeza da ANS
df_ans.columns = ['id_municipio_str', 'total_beneficiarios']
# Pega só os 6 primeiros números antes do nome da cidade
df_ans['id_chave'] = df_ans['id_municipio_str'].astype(str).str[:6]

# Limpeza do IBGE e Mortalidade
# Cortamos o 7º dígito verificador para que fiquem com 6 dígitos igual à ANS
df_mort['id_chave'] = df_mort['id_municipio_residencia'].astype(str).str[:6]
df_pop['id_chave'] = df_pop['id_municipio'].astype(str).str[:6]

print("Realizando o Merge das tabelas...")

# O Merge (Unindo tudo pela nova coluna 'id_chave')
# Primeiro une População com Mortalidade
df_undaya = pd.merge(df_pop, df_mort, on='id_chave', how='left')

# Depois une o resultado com a ANS
df_undaya = pd.merge(df_undaya, df_ans[['id_chave', 'total_beneficiarios']], on='id_chave', how='left')

# Enriquecimento dos Dados (Tratando nulos e calculando taxas)
df_undaya['total_obitos'] = df_undaya['total_obitos'].fillna(0)
df_undaya['total_beneficiarios'] = df_undaya['total_beneficiarios'].fillna(0)


# Taxa de Mortalidade (por 100 mil habitantes)
df_undaya['taxa_mortalidade'] = (df_undaya['total_obitos'] / df_undaya['populacao']) * 100000

# Percentual de cobertura de saúde privada
df_undaya['perc_cobertura_saude'] = (df_undaya['total_beneficiarios'] / df_undaya['populacao']) * 100

# Salvando o Resultado no CSV unificado
df_undaya.to_csv('./datasets/base_consolidade_saude.csv', index=False)
print('Sua base ta pronta paizão hue hue hue hue, foi gerada na pasta de "datasets"!!')

print(df_undaya.head())