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


def compute_depth(n: int) -> int:
    step = 0
    nums = set()
    while len(nums) < 10:
        step += 1
        mult_num = n * step
        nums.update(list(str(mult_num)))
    return step


def list_squared(m: int, n: int) -> list:
    right_list = []
    for i in range(m, n + 1):
        unique_devs = set()
        devs = [(x, i // x) for x in range(1, int(i ** 0.5) + 1) if (i % x == 0)]
        for item in devs:
            unique_devs.update(item)
        squares_sum = sum([x ** 2 for x in unique_devs])
        if squares_sum ** 0.5 == int(squares_sum ** 0.5):
            right_list.append([i, squares_sum])
    return(right_list)


def scramble(str1: str, str2: str) -> bool:
    for item in set(str2):
        if str2.count(item) > str1.count(item):
            return False
    return True


def linear_dl(n):
    linear_lst = [1]
    item = 0
    #for item in range(int(n / 2) + 3):
    for item in range(n + 1):
        linear_lst.append(2 * linear_lst[item] + 1)
        linear_lst.append(3 * linear_lst[item] + 1)
        linear_lst = sorted(list(set(linear_lst)))
        item += 1
    print(linear_lst)
    return linear_lst[n]


print(linear_dl(20))
