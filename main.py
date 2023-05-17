records = []
for _ in range(int(input('Enter the number of students: '))):
    name = input('Enter The Name: ')
    score = float(input('Enter The score: '))
    records.append([name, score])

grades = [record[1] for record in records]

min_grade = min(grades)
grades.remove(min_grade)

if all(g == grades[0] for g in grades):
    print('There is no second lowest grade.')
else:
    second_min_grade = min(grades)

    second_min_records = []
    for record in records:
        if record[1] == second_min_grade:
            second_min_records.append(record)

    second_min_records.sort()

    for record in second_min_records:
        print(record[0])
