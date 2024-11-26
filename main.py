import chevron
from dotenv import load_dotenv
import json
import shutil
import os

load_dotenv()

data = {
    "icons": []
}

# Get icons
print("Collecting icons from metadata...")
with open("./meta.json", 'r') as f:
    json_data = json.load(f)

data["icons"] = json_data["icons"]

print("Rebuilding assets...")
if os.path.exists("./docs"):
    shutil.rmtree("./docs")
if not os.path.exists("./docs"):
    os.mkdir("./docs")
os.makedirs("./docs/assets/icons")

for icon in data["icons"]:
    shutil.copy(f"./icons/{icon['file']}", "./docs/assets/icons")

print("Writing new docs...")
with open("INDEX.mustache", "r") as f:
    doc_content = chevron.render(f, data)
    with open("docs/index.html", "w") as w:
        w.write(doc_content)