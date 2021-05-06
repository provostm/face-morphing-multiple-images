# face-morphing-multiple-images

Credit to: https://github.com/Azmarie/Face-Morphing 
This repo is an upgrade where we can morph multiple images into video.
Check Azmarie's repo first.

# Execution

1. Place you images in a folder.
2. use the command python code/utils/align_images.py raw_images/ images/aligned_images --output_size=1024
3. Launch the command to create the video : python code/__init__.py --folder aligned_images --output video_output.mp4 --duration 4
