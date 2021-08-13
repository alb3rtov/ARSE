# ARSE
Apartment Rental Search Engine (ARSE) makes it easy to search for cheap rentals in an particular area and at a price specified by the user. A XLSX file is automatically generated with the information extracted from the selected websites.

## Requeriments
Use the command `pip install -r requeriments.txt` to install all the required modules.

For Linux users, in order to install the `xlsxwriter` correctly, you must install it from your package manager. For Debian/Ubuntu just type `sudo apt-get install python-xlsxwriter`. If this doesn't work, and still getting a _ImportError: No module named xlsxwriter_, you must to clone de official repository of **[xlsxwriter](https://github.com/jmcnamara/XlsxWriter)** and then install it using `sudo python3 setup.py install`. If you still getting any issue with `xlsxwriter` module visit the [official website](https://xlsxwriter.readthedocs.io/getting_started.html). 

## Install Tkinter
### Windows
Installing _python3_ from <a href="https://www.python.org/" target="_blank">**python.org**</a> will automatically install Tcl/Tk, which of course, is needed by Tkinter.

### Linux
For Debian/Ubuntu distributions use the command: `sudo apt-get install python3-tk`

For more information visit **[the official Tk website](https://tkdocs.com/tutorial/install.html)**

## Execute
### Windows
First move to **ARSE** directory typing `cd ARSE` and then execute the program using `python.exe .\main.py`

### Linux
First move to **ARSE** directory typing `cd ARSE` and then execute the program using `python3 main.py`

## Compilation
If you want to compile the python code you need to use **[pyinstaller](https://www.pyinstaller.org/)**, so first you need to download the **pyinstaller** module for your OS (it will install automatically if you use _[requeriments.txt](https://github.com/alb3rtov/ARSE/blob/main/requeriments.txt)_)

Type this command to compile the code: 

    pyinstaller.exe --onefile --windowed --name ARSE --icon=img/icon.icon main.py

It will generate a EXE file in the _dist_ directory, you have to move this EXE file to the main directory (ARSE).

### Download a compiled version of this program
You can download a compiled version in the releases page: https://github.com/alb3rtov/ARSE/releases

## Crawling websites and generate XLSX
This program use **[requests](https://docs.python-requests.org/en/master/)** and **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** to scrap the websites and get all the information. In order to save this information, the **[xlsxwriter](https://xlsxwriter.readthedocs.io/)** module is used. The fields that contain the XLSX file are: _apartment address, price, telephone number, website URL, real estate agency or private and other info_.
I recommend reading this [article](https://www.blog.datahut.co/post/is-web-scraping-legal) on the legality of web crawling.


## Why only works for Spain region?
At this moment, this program only works on Spain communities and provinces. This is because the websites used only list flats, houses and apartments of Spain and the JSON files used for users to select the regions only have the provinces and towns/villages of Spain. The JSON files used are from the _[pselect](https://github.com/IagoLast/pselect)_ of [IagoLast](https://github.com/IagoLast) but the _[provincias.json](https://github.com/alb3rtov/ARSE/blob/main/data/provincias.json)_ file has been modified to sort alphabetically. Perhaps in the future I can upgrade so that it can be used in all countries.
