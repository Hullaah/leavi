from pathlib import Path
from typing import Final

from schemas.configs.settings import Settings

PROJECT_ROOT: Final[Path] = Path(__file__).parent
settings = Settings(PROJECT_ROOT / ".env")
