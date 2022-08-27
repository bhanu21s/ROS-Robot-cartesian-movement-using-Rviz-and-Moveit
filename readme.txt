Bhanu Pratap Singh
ID- 210760006
mail -ec21279@qmul.ac.uk

%%overview
The folder contain 4 scripts responsible for generating the random cubic trajectories. With the help of ros launch file we dont have the run the scripts in seperately by run the command  roslaunch ar_week5_test cubic_traj_gen.launch we can run all the scripts. later we are plotting and visualising the trajectories 

%%dependency
python2.7
ros-melodic
numpy
catkin

%%steps to run the file
- make the catkin workspace using  
  catkin_make
- unzip the zipped folder 
- download the folder in your catkin workspace
- launch the rospackage using
  roslaunch ar_week5_test cubic_traj_gen.launch
- after launching the file after 20 second for seeing the graph run the following command
  rqt_graph
- for visualising the trajectories use the below command
  rqt_plot

