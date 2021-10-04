import tensorflow as tf

pretrained_model = tf.keras.applications.MobileNetV2(include_top=True,
                                                    weights='imagenet')
pretrained_model.trainable = False

# ImageNet labels
decode_predictions = tf.keras.applications.mobilenet_v2.decode_predictions

def preprocess(image):
    """
    Helper function to preprocess the image so that it can be inputted in MobileNetV2
    """
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = image[None, ...]
    return image

def get_imagenet_label(probs):
    """
    Helper function to extract labels from probability vector
    """
    return decode_predictions(probs, top=1)[0][0]

def get_image_from_path(image_path):
    image_raw = tf.io.read_file(image_path)
    image = tf.image.decode_image(image_raw)
    image = preprocess(image)
    return image

def get_image_probs(image):
    image_probs = pretrained_model.predict(image)
    return image_probs