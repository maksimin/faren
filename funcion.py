import re


def clear(st):
    st1 = st.replace(' ', '')
    return st1


def calck(str1):
    text_str = re.findall(r"(\d+)([\+\-\*\/]+)(\d+)", str1)
    pervoe, operation, vtoroe = text_str[0]
    result = 'None'
    if operation == '+':
        result = int(pervoe) + int(vtoroe)
    elif operation == '/':
        if vtoroe == 0:
            print("Error! zero division")
        else:
            result = int(pervoe) / int(vtoroe)
    elif operation == '-':
        result = int(pervoe) - int(vtoroe)
    elif operation == '*':
        result = int(pervoe) * int(vtoroe)
    return result


def explode(st):
    operators = ['+', '-', '*', '/']
    for operator in operators:
        st2 = st.split(operator, 2)
        if len(st2) == 2:
            st2 = [str(parse(i)) for i in st2]
            return calck(operator.join(st2))


def legkoe(str1):
    st = re.fullmatch(r"(\d+)([\+\-\*\/]+)(\d+)", str1)
    return st


def prosto(str1):
    st = re.fullmatch(r"(\d+)", str1)
    return st


def parse(str1):
    if legkoe(str1):
        return calck(str1)
    elif prosto(str1):
        return str1[0]
    else:
        return explode(str1)
