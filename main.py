# Importando minhas funções
import despesas
# Loop infinito
while True:
    # Chamando a função menu
    usu_op = despesas.menu('Cadastrar Despesa',
                           'Exibir Despesas', 'Excluir Despesa', 'Sair')
    # Dependendo da escolha do usúario, umas das opções será ativada.
    if usu_op == 1:
        despesas.cadastrar()
    elif usu_op == 2:
        despesas.exibir()
    elif usu_op == 3:
        despesas.excluir()
    elif usu_op == 4:
        break
# Fim
print('-' * 50)
print('OBRIGADO POR USAR O MEU GRÁFICO DE DESPESAS'.center(50))
print('-' * 50)
