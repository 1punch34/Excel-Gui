import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

class File:
    def __init__(self, file_path):
        self.file_name = os.path.basename(file_path)
        self.file_path = file_path
        self.is_favorite = False

class FileExplorerApp:
    def __init__(self, master):
        self.master = master
        master.title("File Explorer")

        # Get the screen width and height
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Set the window size and position
        window_width = 600
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Dictionary to store file paths and names
        self.file_dict = {}

        # Create frame for buttons and table
        self.buttonFrame = tk.Frame(master)
        self.buttonFrame.place(relx=0.05, rely=0.1, relwidth=0.2, relheight=1)

        # Button to open file explorer
        self.openFileExplorerButton = tk.Button(self.buttonFrame, text="File Explorer", command=self.open_file_explorer, width=20, height=2)
        self.openFileExplorerButton.pack(pady=10)

        # Button to open selected files
        self.openSelectedFiles = tk.Button(self.buttonFrame, text="Open Files", command=self.open_selected_file, width=20, height=2)
        self.openSelectedFiles.pack(pady=12)

        # Placeholder button
        self.functionButton = tk.Button(self.buttonFrame, text="undefined", command=self.undefinedFunction, width=20, height=2)
        self.functionButton.pack(pady=12)

        # Button to close the application
        self.closeButton = tk.Button(self.buttonFrame, text="Close", command=self.close_app, width=20, height=2)
        self.closeButton.pack(pady=80)

        # Create frame for table
        self.tableFrame = tk.Frame(master)
        self.tableFrame.place(relx=0.3, rely=0.1, relwidth=0.65, relheight=0.8)

        # Table to display opened files
        self.openedFilesWindow = ttk.Treeview(self.tableFrame, columns=("File Name",), show="headings", height=10)
        self.openedFilesWindow.heading("File Name", text="File Name")
        self.openedFilesWindow.pack(fill=tk.BOTH, expand=True)
        self.openedFilesWindow.bind("<Double-1>", self.on_double_click)
        self.openedFilesWindow.bind("<ButtonRelease-1>", self.select_file)
        self.openedFilesWindow.bind("<Button-3>", self.clear_selection)

    def open_file_explorer(self):
        filenames = filedialog.askopenfilenames(initialdir="/", title="Select files")
        if filenames:
            print("Selected files:", filenames)
            for filename in filenames:
                self.update_recent_files(filename)

    def update_recent_files(self, file_path):
        # Create File object
        file = File(file_path)
        # Add file to dictionary
        self.file_dict[file.file_name] = file
        # Insert file name into treeview
        self.openedFilesWindow.insert("", "end", values=(file.file_name, file))

    def clear_selection(self, event):
        self.openedFilesWindow.selection_remove(self.openedFilesWindow.selection())

    def select_file(self, event):
        global selected_files
        items = self.openedFilesWindow.selection()
        selected_files = [self.openedFilesWindow.item(item, "values")[1] for item in items]

    def open_selected_file(self):
        for selected_file in selected_files:
            if selected_file:
                print("Opening selected file:", selected_file.file_path)
                os.startfile(selected_file.file_path)

    def on_double_click(self, event):
        item = self.openedFilesWindow.selection()[0]
        file = self.openedFilesWindow.item(item, "values")[1]
        
        if file:
            if file.is_favorite:
                self.openedFilesWindow.set(item, "#1", file.file_name)
                file.is_favorite = False
            else:
                self.openedFilesWindow.set(item, "#1", "⭐ " + file.file_name)
                file.is_favorite = True
                
    def undefinedFunction(self):
        pass

    def close_app(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
