from django.db import models
from keras.utils import load_img, img_to_array
import numpy as np
from keras.applications.inception_resnet_v2 import InceptionResNetV2, decode_predictions, preprocess_input

# Create your models here.
class CornerImage(models.Model):
    picture = models.ImageField()
    picture_id = models.CharField(max_length=13, blank=True)
    info = models.CharField(max_length=200, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Corner Image took at {}".format(self.uploaded.strftime('%Y-%m-%d %H:%M'))
    
    def save(self, *args, **kargs):
        try:
            img = load_img(self.picture.path, target_size=(299, 299))
            img_arry = img_to_array(img)
            to_pred = np.expand_dims(img_arry, axis=0)
            prep = preprocess_input(to_pred)
            model = InceptionResNetV2(weights='imagenet')
            prediction = model.predict(prep)
            decoded = decode_predictions(prediction)
            self.info = str(decoded[0][0][1])
            print('success')
        except Exception as e:
            print("classification failed", e)
        super().save(*args, **kargs)