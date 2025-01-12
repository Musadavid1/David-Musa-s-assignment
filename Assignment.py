

import tkinter as tk

igala_dict = {
    "eju": "eyes", "imo": "nose", "olo": "neck", "alu": "mouth", "owo": "hand",
    "anyi": "laugh", "akwu": "cry", "uko": "cough", "ola": "body", "ebie": "blood",
    "ojima": "respect", "ogba": "front", "ubi": "back", "uyo": "joy", "ikpa": "bag",
    "oma": "child", "afe": "cloths", "agba": "cheek", "iwo": "pain", "ule": "run"


def search_word():
    word = entry.get()
    result = igala_dict.get(word, "Word not found")
    output.delete(1.0, tk.END)
    output.insert(tk.END, result)

root = (link unavailable)()
root.title("Igala-English Dictionary")

label = tk.Label(root, text="Enter Igala word:")
label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Search", command=search_word)
button.pack()

output = tk.Text(root, height=2, width=20)
output.pack()

root.mainloop()
