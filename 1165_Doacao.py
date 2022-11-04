#Ao perceber que um de seus amigos estava com dificuldades financeiras,
#Victória, uma garota muito inteligente, decidiu ajudá-lo com uma
#"vaquinha digital", em que todos poderiam doar quanto pudessem para ajudar seuamigo.
#Para isso, Victória criou uma criptomoeda, a Vic Coin,
#em que cada unidade equivale à R$ 2,50. Assim, os doadores primeiro compram
#a criptomoeda e, em seguida, depositam uma parte delas para doação.
#A parte que não foi doada pode ficar guardada em uma carteira digital e poderá
#ser usada no futuro para outras doações. Genial!
#Victória está ocupada implementando o que é necessário para o funcionamento do
#ambiente de doações, por isso pediu para que você a ajudasse com uma das partes
#essenciais: a contabilização de doações e a conversão para reais.
#Seu objetivo é criar um programa que receba como entrada diversas doações feitas
#em Vic Coin e, ao final, exiba o total de doações em Vic Coin (VC$) e o
#total convertido para reais (R$).

#ENTRADA
#Diversos números reais, um por linha, que representam os valores das doações feitas em Vic Coin.
#A entrada é finalizada quando o número -1.0 for lido e, evidentemente,
#não deverá ser contabilizado como doação.

#SAIDA
#A saída será composta de duas linhas:
#A primeira linha será um número real com duas casas decimais indicando o total
#doado em Vic Coins (VC$);
#A segunda linha será um número real com duas casas decimais indicando o total
#doado em reais (R$).

VicCoin = float(0)
soma_qtd = 0

while VicCoin != -1:
    VicCoin = float(input())
    soma_qtd += VicCoin
    if VicCoin == -1:
        soma_qtd += 1
        reais = soma_qtd * 2.50
        print(f'VC$ {soma_qtd:.2f}')
        print(f'R$ {reais:.2f}')
