'''
Isso é um bloco de comentário. 

>PO (Como dono do negócio): Levantar as necessidades da padaria, definir prioridades e acompanhar o desenvolvimento.

>QA (Como cliente):Testar o sistema, verificar se tudo está funcionando corretamente e registrar possiveis erros.

>TECH (Como programador): Definir a estrutura técnica do sistema, orientar a equipe e revisar o código.

>DEV (como programador): Desenvolver o sistema da padaria (cadastro de produtos, vendas, estoque, pedidos, etc).

>UX (Como designer de experiência do usuário): Criar telas simples e práticas para a funcionalidade dos clientes.

>IA (Como analista de dados):  Analisar os dados coletados, identificar padrões e fornecer insights para melhorar o sistema e a experiencia do usúario.
'''

# Isso é um comentário de linha. Finalmente quebramos a maldição
# print('Olá, mundo!')
# print('\n---------------------\n')

p1_home = " "
p2_nome = " "
p3_nome = " "

while True:

    print('-' * 48 + '\n')
    print('Bem-vindo ao projeto de desenvolvimento de um sistema de vendas para açaiteria!\n')
    print('1 - Cadastro do cliente...')
    print('2 - Cadastro de produtos...')
    print('3 - Listar produtos...')
    print('4 - Realizar venda...')
    print('5 - Cancelar produto...')
    print('6 - Consultar estoque...')
    print('7 - Cancelar produto...')
    print('8 - Histórico de vendas...')
    print('9 - Gerar relatório de venda...')
    print('0 - Sair')

    opcao = input('Digite a opção desejada:')

    if opcao == '1':
        print('Opção 1 - Cadastrando cliente...\n')

        nome_cliente = input('Digite o nome do cliente:')
        nome_produto = input('Digite o nome do produto:')
        descricao_produto = input('Digite a descrição do produto:')
        listar_produto = input('Digite a lista do produto:')
        realizar_venda = input('Digite realizar venda:')
        cancelar_produto = input('Digite cancelar produto:')
        consultar_estoque = input('Digite consultar venda:')
        cancelar_produto = input('Digite cancelar produto:')
        historico_vendas = input('Digite histórico de vendas:')
        gerar_relatorio = input('Digite gerar relatório de venda:')

    elif opcao == '2':
        print('Opção 2 - Cadastrando produto')

    elif opcao == '3':
        print('Opção 3 - Listando produtos')

        if p1_home == " " and p2_nome == " " and p3_nome == " ":
            print('Nenhum produto cadastrado no sistema ainda.')

    elif opcao == '4':
        print('Opção 4 -Realizando venda')

    elif opcao == '5':
        print('Opção 5 - Cancelando produtos')

    elif opcao == '6':
        print('Opção 6 - Consultando estoque')

    elif opcao == '8':
        print('Opção 8 - Histórico de vendas')

    elif opcao == '9':
        print('Opção 9 - Gerando relatório de vendas')

    elif opcao == '0':
        print('Opção 0 - Sair do sistema')
        break

    else:
        print('Opção inválida')