from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5, 6]

json_path = Path("numbers.json")
# content = json.dumps(numbers)

# json_path.write_text(content)

content = json_path.read_text()
numbers = json.loads(content)

print(numbers)