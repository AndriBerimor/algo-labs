# Задача 2.14. Доведіть співвідношення.
# Зауваження з методички: для доведення треба запропонувати алгоритм
# обчислення виразу з лівої частини, що має вказану асимптотичну оцінку.
# Нижче для кожного пункту наведено функцію та пояснення її складності.


# a) sum_{i=0}^{n} i = O(n)
def task_a(n):
    s = 0
    for i in range(n + 1):      # n + 1 ітерацій по O(1)
        s += i
    return s                     # O(n)


# b) sum_{i=0}^{n} i^2 = O(n)
def task_b(n):
    s = 0
    for i in range(n + 1):      # n + 1 ітерацій, i * i — одна операція
        s += i * i
    return s                     # O(n)


# c) sum_{i=0}^{n} a^i = O(n)
def task_c(n, a):
    s = 0
    p = 1                        # p = a^i, оновлюємо множенням на a
    for i in range(n + 1):
        s += p
        p *= a
    return s                     # O(n): не підносимо до степеня кожного разу


# d) sum_{i=0}^{n} i^i = O(n^2)
def task_d(n):
    s = 0
    for i in range(n + 1):
        p = 1
        for _ in range(i):      # i^i рахуємо за i множень
            p *= i
        s += p                   # при i = 0 маємо 0^0 = 1
    return s                     # 1 + 2 + ... + n = O(n^2) множень


# e) prod_{i=1}^{n} 1 / (1 + i) = O(n)
def task_e(n):
    r = 1.0
    for i in range(1, n + 1):   # n ітерацій по O(1)
        r *= 1 / (1 + i)
    return r                     # O(n)


# f) prod_{i=1}^{n} 1 / (1 + i!) = O(n)
def task_f(n):
    r = 1.0
    fact = 1                     # fact = i!, оновлюємо множенням на i
    for i in range(1, n + 1):
        fact *= i
        r *= 1 / (1 + fact)
    return r                     # O(n): факторіал не перераховуємо з нуля


# g) prod_{i=1}^{n} a^i / (1 + i!) = O(n)
def task_g(n, a):
    r = 1.0
    p = 1                        # p = a^i
    fact = 1                     # fact = i!
    for i in range(1, n + 1):
        p *= a
        fact *= i
        r *= p / (1 + fact)
    return r                     # O(n)


# h) prod_{i=1}^{n} 1 / (1 + i^m) = O(nm)
def task_h(n, m):
    r = 1.0
    for i in range(1, n + 1):
        p = 1
        for _ in range(m):      # i^m рахуємо за m множень
            p *= i
        r *= 1 / (1 + p)
    return r                     # n * m операцій = O(nm)


# i) prod_{i=1}^{n} 1 / (1 + i^i) = O(n^2)
def task_i(n):
    r = 1.0
    for i in range(1, n + 1):
        p = 1
        for _ in range(i):      # i^i рахуємо за i множень
            p *= i
        r *= 1 / (1 + p)
    return r                     # 1 + 2 + ... + n = O(n^2)


if __name__ == "__main__":
    n = int(input("n = "))
    a = float(input("a = "))
    m = int(input("m = "))
    print("a)", task_a(n))
    print("b)", task_b(n))
    print("c)", task_c(n, a))
    print("d)", task_d(n))
    print("e)", task_e(n))
    print("f)", task_f(n))
    print("g)", task_g(n, a))
    print("h)", task_h(n, m))
    print("i)", task_i(n))
