# ARSE
Apartment Rental Search Engine (ARSE) makes it easy to search for cheap rentals in an particular area and at a price specified by the user. A XLSX file is automatically generated with the information extracted from the selected websites.

## Requeriments
Use `pip install -r requeriments.txt` to install all the required modules.


## Install Tkinter
### Windows
Installing _python3_ from **[python.org](https://www.python.org/)** will automatically install Tcl/Tk, which of course, is needed by Tkinter.

### Linux
Debian/Ubuntu distributions:
Use the command `sudo apt-get install python3-tk`

For more information visit **[the official Tk website](https://tkdocs.com/tutorial/install.html)**

## Execute
### Windows
First move to **ARSE** directory typing `cd ARSE` and then execute the program using `python.exe .\main.py`

### Linux
First move to **ARSE** directory typing `cd ARSE` and then execute the program using `python3 main.py`

## Compilation
If you want to compile the python code you need to use **[pyinstaller](https://www.pyinstaller.org/)**, so first you need to download the **pyinstaller** module for your OS.

Type this command to compile the code: `pyinstaller.exe --onefile --windowed --name ARSE --icon=img/icon.icon main.py`

It will generate a EXE file in the _dist_ directory, you have to move this EXE file to the main directory (ARSE).

### Download a compiled version of this program
Here is an already compiled version: https://drive.google.com/drive/folders/1CImQizEo8yqQVQJkzuDl8Sdb3LEijBmW

## Crawling websites and generate XLSX
This program use **[requests](https://docs.python-requests.org/en/master/)** and **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** to scrap the websites and get all the information. In order to save this information, the **[xlsxwriter](https://xlsxwriter.readthedocs.io/)** module is used. The fields that contain the XLSX file are: _apartment address, price, telephone number, website URL, real estate agency or private and other info_.
<!--- (I recommend reading this [article](https://www.blog.datahut.co/post/is-web-scraping-legal) on the legality of web crawling) -->


## Why only works for Spain region?
At this moment, this program only works on Spain communities and provinces. This is because the websites used only list flats, houses and apartments of Spain and the JSON files used for users to select the regions only have the provinces and towns/villages of Spain. The JSON files used are from the _[pselect](https://github.com/IagoLast/pselect)_ of [IagoLast](https://github.com/IagoLast) but the _[provincias.json](https://github.com/alb3rtov/ARSE/blob/main/data/provincias.json)_ file has been modified to sort alphabetically. Perhaps in the future I can upgrade so that it can be used in all countries.
