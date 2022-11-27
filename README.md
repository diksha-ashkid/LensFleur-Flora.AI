# Centuriton-Hackathon_Flora.AI

# Aim and Target
### Motive: Horticulture employs approximately 58% of the Indian population. Every year, 15–25% of crops are damaged due to crop diseases. On an annual basis, the whole economic loss is roughly Rs. 50,000 crore. Crop loss is a big blot on the economy, as is the possibility for many farmers whose entire source of income depends on these crops. The crop loss gets even more significant when 200 Indians go to bed hungry every night.
The primary cause of such massive losses is due to the following factors:

1. Diseases that go undetected.
2. Diseases that were detected but not treated correctly.
3. Disease is discovered too late to prevent crop failure.

The current approach to dealing with this scenario is unsustainable, resulting in starvation, soil erosion, and a variety of other problems. Farmers living in distant areas lack access to, and sometimes the means to finance, proper disease management. In the long term, this becomes a sustainability issue caused by farmers' lack of understanding as well as inappropriate treatment procedures that lead to resource deterioration.

Regardless of the cause of crop loss, farmers bear the brunt of the consequences.

Lensfleur provides a dynamic, user-friendly solution to all of the problems described above under a single roof, including providing farmers with full crop health details, organic and inorganic treatment, a one-on-one chat window with specialists, and product comparison, all available to them through a medium and a language that is most comfortable to them.

## 1. Introduction

This repository contains the code for the Centuriton-Hackathon Flora.AI project. The project is a web application that allows users to upload images of their symptomatic corp and receive information about the plant including the diagnosts for the current display of symptom. Along with this the application is integrated with a chat service that allows the user to connect to experts post diagnosis or just to seek advice. The webapp is integrated with the Google Translate API that allows translation of all aspects of the window into any one of 113 languages that are supported. The project is built using the Flask framework which is used to integrate all the different features of the aplication and present it in a easy to read and use format, as accessibility and sustainability were the key principles in developing this project.

Wehile the project has many innovative features such as chat-window, which allows users to ask questions and receive answers all of them surround the central featurei, image recognition, which allows users to upload images of the symptoms that their plants are showing and receive the best course of treatment in accordance to their profile. Once the image has been recognized it provides the information along with the geographical location of the plant, which serves as the central data backing store that allows for historical data analysis and processing along with deeper insights and knowledge gathering.


## 2. Installation

### 2.1. Requirements

The project requires Python 3.6 or higher. The project also requires the following Python packages:

  * tensorflow==2.10.1
  * opencv-python==4.6.0
  * matplotlib==3.6.0
  * numpy==1.23.3
  * flask==2.2.2
  * geopy==2.3.0
  * wikipedia==1.4.0
  * exif==1.3.5
  * flask-socketio==5.3.2

### 2.2. Installation

To install the project, first clone the repository:

`git clone 'https://github.com/diksha-ashkid/Centuriton-Hackathon_Flora.AI.git'`

Then, install the required packages:

`pip install -r requirements.txt`

## 3. Usage

To run the project, first navigate to the project directory:

`cd Centuriton-Hackathon_Flora.AI`

Then, run the following command:

`python flora.py`

The project will be running on `http://127.0.0.1:3000/`

## 4. Contributors

  * [Diksha Chakravarthy](https://github.com/diksha-ashkid)
  * [Aakash Rajaraman](https://github.com/aakashrajaraman)
  * [Yashas S](https://github.com/Yashas2001)
  * [Nishtha Jain](https://github.com/2002nishthajain)

