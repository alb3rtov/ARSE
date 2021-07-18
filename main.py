from os import close
import tkinter as tk
import tkinter.font as font
import crawler
import locations
import requests
import urllib.parse
from tkinter import ttk
from PIL import ImageTk,Image
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class MainFrame:
    """ Class that contains the main items of the frame """
    def __init__(self, master):
        """ Creates the items that contains main frame """
        title_font = font.Font(size="18", family="Helvetica")
        main_font = font.Font(size="13", family="Helvetica")

        self.lbl_title = tk.Label(master, font=title_font, bg="white", text="Buscador de alquiler de pisos")
        self.lbl_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.lbl_ccaa = tk.Label(master, font=main_font, bg="white", text= "CCAA")
        self.lbl_ccaa.place(x=30,y=100)
        #self.entry_location = tk.Entry(master, font=main_font, width= 20, bd=2)
        #self.entry_location.place(x=120,y=102)

        self.ccaa_key_list, self.ccaa_value_list = locations.get_locations("https://apiv1.geoapi.es/comunidades?type=JSON&key=&sandbox=1", "CCOM", "COM")

        self.ccaa_var = tk.StringVar()
        self.ccaa_var.set(self.ccaa_value_list[0])
        self.ccaa_var.trace("w", self.update_provinces_menu)
        self.dropdown_ccaa = ttk.Combobox(master, state="readonly", textvariable=self.ccaa_var, values=self.ccaa_value_list)
        self.dropdown_ccaa.configure(font=main_font)
        self.dropdown_ccaa.place(x=120,y=100)

        self.lbl_province = tk.Label(master, font=main_font, bg="white", text= "Provincia")
        self.lbl_province.place(x=30,y=140)

        self.province_key_list = []
        self.province_value_list = []

        self.province_var = tk.StringVar()
        self.dropdown_province = ttk.Combobox(master, state=tk.DISABLED, textvariable=self.province_var)
        self.dropdown_province.configure(font=main_font)
        self.dropdown_province.place(x=120,y=140)

        self.lbl_flat_type = tk.Label(master, font=main_font, bg="white", text= "Tipo")
        self.lbl_flat_type.place(x=30,y=188)

        self.housing_var = tk.StringVar()
        self.housing_var.set(crawler.housing_types[0])
        self.dropdown_menu_flat_type = ttk.Combobox(master, state="readonly", textvariable = self.housing_var, values=crawler.housing_types)
        self.dropdown_menu_flat_type.configure(font=main_font)
        self.dropdown_menu_flat_type.place(x=120, y=188)

        self.lbl_min_price = tk.Label(master, font=main_font, bg="white", text= "Precio mínimo")
        self.lbl_min_price.place(x=30,y=240)
        self.entry_min_price = tk.Entry(master, font=main_font, width= 20, bd=2)
        self.entry_min_price.place(x=160,y=242)

        self.lbl_max_price = tk.Label(master, font=main_font, bg="white", text= "Precio máximo")
        self.lbl_max_price.place(x=30,y=280)
        self.entry_max_price = tk.Entry(master, font=main_font, width= 20, bd=2)
        self.entry_max_price.place(x=160,y=282)

        self.v_cb1 = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(master, text="Milanuncios", variable=self.v_cb1, bg="white", onvalue=1, offvalue=0)
        self.checkbox1.place(x=30,y=340)

        self.v_cb2 = tk.IntVar()
        self.checkbox2 = tk.Checkbutton(master, text="Fotocasa", variable=self.v_cb2, bg="white", onvalue=1, offvalue=0)
        self.checkbox2.place(x=30,y=380)
        
        self.v_cb3 = tk.IntVar()
        self.checkbox3 = tk.Checkbutton(master, text="Idealista", variable=self.v_cb3, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox3.place(x=30,y=420)

        self.v_cb4 = tk.IntVar()
        self.checkbox4= tk.Checkbutton(master, text="Pisos.com", variable=self.v_cb4, bg="white", highlightcolor="white", onvalue=1, offvalue=0)
        self.checkbox4.place(x=200,y=340)

        self.v_cb5 = tk.IntVar()
        self.checkbox5= tk.Checkbutton(master, text="Vivados", variable=self.v_cb5, bg="white", highlightcolor="white", onvalue=1, offvalue=0)
        self.checkbox5.place(x=200,y=380)

        self.v_cb6 = tk.IntVar()
        self.checkbox6= tk.Checkbutton(master, text="Enalquier", variable=self.v_cb6, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox6.place(x=200,y=420)

        self.v_cb7 = tk.IntVar()
        self.checkbox7= tk.Checkbutton(master, text="Yaencontre", variable=self.v_cb7, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox7.place(x=370,y=340)

        self.v_cb8 = tk.IntVar()
        self.checkbox8= tk.Checkbutton(master, text="Tucasa", variable=self.v_cb8, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox8.place(x=370,y=380)

        self.v_cb9 = tk.IntVar()
        self.checkbox9= tk.Checkbutton(master, text="Departiculares", variable=self.v_cb9, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox9.place(x=370,y=420)

        self.checkboxes_list = [self.v_cb1, self.v_cb2, self.v_cb3, self.v_cb4, self.v_cb5, self.v_cb6, self.v_cb7, self.v_cb8, self.v_cb9]

        self.button_search = tk.Button(master, font=title_font, text="BUSCAR", command = lambda: self.search_matches(self.province_var.get(), self.housing_var.get(), self.entry_max_price.get(), self.entry_min_price.get(), master))
        self.button_search.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def update_provinces_menu(self, *args):
        """ Update provinces menu based on selected CCAA """
        index = self.ccaa_value_list.index(self.ccaa_var.get())
        ccaa_index = self.ccaa_key_list[index]
        
        url = "https://apiv1.geoapi.es/provincias?CCOM=" + ccaa_index + "&type=JSON&key=&sandbox=1"
        self.province_key_list, self.province_value_list = locations.get_locations(url, "CPRO", "PRO")

        self.dropdown_province.configure(values=self.province_value_list, state="readonly")
        self.province_var.set(self.province_value_list[0])
    
    def update_loading_wheel(self, ind, frames, num_frames, canvas, master, cnt):
        """ Update the canvas loading wheel gif """
        frame = frames[ind]
        ind += 1
        if ind == num_frames:
            ind = 0
        canvas.create_image(60, 26, image=frame, anchor=tk.CENTER)
        
        if cnt == 100: # Here check if the search has ended
            canvas.destroy()
        else:
            master.after(20, self.update_loading_wheel, ind, frames, num_frames, canvas, master, cnt+1)

    def create_loading_wheel(self, master, canvas):
        """ Create a canvas with a loading wheel gif """
        num_frames = 25
        filename = "img/loading.gif"

        frames = [tk.PhotoImage(file=filename, format='gif -index %i' %(i)).subsample(4) for i in range(num_frames)]
        
        canvas.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        canvas.configure(bg="white", highlightbackground ="white")
        master.after(0, self.update_loading_wheel, 0, frames, num_frames, canvas, master, 0)

    def search_matches(self, location, flat_type, max_price, min_price, master):
        """ Generates the list of checked websites and call the crawler function """
        canvas = tk.Canvas(width=120, height=52)

        self.create_loading_wheel(master, canvas)
        
        format_address = location.lower()
        format_address = format_address.replace(" ","-")


        checked_sites_list = []

        for cb in self.checkboxes_list:
            checked_sites_list.append(cb.get())

        websites_list = []

        for i in range(len(checked_sites_list)):
            if checked_sites_list[i] == 1:
                websites_list.append(crawler.def_url_sites_list[i])

        crawler.main_crawler(format_address, websites_list, flat_type, max_price, min_price)

def main():
    """ Main function """
    root = tk.Tk()
    root.title("Buscador de alquiler de pisos")
    root.iconbitmap("img/icon.ico")
    root.geometry("500x560")
    root.resizable(False, False)
    root.configure(bg="white")

    main_frame = MainFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()