Sistema de Gerenciamento de Vendas
Requisitos Funcionais:
● Criar, visualizar, atualizar e excluir vendas.
● Cada venda deve ter um número, cliente, data e lista de itens vendidos.
Cada venda pode ter vários itens associados.
● Requisitos Não Funcionais:
Cálculo automático do total da venda.
● DER:
● Tabela "Venda" com os campos:
● ID (chave primária)
● Número
● Cliente
● Data
● Tabela "ItemVenda" com os campos:
● ID (chave primária)
● Descrição
● Quantidade
● Preço
● ID_Venda (chave estrangeira para a tabela "Venda")
Telas:
● Tela de Lista de Vendas: Exibe a lista de todas as vendas registradas,
permitindo a visualização, edição e exclusão.
● Tela de Detalhes da Venda: Mostra as informações detalhadas de uma venda
selecionada, permitindo a edição, exclusão e gerenciamento dos itens
vendidos associados.
