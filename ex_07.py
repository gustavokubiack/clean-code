"""
Evite funções com um grande número de parâmetros. 
Refatore para usar classes ou dicionários.
"""

def create_person(person_data: dict):
    """
    Create person
    """
    for key, value in person_data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    _person_data = {
        "name": "Gustavo",
        "age": 20,
        "country": "Brasil",
        "job": "Full Stack Developer",
        "email": "gustavo@gmail.com",
    }
    create_person(_person_data)
