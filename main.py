# n = int(input())
# arr = list(map(int, input().split()))
# max_element = max(arr)
# print(max_element)

# n = int(input())
# num_set = set()
# results = []
# for _ in range(n):
#     query = input().split()
#     if query[0] == "ADD":
#         num = int(query[1])
#         num_set.add(num)
#     elif query[0] == "PRESENT":
#         num = int(query[1])
#         if num in num_set:
#             results.append("YES")
#         else:
#             results.append("NO")
#     elif query[0] == "COUNT":
#         results.append(str(len(num_set)))
# for result in results:
#     print(result)

n = int(input())

# Словарь для хранения баллов участников
scores = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    score = int(data[1])
    scores[name] = score

# Сортируем участников по убыванию баллов
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# Вычисляем количество призеров
num_winners = max(1, min(n // 20, n // 2))

# Находим минимальный балл призера
min_winner_score = sorted_scores[num_winners - 1][1]

# Выводим результат
print(min_winner_score)
