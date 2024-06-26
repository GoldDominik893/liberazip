import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import zipfile
import os

class LiberaZip:
    def __init__(self, root):
        self.root = root
        self.root.title("LiberaZip")
        self.root.geometry("450x310")

        # Load and set the icon
        self.icon = tk.PhotoImage(file="icon.png")
        self.root.iconphoto(False, self.icon)

        # Create and set up the main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True, fill="both")

        # Create a label for the icon
        self.icon_label = ttk.Label(self.main_frame, image=self.icon)
        self.icon_label.pack(pady=10)

        # Add description text
        self.description_label = ttk.Label(
            self.main_frame, 
            text="LiberaZip v0.01 Alpha - LiberaZip is better than 7Zip",
            font=("Helvetica", 12)
        )
        self.description_label.pack(pady=10)

        # Create and place buttons in the main frame
        self.create_widgets()

    def create_widgets(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=10, fill='x')

        self.zip_button = ttk.Button(button_frame, text="Zip Files", command=self.zip_files)
        self.zip_button.pack(side='left', padx=10, fill='x', expand=True)

        self.unzip_button = ttk.Button(button_frame, text="Unzip Files", command=self.unzip_files)
        self.unzip_button.pack(side='left', padx=10, fill='x', expand=True)

    def zip_files(self):
        files = filedialog.askopenfilenames(title="Select files to zip")
        if not files:
            return

        zip_filename = filedialog.asksaveasfilename(defaultextension=".zip", title="Save zip file as")
        if not zip_filename:
            return

        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))

        messagebox.showinfo("Success", f"Files zipped successfully to {zip_filename}")

    def unzip_files(self):
        zip_filename = filedialog.askopenfilename(title="Select zip file to unzip", filetypes=[("ZIP files", "*.zip")])
        if not zip_filename:
            return

        extract_dir = filedialog.askdirectory(title="Select directory to extract files to")
        if not extract_dir:
            return

        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall(extract_dir)

        messagebox.showinfo("Success", f"Files unzipped successfully to {extract_dir}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LiberaZip(root)
    root.mainloop()
