# QR Code Generator
 Code Project

This project contains scripts for generating and reading QR codes using Python. It utilizes the `qrcode` library for generating QR codes and the `cv2` library (OpenCV) for reading QR codes from images in device storage and camera feeds.

## Files

- `QRCode generator.py`: Script to generate QR codes and save them as image files.
- `QRCode reader.py`: Script to read QR codes from image files.
- `QRCode reader from camera.py`: Script to read QR codes using the device's camera.

## Requirements

- Python 3.0 and above
- `qrcode` library
- `opencv-python` library

You can install the required libraries using pip:

```sh
pip install qrcode[pil] opencv-python
```

## Usage

To generate a QR code, run the following command:

```sh
python QRCode_generator.py

```

To read a QR code from an image file, run the following command:

```sh
python QRCode_reader.py

```

To read a QR code using the device's camera, run the following command:

```sh
python QRCode_read_from_camera.py
```

## Updates

Subject to updates in coming days.