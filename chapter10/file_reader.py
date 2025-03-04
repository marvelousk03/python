from pathlib import Path


path = Path('my_name.txt')
contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

new_path = Path("new_file.txt")
new_path.write_text("Today was a day that was being a day.")
