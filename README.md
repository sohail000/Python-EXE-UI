# Python-EXE-UI

Objective:
The objective of the "run_exe" function is to execute an external executable file with a given input file and capture its output and errors. The function then displays the output in the console widget and any errors encountered during execution in the error widget.

Inputs:
- exe_file: a string representing the path to the executable file to be executed
- file_name: a string representing the path to the input file to be used by the executable

Flow:
1. The function opens a pipe to the subprocess to capture its output and errors.
2. It reads the output of the subprocess line by line and displays it in the console widget.
3. If any errors are encountered during execution, they are displayed in the error widget.
4. If no errors are encountered, a message indicating that no errors were encountered is displayed in the error widget.
