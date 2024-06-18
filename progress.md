### Day 1 (20/5/24)
- [Explored PyQt by building a calculator](./calculator.py)
- [Learnt requests module by interfacing weather api](./weatherAPI.py)

### Day 2 (21/5/24)
- [Implemented a simple PyQt GUI](./printToConsole.py)
- [Learnt ROS](https://youtube.com/playlist?list=PLLSegLrePWgIbIrA4iehUQ-impvIXdd9Q&si=cJwYn6-BzNe0fUXn)
    - nodes
    - topics
    - service
    - client 
    - subscribing and publishing
- [Explored MVC in PyQt](https://stackoverflow.com/questions/26698628/mvc-design-with-qt-designer-and-pyqt-pyside)
- [Installed ROS on an ubuntu vm thru qemu](https://youtu.be/wxxP39cNJOs?si=y4PSs5F1F44fqTKm)

### Day 3 (22/5/24)
- Explored PolyScope interface in a Universal Robot 5, other welding technologies and the robots along with the automations involved in it (@ PSG COEs for Welding)
- Skimmed through UR5's github repository for its ROS drivers
- Got a glimpse of gazebo and moveit for ROS(link yet to be added)
- [Learnt components and features of PyQt in-depth](https://www.pythonguis.com/tutorials)
    - Signals
    - Widgets
    - Layouts
- [Learnt about using Qt designer](https://youtube.com/playlist?list=PLYf4Vz9V1ESrVD_NMDlwRjgo8jn2UNEND&si=i0n0HvsFHqAoQWK5) ( 2.5 out of 8 videos done)
  
### Day 4 (23/5/24)
- [Completed learning PyQt components and principles](https://www.pythonguis.com/tutorials)
    - Menus
    - Dialogs
    - Multi-window implementation
    - [Qt designer layouts](./images/ui_v1_may_23(day_4).png)
    - Dialogs in Qt designer
    - Long running tasks (using QRunnable and QThreadPool)
    - External processes (using QProcess)
    - Model views
- [Implemented skeletons of feature, robot and TCP parts of the move tab in PolyScope using Qt Designer.](./mainUI_v1.ui)
- Learnt to use the `.ui` file genereated by Qt designer in a python program to implement its functionality.

### Day 5 (24/5/24)
- [Implemented prototype for the bottom panel in move tab of ur5 polyscope software.](./mainUI_v2.ui)
    - Implemented states
        - [Image 1](./images/ui_v2_may_24(day_5)_1.png)
        - [Image 2](./images/ui_v2_may_24(day_5)_2.png)
        - [Image 3](./images/ui_v2_may_24(day_5)_3.png)
    - [Actual panel](./images/move_polyscope_ur5.png)
- Learnt to customize widgets using css and various properties in the properties widget of Qt designer.

### Day 6 (25/5/24)
- Helped in exploring datasets for welding defect detection and found a [reliable dataset along with code for developing CNN model](https://www.kaggle.com/code/mayankgupta1609/model-1)
- Completed designing the interface of model tab's tool and joint position
    - [Implemented interface](./images/ui_v2_may_25(day_6).png)
    - [`.ui` code](./mainUI_v2_may_25.ui)

__26/5/24 - SUNDAY : Holiday__

### Day 7 (27/5/24)
- Completed implementing the tcp position and movement panels of move tab.
- Found dataset and model implementation for welding defect detection.
### Day 8 (28/5/24)
- Completed move tab ui entirely.
- Explored implementation of digital twin
- Created a private git repo for the implementation.
### Day 9 (29/5/24)
- [Learnt ROS2 through youtube tutorial(started)](https://youtube.com/playlist?list=PLLSegLrePWgJudpPUof4-nVFHGkB62Izy&si=ayoYlhHKQpKyhZMt)
- Installed Ubuntu 22.04 VM to try ROS2
### Day 10 (30/5/24)
- Learnt ROS2 through youtube tutorial(completed)
- Helped with implementing CNN and YOLOv7
### Day 11 (31/5/24)
- Implemented a simple controller in ROS2 that moves turtle in the turtlesim in a specific path
### Day 12 (1/6/24)
- Imlpemented service-client in ROS2

__2/6/24 - SUNDAY : Holiday__
### Day 13 (3/6/24)
- Configured the Nvidia ORIN AGX 64 GB.
- Explored vision AI options and features provided by Nvidia (like deepstream sdk, jetson sdk)
### Day 14 (4/6/24)
- Attempted running the [kaggle note](https://www.kaggle.com/code/mayankgupta1609/model-1) in the Nvidia ORIN AGX 64 GB
- Fixed import errors
### Day 15 (5/6/24)
- Explored [hello AI tutorials](https://youtube.com/playlist?list=PL5B692fm6--uQRRDTPsJDp4o0xbzkoyf8&si=lk2ME102RYzRw8NQ) by Nvidia Developers
- Cloned [jetson-inference github repository](https://github.com/dusty-nv/jetson-inference) to the Orin AGX.
### Day 16 (6/6/24)
- Tested image classification program
- Fixed library errors 
### Day 17 (7/6/24)
- Tested classification from live camera feed
- Wrote a [python script](./operate_files.py) to reorganize the image data obtained from kaggle
### 8/6/24 : Leave (marriage)

__9/6/24 - SUNDAY : Holiday__

### Day 18 (10/6/24)
- Started training the model using transfer learning and PyTorch
- Fixed library version issues

### 11/6/24 : Leave (sick)


### Day 19 (12/6/24)
- Retrained the model due to minor bug during labeling
- Started implementing functionality of the UI(joint angle sliders)

### Day 20 (13/6/24)
- Evaluated model based on the test data by converting frames to video and feeding it to the model
- Explored Singularity containerisation and openRAVE 
- Tried implementing [Leed's repository](https://github.com/roboticsleeds/ur5controller/tree/master) for ur5 controller
### Day 21 (14/6/24)
- Wrote bash scripts to take logs of the output
    - run.sh
    - parse.awk
    - script.awk
- Restructured the GUI's backend
### Day 22 (15/6/24)
- Explored PyADS and inverse kineamatics


__16/6/24 - SUNDAY : Holiday__

### 17/6/24 - ID MUBARAK : Holiday

### Day 23 (18/6/24)