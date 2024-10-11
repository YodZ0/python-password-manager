from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
FONTS_DIR = BASE_DIR / "fonts"


class WindowConfig:
    width: int = 800
    height: int = 600


class FontsConfig:
    regular: str = "../fonts/TitilliumWeb-Regular.ttf"
    italic: str = "../fonts/TitilliumWeb-Italic.ttf"
    bold: str = "../fonts/TitilliumWeb-Bold.ttf"


class Settings:
    base_dir: Path = BASE_DIR
    fonts: FontsConfig = FontsConfig()
    window: WindowConfig = WindowConfig()


settings = Settings()
