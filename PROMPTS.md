# Registro de Prompts — Gestão de Manutenção

## 1. Objetivo

Este documento registra a utilização de inteligência artificial como ferramenta de apoio ao desenvolvimento do sistema acadêmico **Gestão de Manutenção**, desenvolvido para a disciplina de Banco de Dados da FAESA.

A ferramenta foi utilizada como apoio para esclarecimento de dúvidas, elaboração e revisão de código, desenvolvimento de consultas SQL, resolução de problemas, testes e documentação.

As sugestões recebidas foram analisadas e adaptadas às necessidades do projeto, sendo aplicadas e verificadas progressivamente no ambiente Linux com Python, Flask e Oracle Database XE 21c.

O objetivo deste registro é garantir transparência sobre a utilização de inteligência artificial durante o desenvolvimento, documentando os principais prompts, suas finalidades e a forma como as respostas foram aproveitadas pela equipe.

## 2. Ferramenta de inteligência artificial utilizada

- **Ferramenta:** ChatGPT
- **Desenvolvedora:** OpenAI
- **Finalidade:** Apoio técnico e acadêmico durante as etapas de desenvolvimento, implementação, testes e documentação do sistema.

## 3. Registro dos prompts utilizados

Os registros abaixo representam as principais solicitações realizadas durante o desenvolvimento. Os textos foram organizados e consolidados para facilitar a documentação, não sendo necessariamente transcrições literais e integrais das conversas originais.

### 3.1. Desenvolvimento e estruturação da aplicação

**Objetivo:** Estruturar a aplicação web e organizar suas funcionalidades.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar no desenvolvimento de um sistema acadêmico de Gestão de Manutenção utilizando Python, Flask, Oracle Database, HTML e CSS, com separação de responsabilidades entre modelos, controladores e páginas da aplicação.

**Como a resposta foi utilizada:**

As orientações foram utilizadas como apoio na organização da estrutura do projeto, na criação dos arquivos principais e na separação das responsabilidades entre as camadas `models`, `controllers` e `templates`.

A equipe adaptou a estrutura sugerida às necessidades do sistema e ao ambiente disponibilizado para a disciplina.

### 3.2. Cadastro e gerenciamento de equipamentos

**Objetivo:** Implementar as operações de gerenciamento de equipamentos.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar na implementação das funcionalidades de cadastro, listagem, edição e exclusão de equipamentos, utilizando consultas SQL parametrizadas e conexão com Oracle Database por meio da biblioteca oracledb.

**Como a resposta foi utilizada:**

As sugestões foram utilizadas como apoio na implementação das operações de acesso aos dados e das rotas Flask responsáveis pelo gerenciamento dos equipamentos.

Também foram utilizadas orientações para tratamento de erros, validação de informações e impedimento da exclusão de equipamentos que possuem manutenções vinculadas.

As funcionalidades foram adaptadas e testadas no ambiente de desenvolvimento.

### 3.3. Cadastro e gerenciamento de técnicos

**Objetivo:** Implementar o gerenciamento dos técnicos responsáveis pelas manutenções.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar na criação das operações de cadastro, consulta, atualização e exclusão de técnicos, integradas ao banco de dados Oracle, utilizando Python, Flask e consultas SQL.

**Como a resposta foi utilizada:**

As orientações foram aproveitadas na implementação das funções de acesso ao banco de dados, nas rotas do controlador de técnicos e nas páginas de cadastro, atualização e remoção.

Também foram utilizadas sugestões para tratar as restrições de integridade referencial, impedindo a exclusão de técnicos que possuem manutenções vinculadas.

### 3.4. Registro e gerenciamento de manutenções

**Objetivo:** Implementar o registro dos serviços realizados nos equipamentos.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar no desenvolvimento do módulo de gerenciamento de manutenções, relacionando equipamentos e técnicos e registrando informações como data, descrição e custo do serviço.

**Como a resposta foi utilizada:**

As sugestões foram utilizadas como apoio na implementação das operações de cadastro, consulta, atualização e exclusão de manutenções.

Também foram aproveitadas orientações para validação de datas, custos, identificação de equipamentos e técnicos, além do tratamento das chaves estrangeiras.

### 3.5. Relatório de custos por equipamento

**Objetivo:** Desenvolver uma consulta sumarizada para análise dos custos de manutenção.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar na elaboração de uma consulta SQL que apresente a quantidade de manutenções e o custo total acumulado por equipamento, utilizando funções agregadas, COUNT, SUM, NVL, LEFT JOIN e GROUP BY.

**Como a resposta foi utilizada:**

A consulta foi utilizada como referência para implementar o relatório de custos por equipamento.

O resultado apresenta o identificador e o nome do equipamento, a quantidade de manutenções e o custo total acumulado.

A consulta utiliza agrupamento e funções de agregação SQL, atendendo ao requisito de relatório sumarizado.

### 3.6. Histórico detalhado de manutenções

**Objetivo:** Apresentar informações relacionadas de diferentes tabelas do banco de dados.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar na elaboração de uma consulta SQL utilizando JOIN entre as tabelas MANUTENCAO, EQUIPAMENTO e TECNICO, retornando a data, o equipamento, o técnico responsável, a descrição e o custo de cada manutenção.

**Como a resposta foi utilizada:**

A consulta foi utilizada como referência para implementar o relatório de histórico detalhado de manutenções.

Foram aproveitados os relacionamentos entre as três tabelas para apresentar informações completas sobre cada serviço registrado.

### 3.7. Testes, validação e depuração

**Objetivo:** Verificar o funcionamento das funcionalidades implementadas e identificar possíveis problemas.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar na elaboração e execução de testes para validar as rotas Flask, as consultas Oracle, a persistência dos dados e a exibição das informações nas páginas HTML, identificando possíveis erros de integração.

**Como a resposta foi utilizada:**

As orientações foram utilizadas durante a investigação e correção de problemas relacionados à conexão com o Oracle, execução de consultas SQL, funcionamento das rotas e integração entre modelos, controladores e páginas.

Também foram realizadas verificações práticas no navegador e no ambiente Linux para confirmar o funcionamento das funcionalidades.

### 3.8. Documentação do projeto

**Objetivo:** Organizar os materiais de documentação necessários para a entrega acadêmica.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar na elaboração e revisão da documentação do sistema, incluindo README, instruções de execução no Linux, documentação do banco de dados e diagrama relacional, considerando a estrutura real das tabelas, chaves primárias e chaves estrangeiras.

**Como a resposta foi utilizada:**

As sugestões foram utilizadas como apoio na organização do README, na descrição das tecnologias utilizadas, na documentação da estrutura do projeto e nas instruções necessárias para executar a aplicação no ambiente Linux.

A documentação foi adaptada de acordo com a estrutura e os recursos efetivamente utilizados no projeto.

### 3.9. Implementação dos fluxos de cadastro, atualização e exclusão

**Objetivo:** Melhorar a navegação e atender aos requisitos de interação definidos no edital.

**Fonte:** ChatGPT — OpenAI.

**Prompt registrado:**

Auxiliar na implementação dos fluxos de cadastro, atualização e exclusão de equipamentos, técnicos e manutenções, incluindo telas de confirmação, mensagens de sucesso e tratamento de erros.

**Como a resposta foi utilizada:**

As orientações foram utilizadas para implementar telas de confirmação após operações realizadas com sucesso, permitindo ao usuário escolher entre realizar uma nova operação ou retornar ao menu principal.

Também foram aproveitadas sugestões para melhorar o tratamento de erros de integridade referencial e a apresentação das mensagens ao usuário.

## 4. Validação das soluções

As sugestões geradas pela ferramenta de inteligência artificial foram analisadas e aplicadas gradualmente durante o desenvolvimento.

A equipe realizou verificações práticas no ambiente Linux, incluindo:

- Testes de conexão com o Oracle Database XE 21c.
- Execução e validação de consultas SQL.
- Verificação da persistência dos registros no banco de dados.
- Testes das operações de cadastro, consulta, atualização e exclusão.
- Verificação das restrições de integridade referencial.
- Testes das rotas da aplicação Flask.
- Conferência das informações apresentadas nas páginas HTML.
- Verificação dos relatórios e agrupamentos de dados.

As respostas da ferramenta foram utilizadas como apoio, sendo necessário revisar, compreender, adaptar e validar as soluções antes de sua utilização no projeto.

## 5. Participação da equipe

A inteligência artificial foi utilizada como ferramenta complementar de apoio ao desenvolvimento.

A responsabilidade pela análise dos requisitos, tomada de decisões, integração dos componentes, validação das funcionalidades e organização da entrega permaneceu com os integrantes da equipe.

Todos os integrantes devem compreender as funcionalidades implementadas e estar preparados para explicar o funcionamento do sistema durante a apresentação.

## 6. Versionamento e histórico de alterações

Este documento deve acompanhar a evolução do projeto, registrando as principais alterações realizadas na documentação dos prompts.

| Versão | Descrição | Data |
|---|---|---|
| 1.0 | Registro inicial dos principais usos de inteligência artificial durante o desenvolvimento. | 30/10/2026 |
| 1.1 | Ampliação dos registros, identificação da ferramenta utilizada e inclusão da descrição de como as respostas foram aplicadas. | 30/10/2026 |

As alterações futuras neste documento deverão ser registradas por meio de novas versões e commits no repositório GitHub.

## 7. Observações finais

Este documento apresenta uma consolidação dos principais usos de inteligência artificial durante o desenvolvimento do sistema Gestão de Manutenção.

Os prompts registrados representam as principais categorias de solicitações realizadas e não substituem o histórico integral das conversas com a ferramenta.

A utilização de inteligência artificial teve caráter de apoio técnico e acadêmico, não substituindo a participação, a análise crítica e a responsabilidade dos integrantes da equipe pelo desenvolvimento do projeto.

O código-fonte e as soluções implementadas devem ser compreendidos e validados pela equipe antes da entrega final.