def main():

    with open("samples/short.txt") as f:
        text = f.read()
        char_count = len(text)
        words = text.replace(".", "").replace(",", "").replace("!", "").replace("?", "").split()

        char_count_exc_spaces = 0
        max = words[0]
        for word in words:
            if len(word) > len(max):
                max = word
            char_count_exc_spaces += len(word)


        word_count = len(words)

        pieces = text.replace("!", ".").replace("?", ".").split(".")
        sentences = [s.strip() for s in pieces if s.strip()]
        sentence_count = len(sentences)

        avg_word_length = round(char_count_exc_spaces / word_count, 2)

        avg_words_per_sentence = round(word_count / sentence_count, 2)


        print(f"""
Character count: {char_count} characters
Character count (excluding spaces): {char_count_exc_spaces} characters
Word count: {word_count} words
Sentence count: {sentence_count} sentences
Average word length: {avg_word_length} characters
Average words per sentence: {avg_words_per_sentence} words
Longest word: {max}
""")






if __name__ == '__main__':
    main()