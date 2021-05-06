# face-morphing-multiple-images

Credit to: https://github.com/Azmarie/Face-Morphing 

This repo is an upgrade where we can morph multiple images into video.

Check out Azmarie's repo first to understand all the details.

# Execution

1. Place you images in a folder, for example ```raw_images```
2. Use the command ```python code/utils/align_images.py raw_images/ aligned_images/ --output_size=1024``` to select images from "raw_images" with a face and align/rotate them and put them in "aligned_images".
3. Launch the command to create the video : 

```python code/__init__.py --folder aligned_images --output video_output.mp4 --duration 4```

Note that this will create temporary videos (```--tmpfolder```) and then combine them into one video (```--output```).

# Details to call code/__init__.py
- ```--img1``` : The First Image (not necessary when ```--folder``` is used)
- ```--img2``` : The Second Image (not necessary when ```--folder``` is used)
- ```--folder``` : The folder with all images to morph (not necessary when ```--img1``` and ```--img2``` are used)
- ```--duration``` : The duration of morphing from one image to the other.
- ```--frame``` : The frame rate of the encoding.
- ```--output``` : Final video path.
- ```--tmpfolder``` : Folder to store intermediate videos.
