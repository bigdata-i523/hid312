# i523 Project

# Purpose

* This program parses and analyzes multiple data files collected from the Apple Health app on iPhone 6s.
* It outputs a table with steps per week and day, as well as a time series graph of all steps by date and average steps per day of the week.
* To analyze your own data, remove xml files from iPhoneData file, and place iPhone 6s Health export files to be analyzed in file. Then run `python3 makefile.py`.

# Installation and Run Instructions

1. Create a new installation of Ubuntu 16.04 on Oracle Virtual Box
2. Open terminal
3. To install, execute the following code:
  ~~~~
  sudo apt-get install git
  mkdir project
  git clone https://github.com/bigdata-i523/hid312
  cd ~/project/hid312/project/code
  chmod 755 make_install.sh
  sudo ./make_install.sh
  ~~~~
4. To run the program, execute: `python3 makefile.py`

 
