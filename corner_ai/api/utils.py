from keras.utils import load_img, img_to_array
import numpy as np
from keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input
from PIL import Image

from keras.models import load_model
import cv2

from django.core.cache import cache

##### test용 ai 모델 #####
# def process_image(uploaded_file):
#     # 이미지 처리 로직을 작성
#     # 여기서는 간단히 이미지의 파일명을 반환하는 예시 코드
#     try:
#         img = Image.open(uploaded_file)
#         target_size=(299, 299)
#         img = img.resize(target_size)
        
#         print(type(img))
            
#         img_arry = img_to_array(img)
#         to_pred = np.expand_dims(img_arry, axis=0)
#         prep = preprocess_input(to_pred)
#         model = InceptionResNetV2(weights='imagenet')
#         prediction = model.predict(prep)
#         decoded = decode_predictions(prediction)
#         result = str(decoded[0][0][1])
#         print('success')
#     except Exception as e:
#         print("classification failed", e)
#         result = "실패"
#     print(result)
#     return result


def process_image(uploaded_file):
    # 이미지 처리 로직을 작성
    # 여기서는 간단히 이미지의 파일명을 반환하는 예시 코드
    try:
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model

        model = cache.get('ishopping_ai_model')  # Change the path to your model  

        if model is None:
            model = load_model("/srv/ishopping-ai/ai_model/keras_model.h5", compile=False)
            cache.set('ishopping_ai_model', model)
        # Load the labels
        class_names = [line.strip() for line in open("/srv/ishopping-ai/ai_model/labels.txt", "r")]

        image = Image.open(uploaded_file)
        print(type(image))

        image = np.array(image)

        # Read the input image
        # image = cv2.imread("/content/참깨라면.jpg")  # Change the path to your input image

        # Resize the raw image into (224-height, 224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Convert BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Make the image a numpy array and reshape it to the model's input shape
        image_array = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image_array = (image_array / 127.5) - 1

        # Predict the model
        predictions = model.predict(image_array)
        class_index = np.argmax(predictions)
        class_name = class_names[class_index]
        confidence_score = predictions[0][class_index]

        # Print prediction and confidence score
        print("Class:", class_name, end="")
        print(" Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        _, cname = class_name.split()
        result = cname
        print('success')
    except Exception as e:
        print("classification failed", e)
        result = "실패"
    print(result)


    return result