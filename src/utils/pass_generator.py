import secrets


def generate_password(length: int, charset: list[str]):
    return "".join(secrets.choice(charset) for _ in range(length))
