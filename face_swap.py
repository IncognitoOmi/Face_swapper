# -*- coding: utf-8 -*-
"""1_click_deep_fake_for_free_by_SECourses.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/FurkanGozukara/Stable-Diffusion/blob/main/ColabNotebooks/1_click_deep_fake_for_free_by_SECourses.ipynb

## Updated 6 June 2024 Working
## Rope is better and more advanced than Roop
## Better APP Rope Cloud : https://youtu.be/HLWLSszHwEc
## Better APP Rope Windows : https://youtu.be/RdWKOUlenaY
## 1-Click Installer for Roop Windows : https://www.patreon.com/posts/1-click-auto-88234834
## 1-Click Installer for Roop RunPod : https://www.patreon.com/posts/auto-installer-84511510

**If you want to use the latest version remove `!git checkout 312208a41102ba86d2454ae8efc9d3f0b786a6e7`**
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/FurkanGozukara/roop
# %cd roop
#Tested and updated 23 August 2023 commit
#!git checkout da1ef285f1d43bd0cc8b9cdb9a0f80f7ae793a97
!pip install onnxruntime-gpu && pip install -r requirements.txt
!pip install onnxruntime-gpu --upgrade
!apt-get update --yes
!apt install nvidia-cuda-toolkit --yes
!pip install opennsfw2 keras --upgrade

"""**You will see processing message at the end of below printed messages e.g. Processing:  43% 136/318 00:38<00:24, 7.47frame/s**

**Make sure to upload root roop folder not inside the sub roop folder and don't forget to change image and video file names**

**1 is best quality big video size, 100 worst quality low video size**
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/roop"
!python run.py -s "face2.png" -t "video3.mp4" -o "face_changed_video_v2.mp4" --keep-frames --keep-fps --temp-frame-quality 1 --output-video-quality 1 --execution-provider cuda

"""**Below code will do also face restoration to improve quality significantly but it will take longer**"""

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/roop"
!python run.py -s "face2.png" -t "video3.mp4" -o "face_restored_video3.mp4" --keep-frames --keep-fps --temp-frame-quality 1 --output-video-quality 1 --execution-provider cuda --frame-processor face_swapper face_enhancer

"""### All options are displayed below
Append any of them to the above commands before executing
```
python run.py [options]

-h, --help                                                                 show this help message and exit
-s SOURCE_PATH, --source SOURCE_PATH                                       select an source image
-t TARGET_PATH, --target TARGET_PATH                                       select an target image or video
-o OUTPUT_PATH, --output OUTPUT_PATH                                       select output file or directory
--frame-processor FRAME_PROCESSOR [FRAME_PROCESSOR ...]                    frame processors (choices: face_swapper, face_enhancer, ...)
--keep-fps                                                                 keep target fps
--keep-frames                                                              keep temporary frames
--skip-audio                                                               skip target audio
--many-faces                                                               process every face
--reference-face-position REFERENCE_FACE_POSITION                          position of the reference face
--reference-frame-number REFERENCE_FRAME_NUMBER                            number of the reference frame
--similar-face-distance SIMILAR_FACE_DISTANCE                              face distance used for recognition
--temp-frame-format {jpg,png}                                              image format used for frame extraction
--temp-frame-quality [0-100]                                               image quality used for frame extraction
--output-video-encoder {libx264,libx265,libvpx-vp9,h264_nvenc,hevc_nvenc}  encoder used for the output video
--output-video-quality [0-100]                                             quality used for the output video
--max-memory MAX_MEMORY                                                    maximum amount of RAM in GB
--execution-provider {cpu} [{cpu} ...]                                     available execution provider (choices: cpu, ...)
--execution-threads EXECUTION_THREADS                                      number of execution threads
-v, --version                                                              show program's version number and exit
  ```

### Download generated images folder
"""

import shutil
import os
from google.colab import files

def zip_directory(directory_path, zip_path):
    shutil.make_archive(zip_path, 'zip', directory_path)

# Set the directory path you want to download
directory_path = '/content/roop/video3'

# Set the zip file name
zip_filename = 'video3.zip'

# Zip the directory
zip_directory(directory_path, zip_filename)

# Download the zip file
files.download(zip_filename+'.zip')

"""# below is last working pip freeze of libraries 6 June 2024"""

!pip freeze