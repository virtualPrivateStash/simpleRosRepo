#!/usr/bin/python
import os
import time 
for i in range(10) :
	#os.system("rosnode info rosout")
	#os.system("rosnode info qrCreator")
	#os.system("rosnode info creation")
	os.system("rosrun ar_track_alvar createMarker {0}".format(i))
	#os.system("rosnode info qrCreator")
	#os.system("rosnode info creation")
	#time.sleep(100)
	#print(str(os.path.dirname(os.path.realpath(__file__))))
	#tmpPath = os.path.dirname(os.path.realpath(__file__))
	#print(os.listdir(tmpPath))
	
	fn = "MarkerData_{0}.png".format(i)
	os.system("convert {0} -bordercolor white -border 100x100 {0}".format(fn))
	with open("product_{0}.material".format(i), 'w') as f:
		f.write("""
material product_%d {
	receive_shadows on
		technique {
			pass {
			ambient 1.0 1.0 1.0 1.0
			diffuse 1.0 1.0 1.0 1.0
			specular 0.5 0.5 0.5 1.0
			lighting on
			shading gouraud
			texture_unit { texture MarkerData_%d.png }
			}
		}
}
""" % (i, i))

