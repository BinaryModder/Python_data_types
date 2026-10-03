def main():
    formatted_dict = dict()

    students = [
        {"name": "Alice", "grades": [5, 4, 5, 3]},
        {"name": "Bob", "grades": [4, 4, 4, 5]},
        {"name": "Charlie", "grades": [5, 5, 5, 5]},
    ]
    for student in students:
        average_grade = sum(student.get('grades'))
        average_grade /= len(student.get('grades'))
        formatted_dict[student.get('name')] = average_grade
    print(
        f'Best Student : ', sorted(formatted_dict.items(), key=lambda wrd: wrd[1])[len(formatted_dict) - 1])


if __name__ == "__main__":
    main()
