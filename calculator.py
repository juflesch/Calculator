# Here is a small problem for you:
# You will have to use list and dictionary to create a tool, which will take input like
# (* (+ 3 4) 2) and return the answer like 14. The four valid operators are + - / *.
# Every operator will need two operands to work on. Another input (* 2 3) and the output is 6.

from operator import add
from operator import sub
from operator import mul
from operator import truediv
from ast import literal_eval

operators = {
  '+': add,
  '-': sub,
  '*': mul,
  '/': truediv
}

def lister(lista):
    if isinstance(lista[1], list):
        new = lister(lista[1])
        lista.remove(lista[1])
        lista.insert(1, new)
    if isinstance(lista[2], list):
        new = lister(lista[2])
        lista.remove(lista[2])
        lista.insert(2, new)
    numero = operators[lista[0]](lista[1], lista[2])
    return numero

# Convert a string with parentheses into nested list
# expression = '(* (+ 3 4) 2)'
expression = input("Enter your operation: ")
expression = expression.replace('(',"[").replace(')',"]").replace(' ',', ')
expression = expression.replace("+","'+'").replace("-","'-'").replace("*","'*'").replace("/","'/'")
expression = literal_eval(expression)

# Enquanto temos expressões dentro da lista
# type() -> 'str' 'list' ou 'int'
oper = expression.copy()
numero = 0

# quase como uma arvore até todos os nodos da arvore serem int?
if isinstance(oper[1], list):
    lista = oper[1]
    newval = lister(oper[1])
    oper.remove(oper[1])
    oper.insert(1, newval)

if isinstance(oper[2], list):
    lista = oper[2]
    newval = lister(oper[2])
    oper.remove(oper[2])
    oper.insert(2, newval)

numero = operators[oper[0]](oper[1], oper[2])
print(numero)
