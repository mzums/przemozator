import os 
import pytesseract
from PIL import Image


def get_text():
    frames_folder = 'frames'
    text_folder = 'text'
    frame_files = [f for f in os.listdir(frames_folder) if os.path.isfile(os.path.join(frames_folder, f))]
    for frame_file in frame_files:
        frame_path = os.path.join(frames_folder, frame_file)
        # print(f"Processing frame: {frame_path}")
        text = pytesseract.image_to_string(Image.open(frame_path), lang='pol')
        text_one_line = text.replace("\n", " ")
        if not os.path.exists(text_folder):
            os.makedirs(text_folder)
        with open(os.path.join(text_folder, frame_file + '.txt'), 'w+') as file:
            file.write(text_one_line)
            

if __name__ == '__main__':
    get_text()
