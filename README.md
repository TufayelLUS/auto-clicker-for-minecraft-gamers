# Auto Clicker for Minecraft Gamers
Need blazing-fast autoclicker? Here's this Python repository for you that uses pyautogui and keyboard library to auto-click at 570 cps!

# Screenshot from cpstest
<img src="https://raw.githubusercontent.com/TufayelLUS/auto-clicker-for-minecraft-gamers/refs/heads/main/cps.png"> 

# Libraries needed
<pre>pip install pyautogui keyboard</pre>

# Caution
As this is a multithreaded program, it may crash or slow down your PC/laptop if the number of threads is too much for your CPU to handle

# How does it work?
This script listens for a specified key press event to start clicking for a limited time and then stops (it's not indefinite because it hangs the computer if we plan it to run indefinitely, so I used the approach of limited iteration for clicks so that you can press as many times as you want and your clicks multiply)<br>
Currently, it's set to listen to "a" button being pressed. And when you press ESC, the script will stop. You can customize the keys in the source code.<br>
I'll compile this to a Windows executable and add a GUI screen in the future for enough interested people. 
