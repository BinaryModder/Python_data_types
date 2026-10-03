
def main():

    data = [
        {"student": "Alice", "subject": "Math", "grade": 5},
        {"student": "Bob", "subject": "Math", "grade": 4},
        {"student": "Alice", "subject": "History", "grade": 3},
        {"student": "Bob", "subject": "History", "grade": 5},
    ]

    subjects = dict()

    for element in data:
        if element.get('subject') not in subjects:
            subjects[element.get('subject')] = dict()

    for student in data:
        subjects[student.get('subject')].update({
            student.get('student'): student.get('grade')})
    print(subjects)


if __name__ == "__main__":
    main()
