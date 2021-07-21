import tkinter as tk
import tkinter.font as font
import crawler
import json
import os
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

class MainFrame:
    """ Class that contains the main items of the frame """
    def __init__(self, master):
        """ Creates the items that contains main frame """
        title_font = font.Font(size="18", family="Helvetica")
        main_font = font.Font(size="13", family="Helvetica")
        small_font = font.Font(size="10", family="Helvetica")

        self.lbl_title = tk.Label(master, font=title_font, bg="white", text="Buscador de alquiler de pisos")
        self.lbl_title.place(relx=0.5, rely=0.093, anchor=tk.CENTER)
        self.lbl_province = tk.Label(master, font=main_font, bg="white", text= "Provincia")
        self.lbl_province.place(x=30,y=100)

        with open("data/provincias.json", encoding="utf8") as json_file:
            data = json.load(json_file)

        self.province_key_list = []
        self.province_value_list = []

        for i in range(len(data)):
            self.province_key_list.append(data[i]["id"])
            self.province_value_list.append(data[i]["nm"])

        self.province_var = tk.StringVar()
        #self.province_var.set(self.province_value_list[0])
        self.province_var.trace("w", self.update_towns_menu)
        self.dropdown_province = ttk.Combobox(master, width=20, state="readonly", textvariable=self.province_var, values=self.province_value_list)
        self.dropdown_province.configure(font=main_font)
        self.dropdown_province.place(x=120,y=100)

        self.lbl_town = tk.Label(master, font=main_font, bg="white", text= "Municipio")
        self.lbl_town.place(x=30,y=140)

        self.town_value_list = []

        self.town_var = tk.StringVar()
        self.dropdown_town = ttk.Combobox(master, width=20, state=tk.DISABLED, textvariable=self.town_var)
        self.dropdown_town.configure(font=main_font)
        self.dropdown_town.place(x=120,y=140)

        self.lbl_flat_type = tk.Label(master, font=main_font, bg="white", text= "Tipo")
        self.lbl_flat_type.place(x=30,y=188)

        self.housing_var = tk.StringVar()
        self.housing_var.set(crawler.housing_types[0])
        self.dropdown_menu_flat_type = ttk.Combobox(master, width=15, state="readonly", textvariable = self.housing_var, values=crawler.housing_types)
        self.dropdown_menu_flat_type.configure(font=main_font)
        self.dropdown_menu_flat_type.place(x=80, y=188)

        self.lbl_min_price = tk.Label(master, font=main_font, bg="white", text= "Precio mínimo (€)")
        self.lbl_min_price.place(x=30,y=240)
        self.entry_min_price = tk.Entry(master, font=main_font, width= 20, bd=2)
        self.entry_min_price.place(x=180,y=242)
        self.lbl_optional1 = tk.Label(master, font=small_font, bg="white", fg="gray", text= "(Opcional)")
        self.lbl_optional1.place(x=370,y=242)

        self.lbl_max_price = tk.Label(master, font=main_font, bg="white", text= "Precio máximo (€)")
        self.lbl_max_price.place(x=30,y=280)
        self.entry_max_price = tk.Entry(master, font=main_font, width= 20, bd=2)
        self.entry_max_price.place(x=180,y=282)
        self.lbl_optional2 = tk.Label(master, font=small_font, bg="white", fg="gray", text= "(Opcional)")
        self.lbl_optional2.place(x=370,y=282)

        self.lbl_num_page_search = tk.Label(master, font=main_font, bg="white", text= "Número de páginas")
        self.lbl_num_page_search.place(x=30,y=320)

        self.num_page_search = tk.StringVar()
        self.num_page_search.set(1)
        self.dropdown_num_page_search = ttk.Combobox(master, width=7, state="readonly", textvariable=self.num_page_search, values=[1,2,3,4,5,"6 o más"])
        self.dropdown_num_page_search.configure(font=main_font)
        self.dropdown_num_page_search.place(x=190, y=320)

        self.info_image = Image.open("img/info.png")
        self.info_image = self.info_image.resize((20, 20), Image.ANTIALIAS)
        self.info_icon = ImageTk.PhotoImage(self.info_image)
        self.info_icon_label = tk.Label(master, image=self.info_icon, bg="white")
        self.info_icon_label.place(x=290, y=320)
        self.info_icon_label.bind("<Enter>", self.on_enter)
        self.info_icon_label.bind("<Leave>", self.on_leave)

        self.v_cb1 = tk.IntVar()
        self.checkbox1 = tk.Checkbutton(master, text="Milanuncios", variable=self.v_cb1, bg="white", onvalue=1, offvalue=0)
        self.checkbox1.place(x=30,y=380)

        self.v_cb2 = tk.IntVar()
        self.checkbox2 = tk.Checkbutton(master, text="Fotocasa", variable=self.v_cb2, bg="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox2.place(x=30,y=420)
        
        self.v_cb3 = tk.IntVar()
        self.checkbox3 = tk.Checkbutton(master, text="Idealista", variable=self.v_cb3, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox3.place(x=30,y=460)

        self.v_cb4 = tk.IntVar()
        self.checkbox4= tk.Checkbutton(master, text="Pisos.com", variable=self.v_cb4, bg="white", highlightcolor="white", onvalue=1, offvalue=0)
        self.checkbox4.place(x=200,y=380)

        self.v_cb5 = tk.IntVar()
        self.checkbox5= tk.Checkbutton(master, text="Vivados", variable=self.v_cb5, bg="white", highlightcolor="white", onvalue=1, offvalue=0)
        self.checkbox5.place(x=200,y=420)

        self.v_cb6 = tk.IntVar()
        self.checkbox6= tk.Checkbutton(master, text="Enalquier", variable=self.v_cb6, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox6.place(x=200,y=460)

        self.v_cb7 = tk.IntVar()
        self.checkbox7= tk.Checkbutton(master, text="Yaencontre", variable=self.v_cb7, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox7.place(x=370,y=380)

        self.v_cb8 = tk.IntVar()
        self.checkbox8= tk.Checkbutton(master, text="Tucasa", variable=self.v_cb8, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox8.place(x=370,y=420)

        self.v_cb9 = tk.IntVar()
        self.checkbox9= tk.Checkbutton(master, text="Departiculares", variable=self.v_cb9, bg="white", highlightcolor="white", onvalue=1, offvalue=0, state=tk.DISABLED)
        self.checkbox9.place(x=370,y=460)

        self.checkboxes_list = [self.v_cb1, self.v_cb2, self.v_cb3, self.v_cb4, self.v_cb5, self.v_cb6, self.v_cb7, self.v_cb8, self.v_cb9]

        self.button_search = tk.Button(master, font=title_font, relief='groove', text="BUSCAR", command = lambda: self.search_matches(self.town_var.get(), self.province_var.get(), self.housing_var.get(), self.entry_max_price.get(), self.entry_min_price.get(), master))
        self.button_search.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.info_label = tk.Label(master, font=small_font, fg="gray", bg="white", text="",anchor='w', justify=tk.LEFT)
        self.info_label.place(x=200, y=350)

    def on_enter(self, event):
        self.info_label.configure(bg="gray90", relief=tk.GROOVE, text=" Este campo indica el número de \n páginas que se analizarán por cada \n uno de los sitios web seleccionados ")

    def on_leave(self, enter):
        self.info_label.configure(bg="white",relief=tk.FLAT, text="")

    def update_towns_menu(self, *args):
        """ Update town menu based on selected province """
        self.town_value_list = []

        index = self.province_value_list.index(self.province_var.get())
        province_index = self.province_key_list[index]
        
        with open("data/municipios.json", encoding="utf8") as json_file:
            data = json.load(json_file)

        for i in range(len(data)):
            if data[i]["id"][0:2] == str(province_index):
                self.town_value_list.append(data[i]["nm"])

        self.dropdown_town.configure(values=self.town_value_list, state="readonly")
        self.town_var.set(self.town_value_list[0])
    
    def update_loading_wheel(self, ind, frames, num_frames, canvas, master, cnt):
        """ Update the canvas loading wheel gif """
        global search_completed
        frame = frames[ind]
        ind += 1
        if ind == num_frames:
            ind = 0
        canvas.create_image(60, 26, image=frame, anchor=tk.CENTER)

        if cnt == 100: # Here check if the search has ended
            canvas.destroy()
        else:
            master.after(20, self.update_loading_wheel, ind, frames, num_frames, canvas, master, cnt+1)

    def create_loading_wheel(self, master):
        """ Create a canvas with a loading wheel gif """
        num_frames = 25
        filename = "img/loading.gif"

        frames = [tk.PhotoImage(file=filename, format='gif -index %i' %(i)).subsample(4) for i in range(num_frames)]
        canvas = tk.Canvas(width=120, height=52)
        canvas.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        canvas.configure(bg="white", highlightbackground ="white")

        master.after(0, self.update_loading_wheel, 0, frames, num_frames, canvas, master, 0)

    def search_matches(self, town, province, flat_type, max_price, min_price, master):
        """ Generates the list of checked websites and call the crawler function """

        if len(town) == 0 or len(province) == 0:
            messagebox.showerror("Campos incompletos","Selecciona una provincia y municipio")
        else:
            at_least_one_ws_selected = False
            checked_sites_list = []

            for cb in self.checkboxes_list:
                checked_sites_list.append(cb.get())

            websites_list = []

            for i in range(len(checked_sites_list)):
                if checked_sites_list[i] == 1:
                    websites_list.append(crawler.def_url_sites_list[i])
                    at_least_one_ws_selected = True
            
            if at_least_one_ws_selected:
                province = province.lower()
                province = province.replace(" ","-")

                town = town.lower()
                town = town.replace(" ", "-")

                self.create_loading_wheel(master)
                crawler.main_crawler(town, province, websites_list, flat_type, max_price, min_price)
            else:
                messagebox.showerror("Campos incompletos","Selecciona al menos un sitio web para realizar las búsquedas")

def main():
    """ Create main frame and set configuration of frame """
    root = tk.Tk()
    root.title("Buscador de alquiler de pisos")
    
    if os.name == "nt":
        root.iconbitmap("img/icon.ico")
    else:
        root.iconbitmap("@img/icon.xbm")
    
    root.geometry("500x600")
    root.resizable(False, False)
    root.configure(bg="white")

    main_frame = MainFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
