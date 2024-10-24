def count_word_occurrences(text, word):
    text = text.lower()
    word = word.lower()
    count = text.count(word)
    return count
if __name__ == "__main__":
    text_input = input("Введите текст: ")
    word_input = input("Введите слово для поиска: ")
    occurrences = count_word_occurrences(text_input, word_input)
    print(f"Слово '{word_input}' встречается {occurrences} раз(а) в тексте.")