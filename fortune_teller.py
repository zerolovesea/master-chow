import cv2
import time
import os

from app.audio import play_audio
from app.tools import encode_image, analyze_image

ELEVENLABS_API_KEY = '6aadc5ea99cfd3143ff14814016bec63'

os.environ["ELEVEN_API_KEY"] = ELEVENLABS_API_KEY

def main():
    camera = cv2.VideoCapture(0)

    width  = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = width, height


    fps = 2
    pre_frame = None
    script = []  

    while (1):
        start = time.time()

        ret, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if not ret:
            print("Failed to open camera")
            break

        end = time.time()
        seconds = end - start

        if seconds < 1.0 / fps:
            time.sleep(1.0 / fps - seconds)

        gray_frame = cv2.resize(gray_frame, (480, 480))
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

        if pre_frame is None:
            pre_frame = gray_frame
        else:
            img_delta = cv2.absdiff(pre_frame, gray_frame)
            thresh = cv2.threshold(img_delta, 30, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv2.contourArea(c) < 1000:
                    continue
                else:
                    print("OH! Here you are! 🚀 \nDear traveler from afar, let me take a look at how your fortune is today.\n")

                    image_path = os.path.join(os.getcwd(), "frames", "frame.jpg")
                    image_path = 'frames/frame.jpg'
                    cv2.imwrite(image_path, frame)

                    base64_image = encode_image(image_path)

                    # Analyzing the image
                    print("🥸 Master Chow is watching you...")
                    analysis = analyze_image(base64_image, script)

                    print("🥸 Master Chow says:")
                    print(analysis)

                    play_audio(analysis)

                    script.append({"role": "assistant", "content": analysis})

                    # Wait for 5 seconds
                    time.sleep(5)

                    break
            pre_frame = gray_frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()