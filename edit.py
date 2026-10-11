with open(r"C:\Users\Rishi\Documents\Rishi\Personal\Sarah 2026\00000001.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = "".join(text.split())

with open(r"C:\Users\Rishi\Documents\Rishi\Personal\Sarah 2026\00000001.txt", "w", encoding="utf-8") as file:
    file.write(text)