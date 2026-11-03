
grades = [4, 5, 3, 5, 4, 3, 5, 4, 5, 3]

average_grade = sum(grades) / len(grades)

only_fives = [grade for grade in grades if grade == 5]

grade_names = {
    3: "удовлетворительно",
    4: "хорошо",
    5: "отлично"
}

text_grades = [grade_names[grade] for grade in grades]

print(f"Исходные оценки: {grades}")
print(f"Средний балл: {average_grade:.2f}")
print(f"Только пятёрки: {only_fives} (всего: {len(only_fives)} шт.)")
print("Оценки в текстовом виде:")
for num, text in zip(grades, text_grades):
    print(f"  {num} -> {text}")
  
