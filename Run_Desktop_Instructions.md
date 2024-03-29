To launch your Python script on Ubuntu desktop without using the terminal, you can create a .desktop file that acts as a shortcut to run your script. This method allows you to double-click the shortcut and run your Python script like any other application. Here's how you can do it:

    Ensure Your Python Script is Executable: First, make sure your Python script is executable. You can do this by adding a shebang line at the top of your script and then making the script executable with chmod. Add the following line to the top of your script if it's not already there:

#!/usr/bin/env python3

Then, make your script executable by running the following command in the terminal:

chmod +x /home/capstone15/Desktop/Next-Generation-Storage-master/Raspberry_Pi_4B/main.py



    Create a .desktop File: Next, create a .desktop file on your desktop or in ~/.local/share/applications to create a shortcut for your script. Here's an example of what the .desktop file could look like:

[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Stepper Motor Controller
Comment=Control stepper motors via Arduino
Exec=/home/capstone15/Desktop/Next-Generation-Storage-master/Raspberry_Pi_4B/main.py
Icon=application-python
Terminal=false



    Make the .desktop File Executable: For the .desktop file to work properly, it needs to be marked as executable. You can do this by right-clicking the file, selecting Properties, going to the Permissions tab, and checking the box that allows executing the file as a program. Alternatively, you can use the terminal:

chmod +x /home/capstone15/Desktop/Run.desktop



    Double-Click to Run: Now, you should be able to double-click the .desktop file to run your Python script without opening the terminal.

