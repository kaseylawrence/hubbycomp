import customtkinter
import string
import sqlite3

db  = sqlite3.connect('sequences.db')
cursor = db.cursor()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x600")
root.title("Hubby Comp")

def revComp():
    sequence = entryTextbox.get("1.0", "end-1c")
    old_chars = "ACGT"
    replace_chars = "TGCA"
    tab = str.maketrans(old_chars, replace_chars)
    revcomp_result = sequence.translate(tab)[::-1]
    query = cursor.execute('select * from indexes where i5_sequence like ?;', (sequence,)).fetchall()
    revComp_query = cursor.execute('select * from indexes where i5_sequence like?;', (revcomp_result,)).fetchall()
    if query:
        if len(query) > 1:
            messageLabel.configure(text="Original Index found in multiple i5s")
        
        else:
            messageLabel.configure(text="Original Index found in 1 i5")
        for uid,iid,i7seq,i5seq,kitname,manuf,indlen in query:
            #print(f"{row['i5_sequence']} found in {row['index_group']} ")
            message = f"{i5seq} found in {kitname}"
            messageLabel.configure(text=message)
        
        #print(f"{query[0][3]} from {query[0][4]}")
    
    


    if revComp_query:
        if len(revComp_query) > 1:
            messageLabel.configure(text="RevComp Sequence found in multiple i5s")

        else:
            messageLabel.configure(text="RevComp Sequence found")
        for uid,iid,i7seq,i5seq,kitname,manuf,indlen in revComp_query:
            messageLabel.configure(text=f"{i5seq} found in {kitname}")

    if not query and not revComp_query:
        messageLabel.configure(text='No Sequences found in database. Database might be incomplete')

    #print (query)
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

logLabel = customtkinter.CTkLabel(master=frame, text = "Log:")
logLabel.pack(pady=12,padx=12)
messageLabel = customtkinter.CTkLabel(master=frame, text = "")
messageLabel.pack(pady=12,padx=12)



root.mainloop()
