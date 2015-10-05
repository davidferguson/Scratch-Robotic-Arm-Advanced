# Scratch-Robotic-Arm-Advanced
An interface between Scratch 1.4 and a USB robotic arm from Maplin. Simultaneous commands allowed!

To use, you will first need to install scratchpy and pyusb.
<p>
To install scratchpy;</br>
<ol>
<li>run <b>sudo pip install scratchpy</b></li>
</ol>
</p>
</br>
<p>
To install pyusb;</br>
<ol>
<li>download the latest release from http://sourceforge.net/projects/pyusb/</li>
<li>extract the folder, and use Terminal to cd into it's directory</li>
<li>run <b>sudo python setup.py install</b></li>
</ol>
</p>

Once you have pyusb and scratchpy installed, plug in your Robotic Arm, open the Scratch Interface.sb project, and run the python-handler.py file. You should now be able to control the robotic arm with Scratch broadcasts.
