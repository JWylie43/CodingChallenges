#Joseph Wylie
#May 5 2021

#equation = '8*(5+1/15)-52'
#print(equation)
equation = input('Enter equation:\n')

minus = []

char = list(equation)

for e in range(len(char)):
    # if char[e] == '(' or char[e] == ')' or char[e] == '+' or char[e] == '-' or char[e] == '*' or char[e] == '/':
    if e <= len(char)-2 and char[e] != '(' and char[e] != ')' and char[e] != '+' and char[e] != '-' and char[e] != '*' and char[e] != '/':
        if char[e+1] != '(' and char[e+1] != ')' and char[e+1] != '+' and char[e+1] != '-' and char[e+1] != '*' and char[e+1] != '/':
            char[e:e+2] = [''.join(char[e:e+2])]


def solve(equation):
    if char.count('(') > 0:
        open_index = char.index('(')
        close_index = char.index(')')
    par = char[open_index+1:close_index]
    #print('par:',par)
    for x in range(len(par)):
        if par.count('*') > 0:
            mult_index = par.index('*')
            #print(mult_index)
            val = int(par[mult_index-1])*float(par[mult_index+1])
            #print(val)
            par[mult_index-1:mult_index+2] = [''.join(par[mult_index])]
            par[mult_index-1]=val
            #print(par)
        if par.count('/') > 0:
            div_index = par.index('/')
            #print(div_index)
            val = float(par[div_index-1])/float(par[div_index+1])
            #print(val)
            par[div_index-1:div_index+2] = [''.join(par[div_index])]
            par[div_index-1]=val
            #print(par)
        if par.count('+') > 0:
            mult_index = par.index('+')
            #print(mult_index)
            val = float(par[mult_index-1])+float(par[mult_index+1])
            #print(val)
            par[mult_index-1:mult_index+2] = [''.join(par[mult_index])]
            par[mult_index-1]=val
            #print('par:',par)
        if par.count('-') > 0:
            div_index = par.index('-')
            #print(div_index)
            val = float(par[div_index-1])-float(par[div_index+1])
            #print(val)
            par[div_index-1:div_index+2] = [''.join(par[div_index])]
            char[div_index-1]=val
            #print(par)

    char[open_index:close_index+1] = [''.join(char[open_index:close_index+1])]
    #print(char)
    char[open_index] = par[0]
    #print(char)

    if char.count('*') > 0:
        mult_index = char.index('*')
        #print(mult_index)
        val = float(char[mult_index-1])*float(char[mult_index+1])
        #print(val)
        #print(char)
        #print(char[mult_index-1:mult_index+2])
        char[mult_index-1:mult_index+2] = [''.join(char[mult_index:mult_index])]
        char[mult_index-1]=val
        #print(char)
        
            
    if char.count('/') > 0:
        div_index = char.index('/')
        #print(div_index)
        val = float(char[div_index-1])/float(char[div_index+1])
        #print(val)
        #print(char)
        #print(char[div_index-1:div_index+2])
        char[div_index-1:div_index+2] = [''.join(char[div_index:div_index])]
        char[div_index-1]=val
        #print(char)

    if char.count('+') > 0:
        mult_index = char.index('+')
        #print(mult_index)
        val = float(char[mult_index-1])+float(char[mult_index+1])
        #print(val)
        char[mult_index-1:mult_index+2] = [''.join(char[mult_index:mult_index])]
        char[mult_index-1]=val
        #print('char:',char)

    if char.count('-') > 0:
        #print('here')
        div_index = char.index('-')
        #print(div_index)
        val = float(char[div_index-1])-float(char[div_index+1])
        #print(val)
        char[div_index-1:div_index+2] = [''.join(char[div_index:div_index])]
        char[div_index-1]=val
        #print(char)

    print(char[0])

solve(equation)