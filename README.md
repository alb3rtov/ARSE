# ARSE
Apartment Rental Search Engine (ARSE) makes it easy to search for cheap rentals in an particular area and at a price specified by the user. A XLSX file is automatically generated with the information extracted from the selected websites.

## Requeriments
Use `pip install -r requeriments.txt` to install the required modules.


## Install Tkinter
### Windows
Installing _python3_ from **[python.org](https://www.python.org/)** will automatically install Tcl/Tk, which of course, is needed by Tkinter.

### Linux
Debian/Ubuntu distributions:
Use this command `sudo apt-get install python3-tk`

For more information visit **[this website](https://tkdocs.com/tutorial/install.html)**

## Execute
### Windows
First move to **ARSE** directory typing `cd ARSE` and then execute the program using `python.exe .\main.py`.

### Linux
First move to **ARSE** directory typing `cd ARSE` and then execute the program using `python3 main.py`.


## Crawling websites and generate XLSX
This program use **[requests](https://docs.python-requests.org/en/master/)** and **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** to scrap the websites and get all the information. In order to save this information, it's used the **[xlsxwriter](https://xlsxwriter.readthedocs.io/)** module. The fields that contain the XLSX file are: apartment address, price, telephone number, website URL, real estate agency or private and other info.


## Why only works for Spain region?
At this moment, this program only works on Spain communities and provinces. This is because the websites used only list flats, houses and apartments of Spain and the JSON files used for users to select the regions only have the provinces and towns/villages of Spain. Perhaps in the future I can upgrade so that it can be used in all countries.


## Download a compiled version of this program
Onedrive link very soon...
