import cv2
import time
import os

from app.movement import MovementDetect 
from app.audio import play_audio
from app.tools import encode_image, analyze_image

ELEVENLABS_API_KEY = '6aadc5ea99cfd3143ff14814016bec63' # Change this to your Eleven Labs API key
os.environ["ELEVEN_API_KEY"] = ELEVENLABS_API_KEY

def main():
    detector = MovementDetect()  

    script = []  

    while True:
        movement_detected = detector.detect()  # Detect movement

        if movement_detected:
            print("OH! Here you are! 🚀 \nDear traveler from afar, let me take a look at how your fortune is today.\n")

            # Capture a frame from the camera
            ret, frame = detector.camera.read()
            if not ret:
                print("Failed to capture frame from camera.")
                break

            image_path = 'frames/frame.jpg'
            if not os.path.exists('frames'):
                os.makedirs('frames')
            cv2.imwrite(image_path, frame)

            base64_image = encode_image(image_path)

            # Analyze the image
            print("🥸 Master Chow is watching you...")
            analysis = analyze_image(base64_image, script)

            print("🥸 Master Chow says:")
            print(analysis)

            play_audio(analysis)

            script.append({"role": "assistant", "content": analysis})

            # Wait for 5 seconds before detecting movement agains
            time.sleep(5)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    detector.camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
