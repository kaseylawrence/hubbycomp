import customtkinter
import string

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x400")
root.title("Hubby Comp")

def revComp():
    sequence = entryTextbox.get("1.0", "end-1c")
    old_chars = "ACGT"
    replace_chars = "TGCA"
    tab = str.maketrans(old_chars, replace_chars)
    revcomp_result = sequence.translate(tab)[::-1]
    resultTextbox.delete("1.0", "end")
    resultTextbox.insert("1.0", revcomp_result)

frame = customtkinter.CTkFrame(master=root,)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Hubby Comp")
label.pack(pady=12, padx=10)

entryLabel = customtkinter.CTkLabel(master=frame, text = "Enter sequence to reverse complement:")
entryLabel.pack(pady=12, padx = 10)

entryTextbox = customtkinter.CTkTextbox(master=frame, width=300, height=2)
entryTextbox.pack(pady=12, padx = 10)

button = customtkinter.CTkButton(master=frame, text="Get Reverse Complement", command=revComp)
button.pack(pady=12, padx=10)


resultLabel = customtkinter.CTkLabel(master=frame, text="Reverse Complement Sequence:")
resultLabel.pack(pady=12, padx=10)
resultTextbox = customtkinter.CTkTextbox(master=frame, width=300, height=2)
resultTextbox.pack(pady=12, padx = 10)

root.mainloop()
