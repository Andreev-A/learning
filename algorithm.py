# Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
#
# def fib(n):
#     if 1 <= n <= 40:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a
#
# def fib(num):
#     prev, cur = 0, 1
#     for i in range(1, num):
#         prev, cur = cur, prev + cur
#     return cur

# Дано число 1 <= n <= 10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.
# Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
# В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа
# Фибоначчи: если 0 <= a,b <= 9 — последние цифры чисел F_i и F_i+1 соответственно, то (a+b) mod10 — последняя цифра
# числа F_i+2. Используем период Пизано.
#
# def fib_digit(n):
#     if 1 <= n <= 10 ** 7:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, (a + b) % 10
#         return a

# Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5 , необходимо найти остаток от деления n-го числа Фибоначчи на m
#
# def fib_mod(n, m):
#     list = [0, 1, 1]
#     for i in range(2, n + 2):
#         if list[i - 1] == 0 and list[i] == 1:
#             break
#         list.append((list[i - 1] + list[i]) % m)
#     out = list[n % (len(list) - 2)]
#     return out

# По данным двум числам 1 <= a, b <= 2*10^9 найдите их наибольший общий делитель.

# def gcd(a, b):
#     list, i = [a, b], 1
#     for i in range(1, max(a, b)):
#         if not list[i] and list[i - 1]:
#             break
#         list.append(list[i - 1] % list[i])
#     return max(list[i], list[i - 1])

# def gcd(a, b):
#     return gcd(b, a % b) if b else a

# a, b = map(int, input().split())
# while b:     # while b != 0
#     a, b = b, a % b
# print(a)

# По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит
# хотя бы одну из точек.
# В первой строке дано число 1<=n<=100 отрезков. Каждая из последующих n строк содержит по два числа 0<=l<=r<=10^9,
# задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек
# несколько, выведите любое из них.

# work_list = [list(map(int, input().split())) for i in range(int(input()))]
# work_list.sort(key=lambda x: x[1])
# point_list = [work_list[0][1]]
# for i in range(len(work_list) - 1):
#     if not work_list[i + 1][0] <= point_list[-1]:
#         point_list.append(work_list[i + 1][1])
# print(len(point_list))
# print(*point_list)
#
# segments = sorted([sorted(map(int,input().split())) for i in range(int(input()))], key=lambda x: x[1])
# dots = [segments.pop(0)[1]]
# for l, r in segments:
#     if l > dots[-1]:
#         dots.append(r)
# print(str(len(dots)) + '\n' + ' '.join(map(str, dots)))
#
# points = [list(map(int, input().split())) for i in range(int(input()))]
# out = []
# for p in reversed(sorted(points)):
#     if not out or out[-1] > p[1]:
#         out.append(p[0])
# print(len(out))
# print(*out)
#
# segs = sorted([[int(i) for i in input().split()] for j in range(int(input()))])
# dots = []
# while segs:
#     dots.append(segs[-1][0])
#     while segs and dots[-1] <= segs[-1][1]:
#         segs.pop()
# print(str(len(dots))+'\n'+' '.join(map(str, dots)))

a = int(input())
b = []
for i in range(1, a + 1):
    a -= i
    if a <= i:
        b.append(i + a)
        break
    b.append(i)
print(len(b))
print(*b)
