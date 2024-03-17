def tokenize(expression) : 
    tokens = [] 
    number = ''
    keywords = ["if", "else", "elif", "while", "for", "def", "true", "false", "return"]
    
    


    
    for char in expression :
        if char.isdigit() or char=='.':
            number += char
        
        elif char in '+-*/' : 
            if number: 
                if '.' in number:
                    tokens.append(("FLOAT" , float(number)))
                else :
                    tokens.append(("INTEGER" , int(number)))
                number = ''
            
            if char == '+' :
                tokens.append(("ADDITION OP", char))
            elif char == '-' :
                tokens.append(("SUBSTRACTION OP", char))
            elif char == '*' :
                tokens.append(("MULTIPLICATION OP", char))
            elif char == '/' :
                tokens.append(("DIVISION OP", char))
            elif char == '**' :
                tokens.append(("POWER OP", char))
                
    if number:
        if '.' in number: 
               tokens.append(("FLOAT" , float(number)))
        else :
            tokens.append(("INTEGER" , int(number)))
            number = ''
    
    return tokens


expression = "1.2 + 1.3 + 9 - 4"
expression2 = "while"
tokens = tokenize(expression2)

for token in tokens: 
    print(token)
                
               
                  
               
                  
                
                    
        
                