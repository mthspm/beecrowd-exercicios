from typing import List

class Student:
    def __init__(self, id: int, height: float) -> None:
        self.id = id
        self.height = height

def getStudents() -> List[Student]:
    MAX_STUDENTS = 10
    students = []
    
    for i in range(MAX_STUDENTS):
        id = int(input(f"{i+1} Digite o codigo do aluno: "))
        height = float(input(f"{i+1} Digite a altura do aluno(cm): "))
        students.append(Student(id=id, height=height))
        
    return students

def getTallestStudent(students: List[Student]) -> Student:
    return max(students, key=lambda student: student.height)

def getShortestStudent(students: List[Student]) -> Student:
    return min(students, key=lambda student: student.height)

def printTallestAndShortest(tallest: Student, shortest: Student):
    print(f"Aluno mais alto: Codigo {tallest.id}, altura {tallest.height}cm")
    print(f"Aluno mais baixo: Codigo {shortest.id}, altura {shortest.height}cm")
    
def main():
    students = getStudents()
    tallest = getTallestStudent(students)
    shortest = getShortestStudent(students)
    printTallestAndShortest(tallest, shortest)
    
if __name__ == "__main__":
    main()