from stats import word_counter, character_counter, full
import sys

list = sys.argv


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def printFunction(source, word_count, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {source}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict  in character_count:
        print(f"{dict["char"]}: {dict["num"]}")



def main(path):
    output_text = get_book_text(path)
    num_word_count = word_counter(output_text)
    dict_word_count = character_counter(output_text)
    character_list = full(dict_word_count)
    printFunction(path,num_word_count, character_list)


if len(list) == 2:
    main(list[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

