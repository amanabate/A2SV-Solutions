# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

number_input = int(input())
for _ in range(number_input):
    word = input()
    if len(word) > 10:
        word2 = word[0] + str(len(word) - 2) + word[-1]
        print(word2)
    else:
        print(word)




