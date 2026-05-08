import os
import glob
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.tex') or file.endswith('.bib'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except:
                with open(path, 'r', encoding='windows-1252', errors='ignore') as f:
                    content = f.read()
            content = content.replace("—", "---").replace("–", "--").replace("₂", "$_2$").replace("’", "'").replace("‘", "'")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
