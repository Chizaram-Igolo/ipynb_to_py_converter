from delimit import check_fix_delimiters
import json

filepath = "test.ipynb"

# Build new file name string
sourcefile = ''.join(filepath.split(".")[:-1]) + ".py"

check_fix_delimiters(filepath)

with open(filepath, "r") as f:
    content = json.load(f)

sourcecode = []

for item in content[0]["cells"]:
    sourcecode.append(item["source"])


def write_source_file(filepath): 
    
    with open(sourcefile, "w") as f:
        for line in sourcecode:
            if isinstance(line, list):
                for l in line:
                    print(l.rstrip('\r\n'), file=f)
            else:
                print(line.rstrip('\r\n'), file=f)

