# Description - PYTHON, check out R version at the end of this guide
This is a python script to make registered scan folder compatible for treeseg algorithm at https://github.com/apburt/treeseg

## Tutorial - run on local machine
Make sure you have python installed.
Clone this repository to your machine

```
git clone https://github.com/vietle94/Treeseg-directories-script.git
```

or just download this and then unzip.

Next, open the terminal inside the folder by typing

```
cmd
```
from the address bar and press enter.

![Open terminal](img/pic1.PNG)

Then type in

```
python treeseg_folder.py
```
and follow instructions. There will be two options:

- Type 0 to copy and make treeseg directories hierarchy from .rxp files in registered scan directory

- Type 1 to rename .DAT files

## Tutorial - run on Puhti

First, copy registered scan folder to Puhti.

Login to Puhti, then located preferred directory for the script

Clone this repository to current directory

```
git clone https://github.com/vietle94/Treeseg-directories-script.git
```

Go inside this directory and run this script:

```
cd Treeseg-directories-script
python treeseg_folder.py
```
and follow instructions. NOTE THAT YOU NEED TO TYPE IN "1" AND "0" with the quotation mark in this environment

There will be two options:

- Type "0" to copy and make treeseg directories hierarchy from .rxp files in registered scan directory or

- Type "1" to rename .DAT files

## Recommended workflow

Use option 0 to create and copy files from registered scan folder in to a new folder, in order to upload to treeseg later

Then open RiSCAN Pro to extract .DAT files into a subfolder called matrix

Finally, run the script again and use option 1 to rename those .DAT files into correct format

# Description - R

There is another version of this application in R. Simply download it, open in Rstudio and follow the instruction
