This model utilizes strictly yolov3 not the updated yolov4

PART 1: Setting up the code 

1. Make a folder called "Cell_Detection" in your google drive. 

  a) add two folders inside the Cell_Detection folder called "put_images_here" and "results"
  
2. Go to this link and save a copy of the file to your google drive. Save it inside the folder 
we made in step 1 called "Cell_Detection" 

  *Go to "file" -> "save a copy in drive"
  
https://colab.research.google.com/drive/1ZUB9c6Vj-amH8jwFdkCvnVAu0BEXjL50?usp=sharing

3. Download this weight file and upload it also to the "Cell_Detection" folder in google drive (your "Cell_Detection" folder should match what is below)

https://www.dropbox.com/s/mxhkwdt8vvbkhoy/final_neutrophil_weights?dl=0
  
![alt text](https://github.com/sthapa320/darknet/blob/master/data/setup.png)


PART 2: Running the code

1. In your "put_images_here" folder, add a zipped folder containing your images. This folder MUST be named "images.zip" (see below)

![alt text](https://github.com/sthapa320/darknet/blob/master/setup0.png)

2. Open the saved copy of the code created in PART 1, step 2. 

3. After opening the code, go to Runtime tab, near the file tab, and select "change runtime type" and ensure it is set to GPU. (see below)

![alt text](https://github.com/sthapa320/darknet/blob/master/gpu.png)

4. Now, run ONLY the first two cells by clicking the dark colored arrows.  

  *STOP before running the cell that is titled 
 " #TRANSFER NEEDED IMAGES and other necessary files FROM GOOGLE DRIVE"

5. Before proceeding, return to your "Cell_Detection" folder and ensure it looks EXACTLY as below.(see below)

![alt text](https://github.com/sthapa320/darknet/blob/master/setup.png)

6. Continue to run the following cells in the code. After this step, the output will be in your "results" folder.  
  
5. After each run, go to the tab labeled "RAM/Disk" and click "terminate." (see below) Then, remove all data from "put_images_here" and "results" folder. 

![alt text](https://github.com/sthapa320/darknet/blob/master/ter0.png)

![alt text](https://github.com/sthapa320/darknet/blob/master/ter1.png)


6. Repeat 1-5 for all necessary samples. 

*If user is experienced with google colab, it is not necessary to terminate the session following each run. 








COMMON ERRORS AND HOW TO FIX THEM

1. When running the last cell you get an error "FileNotFoundError"

The original code is preset to only input jpeg files; if your images are either jpg or some other format, go to the last cell block and look for a line labeled "(((change this to the image file type)))" and change the filetype to that of input. 

2. If in PART 2, step 3, you get an error "No such file or directory"

This means your folder of images isn't labeled correclty. Make sure your folder names match exactly what is shown in PART 2, step 3. 

*This error may also occur in PART 2, step 3, follow the same step - ensure your folders and zip file are named accordingly. 

3. If you get an error saying "Loading weights from /mydrive/Cell_Detection/final_neutrophil_weights...Couldn't open file: /mydrive/Cell_Detection/final_neutrophil_weights"

This means you didn't download the file in PART 1, step 3. Or you did download the file but didn't put it inside your "Cell_Detection" folder. 

4. My output images have random detection boxes on them, or misses many cells in the image

Unfortunately, this means you must manually count. This issue may be result of poor image quality or due to our limited training dataset. Always verify the output, machines aren't perfect... yet.  

