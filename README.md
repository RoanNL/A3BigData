Markdown
# 📊 A3BigData

Este projeto implementa um pipeline de Big Data e processos de ETL (Extract, Transform, Load) focado no processamento e análise de dados públicos de saúde. A aplicação realiza a extração e integração de grandes volumes de dados provenientes do **DATASUS (SIM - Sistema de Informações sobre Mortalidade)** e bases demográficas do **IBGE (via API SIDRA)**.

---

## 🚀 Como Executar

Pensando na melhor experiência para os desenvolvedores e na padronização do ambiente, a configuração do projeto foi totalmente automatizada. Você só precisa ter o **Python** instalado na sua máquina.

Abra o terminal na pasta raiz do projeto e execute o comando orquestrador:

```bash
python start.py
```
⚙️ O que acontece por baixo dos panos?
Ao rodar o comando acima, o script automaticamente:

Identifica o seu sistema operacional.

Cria um ambiente virtual (venv) isolado para evitar conflitos de versão.

Instala todas as bibliotecas listadas no requirements.txt.

Verifica se a base de dados pesada já existe na máquina; caso não, faz o download automático via Google Drive.

Inicia a execução do código principal (main.py).

📂 Arquitetura de Pastas
Abaixo está o mapeamento da estrutura do nosso repositório:

Plaintext
A3BigData/
│
├── utils/
│   ├── download.py      # Script que gerencia o download de datasets pesados do Drive
│   ├── api_sidra.py     # Integração com a API SIDRA para consumir dados do IBGE
│   └── extracao_sim.py  # Script de extração e modelagem do dataset SIM via SQL
│
├── datasets/            # Diretório criado automaticamente para armazenar os dados brutos e processados
├── venv/                # Ambiente virtual do Python (ignorado no versionamento)
│
├── requirements.txt     # Mapeamento de todas as dependências (pandas, gdown, etc.)
├── start.py             # Script orquestrador de setup e inicialização
├── main.py              # Ponto de entrada (entry point) da aplicação
└── README.md            # Documentação oficial do projeto