from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
FONTS_DIR = BASE_DIR / "fonts"
ICONS_DIR = BASE_DIR / "icons"


class WindowConfig:
    width: int = 800
    height: int = 600


class FontsConfig:
    regular: str = "../fonts/TitilliumWeb-Regular.ttf"
    italic: str = "../fonts/TitilliumWeb-Italic.ttf"
    bold: str = "../fonts/TitilliumWeb-Bold.ttf"


class IconConfig:
    small: str = "../icons/icon_16.ico"
    large: str = "../icons/icon_256.ico"


class Settings:
    base_dir: Path = BASE_DIR
    fonts: FontsConfig = FontsConfig()
    icons: IconConfig = IconConfig()
    window: WindowConfig = WindowConfig()


settings = Settings()
