import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def get_charset(nums: bool, chars: bool, capitals: bool, specific: bool) -> str:
    charset = ""
    if nums is True:
        charset += digits
    if chars is True:
        charset += ascii_lowercase
    if capitals is True:
        charset += ascii_uppercase
    if specific is True:
        charset += punctuation

    return charset


def password_generator(length: int, charset: str) -> str:
    return "".join(secrets.choice(charset) for _ in range(length))
