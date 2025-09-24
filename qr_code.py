from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import os

# Initialize main window
root = Tk()
root.title("QR Code Generator")
root.geometry("500x600")
root.configure(bg="#f0f4f8")
root.resizable(True, True)

# Main frame for content
main_frame = Frame(root, bg="#ffffff", bd=2, relief=RIDGE)
main_frame.pack(padx=30, pady=30, fill=BOTH, expand=True)

# Heading
heading = Label(main_frame, text="📱 QR Code Generator", font=("Arial", 24, "bold"), bg="#ffffff", fg="#273b7a")
heading.pack(pady=(20, 10))

# Link name input
name_label = Label(main_frame, text="Link Name", font=("Arial", 13), bg="#ffffff")
name_label.pack(pady=(10, 0))
name_entry = Entry(main_frame, font=("Arial", 13), width=30, bd=2, relief=SOLID)
name_entry.pack(pady=(0, 10))

# Link input
link_label = Label(main_frame, text="Link or Text", font=("Arial", 13), bg="#ffffff")
link_label.pack(pady=(10, 0))
link_entry = Entry(main_frame, font=("Arial", 13), width=30, bd=2, relief=SOLID)
link_entry.pack(pady=(0, 20))

# QR display area
qr_frame = Frame(main_frame, bg="#ffffff")
qr_frame.pack(pady=10)

# Generate function
def generate():
    for widget in qr_frame.winfo_children():
        widget.destroy()

    link_name = name_entry.get().strip()
    link = link_entry.get().strip()

    if not link_name or not link:
        error = Label(qr_frame, text="⚠ Please enter both fields", font=("Arial", 12), fg="red", bg="#ffffff")
        error.pack()
        return

    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)

    # Load and display QR code
    qr_image = Image.open(file_name)
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label = Label(qr_frame, image=qr_photo, bg="#ffffff")
    qr_label.image = qr_photo
    qr_label.pack()

    success = Label(qr_frame, text=f"✅ QR code saved as {file_name}", font=("Arial", 12), fg="green", bg="#ffffff")
    success.pack(pady=10)

# Generate button
generate_btn = Button(main_frame, text="Generate QR Code", font=("Arial", 13, "bold"), bg="#273b7a", fg="white",
                      activebackground="#1e2f5a", activeforeground="white", command=generate)
generate_btn.pack(pady=10)

# Footer
footer = Label(root, text="© 2025 Tabong | QR Tools", font=("Arial", 10), bg="#f0f4f8", fg="#888")
footer.pack(pady=10)

# Run the app
root.mainloop()
