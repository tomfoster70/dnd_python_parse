# dnd_python_parse

Python script to parse the xml output files into the standard dnd pdf format for the andriod app "Fifth Edition Character Sheet"

https://play.google.com/store/apps/details?id=com.wgkammerer.testgui.basiccharactersheet.app&hl=en_GB

# How to setup

 1. Install fdfgen
    - pip install fdfgen
    - or https://github.com/ccnmtl/fdfgen
 2. Install pdftk
    - Windows - https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
    - Ubuntu  - sudo apt-get install pdftk

# How to use

 1. Download this script
 2. Open app and export character xml to Googledrive
 3. Create a folder called "input" and copy the file into it (it will do all files in the input folder). It should look like this.
 
 dnd_python_parse/
    .gitignore
    Character Sheet - Alternative - Form Fillable.pdf
    DnD_5E_CharacterSheet - Form Fillable.pdf
    LICENSE
    README.md
    output_pdf.py
    test1.txt
    input/
        Character_from_app_file_1
        Character_from_app_file_2
 
 
 4. double click output_pdf.py
 5. look in the "output" folder

# TODO

* Make even easier to use for people with no python knowledge

# Known issues

 1. Alternative form dosn't do history properly. 