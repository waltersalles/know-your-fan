# Know Your Fan - Desafio FURIA

Este repositório contém a solução para o **Challenge #2 - Know Your Fan** do processo seletivo para a vaga de Assistente de Engenharia de Software da FURIA Tech. O objetivo deste desafio foi desenvolver uma aplicação para coletar informações sobre os fãs de eSports, proporcionando uma experiência personalizada e relevante.

## Descrição

O projeto é uma aplicação que simula a coleta de dados de fãs de eSports, focando nos fãs do time FURIA. A aplicação permite realizar as seguintes funcionalidades:

- Coleta de dados básicos do usuário, como nome, CPF e interesses.
- Validação do CPF.
- OCR (Reconhecimento Óptico de Caracteres) para ler documentos de identificação (simulado).
- Armazenamento das informações do usuário localmente.

A ideia é fornecer uma solução que ajude a FURIA a conhecer melhor seus fãs e personalizar experiências e serviços.

## Funcionalidades Implementadas

### 1. Coleta de Dados
A aplicação permite que o usuário insira informações básicas, como:
- Nome completo
- CPF
- Interesses e atividades relacionadas ao eSports

### 2. Validação de CPF
Utilizando um script simples de validação, a aplicação garante que o CPF fornecido seja válido, conforme as regras do CPF no Brasil.

### 3. OCR de Documento
Embora não tenha sido feita a integração real com OCR para o reconhecimento de documentos, a estrutura foi preparada para a leitura de imagens de documentos utilizando a biblioteca **pytesseract** (simulada para este desafio).

### 4. Armazenamento Local
Os dados fornecidos pelo usuário são armazenados localmente para simulação do processo de armazenamento de informações em um sistema real.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal utilizada para o desenvolvimento da aplicação.
- **Flask**: Framework utilizado para criação da aplicação web.
- **pytesseract**: Biblioteca para realizar OCR (simulado).
- **Validator**: Biblioteca para validação de CPF.

## Como Rodar o Projeto

### Requisitos

Antes de rodar o projeto, você precisa ter o Python instalado na sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

Além disso, é necessário instalar as dependências do projeto. Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt

Rodando a Aplicação
Após instalar as dependências, você pode rodar a aplicação com o comando:
python app.py
