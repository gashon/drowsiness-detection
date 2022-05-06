import json


# returns an array of img_ref urls associated with the drowsiness classification argument
# e.x. get_images_url(2)
def get_images_url(classification, face_features = False):
    res = get_images(classification, face_features)
    return [res[key]["uri"] for key in res.keys()]

# returns a dict (url, media_ref, and folder) of image frames associated with the drowsiness classification argument
def get_images(classification, face_features = False):
    set = "output" if face_features else "raw"
    with open('../storage/util/images.json', 'r') as f:
        data = json.load(f)
    return data[set]["classification_{}".format(classification)]
