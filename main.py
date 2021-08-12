import tkinter as tk
import tkinter.font as font
from urllib import request
import requests
from bs4 import BeautifulSoup
import crawler
import json
import os
import threading
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
from pathlib import Path

class MainFrame:
    """ Class that contains the main items of the frame """
    def __init__(self, master):
        """ Creates the items that contains main frame """
        title_font = font.Font(size="18", family="Helvetica")
        main_font = font.Font(size="13", family="Helvetica")
        small_font = font.Font(size="10", family="Helvetica")

        self.lbl_title = tk.Label(master, font=title_font, bg="white", text="Buscador de alquiler de pisos")
        self.lbl_title.place(relx=0.5, rely=0.08, anchor=tk.CENTER)

        self.error_label_province = tk.Label(master, width=44, height=2, bg="IndianRed1")

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

        self.error_label_websites = tk.Label(master, bg="IndianRed1", width=65, height=8)

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

        self.checkboxes_list = [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4, self.checkbox5, self.checkbox6, self.checkbox7, self.checkbox8, self.checkbox9]
        self.checkboxes_list_var = [self.v_cb1, self.v_cb2, self.v_cb3, self.v_cb4, self.v_cb5, self.v_cb6, self.v_cb7, self.v_cb8, self.v_cb9]

        self.button_search = tk.Button(master, font=title_font, relief='groove', text="BUSCAR", command = lambda: self.search_matches(self.town_var.get(), self.province_var.get(), self.housing_var.get(), self.entry_max_price.get(), self.entry_min_price.get(), self.num_page_search.get(), self.dir_entry.get(), master))
        self.button_search.place(x=250, y=600, anchor=tk.CENTER)

        self.info_label = tk.Label(master, font=small_font, fg="gray", bg="gray90", height=5, relief=tk.GROOVE, text="  Este campo indica el número de páginas que se  \n  analizarán por cada uno de los sitios web marcados.  \n  Por cada número de página se encontrarán hasta  \n  un máximo de 30 resultados para cada sitio web.  ",anchor='w', justify=tk.LEFT)

        self.dir_entry = tk.Entry(master, bd=2, width=47,font = main_font)
        self.dir_entry.insert(tk.END, os.getcwd() + "\pisos.xlsx")
        self.dir_entry.place(x=35,y=520, height=30)

        self.dir_image = Image.open("img/dir.png")
        self.dir_image = self.dir_image.resize((27, 23), Image.ANTIALIAS)
        self.dir_icon = ImageTk.PhotoImage(self.dir_image)
        self.dir_button = tk.Button(master, bg='white', relief='groove', borderwidth=0, cursor='hand2', image=self.dir_icon, command=self.browse_dir)
        self.dir_button.place(x=430,y=522)
        
        # Launch a thread for check updates
        th = threading.Thread(target=self.check_update)
        th.start()
    
    def check_update(self):
        """ Check if there is a new release on GitHub """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
        }

        res = requests.get("https://github.com/alb3rtov/ARSE", headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        for ver in soup.findAll("span", {"class":"css-truncate css-truncate-target text-bold mr-2"}):
            version = ver.text
            
        if version != crawler.VERSION:
            response = messagebox.askquestion("Actualización disponible", "Hay una nueva actualización disponible. ¿Deseas descargar la nueva versión " + version + "?")
            if response == "yes":
                print("descargar")

    def browse_dir(self):
        """ Request directory for the XLSX file """
        curr_directory = os.getcwd()
        filename = filedialog.askdirectory(initialdir = curr_directory)

        if len(filename) != 0:
            self.dir_entry.delete(0, tk.END)
            self.dir_button.configure(bg="white")
            filename = filename + "/pisos.xlsx"
            self.dir_entry.insert(tk.END, filename)

    def on_enter(self, event):
        """ Show help information """
        self.info_label.place(x=150, y=350)

    def on_leave(self, enter):
        """ Hide help information """
        self.info_label.place_forget()

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
        canvas.place(x=250, y=600, anchor=tk.CENTER)
        canvas.configure(bg="white", highlightbackground ="white")

        master.after(0, self.update_loading_wheel, 0, frames, num_frames, canvas, master, 0)

    def change_cb_color(self, bg, fg):
        """ Change checkboxes bg and fg color """
        for cb in self.checkboxes_list:
            cb.configure(bg=bg, fg=fg)

    def get_xlsxpath_and_name(self, xlsxfile_path):
        """ Get absolute path and name of XLSX file """
        size = len(xlsxfile_path)
        file_length = 0
        for i in range(1, size):
            if xlsxfile_path[size-i] == "\\":
                break
            file_length += 1

        return xlsxfile_path[:-file_length], xlsxfile_path[size-file_length:]

    def rename_xlsxfile(self, xlsxpath, xlsxfilename, xlsxextension):
        """ Rename XSLX file until doesn't exists """
        cnt = 1
        while True:
            aux_xlsxfilename = xlsxfilename + str(cnt)
            xlsx_full_filename = aux_xlsxfilename + "." + xlsxextension
            def_xlsxpath = xlsxpath + xlsx_full_filename
            p = Path(def_xlsxpath)
            
            if not p.exists():
                break
            else:
                cnt += 1

        return def_xlsxpath

    def search_matches(self, town, province, flat_type, max_price, min_price, num_page_search, xlsxfile_path, master):
        """ Generates the list of checked websites and call the crawler function """

        if len(province) == 0:
            self.lbl_province.configure(bg="IndianRed1")
            self.error_label_province.place(x=21,y=95)
            messagebox.showerror("Campos incompletos","Debes seleccionar una provincia donde realizar las búsquedas")
            self.lbl_province.configure(bg="white")
            self.error_label_province.place_forget()
        else:
            at_least_one_ws_selected = False
            checked_sites_list = []

            for cb in self.checkboxes_list_var:
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

                if len(self.dir_entry.get()) != 0:
                    p = Path(xlsxfile_path)
                    if p.exists():
                        res = messagebox.askquestion("El archivo ya existe","El archivo " + xlsxfile_path + " ya existe. ¿Desea crear otro archivo (se creará automáticamente)?")
                        if res == "yes":
                            xlsxpath, xlsxfilename = self.get_xlsxpath_and_name(xlsxfile_path)
                            full_filename = xlsxfilename.split(".")
                            self.dir_entry.delete(0, tk.END)
                            self.dir_entry.insert(tk.END, self.rename_xlsxfile(xlsxpath, full_filename[0], full_filename[1]))
                            self.create_loading_wheel(master)
                            crawler.main_crawler(town, province, websites_list, flat_type, max_price, min_price, num_page_search, self.dir_entry.get(), master)
                    else:
                        self.create_loading_wheel(master)
                        crawler.main_crawler(town, province, websites_list, flat_type, max_price, min_price, num_page_search, xlsxfile_path, master)
                else:
                    self.dir_entry.configure(state="normal")
                    self.dir_entry.configure(bg="IndianRed1")
                    self.dir_button.configure(bg="IndianRed1")
                    messagebox.showerror("Campos incompletos","Debes de indicar una carpeta para\nguardar el archivo XLSX (Excel)")
                    self.dir_entry.configure(bg="white")
                    self.dir_button.configure(bg="white")
            else:
                self.change_cb_color("IndianRed1","white")
                self.error_label_websites.place(x=21,y=370)
                messagebox.showerror("Campos incompletos","Selecciona al menos un sitio web para realizar las búsquedas")
                self.change_cb_color("white","black")
                self.error_label_websites.place_forget()

def main():
    """ Create main frame and set configuration of frame """
    root = tk.Tk()
    root.title("Buscador de alquiler de pisos")
    
    if os.name == "nt":
        root.iconbitmap("img/test.ico")
    else:
        root.iconbitmap("@img/icon.xbm")
    
    root.geometry("500x650")
    root.resizable(False, False)
    root.configure(bg="white")

    main_frame = MainFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()