#Raspberry Security Night Cam using Motion

###Setup

1. Clone the repo into the 'pi' user's home folder
2. Run './motion-dependencies.sh'
3. Install Flask if not already installed (e.g. running 'pip install Flask')
4. Execute './setup-autostart.sh'

###API

######http://your ip:8081/get-images

Returns a json file with names of all captured images.

######http://your ip:8081/get-images/image name

Image name represents one image name contained in the get-images json.
It return the image with the given name.

######http://your ip:8081/delete-all

Deletes all captured images.