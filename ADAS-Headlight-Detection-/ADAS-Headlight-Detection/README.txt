ADAS HEADLIGHT DETECTION - VS CODE

1. Extract this ZIP.
2. Open the extracted "ADAS-Headlight-Detection" folder in VS Code.
3. Open Terminal > New Terminal.
4. Install packages:

   python -m pip install -r requirements.txt

   If you want to explicitly use your Python 3.14:
   C:\Python314\python.exe -m pip install -r requirements.txt

5. Run:

   python headlight_detection.py

   Or:
   C:\Python314\python.exe headlight_detection.py

The supplied sample/day.jpg is already included.

The program:
- loads day.jpg automatically
- calculates average image brightness
- finds very bright regions
- marks bright regions on the output
- saves sample/headlight_result.jpg

IMPORTANT:
This is a basic OpenCV demonstration. It does not use a trained AI model and
cannot reliably distinguish headlights from the sun, lamps, reflections, etc.
For a real ADAS project, a vehicle detector + headlight detector/tracker would
be the next stage.
