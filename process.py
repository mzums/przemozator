import os
import pytesseract
from PIL import Image


def process():
    frames_folder = 'frames'
    frame_files = [f for f in os.listdir(frames_folder) if os.path.isfile(os.path.join(frames_folder, f))]
    for frame_file in frame_files:
        frame_path = os.path.join(frames_folder, frame_file)
        # print(f"Processing frame: {frame_path}")
        text = pytesseract.image_to_string(Image.open(frame_path), lang='pol')
        text_one_line = text.replace("\n", " ")
        print(text_one_line, "\n")


if __name__ == '__main__':
    process()
