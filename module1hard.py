grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#сортируем студентов в алфавитном порядке
sorted_students = sorted(students)
#создаём пустой словарь для хранения среднего балла студентов
students_avg_grades = {}
for student, grades_list in zip(sorted_students, grades):
    average_grade = sum(grades_list) / len(grades_list)
    students_avg_grades[student] = average_grade
print(students_avg_grades)
