expression = input()
acceptedCharacter = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","^","a","b","s","(",")"]
number = ["0","1","2","3","4","5","6","7","8","9"]
operations = ["+","-","*","/","^","a","b","s","(",")"]
functions = ["abs"]
postfixNotation = []
stackExpression = []
lastCharacter = ""
confirmed = False
parethesisCount = 0

expression = expression.replace(" ", "")
#Checks for unauthorized characters
for i in range(0,len(expression)):
    confirmed = False
    for u in range(0,len(acceptedCharacter)):
        if expression[i] == acceptedCharacter[u]:
            confirmed = True
            break
    if confirmed != True:
            print("The given expression is not a valid equation(you can't have letters in the expression")
            input()
            exit()
    if expression[i] == "a" and len(expression)>i+2 and len(expression)>i+1:
        if expression[i+1]!="b" or expression[i+2]!="s":
            print("The given expression is not a valid equation(you can't have letters in the expression")
            input()
            exit()
    if expression[i] == "b" and len(expression)>i+1 and i>1:
        if expression[i-1]!="a" or expression[i+1]!="s":
            print("The given expression is not a valid equation(you can't have letters in the expression")  
            input()
            exit()      
    if expression[i] == "s" and i>2:
        if expression[i-2]!="a" or expression[i-1]!="b":
            print("The given expression is not a valid equation(you can't have letters in the expression")
            input()
            exit()
    if expression[i]=="(":
        parethesisCount+=1
    if expression[i]==")":
        parethesisCount-=1
if parethesisCount!=0:
        print("The given expression is not a valid equation(Theres is not an even amount of parethesis)")
        input()
        exit()



for i in range(0,len(operations)):
    if expression[-1]==operations[i] and expression[-1] != operations[-1] and expression[-1] != operations[-2]:
            print("The given expression is not a valid equation(You can't end in a operator)")
            input()
            exit()

#Checks if theres any ilegal expression while at the same time putting it in postfix
for i in range(0, len(expression)):
    for u in range(0, len(number)):
        if expression[i] == number[u]:
            if i-1>-1:
                lastCharacterInt = False
                for p in range(0, len(number)):
                    if expression[i-1] == number[p]:
                        postfixNotation.pop()
                        postfixNotation.append(lastCharacter+expression[i])
                        lastCharacter = postfixNotation[-1]
                        lastCharacterInt = True
                if lastCharacterInt == False:
                    postfixNotation.append(expression[i])
                    lastCharacter = postfixNotation[-1] 

            else:
                postfixNotation.append(expression[i])
                lastCharacter = postfixNotation[-1]   
    for u in range(0, len(operations)):
        if expression[i] == operations[u]:
            if i > 0 and expression[i-1] == operations[u] and expression[i] != operations[-1] and expression[i] != operations[-2] and expression[i] != operations[-3]:
                print("The given expression is not a valid equation(you can't have two operators in a row)")   
                print("(At character ", i , ", theres a ", expression[i-1], ", and at character", i+1, ", theres a", expression[i])   
                input()
                exit()
            else:
                if expression[i] == "+" or expression[i] == "-":
                    if len(stackExpression) > 0 and (stackExpression[-1] == "*" or stackExpression[-1] == "/" or stackExpression[-1] == "+" or stackExpression[-1] == "-" or stackExpression[-1] == "^" or stackExpression[-1] == "abs" ):
                        while len(stackExpression) > 0 and (stackExpression[-1] == "*" or stackExpression[-1] == "/" or stackExpression[-1] == "+" or stackExpression[-1] == "-" or stackExpression[-1] == "^" or stackExpression[-1] == "abs" ):
                            postfixNotation.append(stackExpression[-1])
                            stackExpression.pop()
                        stackExpression.append(expression[i])
                    else:
                        stackExpression.append(expression[i])
                if expression[i] == "*" or expression[i] == "/":
                        if len(stackExpression) > 0 and (stackExpression[-1] == "*" or stackExpression[-1] == "/" or stackExpression[-1] == "^"):
                            postfixNotation.append(stackExpression[-1])
                            stackExpression.pop()
                            stackExpression.append(expression[i])
                        else:
                            stackExpression.append(expression[i])
                if expression[i] == "(":
                     stackExpression.append(expression[i])
                if expression[i] == ")":
                    while stackExpression and (stackExpression[-1] != "("):
                        postfixNotation.append(stackExpression.pop())

                    # Verifica se o anterior ao '(' é 'abs'
                    if len(stackExpression) >= 2 and stackExpression[-2] == "abs":
                        print("Its absolute")
                        stackExpression.pop()  # Remove o '('
                        postfixNotation.append(stackExpression.pop())  # Remove e envia o 'abs'
                    elif stackExpression and stackExpression[-1] == "(":
                        stackExpression.pop()
                if expression[i] == "^":
                    if len(stackExpression) > 0 and (stackExpression[-1] == "^" or stackExpression[-1] == ")"):
                        postfixNotation.append(stackExpression[-1])
                        stackExpression.pop()
                        stackExpression.append(expression[i])
                    else:
                        stackExpression.append(expression[i])
                if expression[i] == "a":
                    stackExpression.append("abs")
                print(postfixNotation)
                print(stackExpression)
                input()

                     
while stackExpression:
    postfixNotation.append(stackExpression.pop())


postfixNotation = [item for item in postfixNotation if item not in ("(", ")")]
print(postfixNotation)
input()
#Uses the postfix notation to calculate the result
i=0
while len(postfixNotation)>1:
        if postfixNotation[i] == "+":
            postfixNotation[i]=str(float(postfixNotation[i-1]) + float(postfixNotation[i-2]))
            del postfixNotation[i-1]
            i-=1
            del postfixNotation[i-1]
            i-=1
        if postfixNotation[i] == "-":
            postfixNotation[i]=str(float(postfixNotation[i-2]) - float(postfixNotation[i-1]))
            del postfixNotation[i-1]
            i-=1
            del postfixNotation[i-1]
            i-=1
        if postfixNotation[i] == "*":
            postfixNotation[i]=str(float(postfixNotation[i-1]) * float(postfixNotation[i-2]))
            del postfixNotation[i-1]
            i-=1
            del postfixNotation[i-1]
            i-=1
        if postfixNotation[i] == "/":
            postfixNotation[i]=str(float(postfixNotation[i-2]) / float(postfixNotation[i-1]))
            del postfixNotation[i-1]
            i-=1
            del postfixNotation[i-1]
            i-=1
        if postfixNotation[i] == "^":
            postfixNotation[i]=str(float(postfixNotation[i-2]) ** float(postfixNotation[i-1]))
            del postfixNotation[i-1]
            i-=1
            del postfixNotation[i-1]
            i-=1
        if postfixNotation[i] == "abs":
            postfixNotation[i]= str(abs(float(postfixNotation[i-1])))
            del postfixNotation[i-1]
            i-=1
        i+=1
print(postfixNotation)
input()
