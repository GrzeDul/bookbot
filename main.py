def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_count = get_letters_count(text)
    report(num_words, letters_count)



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letters_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
           chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def report(num_words, chars):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{num_words} words found in the document')
    chars_list = sorted(chars.items(),key=lambda x: x[1],reverse=True)
    for char in chars_list:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")
    
    print("--- End report ---")
main()

