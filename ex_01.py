"""
Escreva uma função que calcule o salário líquido de um funcionário a partir do seu salário bruto e dos impostos aplicados. Use nomes significativos para as variáveis e a função.
"""


def f(x):
  y = 0.15 * x  # INSS
  z = 0.275 * x  # IRPF
  return x - y - z

# Example usage:
sb = 10000
sl = f(sb)
print(sl)

# ------- Nova implementação ------- #

def calculate_liquid_salary(base_salary: float) -> float:
    inss = calculate_inss(base_salary)
    irpf = calculate_irpf(base_salary)
    liquid_salary = base_salary - inss - irpf
    return liquid_salary


def calculate_inss(base_salary: float) -> float:
    return base_salary * 0.15


def calculate_irpf(base_salary: float) -> float:
    return base_salary * 0.275


base_salary = 1000.00
liquid_salary = calculate_liquid_salary(base_salary)
print(f"O salário líquido é {liquid_salary:.2f}")
