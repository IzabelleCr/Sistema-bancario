# Sistema-bancario
Desafio DIO Python AI Backend Developer - Projeto Banco - Parte 1

Este projeto faz parte do Bootcamp Python AI Backend Developer e consiste na criação de um sistema bancário simples, implementado em Python. O sistema permite ao usuário realizar operações básicas como depósito, saque, visualização de extrato e saída do programa.

## Funcionalidades Implementadas

### Depósito:

- Permite ao usuário depositar um valor positivo na conta.
- Atualiza o saldo e registra a transação no extrato.

### Saque:

- Permite ao usuário sacar um valor, com as seguintes restrições:
- O valor do saque não pode exceder o saldo disponível.
- O valor do saque não pode exceder o limite diário de R$500.
- O número de saques diários não pode exceder três.
- Atualiza o saldo, registra a transação no extrato e incrementa o contador de saques.

### Extrato:

- Exibe todas as transações realizadas e o saldo atual da conta.
- Informa se nenhuma movimentação foi realizada caso o extrato esteja vazio.

### Sair:

Encerra o programa.
