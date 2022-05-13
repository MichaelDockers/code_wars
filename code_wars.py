def spin_words(sentence: str) -> str:
    reversed_sentence = [x[::-1] if len(x) >= 5 else x for x in sentence.split()]
    return ' '.join(reversed_sentence)


def narcissistic(num: int) -> bool:
    def base(num: int) -> int:
        i = 0
        while num > 0:
            num //= 10
            i += 1
        return i
    
    
    def get_sum(num: int) -> int:
        n = 0
        st = base(num)
        while num > 0:
            n = n + (num % 10) ** st
            num = num // 10
        return n
    return num == get_sum(num)


def to_jaden_case(string: str) -> str:
    return ' '.join([x.capitalize() for x in string.split()])


def last_digit(base: int, degree: int) -> int:
    
    if degree == 0:
        return 1

    last_base_digit = base % 10
    if last_base_digit in [0, 1, 5, 6]:
        return last_base_digit
    else:
        if degree % 4 == 0:
            if base % 2 == 0:
                return 6
            else:
                return 1
        elif degree % 4 == 1:
            return last_base_digit
        elif degree % 4 == 2:
            return (base ** 2) % 10
        elif degree % 4 == 3:
            return (base ** 3) % 10


def square_number(num: int) -> bool:
    if num >= 0:
        return (num ** 0.5) == int(num ** 0.5)
    else:
        return False

print(square_number(16))