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

    n = 0
    st = base(num)
    while num > 0:
        n = n + (num % 10) ** st
        num = num // 10
    print(num, n)
    return num == n


print(narcissistic(1652))