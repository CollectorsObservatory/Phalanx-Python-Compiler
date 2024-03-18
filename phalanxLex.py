def tokenize(expression):
    tokens = [] 
    current = ''
    keywords = ["if", "else", "elif", "while", "for", "def", "true", "false", "return", "print", "and", "or", "class"]
    op_map = {
        '+': "ADDITION",
        '-': "SUBTRACTION",
        '*': "MULTIPLICATION",
        '/': "DIVISION",
        '<': "LESS",
        '>': "GREAT",
        '=': "EQUAL",
        '(': "LEFT BRACKET",
        ')': "RIGHT BRACKET",
        '<=': "LESSEQUAL",
        '>=': "GREATEQUAL",
        '!=': "NOTEQUAL",
        '==': "ASSIGN",
    }

    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isalpha():  
            current += char  #to accumluate the string to check whether or not its a keyword
            while i + 1 < len(expression) and (expression[i + 1].isalpha() or expression[i + 1].isdigit() or expression[i + 1] == '_'):
                i += 1
                current += expression[i]
            if current in keywords:
                tokens.append(("KEYWORD", current))
            else:
                tokens.append(("ID", current))
            current = ''
            
        elif char.isdigit() or char == '.':  
            current += char
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                i += 1
                current += expression[i]
            if '.' in current:
                tokens.append(("FLOAT", float(current)))
            else:
                tokens.append(("INTEGER", int(current)))
            current = ''
        else:  
            if i + 1 < len(expression) and char + expression[i + 1] in op_map:  
                tokens.append((op_map[char + expression[i + 1]] + " OP", char + expression[i + 1]))
                i += 1
            elif char in op_map: 
                tokens.append((op_map[char] + " OP", char))
        i += 1
    
    return tokens





def read_and_tokenize(file_path):

    with open(file_path, 'r') as file:
        file_content = file.read()
    tokens = tokenize(file_content)
    
    return tokens


file_path = 'test.py'


tokens = read_and_tokenize(file_path)
for token in tokens:
    print(token)

