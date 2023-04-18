import xlwings as xw
import pandas as pd
import tkinter as tkt
import base64
import requests
# from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
from io import BytesIO


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"


if __name__ == "__main__":

    # xw.Book("/Users/jeremyperras/Desktop/csv/Excel/excel.xlsm").set_mock_caller()
    # wb = xw.Book.caller()
    # sheet = wb.sheets[0]
    data = pd.read_csv("/Users/jeremyperras/Desktop/csv/cards.csv")
    # xw.view(data, sheet=xw.sheets.active)
    url = data['image_url'][0]
    response = requests.get(url)

    # img.show()
    # print(img)
    print(list(data.columns.values))
    window = tkt.Tk()
    window.geometry('350x750')
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    lbl = tkt.Label(window, text="Hello", image=img)

    lbl.grid(column=0, row=0)
    txt = tkt.Entry(window, width=10)
    txt.grid(column=3, row=0)
    btn = tkt.Button(window, text="Click Me")
    # image_byt = urlopen(url).read()
    # image_b64 = base64.encodestring(image_byt)
    # photo = tk.PhotoImage(data=image_b64)

    # frame = tkt.Frame(window, width=600, height=400)
    # frame.pack()
    # frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
    # frame = tkt.Frame(window, width=200, height=200)
    # cv = tkt.Canvas(bg='white')
    # cv.pack(side='top', fill='both', expand='yes')
    # cv.create_image(10, 10, image=photo, anchor='nw')
    # img = ImageTk.PhotoImage(Image.open(response))
    # img.grid(column=1, row=0)
    # btn.grid(column=1, row=0)
    window.title("Welcome to LikeGeeks app")

    def clicked():

        res = "Welcome to " + txt.get()

        lbl.configure(text=res)

    btn = tkt.Button(window, text="Click Me", command=clicked)
    # btn.grid(column=2, row=0)
    # label = tkt.Label(frame, image=img)
    # label.grid(column=2, row=0)

    # imgURL = 'https://www.marketbeat.com/scripts/temp/estimateswide4879.png'
    # img = ImageTk.PhotoImage(Image.open(url))
    # panel = tkt.Label(root, image=img)
    # panel.pack(side="bottom", fill="both", expand="yes")

    # panel = tkt.Label(window, image=img)

    # lbl.pack(side="bottom", fill="both", expand="yes")

    window.mainloop()
