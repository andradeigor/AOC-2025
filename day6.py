from math import prod
with open("text.txt", "r", encoding="utf-8") as f:
    linhas = [linha.rstrip("\n") for linha in f.readlines()]


largura = max(len(l) for l in linhas)
linhas = [l.ljust(largura) for l in linhas]
total =0
tokens = [] 



for col in range(largura - 1, -1, -1):

    linha = 0
    
    while linha < len(linhas) and linhas[linha][col] == " ":
        linha += 1

    if linha == len(linhas):
        continue  

    ch = linhas[linha][col]
    
    if ch.isdigit():
        token_chars = [ch]
        linha += 1
        while linha < len(linhas) and linhas[linha][col].isdigit():
            token_chars.append(linhas[linha][col])
            linha += 1
        token = "".join(token_chars)
        tokens.append(token)
    else:
        token = ch
        tokens.append(token)
    if(linhas[-1][col] =="*" or linhas[-1][col] =="+" and tokens[-1]!="+" and tokens[-1]!="*"):
                tokens.append(linhas[-1][col])
        
    
    


#print(tokens)

makeMath = []
for numbers in tokens:
    if(numbers!='*' and numbers!='+'):
        makeMath.append(int(numbers))
    elif(numbers=='*'):
        total += prod(makeMath)
        makeMath=[]
    elif(numbers=='+'):
        total += sum(makeMath)
        makeMath=[]
        
print(total)

    