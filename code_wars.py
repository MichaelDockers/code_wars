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
            return (last_base_digit ** 2) % 10
        elif degree % 4 == 3:
            return (last_base_digit ** 3) % 10


def square_number(num: int) -> bool:
    if num >= 0:
        return (num ** 0.5) == int(num ** 0.5)
    else:
        return False


def get_sum(a: int, b: int) -> int:
    return sum(x for x in range(min([a, b]), max([a, b]) + 1))


def to_camel_case(text: str) -> str:
    text_seps = ''.join({x if not x.isalpha() else '' for x in text})
    if text not in ['']:
        if text[0].islower():
            for text_sep in text_seps:
                cameled_text = ''.join([x[0].upper() + x[1:] for x in text.split(text_sep)])
                text = cameled_text
            return cameled_text[0].lower() + cameled_text[1:]
        else:
            for text_sep in text_seps:
                cameled_text = ''.join([x[0].upper() + x[1:] for x in text.split(text_sep)])
                text = cameled_text
            return cameled_text
    else:
        return('')


def from_camel_case(text: str) -> str:
    if text not in ['']:
        normal_text = ''.join([' ' + x if x.isupper() else x for x in text]).strip()
        return normal_text
    else:
        return ''


def create_phone_number(n: list) -> str:
    row_n = ''.join(map(str, n))
    return f'({row_n[0: 3]}) {row_n[3: 6]}-{row_n[6:]}'


def odd_sort(n: list) -> list:
    odd_list = sorted(list(filter(lambda x: x % 2 == 1, n)), reverse=True)
    return [x if x % 2 == 0 else (odd_list).pop() for x in n]


def expanded_form(n: int) -> str:
    itr = 1
    exp_form = []
    while n > 0:
        if n % 10 > 0:
            exp_form.append(n % 10 * itr)
            n //= 10
            itr *= 10
        else:
            n //= 10
            itr *= 10

    return ' + '.join(map(str, exp_form[::-1]))


def generate_hashtag(text: str) -> str:
    tag = '#' + ''.join([x.strip().capitalize() for x in text.split()])
    return tag if 1 < len(tag) < 140 else False


print(generate_hashtag('     HeLlo    World  '))




