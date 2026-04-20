class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]
        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"

def find(self, target_points):
    found = []
    for i in range(len(self.scores)):
        if self.scores[i] == target_points:
            found.append(i)

    return found

def get_sorted(self):
    scores = self.scores[:]
    n = len(scores)
    for i in range(n):
        changed = False
        for k in range(n - 1 - i):
            if scores[k] > scores[k + 1]:
                scores[k], scores[k + 1] = scores[k + 1], scores[k]
                changed = True
        if not changed:
            break
    return scores

def main ():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    students = results.count()
    print(f"Kolik studentů psalo test:{students}")

    for i in range(students):
        j = results.scores[i]
        k = results.get_grade(i)
        index = results.find(100)
        print("Student", i, ":", j, "bodů-",k)
        print("Studenti s plným počtem bodů: {index}")
        print(f"Seřazené výsledky: {results.get_sorted()}")

results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())
print(results.get_by_index(2))
print(results.scores)
print(results.get_grade(2))
print(results.get_grade(6))
print(results.get_grade(7))