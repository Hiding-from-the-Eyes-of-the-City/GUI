# GUI

The graphical interface used to interact with the exhibition

## Steps for Use

1. Get the needed requirements

- get python 3.7
- get pip3
- create a venv
  '''
  python3 -m venv .env
  source .env/bin/activate
  '''
- pip3 install flask
- pip3 install numpy
- pip3 install face_recognition

2. run flask server
   cd into gui directory
   '''
   export FLASK_APP=app.py
   python3 -m flask run  
   '''

3. Open on chrome (make sure to download the extensions needed and change download folder to gui)
   http://127.0.0.1:5000/

## Some Tools

**Hide Downloads** by using the Chrome Extension "Always Clear Downloads"

**Fullscreen App** by using `Command + Shift + F` on Mac and `F11` on Windows when in fullscreen
