import tkinter as tk
from tkinter import ttk, messagebox, font

def generate_reference():

    author = author_var.get()
    year = year_var.get()
    title = title_var.get()
    volume = volume_var.get()
    publisher = publisher_var.get()
    place = place_var.get()
    access = access_var.get()
    url = url_var.get()
    website = website_var.get()

    whole = [author, year, title, volume, website, publisher, place, access, url]
    whole = [f"<{p}>" if p == url and p.strip() else p for p in whole if p.strip()]
    ref1 = ", ".join(whole) + "."

    in_text = [author, year]
    in_text = [p for p in in_text if p.strip()]
    ref2 = "(" + ", ".join(in_text) + ")"

    reference_tab = tk.Toplevel()
    reference_tab.title("Generated Reference")
    reference_tab.geometry("1500x420")

    here_reference = tk.Label(reference_tab, text="Reference:", font=("Arial", 12, "bold"))
    here_reference.pack(anchor="w", padx=10, pady=(10, 0))

    text_tab1 = tk.Text(reference_tab, wrap="word", height=5, font=("Arial", 12))
    text_tab1.pack(expand=False, fill="x", padx=10, pady=(0,10))
    text_tab1.insert("1.0", ref1)
    text_tab1.config(state="disabled")
    italic_font = font.Font(text_tab1, text_tab1.cget("font"))
    italic_font.configure(slant="italic")
    text_tab1.tag_configure("italic", font=italic_font)

    start_index = ref1.find(title)
    if start_index != -1:
        start = f"1.{start_index}"
        end = f"1.{start_index + len(title)}"
        text_tab1.tag_add("italic", start, end)
    
    intext_reference = tk.Label(reference_tab, text="In-Text Reference:", font=("Arial", 12, "bold"))
    intext_reference.pack(anchor="w", padx=10, pady=(10, 0))

    text_tab2 = tk.Text(reference_tab, wrap="word", height=5, font=("Arial", 12))
    text_tab2.pack(expand=False, fill="x", padx=10, pady=(0,10))
    text_tab2.insert("1.0", ref2)
    text_tab2.config(state="disabled")


root = tk.Tk()
root.title("Harvard AGPS Referencer")
root.geometry("700x450")

title = tk.Label(root, text="This AGPS referencer currently supports: Website Home Page, Web Page, Books, Articles, and Paper referencing", fg="red", font=("Arial", 10, "italic"))
title.pack(side="top", fill="x", padx=10, pady=0)
title = tk.Label(root, text="Note: not all fields require an entry, just add what you can", font=("Arial", 10, "bold"))
title.pack(side="top", fill="x", padx=10, pady=0)

author_var = tk.StringVar()
year_var = tk.StringVar()
title_var = tk.StringVar()
volume_var = tk.StringVar()
place_var = tk.StringVar()
publisher_var = tk.StringVar()
website_var = tk.StringVar()
url_var = tk.StringVar()
access_var = tk.StringVar()

ttk.Label(root, text="Author Surname/Organisation:").pack()
ttk.Entry(root, textvariable=author_var).pack()
ttk.Label(root, text="Year:").pack()
ttk.Entry(root, textvariable=year_var).pack()
ttk.Label(root, text="Title:").pack()
ttk.Entry(root, textvariable=title_var).pack()
ttk.Label(root, text="Volume/Edition:").pack()
ttk.Entry(root, textvariable=volume_var).pack()
ttk.Label(root, text="Company/Publication Location:").pack()
ttk.Entry(root, textvariable=place_var).pack()
ttk.Label(root, text="Publisher/Company Name:").pack()
ttk.Entry(root, textvariable=publisher_var).pack()
ttk.Label(root, text="Website Name:").pack()
ttk.Entry(root, textvariable=website_var).pack()
ttk.Label(root, text="URL:").pack()
ttk.Entry(root, textvariable=url_var).pack()
ttk.Label(root, text="Viewed Day Month Year:").pack()
ttk.Entry(root, textvariable=access_var).pack()
ttk.Button(root, text="Generate Reference", command=generate_reference).pack(pady=10)

root.mainloop()
#extra line for goodluck