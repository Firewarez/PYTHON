
while (True):
    C = float(input("Digite a temperatura em graus celsius: "))
    tempFare = (C * 9/5) + 32 
    tempKelvin = C + 273.15
    tempInput = input("Escolha a temperatura em Kelvin(k) ou Fareheint(f): ")

    if "F" == tempInput.upper():
        print(f"A temperatura em Fareiheint é de: {tempFare}")
        
    elif "K" == tempInput.upper():
        print(f"A temperatura em Kelvin é de: {tempKelvin}")
        
    else:
        print("Formato Invalido")  
        continue
    
    sairApp = input("Deseja Sair da aplicação, S ou N? : ")
    if sairApp.upper() == "S":
        break
    

