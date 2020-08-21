def is_valid(isbn: str) -> bool:
    clean_isbn = []

    isbn = isbn.upper().replace('-', '').strip()
    if len(isbn) != 10:
        return False

    for idx, char in enumerate(isbn):
        if char.isdigit():
            clean_isbn.append(int(char))
        elif char == 'X' and idx == 9:
            clean_isbn.append(10)
        else:
            print(char)
            return False  # was an alpha at wrong idx or not an X
    
    checksum_total = 0
    for i, x in enumerate(clean_isbn):
        multiplier = 10 - i  # counts down from 10
        checksum_total += (x * multiplier)
    
    return True if checksum_total % 11 == 0 else False


if __name__ == '__main__':
    print(is_valid('3-598-21508-8'))