from delimit import check_fix_delimiters
from extract_statements import load_code_blocks
from extract_statements import write_source_file

filepath = "files_to_convert/test.ipynb"

filename = filepath.split("/")[1]

# Build new file name string
sourcefile = "converted_files/" + ''.join(filename.split(".")[:-1]) + ".py"

if __name__ == '__main__':
    check_fix_delimiters(filepath)
    write_source_file(filepath, sourcefile, load_code_blocks(filepath))
    