import re
def calculator(formula):
    count = 0
    for i in formula:
        if i == '*':
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


def eq_format(eq):

    '''

    :param eq: 输入的算式字符串

    :return: 格式化以后的列表，如['60','+','7','*','8']

    '''

    format_list = re.findall('[\d\.]+|\(|\+|\-|\*|\/|\)',eq)

    return format_list

if __name__ == '__main__': 
    fomula= '9-2*5/3+7/3*99/4*2998+10*568/14'
    print(eval(fomula))
    x=eq_format(fomula)
    print(calculator(x))
    print(2**3)