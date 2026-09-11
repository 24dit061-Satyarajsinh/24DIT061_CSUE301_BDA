import sys

for line in sys.stdin:
    words = line.strip().lower().split()

    for word in words:
        word = ''.join(ch for ch in word if ch.isalnum())

        if word:
            print(f"{word}\t1")