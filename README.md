# Sistema-bancario
Sistema-bancario: Desafio DIO Python AI Backend Developer - Projeto Banco - 

Este projeto faz parte do Bootcamp Python AI Backend Developer e consiste na criação de um sistema bancário simples, implementado em Python. O sistema permite ao usuário realizar operações básicas como depósito, saque, visualização de extrato, cadastro de usuário, cadastro de conta bancária, listagem de contas e saída do programa.

# Funcionalidades Implementadas
Depósito:

- Permite ao usuário depositar um valor positivo na conta.
- Atualiza o saldo e registra a transação no extrato.

# Saque:

- Permite ao usuário sacar um valor, com as seguintes restrições:
- O valor do saque não pode exceder o saldo disponível.
- O valor do saque não pode exceder o limite diário de R$500.
- O número de saques diários não pode exceder três.
- Atualiza o saldo, registra a transação no extrato e incrementa o contador de saques.

# Extrato:

- Exibe todas as transações realizadas e o saldo atual da conta.
- Informa se nenhuma movimentação foi realizada caso o extrato esteja vazio.
- Cadastro de Usuário:

- Permite cadastrar novos usuários solicitando CPF, nome completo, data de nascimento e endereço.
- Verifica se o CPF já está cadastrado antes de criar um novo usuário.

# Cadastro de Conta Bancária:

- Permite criar uma nova conta bancária associada a um usuário existente.
- Solicita o CPF do usuário para verificar se o mesmo já está cadastrado.
- Listagem de Contas Bancárias:

- Exibe uma lista de todas as contas bancárias cadastradas com informações de agência, número da conta e titular.

# Sair:

- Encerra o programa.

## Atualizações Destaque

# Cadastro de Usuário:

- Nova funcionalidade: Permite cadastrar novos usuários solicitando CPF, nome completo, data de nascimento e endereço.
- Validação: Verifica se o CPF já está cadastrado antes de criar um novo usuário.
- Cadastro de Conta Bancária:

- Nova funcionalidade: Permite criar uma nova conta bancária associada a um usuário existente.
- Validação: Solicita o CPF do usuário para verificar se o mesmo já está cadastrado.
- Listagem de Contas Bancárias:

- Nova funcionalidade: Exibe uma lista de todas as contas bancárias cadastradas com informações de agência, número da conta e titular.
