def salva_transação(preço, cartão_crédito, descrição):
    file = open("transações.txt", "a")
    file.write("%16s%07d%16s\n"
               % (cartão_crédito, preço * 100, descrição))
    file.close()


itens = ["Bauru", "X Salada", "Calafrango"]
preços = [2.50, 3.0, 2.20]
rodando = True

while rodando:
    opção = 1
    for escolha in itens:
        print(str(opção) + ". " + escolha)
        opção = opção + 1
    print(str(opção) + ". Finalizar")
    escolha = int(input("Escolha uma opção: "))
    if escolha == opção:
        # escolheu a última opção Finalizar
        rodando = False
    else:
        cartão = input("Número do cartão de crédito: ")
        salva_transação(preços[escolha - 1], cartão, itens[escolha - 1])
