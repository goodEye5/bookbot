import sys
from stats import get_num_words
from stats import get_chars_dict

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    print('============ BOOKBOT ============')
    filepath = sys.argv[1]
    
    print(f'Analyzing book found at {filepath}')
    book = get_book_text(filepath)

    print('----------- Word Count ----------')
    print(f'Found {get_num_words(book)} total words')

    print('--------- Character Count -------')
    #print(get_chars_dict(book))
    for i in get_chars_dict(book):
        print(f'{i[0]}: {i[1]}')
    print('============= END ===============')

main()