from pathlib import Path

path = Path("roles_xml")
files = [file.stem for file in path.rglob("*.xml")]

print(files)