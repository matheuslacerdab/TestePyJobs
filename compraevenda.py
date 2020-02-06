#Função para definir o melhor dia de venda para obter lucro.
def compra_e_venda(valores):
    #Obtendo o menor valor para definir como dia de compra
    pos_compra = valores.index(min(valores))
    #Obtendo o maior valor a partir do dia de compra para definir o dia de venda.
    pos_venda = valores[pos_compra:len(valores)].index(max(valores[pos_compra:len(valores)]))

    #Se o dia de compra for igual ao ultimo dia informado não teremos como vender a ação, dessa forma não obtiremos lucro.
    if((pos_compra + 1) == len(valores)):
        print(0)
        print("Explicação: Neste caso, não há nenhuma operação que possa ser feita que dê lucro.")
    #Caso contrário informaremos qual foi o melhor cenário de lucro.
    else:
        print((pos_compra + pos_venda) + 1)
        print("Explicação: Este valor acontece quando compramos a ação no", (pos_compra + 1) ,"º dia e a vendemos no", ((pos_venda + pos_compra) + 1) ,"º dia (", valores[pos_compra + pos_venda],"-", valores[pos_compra],")")

#Número de dias
dias = int(input('Digite o número de dias: '))
i = 0
valores = []

#Recebendo os valores das ações de cada dia.
for i in range(i, dias):
    valor = float(input())
    valores.append(valor)

compra_e_venda(valores)