import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def fetch_dog_img():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    img_url = data['message']

    img_data = requests.get(img_url).content
    img = Image.open(BytesIO(img_data))

    img = img.resize((300, 300), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    label.config(image = img_tk)
    label.image = img_tk

root = tk.Tk()
root.title("Random Dog Viewer")

button = tk.Button(root, text="Get Random Dog", command=fetch_dog_img)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()