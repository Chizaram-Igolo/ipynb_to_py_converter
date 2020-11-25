
def line_prepender(filepath, line):
    """Prepends `line` to content in file"""

    with open(filepath, "r+", encoding="utf8") as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def line_appender(filepath, line):
    """Appends `line` to content in file"""

    with open(filepath, "a", encoding="utf8") as f:
        f.write(line)


def check_fix_delimiters(filepath):
    """Check that the content of the .ipynb file is delimited by `[` and `]`, or 
        in other words, that the file's content comes in a list. If it doesn't, 
        delimit by the square brackets."""
        
    with open(filepath, "r", encoding="utf8") as f:
        content = f.readlines()
        if content[0][0] != '[':
            line_prepender(filepath, "[")
        if content[-1][-1] != ']':
            line_appender(filepath, "]")
