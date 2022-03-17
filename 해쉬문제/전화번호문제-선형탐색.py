

def solution(phone_book):
    phone_book.sort()
    phone_book.sort(key=len)

    answer = True

    while True:
        prefix = phone_book[0]
        phone_book = phone_book[1:]
        for phone in phone_book:
            if prefix == phone[:len(prefix)]:
                answer = False
                break
        if len(phone_book) == 1:
            break
    return answer

    이해하고, 효율성 테스트 왜 통과 못했느지 이해하기 