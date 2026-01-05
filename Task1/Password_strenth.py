def check_password_strength(password):
    length_ok = False
    upper = False
    lower = False
    digit = False
    special = False

    if len(password) >= 8:
        length_ok = True

    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            upper = True
        elif ch >= 'a' and ch <= 'z':
            lower = True
        elif ch >= '0' and ch <= '9':
            digit = True
        elif ch in "!@#$%^&*":
            special = True

    count = 0
    if upper:
        count += 1
    if lower:
        count += 1
    if digit:
        count += 1
    if special:
        count += 1

    if length_ok and count == 4:
        return "Strong"
    elif length_ok and count >= 2:
        return "Medium"
    else:
        return "Weak"


test_passwords = [
    "Pass123!",
    "password1",
    "pass",
    "Hello@2024",
    "Pa1!",
    "ABCDEFGH"
]

for pwd in test_passwords:
    print(pwd, "->", check_password_strength(pwd))