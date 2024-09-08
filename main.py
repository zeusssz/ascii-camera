import cv2
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, cols=120, scale=0.55):
    width = cols
    height = int(frame.shape[0] * scale * cols / frame.shape[1])
    resized_frame = cv2.resize(frame, (width, height))
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    ascii_frame = [ASCII_CHARS[val * len(ASCII_CHARS) // 256] for val in gray_frame.flatten()]
    ascii_output = "\n".join("".join(ascii_frame[i:i + width]) for i in range(0, len(ascii_frame), width))
    return ascii_output

def main(cols=120, frame_rate=15):
    cap = cv2.VideoCapture(0)
    delay = int(1000 / frame_rate)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            ascii_frame = frame_to_ascii(frame, cols=cols)
            print(ascii_frame)
            print("\033c", end="")
            cv2.waitKey(delay)

    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
