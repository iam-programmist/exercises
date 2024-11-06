# 1
# def test(a):
#     counter = 1
#     for i in range(1, a + 1):
#         for j in range(i):
#             print(counter, end=" ")
#             counter += 1
#         print()
# test(int(input()))

# 2
# def test(a):
#     while a != 1:
#         print(a, end=", ")
#         if a % 2 == 0:
#             a = a // 2
#         else:
#             a = 3 * a + 1
#     print(a)
# test(int(input()))

# 3
# def test(a):
#     divisors = [i for i in range(1, a) if a % i == 0]
#     return sum(divisors) == a

# def test1(a):
#     perfect_numbers = []
#     for i in range(1, a + 1):
#         if test(i):
#             perfect_numbers.append(i)
#     return perfect_numbers
# print(test1(int(input())))

# 4
# def test(a):
#     counter = {}
#     for i in a:
#         if i.isalpha():
#             i = i.lower()
#             if i in counter:
#                 counter[i] += 1
#             else:
#                 counter[i] = 1
#     return counter
# print(test(input()))

# 5
# def test(a):
#     words = a.split()
#     res = {}
#     counter = 0
#     for word in words:
#         if word in res:
#             res[word].append(counter)
#         else:
#             res[word] = [counter]
#         counter += 1
#     return res
# print(test(input()))

# 6
# original_dict = {'a': [1, 2], 'b': [3, 4]}
# res = {}
# for key, value_list in original_dict.items():
#     for i in value_list:
#         res[i] = key
# print(res)

# 7
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'a': 2, 'b': 3, 'c': 4}
# res = {}
# for i in dict1:
#     res[i] = dict1[i] + dict2[i]
# print(res)

# 8
# def test(a):
#     words = a.lower().split()
#     res = {}
#     for i in words:
#         if i in res:
#             res[i] += 1
#         else:
#             res[i] = 1
#     return res
# print(test(input()))

# 9
# def test(a):
#     for i in range(1, a + 1):
#         line = " " * (a - i)
#         for j in range(1, i + 1):
#             line += str(j)
#         for j in range(i - 1, 0, -1):
#             line += str(j)
#         print(line)
#     for i in range(a - 1, 0, -1):
#         line = " " * (a - i)
#         for j in range(1, i + 1):
#             line += str(j)
#         for j in range(i - 1, 0, -1):
#             line += str(j)
#         print(line)
# lines = 5
# test(lines)

# 10
# def test(a):
#     if a == 0 or a == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, a + 1):
#             result *= i
#         return result

# def test1(a):
#     total = 0
#     for i in str(a):
#         total += test(int(i))
#     return a == total

# def test2(limit):
#     res = []
#     for i in range(1, limit + 1):
#         if test1(i):
#             res.append(i)
#     return res
# print(test2(int(input())))

# 11
# def test(n):
#     sum = 0
#     temp = n
#     while temp > 0:
#         sum += temp % 10
#         temp //= 10
#     return n % sum == 0

# def test1(limit):
#     res = []
#     for num in range(1, limit + 1):
#         if test(num):
#             res.append(num)
#     return res
# print(test1(int(input())))

# 12
# def test(input_file, output_file):
#     with open(input_file, 'a+') as infile, open(output_file, 'a+') as outfile:
#         counter = 1
#         for i in infile:
#             outfile.write(f"{counter}: {i}")
#             counter += 1
# input_file = 'source.txt'
# output_file = 'numbered.txt'
# test(input_file, output_file)

# 13
# filename = "example.txt"
# N = 2
# with open(filename, "a+") as file:
#     lines = file.readlines()
#     last_lines = lines[-N:]
# for line in last_lines:
#     print(line.strip())

# 14
# source_file = "source.txt"
# destination_file = "destination.txt"
# with open(source_file, "a+") as source:
#     content = source.read()
# with open(destination_file, "a+") as destination:
#     destination.write(content)
# print("Копирование завершено.")

# 15
# filename = "example.txt"
# word_count = {}
# with open(filename, "a+") as file:
#     for line in file:
#         words = line.lower().split()
#         for word in words:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
# print(word_count)

# 16
# def test(input_file, output_file):
#     with open(input_file, 'a+') as infile, open(output_file, 'a+') as outfile:
#         for line in infile:
#             if line.strip():
#                 outfile.write(line)
# input_file = 'example.txt'
# output_file = 'output.txt'
# test(input_file, output_file)

# 17
# def test(input_file, old_word, new_word):
#     with open(input_file, 'a+') as file:
#         content = file.read()
#     content = content.replace(old_word, new_word)
#     with open(input_file, 'a+') as file:
#         file.write(content)
# input_file = 'example.txt'
# old_word = 'world'
# new_word = 'Python'
# test(input_file, old_word, new_word)

# 18
# def test(filename):
#     with open(filename, 'a+') as file:
#         text = file.read()
#         words = text.split()
#         return len(words)
# filename = 'example.txt'
# print(test(filename))

# 19
# def test(d):
#     sorted_dict = {}
#     keys = list(d.keys())
#     while keys:
#         min_key = keys[0]
#         for key in keys:
#             if d[key] < d[min_key]:
#                 min_key = key
#         sorted_dict[min_key] = d[min_key]
#         keys.remove(min_key)
#     return sorted_dict
# original_dict = {'apple': 10, 'banana': 5, 'cherry': 15}
# sorted_dict = test(original_dict)
# print(sorted_dict)

# 20
# def test(a):
#     sorted_dict = {}
#     keys = []
#     values = []
#     for key in a:
#         keys.append(key)
#         values.append(a[key])
#     while values:
#         minn = 0
#         for i in range(1, len(values)):
#             if values[i] < values[minn]:
#                 minn = i
#         sorted_dict[keys[minn]] = values[minn]
#         keys.pop(minn)
#         values.pop(minn)
#     return sorted_dict
# original_dict = {'apple': 10, 'banana': 5, 'cherry': 15}
# print(test(original_dict))
