import tkinter as tk
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfile

def saving_file():
    # Open a dialog to save the file and get the file location
    file_location = asksaveasfile(  
        defaultextension="txt",
        filetypes=[("Text files", "*.txt"),
                   ("All files", "*.*")])
    if not file_location:
        return  # Exit if no file location was selected
    # Write the content of the text editor to the selected file
    with open(file_location.name, "w") as file_output:  
        text = text_edit.get(1.0, tk.END)  
        file_output.write(text)
    root.title(f"My NotePad - {file_location.name}")  # Update window title

def opening_file():
    # Open a dialog to choose a file to open
    file_location = askopenfilename(
        filetypes=[("Text files", "*.txt"),  
                   ("All files", "*.*")])
    if not file_location:
        return  # Exit if no file location was selected
    text_edit.delete(1.0, tk.END)  # Clear the text editor
    # Read and insert the content of the selected file
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)  
    root.title(f"My NotePad - {file_location}")  # Update window title

def change_font_color():
    # Open a color chooser dialog to select text color
    color_code = colorchooser.askcolor(title="Choose text color")
    if color_code and text_edit.tag_ranges("sel"):
        start_index = text_edit.index("sel.first")  # Get start of selection
        end_index = text_edit.index("sel.last")  # Get end of selection
        # Apply the selected color to the selected text
        text_edit.tag_add("color", start_index, end_index)
        text_edit.tag_configure("color", foreground=color_code[1])  # Set text color

def change_bg_color():
    # Open a color chooser dialog to select background color
    color_code = colorchooser.askcolor(title="Choose background color")
    if color_code:
        text_edit.config(bg=color_code[1])  # Set background color of the text widget

# Create main window
root = tk.Tk() 
root.title("My NotePad")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)

# Create a text widget for editing
text_edit = tk.Text(root, bg="white", fg="black")  
text_edit.grid(row=0, column=1, sticky="nsew")

# Create a frame for buttons
frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

# Create buttons for various functionalities
button_open = tk.Button(frame_button, text="OPEN FILE", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = tk.Button(frame_button, text="SAVE AS", command=saving_file)
button_save.grid(row=1, column=0, padx=5)

button_color = tk.Button(frame_button, text="FONT COLOR", command=change_font_color)
button_color.grid(row=2, column=0, padx=5)

button_bg_color = tk.Button(frame_button, text="BG COLOR", command=change_bg_color)
button_bg_color.grid(row=3, column=0, padx=5)

# Start the main loop of the application
root.mainloop()
