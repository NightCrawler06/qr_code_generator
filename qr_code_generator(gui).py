import tkinter as tk
from tkinter import messagebox
import pyqrcode
import os

def generate_qr_code(data, file_path, folder='qrcode'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, file_path)
    qr = pyqrcode.create(data)
    qr.png(file_path, scale=6)

def on_generate():
    data = entry_data.get()
    file_name = entry_filename.get()
    file_format = combo_format.get()

    if not data or not file_name:
        messagebox.showerror("Input Error", "Please provide both data and filename.")
        return

    if file_format not in ['png', 'svg', 'jpg']:
        messagebox.showerror("Format Error", "Invalid file format. Supported formats: png, svg, jpg.")
        return

    try:
        generate_qr_code(data, f"{file_name}.{file_format}")
        messagebox.showinfo("Success", f"QR code saved as {file_name}.{file_format} in the qrcode folder.")
    except Exception as e:
        messagebox.showerror("Error", f"Error generating QR code: {e}")

#main window
root = tk.Tk()
root.title("QR Code Generator")


label_data = tk.Label(root, text="Enter QR Code Data:")
label_data.pack(padx=10, pady=5)

entry_data = tk.Entry(root, width=50)
entry_data.pack(padx=10, pady=5)

label_filename = tk.Label(root, text="Enter Filename (without extension):")
label_filename.pack(padx=10, pady=5)

entry_filename = tk.Entry(root, width=50)
entry_filename.pack(padx=10, pady=5)

label_format = tk.Label(root, text="Select File Format:")
label_format.pack(padx=10, pady=5)

combo_format = tk.StringVar()
format_options = ['png', 'svg', 'jpg']
combo_format.set(format_options[0])

dropdown = tk.OptionMenu(root, combo_format, *format_options)
dropdown.pack(padx=10, pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=on_generate)
generate_button.pack(padx=10, pady=20)

# Run the main loop
root.mainloop()
