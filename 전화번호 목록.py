def solution(phone_book):
    phone_book.sort()
    for i,p in enumerate(phone_book):
        if i != len(phone_book)-1:
            if p == phone_book[i+1][:len(p)]:
                return False
    return True