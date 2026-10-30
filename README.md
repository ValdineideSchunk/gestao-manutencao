# Gestão de Manutenção

Sistema acadêmico para gerenciamento de equipamentos, técnicos e manutenções, desenvolvido para a disciplina de Banco de Dados da FAESA.

## Funcionalidades

- Cadastro, consulta, edição e exclusão de equipamentos.
- Cadastro, consulta, edição e exclusão de técnicos.
- Cadastro, consulta, edição e exclusão de manutenções.
- Relatório de custos e quantidade de manutenções por equipamento.
- Histórico detalhado de manutenções com informações de equipamentos e técnicos.

## Tecnologias utilizadas

- Python 3
- Flask
- Oracle Database XE 21c
- Biblioteca `oracledb`
- HTML e CSS

## Estrutura do projeto

- `app.py`: aplicação Flask e registro das rotas.
- `config.py`: configuração e conexão com o banco Oracle.
- `models/`: consultas SQL e operações de acesso aos dados.
- `controllers/`: rotas e controle das funcionalidades.
- `templates/`: páginas HTML renderizadas pelo Flask.
- `static/css/`: estilos da interface.
- `sql/criar_tabelas.sql`: script de criação das tabelas e dos relacionamentos.
- `docs/`: documentação e diagrama relacional.
- `teste_config.py`: teste da conexão com o banco.
- `executar_sql.py`: execução do script de criação das tabelas.

## Pré-requisitos

- Máquina virtual Linux utilizada na disciplina.
- Python 3.
- Docker e Docker Compose.
- Oracle Database XE 21c configurado para uso do projeto.

## Como executar no Linux

### 1. Iniciar o banco Oracle

Em um terminal, execute:

cd ~/database_services
docker compose up -d oracle

Aguarde o banco estar pronto para receber conexões.

### 2. Acessar o projeto

Em outro terminal, execute:

cd ~/gestao-manutencao

### 3. Criar e ativar o ambiente virtual

Caso ainda não exista um ambiente virtual:

python3 -m venv .venv

Ative o ambiente virtual:

source .venv/bin/activate

### 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

pip install -r requirements.txt

### 5. Configurar a senha do banco

Defina a variável de ambiente `ORACLE_PASSWORD` com a senha configurada para o usuário Oracle utilizado pela aplicação:

export ORACLE_PASSWORD='lab@Database2025'

### 6. Verificar a conexão

Execute:

python teste_config.py

O resultado esperado é:

Conexao OK

### 7. Criar as tabelas, se necessário

Em um banco novo, com o usuário e as permissões adequados, execute:

python executar_sql.py

**Atenção:** não execute esse comando novamente em um banco onde as tabelas já existem. O script cria as tabelas e não foi desenvolvido para recriá-las automaticamente.

### 8. Iniciar a aplicação

Execute:

python app.py

Mantenha o terminal aberto enquanto utilizar o sistema.

### 9. Acessar no navegador

Abra:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Telas disponíveis

- Painel inicial: `http://127.0.0.1:5000/`
- Equipamentos: `http://127.0.0.1:5000/equipamentos`
- Técnicos: `http://127.0.0.1:5000/tecnicos`
- Manutenções: `http://127.0.0.1:5000/manutencoes`
- Relatórios: `http://127.0.0.1:5000/relatorios`

## Relatórios disponíveis

### Custo de manutenção por equipamento

Apresenta a quantidade de manutenções e o custo total acumulado por equipamento, utilizando funções agregadas e agrupamento SQL (`GROUP BY`).

### Histórico detalhado de manutenções

Apresenta data, equipamento, técnico responsável, descrição e custo, utilizando junção entre tabelas (`JOIN`).

## Banco de dados

O projeto utiliza o Oracle Database XE 21c.

O script `sql/criar_tabelas.sql` cria as tabelas `EQUIPAMENTO`, `TECNICO` e `MANUTENCAO`, incluindo chaves primárias, chaves estrangeiras e restrições de integridade.

Relacionamentos:

- Um equipamento pode possuir várias manutenções.
- Um técnico pode ser responsável por várias manutenções.
- Cada manutenção está vinculada a um equipamento e a um técnico.

## Trabalho acadêmico

- **Disciplina:** Banco de Dados
- **Instituição:** FAESA
- **Professor:** Howard Roatti

### Integrantes

- Aymar Antônio Silva
- Christopher Soares Nascimento
- Lara Gabrielly da Conceição
- Nathan Lacerda do Nascimento
- Valdineide Schunk

Projeto desenvolvido para fins acadêmicos.