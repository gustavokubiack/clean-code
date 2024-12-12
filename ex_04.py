
"""
Escreva um programa que armazene as oito notas e os nomes dos estudantes da disciplina de POO II. 
Calcule a média da turma e imprima os nomes e as notas daqueles ficaram acima da média.

# armazena os nomes e as notas dos alunos em uma sequência
alunos = "Ana", "Bruno", "Carla", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena"
notas = 8.5, 7.0, 9.0, 6.5, 10.0, 8.0, 7.5, 9.5

"""
from dataclasses import dataclass
from typing import List, Dict 

@dataclass
class CalculateGrades:
    """
    Calculate grades and average of students
    """
    students: List[Dict[str, float]]

    def get_grade(self, student: dict) -> dict:
        """
        Get grade of student
        """
        return student["grade"]

    def show_students_above_average(self, student: dict, average: float):
        """
        Print students that grade is above average
        """
        if student["grade"] > average:
            print(f"{student['name']}: {student['grade']}")


students = [
    {
        "name": "Ana",
        "grade": 8.5  
    },
    {
        "name": "Bruno",
        "grade": 7.0  
    },
    {
        "name": "Carla",
        "grade": 9.0  
    },
    {
        "name": "Daniel",
        "grade": 6.5  
    },
    {
        "name": "Eduardo",
        "grade": 10.0  
    },
    {
        "name": "Fernanda",
        "grade": 8.0  
    },
    {
        "name": "Gabriel",
        "grade": 7.5  
    },
    {
        "name": "Helena",
        "grade": 9.5  
    },
]


instance = CalculateGrades(students)
grades = list(map(instance.get_grade, students))
_average = sum(grades) / len(grades)
list(map(lambda student: instance.show_students_above_average(student, _average), students))
