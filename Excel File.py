import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

file_dict = {}
selected_files = []

def open_file_explorer():
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select files")
    if filenames:
        print("Selected files:", filenames)
        for filename in filenames:
            update_recent_files(filename)

def update_recent_files(filePath):
    # Extract file name from the path
    file_name = os.path.basename(filePath)
    file_dict[filePath] = file_name
    openedFilesWindow.insert("", "end", values=(file_name,filePath))
    # Add file path and file name to dictionary
    
    
def select_file(event):
    global selected_files
    items = openedFilesWindow.selection()
    selected_files = [openedFilesWindow.item(item, "values")[1] for item in items]

def open_selected_file(): #open all the selected files
    for selected_file in selected_files:
        if selected_file:
            file_name = file_dict.get(selected_file)
            if file_name:
                os.startfile(selected_file)

def undefinedFunciton():
    pass

def close_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("File Explorer")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position
window_width = 600
window_height = 400
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# frame to hold the buttons and the table
buttonFrame = tk.Frame(root)
buttonFrame.place(relx=0.05, rely=0.1, relwidth=0.2, relheight=1)

# button to open the file explorer
openFileExplorerButton = tk.Button(buttonFrame, text="File Explorer", command=open_file_explorer, width=20, height=2)
openFileExplorerButton.pack(pady=10)

# button to open the selected file
openSelectedFiles = tk.Button(buttonFrame, text="Open Files", command=open_selected_file, width=20, height=2)
openSelectedFiles.pack(pady=12)


functionButton = tk.Button(buttonFrame, text="undefined", command=undefinedFunciton, width=20, height=2)
functionButton.pack(pady=12)

# button to close the application
closeButton = tk.Button(buttonFrame, text="Close", command=close_app, width=20, height=2)
closeButton.pack(pady=80)

# frame to hold the table
tableFrame = tk.Frame(root)
tableFrame.place(relx=0.3, rely=0.1, relwidth=0.65, relheight=0.8)

# table to display opened files
openedFilesWindow = ttk.Treeview(tableFrame, columns=("File Name",), show="headings", height=10)
openedFilesWindow.heading("File Name", text="File Name")
openedFilesWindow.pack(fill=tk.BOTH, expand=True)
openedFilesWindow.bind("<ButtonRelease-1>", select_file)


root.mainloop()
