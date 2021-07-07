import tkinter as tk
import tkinter.font as font
import crawler
import requests
import urllib.parse
from tkinter import ttk
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

        self.v_cb1 = tk.IntVar()
        self.checkbox1 = ttk.Checkbutton(master, text="Milanuncios", variable=self.v_cb1, onvalue=1, offvalue=0)
        self.checkbox1.place(x=30,y=300)

        self.v_cb2 = tk.IntVar()
        self.checkbox2 = ttk.Checkbutton(master, text="Fotocasa", variable=self.v_cb2, onvalue=1, offvalue=0)
        self.checkbox2.place(x=30,y=340)
        
        self.v_cb3 = tk.IntVar()
        self.checkbox3 = ttk.Checkbutton(master, text="Idealista", variable=self.v_cb3, onvalue=1, offvalue=0)
        self.checkbox3.place(x=30,y=380)

        #self.checkboxes_list = [self.checkbox1, self.checkbox2, self.checkbox3]
        self.checkboxes_list = [self.v_cb1, self.v_cb2, self.v_cb3]
        
        self.button_search = tk.Button(master, font=title_font, text="BUSCAR", command = lambda: self.search_matches(self.entry_location.get()))
        self.button_search.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def search_matches(self, location):
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

        crawler.main_crawler(format_address, websites_list, response[0]["lat"], response[0]["lon"])
    
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
