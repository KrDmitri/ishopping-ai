from keras.utils import load_img, img_to_array
import numpy as np
from keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input
from PIL import Image


def process_image(uploaded_file):
    # 이미지 처리 로직을 작성
    # 여기서는 간단히 이미지의 파일명을 반환하는 예시 코드
    try:
        img = Image.open(uploaded_file)
        target_size=(299, 299)
        img = img.resize(target_size)
        
        print(type(img))
            
        img_arry = img_to_array(img)
        to_pred = np.expand_dims(img_arry, axis=0)
        prep = preprocess_input(to_pred)
        model = InceptionResNetV2(weights='imagenet')
        prediction = model.predict(prep)
        decoded = decode_predictions(prediction)
        result = str(decoded[0][0][1])
        print('success')
    except Exception as e:
        print("classification failed", e)
        result = "실패"
    print(result)


    return result