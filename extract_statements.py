import re
import json

def load_code_blocks(filepath):
    """ Extracts all the code blocks. Each .ipynb file has a JSON key called 
        `cells` residing in the second dimension and containing another key 
        called `source` which contains a list of lists of code."""

    sourcecode = []
    
    with open(filepath, "r") as f:
        content = json.load(f)

    for item in content[0]["cells"]:
        sourcecode.append(item["source"])
        
    return sourcecode


def write_source_file(filepath, sourcefile, sourcecode):
    """Goes through each list and each part of the list if they are lists
    themselves to get the source code."""
    
    with open(sourcefile, "w") as f:
        for line in sourcecode:
            if isinstance(line, list):
                for l in line: # remove markdown code block formating
                    if l.startswith("```"):
                        print("#", l.rstrip('\r\n'), file=f)
                    else:
                        print(l.rstrip('\r\n'), file=f)
            else:
                if line.startswith("```"):
                    print("#", l.rstrip('\r\n'), file=f)
                else:
                    print(line.rstrip('\r\n'), file=f)

