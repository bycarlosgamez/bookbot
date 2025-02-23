import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_dic = get_sorted_dic(num_chars)
    dic_list = get_dic_list(sorted_dic)
    report = get_report(dic_list, book_path, num_words)

    return report


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_chars(text):
    lowerText = text.lower()
    chars = {}
    for char in lowerText:
        if char in chars:
            chars[char] += 1;
        else:
            chars[char] = 1;
    return chars


def get_sorted_dic(num_chars):
    sorted_dic = dict(sorted(num_chars.items(), reverse=True, key=lambda item: item[1]))
    return sorted_dic

def get_dic_list(sorted_dic):
     letters = []
     for key, value in sorted_dic.items():
        if key.isalpha() == True:
            letters.append({"character": key, "num": value})
     return letters

def get_report(dic_list, book_path, num_words):
    print(f"--- Begin report of {book_path} --- {num_words} words found in the document")
    for letter in dic_list:
        print(f"The '{letter["character"]}' character was found {letter["num"]} times")
    print("--- End report ---")



main()