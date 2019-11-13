from flask import Flask, render_template, request
import face_recognition
import cv2
import numpy as np
from os import path
from time import sleep


app = Flask('__name__')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/capture', methods=['GET'])
def capture():
    sleep(2)
    num = request.args.get('name')
    file = str(num)+'.png'
    np.load.__defaults__=(None, True, True, 'ASCII')
    print(file)

    try:
        if (path.exists(file)):
            person_image = face_recognition.load_image_file(file)
            person_name = str(num)
            person_face_encoding = face_recognition.face_encodings(person_image)[0]
            print("Person encoding:", person_face_encoding.shape)
    except Exception as e:
        person_face_encoding = np.array([1, 2])
        person_name = str(num)
        print("No system argument provided, please enter an image file name, followed by person name")
        quit()
        raise

    if(path.exists('encoding.npy') and path.exists('names.npy')):
        original_arr_encoding = np.load('encoding.npy')
        original_arr_encoding = original_arr_encoding.tolist()
        person_face_encoding = person_face_encoding.tolist()
        original_arr_encoding.append(person_face_encoding)

        # Debug Statement
        # print(original_arr_encoding)

        original_arr_names = np.load('names.npy')
        original_arr_names = np.append(original_arr_names, [person_name], axis=0)
        np.save('encoding', original_arr_encoding)
        np.save('names', original_arr_names)

    else:
        known_face_encodings = [person_face_encoding]
        known_face_names = [person_name]
        np.save('encoding', known_face_encodings)
        np.save('names', known_face_names)


    np.load.__defaults__=(None, False, True, 'ASCII')

    return 'success'


app.run(debug=True)
