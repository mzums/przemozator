from pytube import YouTube 
import cv2
import os


def download():
    url = YouTube('https://www.youtube.com/watch?v=n22tLbxTqdM')
    print(url.title)
    # url.streams.filter(file_extension='mp4').first().download(filename='video.mp4')
    return url.title


def play_n_get_frames(file_path, playback_speed=100):
    cap = cv2.VideoCapture(file_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    cap.set(cv2.CAP_PROP_POS_MSEC, 0)
    cap.set(cv2.CAP_PROP_FPS, frame_rate * playback_speed)

    frame_count = 0
    frames_folder = 'frames'
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)
    print("Frames folder path:", os.path.abspath(frames_folder))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                frame_count += 1
                frame_filename = os.path.join(os.path.abspath(frames_folder), f"frame_{frame_count}.png")
                cv2.imwrite(frame_filename, frame)
                print(f"Saved frame as {frame_filename}")
            if key == ord('b'):
                frame_count += 1
                frame_filename = os.path.join(os.path.abspath(frames_folder), f"frame_{frame_count}.png")

                x, y, w, h = 432, 0, 640, 360
                cropped_frame = frame[y:y+h, x:x+w]

                cv2.imwrite(frame_filename, cropped_frame)
                print(f"Saved frame as {frame_filename}")
            if key == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    download()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, 'video.mp4')
    print(file_path)
    play_n_get_frames(file_path)
