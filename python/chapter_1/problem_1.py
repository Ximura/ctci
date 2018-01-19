# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def unique_characters(text: str) -> bool:
    cache = {}
    for c in text:
        cache[c] = 1
    return len(cache) == len(text)


def unique_characters_no_cache(text: str) -> bool:
    bit_mask = 0
    for c in text:
        n = ord(c)
        bit_mask = bit_mask ^ (2 ** n)
        if not is_set(bit_mask, n):
            return False

    return True


def is_set(x, n):
    return x & 2**n != 0