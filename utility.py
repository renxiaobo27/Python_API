import os


def load_image_from_folder(path):
    full_file_path = []
    images_names = []
    exts = []
    valid_file_ext = ['.jpg','.png']
    for root,dirs,files in os.walk(path):
        for filename in files:
            ext = os.path.splitext(filename)[1]
            if ext.lower() not in valid_file_ext:
                continue
            filepath =os.path.join(root,filename)
            full_file_path.append(filepath)
            images_names.append(os.path.splitext(filename)[0])# without ext
            exts.append(ext)
    return full_file_path,images_names,exts

def get_current_subfolers(path):
    return os.listdir(path)

def get_all_subfolders(path):
    res=[]
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            res.append(os.path.join(root,dir))

    return res
#rename images by 05%
def rename_images_by_Id(folders_path,num_leading_zeros=5,startId=1):
    image_folder_path = folders_path
    full_file_path,images_names,exts = load_image_from_folder(image_folder_path)
    a,b,c = zip(*sorted(zip(full_file_path,images_names,exts)))

    for full_path,image,ext in zip(a,b,c):
        newId = str(startId).zfill(num_leading_zeros)
        startId += 1
        os.rename(full_path,os.path.join(image_folder_path,newId+ext))
        
        
#rename_images_by_Id('/home/tcl-admin/data/videos/training/test2')

#print get_current_subfolers('/home/tcl-admin/data/videos/training')
#print get_all_subfolders('/home/tcl-admin/data/videos/training')       


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


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
