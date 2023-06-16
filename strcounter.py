from collections import Counter


def strcounter(s):
    counter = Counter(s)
    for i in counter:
        print(f"{i} - {counter[i]}")