# Object-Detection-Using-YoloV5

## Data Overview

Acutully For this model I've used same data wich i have used in YOLOV4.It's Fruits Images dataset which has Three class like-Apple,Banana,Orange and Each class has around 300 Images.I have done this project using YoloV4 model It's Detecting all the three classes correctly. Data Source:-[Click Here to Download the dataset](https://www.kaggle.com/datasets/mbkinaci/fruit-images-for-object-detection).

## Required Library and Tools

* Python
* Numpy
* Matplotlib
* Open-Cv
* Pre-trained Models
* Streamlit
* Google Colab
* Visual Studio
* YOLOV5
* torch
* IPython
### Tools

* Google Colab
* VS Code

## YOLOV5 Training Steps For Google Colab

 * First Create a folder in google drive and open this folder in google colab
 * Clone the git repository which contain all file and folder of YOLOV5
 * Now you will get file inside that folder which you created 
 * Go inside YOLOv5 folder in colab using (cd yolov5)
 * Inside this folder You'll be having requirements.txt file so intall it.
 * We need to make some change go to data folder and you will get a file named dataset.yaml open it and put your dataset path train and val ,number of classes(nc=3),classes names(names:["Apple","Banana","Orange"]) and move this file to your dataset folder.
 #### Your dataset.yaml file should be lool like it
![dataset yaml](https://user-images.githubusercontent.com/92671804/202411623-b85fd17b-35d3-4b0b-bacd-b74d611343dc.png)

* Dataset folder should setup like this means main folder inside two folder one is images and another labels, inside the images folder You'll be having two folder one is train and second val, train folder contains all the training images and val folder contains all the test images. Now come to the label folder same as images folder it has also two folder train and val but inside this train and val folder you will be having all txt files corresponding to images folder.
* This dataset path should be in your dataset.yaml file.
* Now all set for further just follow my .ipynb file which is in this repository.

## Deployment

* For Deployement I used streamlit and I've followed such steps:-
* Create a Folder
* make a file named requirements.txt and put all the required library inside it.
* Create a Virtual Environment inside this folder Follow these Steps -
* Open your command prompt in VS Code and write this command (python -m venv VE_name) and hit enter.
* After that you need to activate this virtual environment for that write this command (VE_name\Scripts\activate) and hit enter.
* You've Activated your virtual environment and you need to install all your required library for creating this app.
* Then Create a python file and write code for streamlit app
* Fro executing this code run this command in command prompt (streamlit run python_file_name.py)

## Final Output :-

![yoloV5](https://user-images.githubusercontent.com/92671804/202438996-92f7ed1d-f2f3-4b47-b358-c81d587c6a4b.png)

