from tensorflow import keras
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image

signs_translated = ['20 Red Circle', '30 Red Circle', '50 Red Circle', '60 Red Circle', '70 Red Circle',
                    '80 Red Circle', '80 Circle Gray Line', '100 Red Circle', '120 Red Circle', 'Red Car Black Car Red Circle',
                    'Red Truck Black Car Red Circle', 'Priority Crossroad Sign', 'Yellow Diamond in White Diamond', 'Blank Red Triangle','Stop Sign',
                    'Blank Red Circle', 'Black Truck Red Circle', 'Road One Way Street Sign', 'Exclaimation Point Red Triangle', 'Left Turn Red Triangle',
                    'Right Turn Red Triangle', 'Curvey Road Red Triangle', 'Speed Bump Yellow Red Triangle', 'Slippery When Wet Red Triangle', 'Merge Red Triangle',
                    'Road Worker Yellow Red Triangle', 'Stop Light Red Triangle', 'Crosswalk Red Triangle', 'Kids Playing Red Triangle', 'Bicycle Red Triangle',
                    'Snow Red Triangle', 'Deer Red Triangle', 'Black Diagonal Lines Black Circle', 'Right Turn Only Blue Circle', 'Left Turn Only Blue Circle',
                    'Striaght Only Blue Circle', 'Straight Right Turn Blue Circle', 'Straight Left Turn Blue Circle', 'Pass on Right Blue Circle', 
                    'Pass on Left Blue Circle', 'Roundabout Blue Circle', 'No Passing White Circle', 'No Trucks Passing White Circle']


def predict(image_file):
    # dimensions of our images
    img_width, img_height = 30, 30

    model = load_model('traffic_classifierMoreDrop.h5')
    model.compile(loss='binary_crossentropy',
                optimizer='rmsprop',
                metrics=['accuracy'])

    # predicting images
    img = image.load_img(image_file, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    predict_x = model.predict(images, batch_size=10)
    classes_x=np.argmax(predict_x,axis=1)
    return signs_translated[classes_x[0]]

# print(predict('00014.png'))
# print(len(signs_translated))
