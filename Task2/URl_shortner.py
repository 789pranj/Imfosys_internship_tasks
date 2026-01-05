import random
import string

map_long = {}
map_short = {}

def get_code():
    chars = string.ascii_letters + string.digits
    code = ""
    for i in range(10):
        code += random.choice(chars)
    return code


def shorten(url):
    if url in map_long:
        return map_long[url]

    code = get_code()

    while code in map_short:
        code = get_code()

    map_long[url] = code
    map_short[code] = url

    return code


def expand(code):
    if code in map_short:
        return map_short[code]
    return "not found"


u1 = shorten("https://google.com")
print(u1)
print(expand(u1))
