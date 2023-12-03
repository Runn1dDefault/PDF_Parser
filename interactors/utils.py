def word_by_chars_num_to_last_letter(value: str, chars_num: int) -> str:
    # find a word by the number of characters up to the last letter
    assert chars_num > 0

    if len(value) < chars_num:
        return ''

    for s_index, symbol in enumerate(value):
        if s_index + 1 == chars_num and symbol.strip() and not value[s_index + 1].strip():
            return value[:s_index + 1].split()[-1]

    return ''


def word_by_chars_num_to_first_letter(value: str, spaces: int) -> str:
    # find a word by the number of characters up to the first letter
    assert spaces > 0

    if len(value) < spaces:
        return ''

    for s_index, symbol in enumerate(value):
        if s_index + 1 == spaces and symbol.strip() and not value[s_index - 1].strip():
            return value[s_index:].split()[0]
    return ''
