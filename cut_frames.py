import os
import cv2
import math

def get_frames():
    frames_folder = 'frames'
    frame_files = [f for f in os.listdir(frames_folder) if os.path.isfile(os.path.join(frames_folder, f))]
    
    for frame_file in frame_files:

        frame_path = os.path.join(frames_folder, frame_file)
        frame = cv2.imread(frame_path)

        if frame is not None:            
            frame_filename = os.path.join(frames_folder, frame_file)

            print(frame_filename)
            if os.path.exists(frame_filename) and check_color(frame) > 1:
                os.remove(frame_filename)
                print("exists")
                x, y, w, h = 432, 0, 640, 360
                cropped_frame = frame[y:y+h, x:x+w]
                cv2.imwrite(frame_filename, cropped_frame)
            else:
                cv2.imwrite(frame_filename, frame)
        else:
            print(f"Błąd wczytywania obrazu: {frame_file}")


def check_color(image):
    x, y, w, h = 432, 0, 640, 360
    cropped_frame = image[0:h, 0:x]
    hist = cv2.calcHist([cropped_frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = hist / hist.sum()
    colorfulness = -sum(p * math.log2(p + 1e-10) for p in hist.flatten() if p > 0)
    print(colorfulness)
    return colorfulness


if __name__ == '__main__':
    get_frames()
