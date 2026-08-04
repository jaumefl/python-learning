from collections import Counter

def main():

    file = input("Enter file name: ")
    try:
        with open(f"samples/{file}.txt") as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found")
        return
    char_count = len(text)
    words = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "").split()

    if not words:
        print("File has no words to analyze")
        return

    char_count_exc_spaces = 0
    max = words[0]
    for word in words:
        if len(word) > len(max):
            max = word
        char_count_exc_spaces += len(word.strip())


    word_count = len(words)

    counts = Counter(words)
    most_common_word, count = counts.most_common(1)[0]

    pieces = text.replace("!", ".").replace("?", ".").split(".")
    sentences = [s.strip() for s in pieces if s.strip()]
    sentence_count = len(sentences)

    avg_word_length = round(char_count_exc_spaces / word_count, 2)

    avg_words_per_sentence = round(word_count / sentence_count, 2)

    minutes = round(word_count / 200, 2)
    if minutes < 1:
        seconds = round(minutes * 60)

    print(f"""
Character count: {char_count} characters
Character count (excluding spaces): {char_count_exc_spaces} characters
Word count: {word_count} words
Sentence count: {sentence_count} sentences
Average word length: {avg_word_length} characters
Average words per sentence: {avg_words_per_sentence} words
Longest word: {max}
Most common word: -> {most_common_word} <-  which appears {count} times""")
    if minutes < 1:
        print(f"Average reading time: {seconds} seconds \n")
    else:
        print(f"Average reading time: {minutes} minutes \n")






if __name__ == '__main__':
    main()