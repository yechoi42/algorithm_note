import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split(' ')))
M = int(input())
target_cards = list(map(int, input().split(' ')))

count = {}
cards.sort()
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2 
    if array[mid] == target:
        return count.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for target in target_cards:
    print(binary_search(cards, target, 0, N - 1), end = " ")