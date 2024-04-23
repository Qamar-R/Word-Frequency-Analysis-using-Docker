import nltk
from nltk.corpus import stopwords
from collections import Counter

# download NLTK data
nltk.download('stopwords')
file_path = "random_paragraphs.txt"
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def remove_stopwords(text):
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def count_word_frequency(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts

def display_word_frequency(word_counts):
    for word, count in word_counts.items():
        print(f"{word}: {count}")


def main():
    file_path = 'random_paragraphs.txt'
    text = read_file(file_path)
    text_without_stopwords = remove_stopwords(text)
    word_counts = count_word_frequency(text_without_stopwords)
    display_word_frequency(word_counts)

if __name__ == "__main__":
    main()
