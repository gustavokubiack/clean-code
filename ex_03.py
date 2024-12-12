
"""
Escreva uma função que efetue as quatro operações aritméticas 
(i.e. soma, subtração, divisão e multiplição), recebendo como 
parâmetro os dois números e a operação desejada (+, -, * e /) em forma de símbolos.
"""
from dataclasses import dataclass


def calc(x, y, op):
    """
    Faz uma operação entre dois números
    """
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
        """
        Sum two numbers
        """
        return self.number1 + self.number2

    def subtraction(self):
        """
        Substract two numbers
        """
        return self.number1 - self.number2

    def divison(self):
        """
        Divide two numbers
        """
        return self.number1 / self.number2

    def multiplication(self):
        """
        Multiplicate two numbers
        """
        return self.number1 * self.number2

    def result(self):
        """"
        Return result of operation
        """
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
