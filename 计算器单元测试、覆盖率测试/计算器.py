import re
import sys


def conversionFormula(formula):

    # format_list = re.findall('[\w\.]+|\(|\+|\-|\*|\/|\^|\)',formula)
    format_list = re.findall('[\w\.]+|.',formula)
    # format_list = re.findall('.',formula)
    print(format_list)
    for i in format_list:
        if i.isdigit() is False and i.isalpha() is False and\
             i != '(' and i!= ')' and i!='+' and i!= '-' and\
                  i!= '*' and  i!= '/' and i!= '^':
                  print('INPUT ERROR4')
                  return 'ERROR'
    
    if format_list == []:
        print('INPUT ERROR3')
        return 'ERROR'
    switch =0
    switch2=0
    count=0
    print(format_list)
    if format_list[0] == '+' or format_list[0] == '*' or format_list[0] == '/':
        print('INPUT ERROR2')
        return 'ERROR'
    else:
        pass
    for i in format_list:
        if i == '(' or i == ')':
            switch2+=1
        
    for i in format_list:
        if i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
            switch =1
            break
    if switch != 1 :
        print('INPUT ERROR1')
        return 'ERROR'
    
    for i in format_list:
        if i == '+' or i == '-' or i == '*' or i == '/' :
            if format_list[count-1] == '+' or format_list[count-1] == '-' or\
                    format_list[count-1] == '*' or format_list[count-1] == '/' or\
                      format_list[count+1] == '+' or format_list[count+1] == '-' or\
                           format_list[count+1] == '*' or format_list[count+1] == '/' :
                 print('FORMAT ERROR')
                 return 'ERROR'
            elif i == '/' and format_list[count+1] == '0':
                
                print('VALUE ERROR')
                return 'ERROR'
        elif i.isalpha() == True:
            print('INPUT ERROR')
            return 'ERROR'
        count+=1
    if switch2 % 2 != 0:
        print('FORMAT ERROR')
        return 'ERROR'

    return format_list


def calculator(formula):    
    count = 0
    
    if formula[0] == '*' or formula[0] == '/' or formula[0] == '^':
        print('INPUT ERROR')
        return 'ERROR'

    for i in formula:

        if i == '^':
            formula[count-1]=str(float(formula[count-1])**float(formula[count+1]))
            del(formula[count])
            del(formula[count])
            return calculator(formula)

        elif i == '*':
            formula[count-1]=str(float(formula[count-1])*float(formula[count+1]))
            del(formula[count])
            del(formula[count])
            return calculator(formula)

        elif i == '/':
            formula[count-1]=str(float(formula[count-1])/float(formula[count+1]))
            del(formula[count])
            del(formula[count])
            return calculator(formula)

        count+=1

    count=0
    if formula[0]=='-':
        formula[1]=formula[0]+formula[1]
        del(formula[0])
    elif formula[0] == '+':
        del(formula[0])


    for i in formula:

        if i == '+':
            formula[count-1]=str(float(formula[count-1])+float(formula[count+1]))
            del(formula[count])
            del(formula[count])
            return calculator(formula)

        elif i == '-':  
            formula[count-1]=str(float(formula[count-1])-float(formula[count+1]))
            del(formula[count])
            del(formula[count])
            return calculator(formula)

        count+=1

    return float(formula[0])
 
def remove_bracket(formula):
    leftBracket = 0
    count = 0     #用遍历列表进行计数

    for i in formula:
        if i == '(':
            
            leftBracket=count
        elif i == ')':
            
            smallestFomula = formula[leftBracket+1:count]
            smallestFomulaAnswer = calculator(smallestFomula)          
            if isinstance(smallestFomulaAnswer,float) is True and smallestFomulaAnswer < 0:
                if formula[leftBracket-1] == '-':
                    formula[leftBracket-1] = '+'
                    temp = formula[:leftBracket]
                    temp.append(str(abs(smallestFomulaAnswer)))
                    formula = temp+formula[count+1:]
                    
                elif formula[leftBracket-1] == '+':
                    formula[leftBracket-1] = '-'
                    temp = formula[:leftBracket]
                    temp.append(str(abs(smallestFomulaAnswer)))
                    formula = temp+formula[count+1:]
                    
                else:
                    temp = formula[:leftBracket]
                    temp.append(str(smallestFomulaAnswer))
                    formula = temp+formula[count+1:]
            elif isinstance(smallestFomulaAnswer,str) is True and smallestFomulaAnswer is 'ERROR':
                return 'ERROR'
            else:
                temp = formula[:leftBracket]
                temp.append(str(smallestFomulaAnswer))
                formula = temp+formula[count+1:]
            
            return remove_bracket(formula)
        count+=1
    if formula[0] == '+':
        del(formula[0])
    return formula

if __name__ == '__main__': 
    
    formula="".join(sys.argv[1:])
    formula = conversionFormula(formula)

    if formula != 'ERROR':
        formula = remove_bracket(formula)
        if formula != 'ERROR':
            answer = calculator(formula)
            if float(answer).is_integer() == True:
                answer=int(answer)
            else:
                answer=format(answer,'.10f')
                answer=float(str(answer).rstrip('0'))
            print(answer)
    else:
        pass
