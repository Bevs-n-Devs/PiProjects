# PiCam Streaming Flask WebApp
_This project is an example of how to build a run a Flask Webapp for streaming a live PiCamera Freed on a Raspberry Pi_
> NOTE : The following runs with the expectation that wifi network connection is already enabled on the pi.

## Environment Setup
_The picamera library has been updated on the hardware level in the newer Raspberry Pi Linux OS Distribution ()_

> _NOTE: The following steps are only ran once for initial setup, except step 5._
1. To check the OS version, press the following:   
`cat /etc/os-release`

2. If the output states OS Version 12 (bookworm) or newer, run the following system setup commands:   
`sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev python3-full -y`   
   > NOTE: This may take up to 20min to complete depending on your wifi connection.

3. Install opencv for computer vision:   
`sudo apt-get install python3-opencv -y`

4. Create a python virtual environment _(this is required now)_:   
`python -m venv .venv --system-site-packages`
   > NOTE: The system site packages option is needed to utilitize the hardware dependent python libraries that come with the Pi OS/Platform 

5. Start the virtual environment:   
`source ./venv/bin/activate`
   > NOTE This is the only setup step that's repeated after the initial setup, as it is needed to run the webapp.

6. Install all the required packages:   
`pythom -m pip install -r ./requirements.txt`