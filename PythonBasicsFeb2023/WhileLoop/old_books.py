book = input()
book_count = 0

while True:
    new_book = input()
    if new_book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {book_count} books.')
        break
    if new_book == book:
        print(f'You checked {book_count} books and found it.')
        break
    else:
        book_count += 1
