
# Welcome to Talk App!

This is a Python Flask based web app which can read text in images, pdfs and text files.
## Installation
To Install and run locally, you need to have [Python 3.7](https://www.python.org/downloads/) or above installed. You'll also need to install [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Home.html) engine and training data for the languages you want to support. Currently, the app only supports English, Urdu, Hindi and French. So, only install those training data packs.
 ### Steps for Ubuntu
1. Python3 might already be installed for you, if you are on ubuntu. If not then open up terminal and type
	``` bash
     sudo apt install python3
	```
2. Install pip3 for python3
	``` bash
    sudo apt install python3-pip
    ```
3. Install virtual environment for python
	``` bash
    sudo apt install python3-venv 
	```
4. Install tesseract ocr engine for ubuntu and language training data for english, urdu, hindi and french

	``` bash
    sudo apt install tesseract-ocr
    sudo apt install tesseract-ocr-eng
    sudo apt install tesseract-ocr-urd
	sudo apt install tesseract-ocr-hin
    sudo apt install tesseract-ocr-fra
	```
5. Open up a new terminal and get the repo of project from github
	``` bash
    git clone https://github.com/yehyaumar/talk.git
    ```
    **Note**: Install git if you haven't already
	``` bash
	  sudo apt install git
	```
6. Activate python virtual environment within it
	```bash
	cd talk
	python3 -m venv venv
	source venv/bin/activate
	```
7. Install dependencies
	```bash
	pip install -r requirements.txt
	```
8. Now run the server using,
	```bash
	flask run
	```
9. Open up your browser and visit http://localhost:5000. The app should open up.

**Note**: Above steps are required to be followed to run the app first time.
After that just open up a terminal in the *talk* folder and run these instructions one by one.
```bash
source venv/bin/activate
flask run
```

### For Windows
1. Download and Install [python3](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe) for windows. Do not forget to select *Add Python to PATH*

2. Download and Install [Tesseract v4](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v4.1.0.20190314.exe) for windows
3. Download and Install [Git](https://github.com/git-for-windows/git/releases/download/v2.27.0.windows.1/Git-2.27.0-64-bit.exe) for windows
4. Download training data for [Urdu](https://github.com/tesseract-ocr/tessdata/raw/4.00/urd.traineddata), [Hindi](https://github.com/tesseract-ocr/tessdata/raw/4.00/hin.traineddata) and [French](https://github.com/tesseract-ocr/tessdata/raw/4.00/fra.traineddata) languages [English is available by default].
5. Copy the training data files to __*C:\Program Files\Tesseract-OCR\tessdata*__ folder
6. Make sure path to tesseract binaries are added to your PATH variable. 
	If not then copy simply copy  __*C:\Program Files\Tesseract-OCR*__ and on your desktop Right-Click *This PC*, go to *Properties > Advanced System Settings > Environment Variables > Path*. Double click on *Path*, Click *New* and paste, then Click *Ok*.
7. Open *cmd prompt*, and copy these instructions one by one
```bash
mkdir python
cd python
git clone https://github.com/yehyaumar/talk.git
cd talk
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
flask run
```
8. Open up your browser and visit [http://localhost:5000](http://localhost:5000/). The app should open up.

**Note**: Above steps are required to be followed to run the app first time.
After that just open up a *cmd promtp* in the *talk* folder and run these instructions one by one.
```bash
.\venv\Scripts\activate
flask run
```
