# README
### .ipynb to .py converter

A quick and dirty tool to convert Jupyter notebook files to Python files. Markdown is preserved as Python comments for reconversion.

### To Use:
-  Clone repository.
-  Open Command Prompt and cd to folder.
-  Open extract_statements.py and change filepath from "test.ipynb" to the path of your file.
-  Run extract_statements.py from command prompt.
-  Look for your .py file at the file path you specified.


### TODO:
-   Write ArgParser for supplying filepath as parameter.
-   Modify to convert files in batch from specified folder.
-   Strip extra '\n' characters.
