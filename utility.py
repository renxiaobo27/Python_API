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
