'''
Дано три цілих числа. Упорядкуйте їх у порядку зростання. Програма повинна зчитувати три числа a, b, c. Далі програма повинна змінювати їх значення так, щоб стали виконані умови a ≤ b ≤ c.
Результатом роботи програми буде виведення трійки чисел a, b, c в одному рядку. При розв’язуванні задачі не можна використовувати додаткові змінні, тобто єдиною допустимою операцією присвоюванняє обмін значень двох змінних типу (a, b) = (b, a).

Токар Іван
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)
