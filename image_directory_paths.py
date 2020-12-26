import os

image_files = []
os.chdir(os.path.join("data", "images"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/images/" + filename)
    elif filename.endswith(".jpeg"):
        image_files.append("data/images/" + filename)
    elif filename.endswith(".png"):
        image_files.append("data/images/" + filename)
os.chdir("..")
with open("images.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")