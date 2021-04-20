# Python offline packages
This script is used to install packages offline

## Note: couldn't add the tensorflow wheels due to big file size, download it from these links and add it to the Packages folder
https://files.pythonhosted.org/packages/8e/89/3e3b9f29a8e0358d341a6d1eb2df6d3a04e5cac51324c0774f37d6a48d78/tensorflow-2.5.0rc1-cp39-cp39-win_amd64.whl
https://files.pythonhosted.org/packages/ad/fc/fccaa149d7ccc165de01d62d19e5e9492e87ad23a7106f6dfe132800ca6f/tensorflow-2.4.1-cp38-cp38-win_amd64.whl


## Packages included:
Arrow
auto-py-to-exe
black
boto3
bottle
bs4
convertdate
Cython
Eli5
FlashText
ipykernel
jupyter
keras
lightgbm
matplotlib
MoviePy
mypy 
notebook
numpy
opencv-python
openpyxl
pandas
pdfminer
Peewee
pip v21.0.1
pydot
pylint
PyPDF2
PyQt5
PyQt5Designer
PyQt5-stubs
PyQt6
pytest
python-dateutil
Pytil
pyttsx3
pywin32
requests
scikit-learn
scipy
setuptools
spacy + (en_core_web_sm + en_core_web_md)
SQLAlchemy
statsmodels
tensorflow
textract
Theano
wheel
xlrd
XlsxWriter
xlwings

<br>

## Installation:
Edit install.bat
py .\Packages\install_packages.py [requirement file.txt] [path]
e.g. py .\Packages\install_packages.py D:\req.txt D:\Packages

</br>

<br>

### Create new environment
```
python -m venv C:\Program64\Python\venv\Project1
```

## To install: run the following command in CMD
Download the Packages folder to C:\Program64\Python\Packages then run the following command
```
py C:\Program64\Python\Packages\install_packages.py
```
</br>

### Run jupyter notebook
```
jupyter notebook
```
