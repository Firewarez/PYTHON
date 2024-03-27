pizza1 = 25.2
pizza2 = 28.98
chope = 2.80
valor_pizza1 = int(input("Quantas pizzas normais foram comidas?: "))
valor_pizza2 = int(input("Quantas pizzas especiais foram comidas?: "))
valor_chope = int(input("Quantos chopes foram bebidos?: "))
pessoas = int(input("Quantas pessoas estavam na mesa?: "))
total = (pizza1 * valor_pizza1) + (pizza2 * valor_pizza2) + (chope * valor_chope) / 10
pagar = total / pessoas
gorgeta = total / 10

print(f"O valor total da conta foi de R$ {total}, \n cada pessoa deve pagar R$ {pagar} \n e a gorgeta foi de R$ {gorgeta}")