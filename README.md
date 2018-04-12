# Python Face Recognition

## Introduction
Face Recognition using python OpenCV to predict the face of a person, The data itself stored as training data and users are stored in Mysql Database

## Package Needed
- [OpenCV]()
- [pymysql]()
- [numpy]()
- [PIL]()
  `pip install pillow`
- [Custom Open CV]()
  `python -m pip install opencv-contrib-python`

## Setting Up
1. Create Database my pymysql
2. Set Up in `Connection/Controller/connection.py`
3. configure
```Python
import pymysql as database

#Connections
#https://www.simplifiedpython.net/python-mysql-tutorial/

db = database.connect(
    host="localhost",
    user="username",
    password="password",
    db="face_reg"
)

```

## Starting Up
1. Open Directory
2. `python Main.py`

## Image For training
1. Open Directory `Dataset`
2. Paste Image Face with format `User.id.numberofPhoto.format` example `User.1.1.png`
