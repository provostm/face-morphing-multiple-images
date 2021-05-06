from face_landmark_detection import generate_face_correspondences
from delaunay_triangulation import make_delaunay
from face_morph import generate_morph_sequence

import subprocess
import argparse
import shutil
import os
import cv2

def doMorphing(img1, img2, duration, frame_rate, output):

	[size, img1, img2, points1, points2, list3] = generate_face_correspondences(img1, img2)

	tri = make_delaunay(size[1], size[0], list3, img1, img2)

	generate_morph_sequence(duration, frame_rate, img1, img2, points1, points2, tri, size, output)

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--img1", help="The First Image")
	parser.add_argument("--img2", help="The Second Image")
	parser.add_argument("--folder", help="The folder with all images")
	parser.add_argument("--duration", type=int, default=5, help="The duration")
	parser.add_argument("--frame", type=int, default=20, help="The frameame Rate")
	parser.add_argument("--output", help="Output Video Path")
	parser.add_argument("--tmpfolder", default="tmp_videos/", help="The temporary folder to store intermediate videos")
	args = parser.parse_args()

	if(args.img1 and args.img2):
		img1 = cv2.imread(args.img1)
		img2 = cv2.imread(args.img2)
		doMorphing(img1, img2, args.duration, args.frame, args.output)
    
	if(args.folder):
		imgFolder = args.folder
		listImg = os.listdir(imgFolder)
        
		outputList = []
		for i in range(0, len(listImg)-1):
			print("on traite le morphing des images "+listImg[i]+" et "+ listImg[i+1])
			img1 = cv2.imread(os.path.join(imgFolder,listImg[i]))
			img2 = cv2.imread(os.path.join(imgFolder, listImg[i+1]))
			doMorphing(img1, img2, args.duration, args.frame, args.tmpfolder + str(i)+"_"+args.output)
			outputList.append("file '"+ args.tmpfolder + str(i)+"_"+args.output+"'")
		f=open('imageslist.txt','w')
		s1='\n'.join(outputList)
		f.write(s1)
		f.close()
		
    # merge all the temporary videos into one
	os.system('ffmpeg -f concat -safe 0 -i imageslist.txt -c copy ' + args.output)