import string
from collections import Counter
def main():
    with open("sample.txt", encoding="utf-8") as file:
        text = file.read().lower()

        words = [word.strip(string.punctuation) for word in text.split()]
        words = [word for word in words if word]

        #MANUAL ALTERNATIVE
        # counts = {}
        #
        # for word in words:
        #     word = word.strip(string.punctuation)
        #     counts[word] = counts.get(word, 0) + 1
        #
        # ordered = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        #
        # for word, count in ordered:
        #     print(word, count)

        counts = Counter(words)

        for word, count in counts.most_common():
            print(word, count)


if __name__ == "__main__":
    main()