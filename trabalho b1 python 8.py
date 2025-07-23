def gerar_impares():
    num = 1
    while num <10:
         yield num
         num +=2
    print(', '.join(str(n) for n in gerar_impares()))



 



