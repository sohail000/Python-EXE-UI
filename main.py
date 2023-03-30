import sys
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk

# Function to run the executable on the selected file
def run_exe(exe_file, file_name):
    try:
        # Open a pipe to the subprocess to capture its output and errors
        process = subprocess.Popen([exe_file, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Display the output of the subprocess in the console widget
        while True:
            output = process.stdout.readline().decode()
            if output == '' and process.poll() is not None:
                break
            console_widget.insert(tk.END, output)
            console_widget.see(tk.END)
        # Display any errors encountered during execution in the error widget
        error_output = process.stderr.read().decode().strip()
        if error_output:
            error_widget.insert(tk.END, error_output + '\n')
            error_widget.see(tk.END)
        else:
            error_widget.insert(tk.END, "No errors encountered during execution.\n")
            error_widget.see(tk.END)
    except Exception as e:
        error_widget.insert(tk.END, f"Error: {e}\n")
        error_widget.see(tk.END)

# Function to handle the "Browse Executable" button click event
def browse_exe():
    # Show file dialog to select input executable file
    exe_file = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    # Set the executable file name in the text box
    exe_file_entry.delete(0, tk.END)
    exe_file_entry.insert(0, exe_file)

# Function to handle the "Browse Input File" button click event
def browse_file():
    # Show file dialog to select input Excel file
    file_name = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    # Set the file name in the text box
    file_name_entry.delete(0, tk.END)
    file_name_entry.insert(0, file_name)

# Function to handle the "Generate Output" button click event
def generate_output():
    # Get the executable file name from the text box
    exe_file = exe_file_entry.get()
    # Check if file exists
    if not os.path.isfile(exe_file):
        error_widget.insert(tk.END, f"Error: File {exe_file} not found.\n")
        error_widget.see(tk.END)
        return
    # Get the input Excel file name from the text box
    file_name = file_name_entry.get()
    # Check if file exists
    if not os.path.isfile(file_name):
        error_widget.insert(tk.END, f"Error: File {file_name} not found.\n")
        error_widget.see(tk.END)
        return
    # Clear the console and error widgets
    console_widget.delete(1.0, tk.END)
    error_widget.delete(1.0, tk.END)
    # Run the executable on the selected file
    run_exe(exe_file, file_name)

# Create the main window
root = tk.Tk()
root.title("AI Coach Tool")

# Create the executable file selection widgets
exe_file_label = tk.Label(root, text="EXE:")
exe_file_label.grid(row=0, column=0, padx=10, pady=10)
exe_file_entry = tk.Entry(root, width=50)
exe_file_entry.grid(row=0, column=1, padx=10, pady=10)
browse_exe_button = tk.Button(root, text="Browse", command=browse_exe)
browse_exe_button.grid(row=0, column=2, padx=10, pady=10)
# Create the input file selection widgets
file_name_label = tk.Label(root, text="Input Excel File:")
file_name_label.grid(row=1, column=0, padx=10, pady=10)
file_name_entry = tk.Entry(root, width=50)
file_name_entry.grid(row=1, column=1, padx=10, pady=10)
browse_file_button = tk.Button(root, text="Browse", command=browse_file)
browse_file_button.grid(row=1, column=2, padx=10, pady=10)

# Create the output generation widget
generate_button = tk.Button(root, text="Generate Output", command=generate_output)
generate_button.grid(row=2, column=1, padx=10, pady=10)

# Create the console widget to display output
console_label = tk.Label(root, text="Console Output:")
console_label.grid(row=3, column=0, padx=10, pady=10)
console_widget = tk.Text(root, height=10, width=80)
console_widget.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Create the error widget to display errors
error_label = tk.Label(root, text="Error Log:")
error_label.grid(row=5, column=0, padx=10, pady=10)
error_widget = tk.Text(root, height=10, width=80)
error_widget.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Run the main loop
root.mainloop()
