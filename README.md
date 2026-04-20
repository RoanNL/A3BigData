# A3BigData

## Passo a Passo para a execução do código

abra o terminal na pasta raiz e digite:
```bash
python start.py
```

## Arquitetura de pastas

Pasta Raiz/
│
├── utils/
│   ├── download.py      # O script que baixa os dados do Drive (caso não tenha os datasets)
|   ├── api_sidra.py     # Arquivo de script de chamada da API SIDRA para puxar o dataset
|   └── extracao_sim.py  # Arquivo de script para extração do dataset SIM através de sql
│
├── datasets/            # Pasta criada automaticamente para armazenar os datasets (caso já não exista) 
│
├── venv/                # Ambiente virtual criado automaticamente
│
├── requirements.txt     # Lista de dependências (pandas, gdown, etc)
├── readme.md            
├── start.py             # Código inicial que inicia toda a aplicação
└── main.py              # Código Principal


