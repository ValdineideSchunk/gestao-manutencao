
# Registro de Prompts — Gestão de Manutenção

## 1. Objetivo

Este documento registra a utilização de inteligência artificial como ferramenta de apoio ao desenvolvimento do sistema acadêmico Gestão de Manutenção, desenvolvido para a disciplina de Banco de Dados da FAESA.

A ferramenta foi utilizada como apoio para esclarecimento de dúvidas, desenvolvimento de código, testes e documentação. As soluções foram aplicadas e verificadas progressivamente no ambiente Linux com Python, Flask e Oracle Database.

## 2. Prompts utilizados

### 2.1. Desenvolvimento da aplicação

**Objetivo:** estruturar a aplicação web e organizar suas funcionalidades.

**Solicitação:**
Auxiliar no desenvolvimento de um sistema de Gestão de Manutenção utilizando Python, Flask, Oracle Database, HTML e CSS, com separação entre modelos, controladores e páginas.

### 2.2. Cadastro de equipamentos

**Objetivo:** implementar as operações de gerenciamento de equipamentos.

**Solicitação:**
Auxiliar na implementação das funcionalidades de cadastro, listagem, edição e exclusão de equipamentos, utilizando consultas SQL parametrizadas e conexão com Oracle.

### 2.3. Cadastro de técnicos

**Objetivo:** implementar o gerenciamento de técnicos responsáveis pelas manutenções.

**Solicitação:**
Auxiliar na criação das operações de cadastro, consulta, atualização e exclusão de técnicos, integradas ao banco de dados Oracle.

### 2.4. Registro de manutenções

**Objetivo:** registrar serviços realizados nos equipamentos.

**Solicitação:**
Auxiliar no desenvolvimento do módulo de manutenções, relacionando equipamentos e técnicos e registrando data, descrição e custo do serviço.

### 2.5. Relatório de custos por equipamento

**Objetivo:** produzir uma consulta sumarizada para análise dos custos.

**Solicitação:**
Criar uma consulta SQL que apresente a quantidade de manutenções e o custo total por equipamento, utilizando COUNT, SUM, NVL, LEFT JOIN e GROUP BY.

### 2.6. Histórico detalhado de manutenções

**Objetivo:** apresentar informações relacionadas de diferentes tabelas.

**Solicitação:**
Criar uma consulta SQL com JOIN entre MANUTENCAO, EQUIPAMENTO e TECNICO, retornando a data, o equipamento, o técnico responsável, a descrição e o custo de cada manutenção.

### 2.7. Testes e depuração

**Objetivo:** verificar o funcionamento das funcionalidades implementadas.

**Solicitação:**
Auxiliar na elaboração e execução de testes para validar as rotas Flask, as consultas Oracle e a exibição dos dados nas páginas HTML, identificando possíveis erros de integração.

### 2.8. Documentação do projeto

**Objetivo:** organizar os materiais de documentação necessários para a entrega acadêmica.

**Solicitação:**
Auxiliar na elaboração do README e do diagrama relacional, utilizando a estrutura real das tabelas, chaves primárias e chaves estrangeiras do banco de dados.

## 3. Validação das soluções

As sugestões geradas foram aplicadas gradualmente e verificadas no ambiente de desenvolvimento. Os testes realizados incluíram consultas ao banco Oracle, validação das rotas Flask e conferência dos dados exibidos no navegador.

A utilização da ferramenta teve caráter de apoio. A equipe deve revisar, compreender e validar o código e a documentação antes da entrega.

## 4. Observação

Este registro resume os principais tipos de solicitações utilizados durante o desenvolvimento. Ele não representa uma transcrição literal e integral de todas as conversas realizadas com a ferramenta.
