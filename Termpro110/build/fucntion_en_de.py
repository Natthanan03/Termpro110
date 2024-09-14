import os
from Crypto.Cipher import AES
from tkinter import ttk, filedialog, END, messagebox
from gui import entry_1, entry_2, entry_3, entry_4, button_1, button_2, button_3, button_4


def openfile_encryption():
    file = filedialog.askopenfile(
        mode="r",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Csv Files", "*.csv"),
            ("Image Files", "*.png *.jpg *.jpeg *.jp2 *.tiff *.ppm *.bmp"),
            ("Music Files", "*.mp3 *.wav"),
            ("Video Files", "*.mp4 *.mov"),
        ],
    )
    if file:
        entry_1.delete(0, END)
        filepath = os.path.abspath(file.name)
        entry_1.insert(END, str(filepath))
        

def openfile_decryption():
    file = filedialog.askopenfile(
        mode="r",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Csv Files", "*.csv"),
            ("Image Files", "*.png *.jpg *.jpeg *.jp2 *.tiff *.ppm *.bmp"),
            ("Music Files", "*.mp3 *.wav"),
            ("Video Files", "*.mp4 *.mov"),
        ],
    )
    if file:
        entry_2.delete(0, END)
        filepath = os.path.abspath(file.name)
        entry_2.insert(END, str(filepath))


def filetype(plaintext):
    _, file_extension = os.path.splitext(plaintext)
    if file_extension.lower() not in [".txt", ".csv", ".png", ".jpg", ".jpeg", ".mp3", ".wav", ".mp4"]:
        raise ValueError("Unsupported file type!")
    return file_extension


def make_16_bytes(text):
    byte_object = bytes(text, "utf-8")
    if len(byte_object) > 16:
        return byte_object[:16]  # Truncate if too long
    elif len(byte_object) < 16:
        padding_length = 16 - len(byte_object)
        return byte_object + b"\x00" * padding_length  # Pad with null bytes
    return byte_object


# Encryption Function
def encrypt_button_event():
    password = entry_3.get()
    if not password:
        messagebox.showwarning("Error", "Please enter your key.")
        return

    key_en = make_16_bytes(password)
    inputfile = entry_1.get()
    if not os.path.isfile(inputfile):
        messagebox.showwarning("Error", "File not found.")
        return

    encrypted_file = "encrypted_file" + filetype(inputfile)
    try:
        encrypt_file(inputfile, encrypted_file, key_en)
        messagebox.showinfo("Success", "File encrypted successfully.")
        entry_1.delete(0, END)
        entry_3.delete(0, END)
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")


def encrypt_file(input_file, output_file, key):
    try:
        cipher = AES.new(key, AES.MODE_EAX)
        with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
            ciphertext, tag = cipher.encrypt_and_digest(infile.read())
            outfile.write(cipher.nonce)
            outfile.write(tag)
            outfile.write(ciphertext)
    except Exception as e:
        raise e


# Decryption Function
def decrypt_button_event():
    password = entry_4.get()
    if not password:
        messagebox.showwarning("Error", "Please enter your key.")
        return

    key_de = make_16_bytes(password)
    inputfile = entry_2.get()
    if not os.path.isfile(inputfile):
        messagebox.showwarning("Error", "File not found.")
        return

    decrypted_file = "decrypted_file" + filetype(inputfile)
    try:
        decrypt_file(inputfile, decrypted_file, key_de)
        messagebox.showinfo("Success", "File decrypted successfully.")
        entry_2.delete(0, END)
        entry_4.delete(0, END)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")


def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
            nonce = infile.read(16)
            tag = infile.read(16)
            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            ciphertext = infile.read()
            plaintext = cipher.decrypt(ciphertext)
            cipher.verify(tag)  # Verify tag to check integrity
            outfile.write(plaintext)
    except Exception as e:
        raise e
