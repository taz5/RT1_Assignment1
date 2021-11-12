Python Robotics Simulator
================================

This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
Some of the arenas and the exercises have been modified for the Research Track I course

Installing and running
----------------------

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

## Troubleshooting

When running `python run.py <file>`, you may be presented with an error: `ImportError: No module named 'robot'`. This may be due to a conflict between sr.tools and sr.robot. To resolve, symlink simulator/sr/robot to the location of sr.tools.

On Ubuntu, this can be accomplished by:
* Find the location of srtools: `pip show sr.tools`
* Get the location. In my case this was `/usr/local/lib/python2.7/dist-packages`
* Create symlink: `ln -s path/to/simulator/sr/robot /usr/local/lib/python2.7/dist-packages/sr/`

## Assignment
-----------------------------
 

You can run the program with:

```bash
$ python2 run.py assignment.py
```


## Pseudocode

The pseudocode is as follows:

1. Robot start position
2. Robot checks if it is aligned with the token
   - uses drive function to move forward
   - print "Ah, that'll do"
else if the robot is not well aligned with token
	uses turn function to either to move left or right
if distance of silver is not -1 and the distance of the distance of silver is less than the threshold 
	print "The silver token is close!"
	if distance of silver token is less than the distance threshold
	    print "Found it!"
	    grabs the silver token and puts it behind it.

Robot progresses forward till it reaches a wall, which are gold tokens
Robot checks if distance of gold token is less than the threshold and if the distance is not equal to -1.
	if the wall distance on one side is greater than the other side
	    uses turn function to move to the distance that is greater

The above pseudocode will be done endlessly in the same fashion

  


