from pathlib import Path
from datetime import datetime
from dataclasses import dataclass

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_OUTPUT_DEST = ROOT / "data" / "output"

@dataclass
class FileConfig:
  name: str
  ext: str
  add_timestamp_suffix: bool = True
  dest: Path = DEFAULT_OUTPUT_DEST

def write_to_file(text: str, file_config: FileConfig):

  name = file_config.name

  Path(file_config.dest).mkdir(parents=True, exist_ok=True)

  if file_config.add_timestamp_suffix:
    name += f"-{datetime.now().strftime("%Y%m%d_%H%M%S")}"
  name += file_config.ext

  with open(file_config.dest / name, "w") as dest_file:
    dest_file.write(text)