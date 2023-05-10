import math
# print(2.7 / 2)
# print(2 / 4 - 1)
# print(2 // - 1)
# print((2 + 5) % 3)
# print(2 + 5 % 3)
# print(3 * 4 // 6)
# print(3 * (4 // 6))
# print(3 * 2 ** 2)
# print(3 ** 2 * 2)
# print(9 + 6j / 2)
# print(2 ** -2)
# print(-7 // 4)
# print(-7 % 4)
# print(complex(4, 5).conjugate().imag)
# print(abs(complex(5, -4)) == math.hypot(4, 5))


# 2.2.7
# a, b = 2, 6
# print(3 * (a ** 3 * b - a * b ** 3) % 7)
# a, b = 3, 5
# print(3 * (a ** 3 * b - a * b ** 3) % 7)


# 32.2.2.
# print(math.sin(2017 * 2 ** (1 / 5)))
# print((math.pi + 20) ** complex(0, 1))
# print(math.hypot(1.5 * 10 ** 200, 3.5 * 10 ** 201))
# print(math.sqrt((1.5 * 10 ** 200) ** 2 + (3.5 * 10 ** 201) ** 2))


# a = 6378137.0
# c = 6356742.314245
# e = math.sqrt(1 - (c ** 2 / a ** 2))
# print(2 * math.pi * a ** 2 * (1 + ((1 - e ** 2) / e) * math.atanh(e)))
# print(4 * math.pi * 6371000 ** 2)


# 2.4.4
# s = 0
# k = 0
# for i in range(3, 43, 2):
#     k += 1
#     if k % 2 == 0:
#         s -= 1 / (i * 3 ** k)
#     else:
#         s += 1 / (i * 3 ** k)
# s = 1 - s
# s = s * math.sqrt(12)
# print(s)


# 2.5.1
# a = [3, 6, 9]
# a_normal = []
# min_n = min(a)
# max_n = max(a)
# spread = max_n - min_n
# for i in a:
#     a_normal.append((i - min_n) / spread)
# print(a_normal)


# 32.5.3
# card_number = '2200 4803 5648 3014'
# transformed_number = ''.join(card_number[::-1].split())
# digit_arr = []
# for i in transformed_number:
#     digit_arr.append(int(i))
# d_sum = 0
# for number in range(len(digit_arr)):
#     if (number + 1) % 2 == 0:
#         digit_arr[number] *= 2
#         if digit_arr[number] > 9:
#             digit_arr[number] = digit_arr[number] // 10 + digit_arr[number] % 10
#     d_sum += digit_arr[number]
# print("Y" if d_sum % 10 == 0 else "N")


# 32.5.4
# x0 = 0
# x = 2000
# S = 2117519.73
# for i in range(10):
#     x = 0.5 * (x + S/x)
#     if abs(x - x0) < 0.01:
#         break
#     x0 = x
# print(math.sqrt(S), x, abs(math.sqrt(S) - x))


# 32.5.7
# def calculate_length_heighth(a, v):
#     return f"Дальность - {(v ** 2 * math.sin(2 * a)) / 9.81}\nВысота - {(v ** 2 * math.sin(2 * a)) / (2 * 9.81)}"

# print(calculate_length_heighth(math.pi / 6, 10))


# def egg(m, t0, ty):
#     return ((m ** (2 / 3) * 3.7 * 1.038 ** (1 / 3)) / (5.4 * 10 ** -3 * math.pi ** 2 * (4 * math.pi / 3) ** (2 / 3))) * math.log(0.76 * ((t0 - 100) / (ty - 100)))

# print(egg(50, 20, 65))


# s = 0
# for i in range(1, 2024):
#     s += (-1) ** i * 1000
# print(-s)