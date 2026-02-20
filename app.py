import tkinter as tk
from tkinter import filedialog, messagebox
import os

def combine_files(files, output_file):
    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            for file in files:
                try:
                    with open(file, "r", encoding="utf-8") as infile:
                        content = infile.read()
                        entry = f"\n===== {os.path.basename(file)} =====\n{content}\n\n"
                        outfile.write(entry)
                except Exception as e:
                    print(f"Skipping {file}: {e}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def select_files():
    files = filedialog.askopenfilenames(
        title="Select Files to Combine",
        filetypes=[("All Files", "*.*")]
    )
    if files:
        output_file = filedialog.asksaveasfilename(
            title="Save Combined File As",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if output_file:
            success = combine_files(files, output_file)
            if success:
                messagebox.showinfo("Success", f"✅ {len(files)} files combined into one!\nSaved as {output_file}")
            else:
                messagebox.showerror("Error", "Something went wrong!")

# GUI Setup
root = tk.Tk()
root.title("Code Combiner")
root.geometry("420x220")

label = tk.Label(
    root,
    text="📂 Combine Multiple Code Files into One Text File\n(All files will be merged into a single output)",
    wraplength=350,
    justify="center"
)
label.pack(pady=20)

button = tk.Button(root, text="Select Files & Combine", command=select_files, bg="blue", fg="white", padx=10, pady=5)
button.pack()

root.mainloop()