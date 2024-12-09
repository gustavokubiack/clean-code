from dataclasses import dataclass

"""
Escreva uma função que efetue as quatro operações aritméticas (i.e. soma, subtração, divisão e multiplição), recebendo como parâmetro os dois números e a operação desejada (+, -, * e /) em forma de símbolos.
"""

def calc(x, y, op):
    # faz uma operação entre dois números
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        return "Operação inválida"
    

@dataclass
class Calculator:
    number1: float
    number2: float
    operation: str

    def addition(self):
        return self.number1 + self.number2
    
    def subtraction(self):
        return self.number1 - self.number2
    
    def divison(self):
        return self.number1 / self.number2
    
    def multiplication(self):
        return self.number1 * self.number2

    def result(self):
        match self.operation:
            case "+":
                return self.addition()
            case "-":
                return self.subtraction()
            case "/":
                return self.divison()
            case "*":
                return self.multiplication()
            case _:
                return "Operação inválida!"

calculator = Calculator(1, 2, "+")
print(calculator.result())