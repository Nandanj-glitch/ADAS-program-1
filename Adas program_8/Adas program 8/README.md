# HOG Pedestrian Detection

## Folder
HOG_Pedestrian_Detection_VSCode/
- main.py
- requirements.txt
- README.md
- road1.jpg

## Run in VS Code

1. Put your pedestrian image in this folder.
2. Rename it to `road1.jpg`.
3. Open the VS Code terminal.
4. Run:

```text
pip install -r requirements.txt
python main.py
```

The program uses OpenCV HOG with the built-in pre-trained people detector.
It prints the number of detected pedestrians and displays green bounding boxes.
