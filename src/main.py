import re
import sys
import urllib.parse
import requests
from bs4 import BeautifulSoup

command = ""
if len(sys.argv) > 1:
    command = sys.argv[1]
else:
    print("Error: No command string provided.")
    sys.exit(1)

print(f"Analyzing command: {command}")

encoded_command = urllib.parse.quote(command)
url = f"https://explainshell.com/explain?cmd={encoded_command}"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

explainations = {}

command_div = soup.find(id="command")
help_refs = {}

command_parts = command_div.find_all(attrs={"helpref": re.compile(r"^help-")})
print("command parts", command_parts)
for part in command_parts:
  help_ref = part.get('helpref')
  print("helpref", help_ref)
  help_ref_text = part.get_text().strip()
  help_refs[help_ref] = help_ref_text


help_boxes = soup.find_all(class_="help-box")

for box in help_boxes:
  box_id = box.get('id')
  text = box.get_text(separator=" ").strip()
  if box_id:
    key = help_refs[box_id]
    explainations[key] = text
    print(f"\n[\033[1;36m{key}\033[0m]")
    print(text)
