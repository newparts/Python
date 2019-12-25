import face_recognition

imaginea_lui_obama = face_recognition.load_image_file('./img/cunoscuti/obama.jpg')
obama_face_encoding = face_recognition.face_encodings(imaginea_lui_obama)[0]

imagine_necunoscuta = face_recognition.load_image_file('./img/necunoscuti/sosie.jpg')
necunoscuta_face_encoding = face_recognition.face_encodings(imagine_necunoscuta)[0]

results = face_recognition.compare_faces([obama_face_encoding], necunoscuta_face_encoding) 

if results[0]:
    print('Acesta este Obama')
else:
 print('Acesta nu este Obama')
