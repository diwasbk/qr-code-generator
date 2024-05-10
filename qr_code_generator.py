import qrcode
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("QR generator")
root.geometry("800x500") 
root.config(bg="red") 
root.resizable(False, False)

def generate():
    name = title_entry.get()
    text = link_entry.get()
    qr = qrcode.make(text)
    qr.save("Qrcodes/" + str(name) + ".png")

    # Open the generated QR code image
    qr_image = Image.open("Qrcode/" + str(name) + ".png")
    # Resize the image to fit the label
    qr_image = qr_image.resize((300, 300))

    # Convert the image to a format that Tkinter can display
    photo = ImageTk.PhotoImage(qr_image)

    # Display the image in the Label
    Image_view.config(image=photo)
    Image_view.image = photo
    
#Making label for image
Image_view = Label(root, bg="red")
Image_view.pack(padx=30, pady=10, side=RIGHT)

qr_code_generator_label = Label(root, text="QR Code Generator", fg="white", bg="red", font="Arial 25 bold")
qr_code_generator_label.place(x=40, y=50)

title = Label(root, text="Title: ", fg="white", bg="red", font="Arial 14 bold")
title.place(x=40, y=200)

title_entry = Entry(root, width=30, font="Arial 14 bold")
title_entry.place(x=100, y=200)

link = Label(root, text="Link: ", fg="white", bg="red", font="Arial 14 bold")
link.place(x=40, y=250)

link_entry = Entry(root, width=30, font="Arial 14 bold")
link_entry.place(x=100, y=250)

btn = Button(root, text="Generate", width=20, font="Arial 8 bold", height=2, bg="black", fg="white",cursor="hand2", command=generate)
btn.place(x=150, y=350)

root.mainloop()
