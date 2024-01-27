# Eye and Face Detection with OpenCV

This Python project utilizes OpenCV to perform real-time eye and face detection through your webcam. It aims to determine whether the eyes in the captured frames are open or closed. The script provides a dynamic interface, allowing you to adjust parameters such as `min_neighbors` and `scale_factor` in real-time to optimize the eye detection process.

## Requirements

- Python 3.x
- OpenCV (cv2)
--

## Installation

1. Install Python: [Python Downloads](https://www.python.org/downloads/)

2. Install OpenCV:

   ```bash
   pip install opencv-python
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```

2. Adjust the parameters for eye detection using the following keyboard controls:

   - `Q`: Quit the application.
   - `Up Arrow Key`: Increase `min_neighbors`.
   - `Down Arrow Key`: Decrease `min_neighbors`.
   - `Right Arrow Key`: Increase `scale_factor`.
   - `Left Arrow Key`: Decrease `scale_factor`.

## Important Note

This script opens two windows for eye and face detection. Please ensure that you have a working webcam connected to your system.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests.
