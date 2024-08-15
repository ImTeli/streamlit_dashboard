# Projeto: Dashboard Para de Análise de Vendas

Este projeto é uma aplicação desenvolvida em Python para a análise de dados de vendas. Ele inclui ferramentas para importação de dados, manipulação de dataframes, e visualização de informações importantes sobre vendas.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
app/
├── main.py             # Arquivo principal que executa a aplicação
├── __init__.py         # Arquivo de inicialização do módulo
├── data/
│   └── vendas.json     # Dados de vendas em formato JSON
├── pages/
│   └── dataframe.py    # Página dedicada ao manuseio e download de dataframes
└── utils/
    ├── data_import.py  # Funções para importação de dados
    ├── df_class.py     # Classe para manipulação de dataframes
    ├── tools.py        # Ferramentas utilitárias
    └── __init__.py     # Arquivo de inicialização do módulo
```

## Requisitos

- Python 3.x
- Bibliotecas necessárias podem ser instaladas utilizando o arquivo `requirements.txt`.

## Como Executar

1. Clone este repositório.
2. Navegue até o diretório do projeto.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Execute a aplicação utilizando `streamlit run app/main.py`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Basta seguir os passos:

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nome-da-sua-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nome-da-sua-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
