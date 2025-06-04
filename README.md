# BitHide

**BitHide** is a simple yet powerful steganography tool that allows you to hide secret text messages inside images and retrieve them later — all through a user-friendly command-line interface.

## 🔐 Features

- Embed secret text into common image formats (PNG, JPG, BMP, etc.)
- Extract hidden messages from encoded images
- File picker GUI for easy image selection
- Clear CLI experience with styled prompts and banners
- Minimal dependencies and cross-platform support

## 🛠️ Technologies Used

- Python 3
- PIL (Pillow)
- Colorama
- Tkinter (for file dialog)

## 🚀 Usage

1. **Run the app:**
   python app.py

2. **Choose an option:**
   - 1: Embed secret text into an image
   - 2: Extract hidden text from an image

3. **Follow the prompts**:
   - Select your image file
   - Enter your secret message or view decoded output
   - Save to a custom or default output file

## 📦 Installation

1. Clone the repo:
   git clone https://github.com/ItamaRoginsky/BitHide
   cd BitHide

2. (Optional) Create a virtual environment:
   python -m venv .venv
   .\.venv\Scripts\activate   # Windows

3. Install dependencies:
   pip install -r requirements.txt

## 📂 Example

- Input image: your_image.png
- Embedded output: stego_output.png
- Hidden message: This is a secret.

## ⚠️ Notes

- BitHide uses LSB (Least Significant Bit) technique for encoding.
- Do not resize or recompress the output image — doing so may destroy the hidden data.

## 📃 License

MIT License

---

Made with ❤️ by Itamar Roginsky
