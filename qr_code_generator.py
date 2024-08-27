import sys
import pyqrcode
import os

def generate_qr_code(data, file_path, folder='qrcode'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, file_path)
    qr = pyqrcode.create(data)
    qr.png(file_path, scale=6)
    
if __name__ == "__main__":
    if len(sys.argv)!= 2:
        print("Usage: python qr_code_generator.py <qr_code_data>")
        sys.exit(1)
    data = sys.argv[1]
    file_name = input("Enter the filename (without extension): ")
    file_format = input("Enter the file format (png, svg, or jpg): ")
    if file_format not in ['png', 'svg', 'jpg']:
        print("Invalid file format. Supported formats: png, svg, jpg")
        sys.exit(1)
    generate_qr_code(data, f"{file_name}.{file_format}")
    print(f"QR code saved as {file_name}.{file_format} in the qrcode folder.")
