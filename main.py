from os import close
import tkinter as tk
import tkinter.font as font
import crawler
import requests
import urllib.parse
from tkinter import ttk
from PIL import ImageTk,Image
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class MainFrame:
    def __init__(self, master):
        title_font = font.Font(size="18", family="Helvetica")
        main_font = font.Font(size="13", family="Helvetica")

        self.lbl_title = tk.Label(master, font=title_font, bg="white", text="Buscador de alquiler de pisos")
        self.lbl_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.lbl_location = tk.Label(master, font=main_font, bg="white", text= "Localidad")
        self.lbl_location.place(x=30,y=100)
        self.entry_location = tk.Entry(master, font=main_font, width= 20, bd=2)
        self.entry_location.place(x=120,y=102)

        self.lbl_flat_type = tk.Label(master, font=main_font, bg="white", text= "Tipo")
        self.lbl_flat_type.place(x=30,y=148)

        self.clicked = tk.StringVar()
        self.clicked.set(crawler.flat_types[0])
        self.dropdown_menu_flat_type = tk.OptionMenu(master, self.clicked, *crawler.flat_types)
        self.dropdown_menu_flat_type.configure(font=main_font)
        self.dropdown_menu_flat_type.place(x=120, y=142)

        self.lbl_min_price = tk.Label(master, font=main_font, bg="white", text= "Precio mínimo")
        self.lbl_min_price.place(x=30,y=200)
        self.entry_min_price = tk.Entry(master, font=main_font, width= 20, bd=2)
        self.entry_min_price.place(x=160,y=202)

        self.lbl_max_price = tk.Label(master, font=main_font, bg="white", text= "Precio máximo")
        self.lbl_max_price.place(x=30,y=240)
        self.entry_max_price = tk.Entry(master, font=main_font, width= 20, bd=2)
        self.entry_max_price.place(x=160,y=242)

        self.v_cb1 = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(master, text="Milanuncios", variable=self.v_cb1, bg="white", onvalue=1, offvalue=0)
        self.checkbox1.place(x=30,y=300)

        self.v_cb2 = tk.IntVar()
        self.checkbox2 = tk.Checkbutton(master, text="Fotocasa", variable=self.v_cb2, bg="white", onvalue=1, offvalue=0)
        self.checkbox2.place(x=30,y=340)
        
        self.v_cb3 = tk.IntVar()
        self.checkbox3 = tk.Checkbutton(master, text="Idealista", variable=self.v_cb3, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox3.place(x=30,y=380)

        self.v_cb4 = tk.IntVar()
        self.checkbox4= tk.Checkbutton(master, text="Pisos.com", variable=self.v_cb4, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox4.place(x=200,y=300)

        self.v_cb5 = tk.IntVar()
        self.checkbox5= tk.Checkbutton(master, text="Vivados", variable=self.v_cb5, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox5.place(x=200,y=340)

        self.v_cb6 = tk.IntVar()
        self.checkbox6= tk.Checkbutton(master, text="Enalquier", variable=self.v_cb6, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox6.place(x=200,y=380)

        self.v_cb7 = tk.IntVar()
        self.checkbox7= tk.Checkbutton(master, text="Yaencontre", variable=self.v_cb7, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox7.place(x=370,y=300)

        self.v_cb8 = tk.IntVar()
        self.checkbox8= tk.Checkbutton(master, text="Tucasa", variable=self.v_cb8, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox8.place(x=370,y=340)

        self.v_cb9 = tk.IntVar()
        self.checkbox9= tk.Checkbutton(master, text="Departiculares", variable=self.v_cb9, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox9.place(x=370,y=380)

        self.checkboxes_list = [self.v_cb1, self.v_cb2, self.v_cb3, self.v_cb4, self.v_cb5, self.v_cb6, self.v_cb7, self.v_cb8, self.v_cb9]

        self.button_search = tk.Button(master, font=title_font, text="BUSCAR", command = lambda: self.search_matches(self.entry_location.get(), self.clicked.get(), self.entry_max_price.get(), self.entry_min_price.get()))
        self.button_search.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def search_matches(self, location, flat_type, max_price, min_price):
        #Go to list of each site selected and scrap that website
        url_location = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'
        response = requests.get(url_location).json()

        format_address = location.lower()
        format_address = format_address.replace(" ","-")

        checked_sites_list = []

        for cb in self.checkboxes_list:
            checked_sites_list.append(cb.get())

        websites_list = []

        for i in range(len(checked_sites_list)):
            if checked_sites_list[i] == 1:
                websites_list.append(crawler.def_url_sites_list[i])

        crawler.main_crawler(format_address, websites_list, response[0]["lat"], response[0]["lon"], flat_type, max_price, min_price)
    
def main():
    root = tk.Tk()
    root.title("Buscador de alquiler de pisos")
    #root.iconbitmap("img/icaad.ico")
    root.geometry("500x500")
    root.resizable(False, False)
    root.configure(bg="white")

    main_frame = MainFrame(root)

    root.mainloop()

if __name__ == "__main__":
    main()