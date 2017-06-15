import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import os

from scipy import misc


class ImageClass():
    "Stores the paths to images for a given class"

    def __init__(self, name, image_paths,dir):
        self.name = name
        self.image_paths = image_paths
        self.dir = dir

    def __str__(self):
        return self.name + ', ' + str(len(self.image_paths)) + ' images'

    def __len__(self):
        return len(self.image_paths)


def get_dataset(paths):
    dataset = []
    for path in paths.split(':'):
        path_exp = os.path.expanduser(path)
        classes = os.listdir(path_exp)
        classes.sort()
        nrof_classes = len(classes)
        for i in range(nrof_classes):
            class_name = classes[i]
            facedir = os.path.join(path_exp, class_name)
            if os.path.isdir(facedir):
                images = os.listdir(facedir)
                image_paths = [os.path.join(facedir, img) for img in images]
                dataset.append(ImageClass(class_name, image_paths,facedir))

    return dataset



def load_image_from_folder(path):
    full_file_path = []
    images_names = []
    valid_file_ext = ['.jpg','.png']
    for root,dirs,files in os.walk(path):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if ext.lower() not in valid_file_ext:
                continue
            filepath =os.path.join(root,filename)
            full_file_path.append(filepath)
            images_names.append(filename)
    return full_file_path,images_names


#Handle single aug to images

#define aug class
blurer = iaa.GaussianBlur(1.5)
CN1 = iaa.ContrastNormalization(0.8)
CN2 = iaa.ContrastNormalization(1.2)

# add aug list
augment_list = [blurer, CN1, CN2]


def augment_all_folders():
    dataset = get_dataset('/home/tcl-admin/face/facenet/data/owndata')
    for cls in dataset:
        for file in cls.image_paths:
            id = len(cls.image_paths) + 1
            img = misc.imread(file)
            for ag in augment_list:
                augment = ag.augment_image(img)
                ouputfile = os.path.join(cls.dir, cls.name + "_" + str(id).zfill(4) + '.png')
                misc.imsave(ouputfile, augment)

def augment_one_folder():
    image_folder = '/home/tcl-admin/face/facenet/data/owndata/GH/' # careful about the last '/'
    full_image_paths, image_names = load_image_from_folder(image_folder)
    output_folder = '/home/tcl-admin/face/facenet/data/owndata/GH/'

    # start ID
    id = len(image_names) + 1
    classname = image_folder.split('/')[-2]

    for ag in augment_list:
        for img_path in image_names:
            img = misc.imread(os.path.join(image_folder, img_path))
            augment = ag.augment_image(img)
            ouputfile = os.path.join(output_folder, classname + "_" + str(id).zfill(4) + '.png')
            # misc.imshow(augment)
            misc.imsave(ouputfile, augment)
            id = id + 1

augment_one_folder()
