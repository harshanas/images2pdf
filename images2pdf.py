from fpdf import FPDF
import os
import argparse


supported_file_types = ["png", "jpg", "jpeg"]
images_count = 0
parser = argparse.ArgumentParser(description="Images2PDF combines a set of images into a PDF file..")
parser.add_argument("images_folder", metavar="images_folder_name", help="Path to images folder")
parser.add_argument("output_file_name", metavar="output_file_name", help="Output PDF File Name")
args = parser.parse_args()

images_folder = args.images_folder
if images_folder[-1] == "/":
    images_folder = images_folder[0:-1]
output_file_name = args.output_file_name

print("Images2PDF => Combination Started...")

output_file = FPDF()
for file_name in os.listdir(images_folder):
    file_type = file_name.split(".")[-1]
    if file_type in supported_file_types:
        output_file.add_page()
        output_file.image(images_folder+"/"+file_name, x=0, y=0, w=output_file.w, h=output_file.h)
        images_count +=1

print("Images2PDF => Combination Ended..")
print("Images2PDF => Combined {0} images to a PDF".format(images_count))
print("Images2PDF => Saved PDF as '{0}'".format(output_file_name))

output_file.output(output_file_name)
    
