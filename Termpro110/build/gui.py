from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Termpro110\build\assets\frame0")

def op_en():
    from fucntion_en_de import openfile_encryption
    openfile_encryption()

def op_de():
    from fucntion_en_de import openfile_decryption
    openfile_decryption()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def event_encryption_button():
    from fucntion_en_de import encrypt_button_event
    encrypt_button_event()

def event_decryption_button():
    from fucntion_en_de import decrypt_button_event
    decrypt_button_event()

window = Tk()
window.title("Encryption & Decryption")
window.geometry("558x354")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 354,
    width = 558,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    558.0,
    354.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    command=event_encryption_button,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
)
button_1.place(
    x=448.0,
    y=92.0,
    width=90.0,
    height=34.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    70.0,
    278.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    77.0,
    97.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    345.5,
    87.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=277.0,
    y=76.0,
    width=137.0,
    height=20.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=op_en
)
button_2.place(
    x=145.0,
    y=54.0,
    width=48.0,
    height=48.0
)

canvas.create_text(
    143.0,
    126.0,
    anchor="nw",
    text="กรุณากรอกรหัส",
    fill="#000000",
    font=("Inter", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    331.5,
    263.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=263.0,
    y=252.0,
    width=137.0,
    height=20.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=op_de
)
button_3.place(
    x=138.0,
    y=231.0,
    width=48.0,
    height=48.0
)

canvas.create_text(
    142.0,
    301.0,
    anchor="nw",
    text="กรุณากรอกรหัส",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    41.0,
    26.0,
    anchor="nw",
    text="Encryption",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    35.0,
    208.0,
    anchor="nw",
    text="Decryption",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_rectangle(
    -1.0,
    177.99999998419773,
    558.0000175222922,
    180.0,
    fill="#000000",
    outline="")

canvas.create_text(
    190.0,
    253.0,
    anchor="nw",
    text="เลือกไฟล์",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    202.0,
    75.0,
    anchor="nw",
    text="เลือกไฟล์",
    fill="#000000",
    font=("Inter", 16 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    command=event_decryption_button,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    
)
button_4.place(
    x=448.0,
    y=268.0,
    width=90.0,
    height=34.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    345.5,
    136.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=277.0,
    y=125.0,
    width=137.0,
    height=20.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    333.5,
    311.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=265.0,
    y=300.0,
    width=137.0,
    height=20.0
)
window.resizable(False, False)
window.mainloop()
