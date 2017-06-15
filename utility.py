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



class ImageClass():
    "Stores the paths to images for a given class"

    def __init__(self, name, image_paths):
        self.name = name
        self.image_paths = image_paths

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
                dataset.append(ImageClass(class_name, image_paths))

    return dataset
