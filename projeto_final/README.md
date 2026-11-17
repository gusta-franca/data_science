# Interrupções de carga do ONS (Subsistema Sul), clima do INMET e feriados

O presente repositório constrói uma base de dados diária que combina as interrupções de carga do Subsistema Sul, o clima das estações do INMET no Paraná, Santa Catarina e Rio Grande do Sul, e seus feriados respectivos. A base serve para as seguintes análises: prever com 24 horas de antecedência um dia de alta interrupção; e investigar a sazonalidade das interrupções.

## Execução

Baixe os dados originais e coloque-os em `data/`. Os dados originais estão disponíveis em https://drive.google.com/drive/folders/1WOR75nEH4vROI2sjqv3X69ShboziCnPH?usp=sharing.

Para criar um abiente com as dependências do projeto, execute:

```bash
make setup
```

Acesse a pasta `notebooks/` e execute, em ordem:

1. `ons_preparing.ipynb`: Preparação dos dados da ONS.
2. `inmet_preparing.ipynb`: Preparação dos dados do INMET.
3. `integrating.ipynb`: Contrução do dataset final integrando os dados preparados da ONS e do INMET.

## Decisões de Projeto

- A granularidade é diária, no horário de Brasília (UTC-3). Os horários dos datasets do INMET foram convertidos para UTC-3 antes de extrair as datas e agregamos cada estação por dia (chuva total, temperatura máxima e mínima, rajada máxima), exigindo ao menos 18 horas válidas.

- O período para a análise é de 2021-01-01 a 2025-12-31. O ano de 2026 foi desconsiderado por conter dados parciais.

- Apenas as estações do INMET com pelo menos 80% dos dias válidos no período são considerados. Isso evita que uma estação nova, com poucos dados disponíveis, seja considerada na análise.

- Feriados são identificados a partir da biblioteca `holidays`.  Feriados nacionaias, pontos facultativos nacionais e a fração dos três estados em feriado no dia são considerados para identificar feriados estaduais. Feriados municipais ficam de fora, porque não há como associá-los a um único município do subsistema.

## Conjunto de dados final

Há um registro por dia, totalizando 1826 registros. Na tabela abaixo, estão listadas as colunas do conjunto de dados final e para que serão utilizas:

| Grupo | Colunas | Uso |
|---|---|---|
| Chave | `data` | Índice |
| Calendário | `feriado_nacional`, `ponto_facultativo`, `frac_estados_feriado`, `dia_semana`, `mes` | Variáveis preditoras |
| Observações | `n_perturbacoes`, `mw_interrompido`, `chuva_media`, `chuva_max`, `temp_max_media`, `temp_min_media`, `rajada_max` | Análise |

## Limitações conhecidas

- Os indicadores CIPER e SM são mensais e anuais, portanto ainda não estão integrados. Eles serão utilizados na análise sazonal da segunda pergunta, em uma tabela mensal à parte.
- Indicadores econômicos não foram incluídos.
