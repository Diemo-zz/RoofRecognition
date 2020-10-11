import cv2
import os

ALLOWED_EXTENSIONS = [".png", ".jpg", ".jpeg"]


def post_process_file(input_path, file):
    image_path = os.path.join(input_path, "images")
    label_path = os.path.join(input_path, "labels")
    image_file_path = os.path.join(image_path, file)
    label_file_path = os.path.join(label_path, file)
    new_image_path = os.path.join(input_path, "processed_images")
    if not os.path.isdir(new_image_path):
        os.mkdir(new_image_path)

    new_label_path = os.path.join(input_path, "processed_labels")

    if not os.path.isfile(image_file_path):
        return

    label_exists = os.path.isfile(label_file_path)
    if label_exists and not os.path.isdir(new_label_path):
        os.mkdir(new_label_path)

    new_image = cv2.imread(image_file_path)
    if label_exists:
        label_image = cv2.imread(label_file_path)

    for i in range(0,4):
        rotation = i*90
        new_name = os.path.splitext(file)[0] + f"_Rotation_{rotation}" + os.path.splitext(file)[1]
        new_name =os.path.join(new_image_path, new_name)
        cv2.imwrite(new_name, new_image)
        new_image = cv2.rotate(new_image, cv2.ROTATE_90_CLOCKWISE)
        if label_exists:
            new_label_name = os.path.splitext(file)[0] + f"_Rotation_{rotation}" + os.path.splitext(file)[1]
            new_label_name = os.path.join(new_label_path, new_label_name)
            cv2.imwrite(new_label_name, label_image)
            label_image = cv2.rotate(label_image, cv2.ROTATE_90_CLOCKWISE)

    image = cv2.imread(image_file_path)
    if label_exists:
        label_image = cv2.imread(label_file_path)
    for i in range(-1,2):
        flipped_image = cv2.flip(image, i)
        new_name = os.path.splitext(file)[0] + f"_Mirror_{i}" + os.path.splitext(file)[1]
        cv2.imwrite(os.path.join(new_image_path, new_name), flipped_image)
        if label_exists:
            flipped_label = cv2.flip(label_image, i)
            cv2.imwrite(os.path.join(new_label_path, new_name), flipped_label)



if __name__ == "__main__":
    input_path = os.path.join(os.getcwd(), "Images")
    for file in os.listdir(os.path.join(input_path, "images")):
        extension = os.path.splitext(file)[1]
        if extension in ALLOWED_EXTENSIONS:
            res = post_process_file(input_path, file)

