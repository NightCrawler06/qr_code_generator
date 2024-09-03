# QR Code Generator

This Python script generates QR codes from provided text. You can use it to create QR codes that encode URLs, messages, or any other data.

## Installation and Usage

To get started with the QR Code Generator:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/NightCrawler06/qr-code-generator.git
    cd qr-code-generator
    ```

2. **Install the required Python packages:**
    ```bash
    pip install pyqrcode
    ```

3. **Generate a QR code by running:**
    ```bash
    python qr_code_generator.py <text>
    ```
    Replace `<text>` with the data you want to encode in the QR code. The script will prompt you to enter the filename (without extension) and file format (png, svg, or jpg). For example:
    ```bash
    python qr_code_generator.py "https://example.com"
    ```
    When prompted, you might enter:
    ```
    Enter the filename (without extension): my_qr_code
    Enter the file format (png, svg, or jpg): png
    ```
    This command will generate a QR code encoding the URL `https://example.com` and save it as `my_qr_code.png` in the `qrcode` folder.

## Requirements

- Python 3.x
- `pyqrcode` library (install via `pip install pyqrcode`)
