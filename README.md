# RTTrPMtoOSC

usage: python RTTrPMtoOSC.py [-h] [-oscIP OSC_IP] [-oscPort OSC_PORT] [-udpIP UDP_IP] [-udpPort UDP_PORT]

optional arguments:
  -h, --help         show this help message and exit
  -oscIP OSC_IP      ip of OSC client
  -oscPort OSC_PORT  port of OSC client
  -udpIP UDP_IP      ip of tracking server
  -udpPort UDP_PORT  port of tracking server


## OSC address pattern

/ {trackableName} / {module}

for the object "car1"

|PacketModule| address pattern               | args           |
|------| -------------------- |:-------------:| 
|Centroid Positioin|/{trackableName}/centroid       | x, y, z     | 
|Centroid Acceleration and Velocity|/{trackableName}/centroidAccVel | x, y, z, accel_x, accel_y, accel_z, vel_x, vel_y, vel_z     |
|Euler|/{trackableName}/euler | roll, pitch, yaw, roll_degree, pitch_degree, yaw_degree    |
|Quaternion |/{trackableName}/quaternion     | qx, qy, qz, qw |
