# RTTrPMtoOSC

## Usage 

#### $ python RTTrPMtoOSC.py [-h] [-oscIP OSC_IP] [-oscPort OSC_PORT] [-udpIP UDP_IP] [-udpPort UDP_PORT]

optional arguments:

    -h, --help         show this help message and exit
    -oscIP OSC_IP      ip of OSC client
    -oscPort OSC_PORT  port of OSC client
    -udpIP UDP_IP      ip of tracking server
    -udpPort UDP_PORT  port of tracking server

## Usage example

#### $ python RTTrPMtoOSC.py -oscIP 127.0.0.1 -oscPort 9000 -udpIP 192.168.8.102 -udpPort 24220
```
RTTrPM to OSC conversion started on 192.168.8.102 port 24220 to 127.0.0.1 port 9000
```




## OSC address pattern

#### / {trackableName} / {packetModule}

## Packet Modules and arguments

|PacketModule| address pattern               | args           |
|------| -------------------- |:-------------:| 
|Centroid Positioin|/{trackableName}/centroid       | x, y, z     | 
|Centroid Acceleration and Velocity|/{trackableName}/centroidAccVel | x, y, z, accel_x, accel_y, accel_z, vel_x, vel_y, vel_z     |
|Euler|/{trackableName}/euler | roll, pitch, yaw, roll_degree, pitch_degree, yaw_degree    |
|Quaternion |/{trackableName}/quaternion     | qx, qy, qz, qw |

## OSC example
A trackable with the name "beacon12" will result in a centroid OSC messages of the form "/beacon12/centroid"

