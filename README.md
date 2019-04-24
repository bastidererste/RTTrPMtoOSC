# RTTrPMtoOSC
RTTrPM is part of the RTTrP trtacking protocol used by BlackTrax, Disguise and many other realtime software and media servers to send/recive object tracking data. The RTTrPMtoOSC bridge brings this robust tracking protocol to applications that until now have no direct support for RTTrP, like Ventuz, processing or in generall all ohter applications that support OSC.

## Usage 
```
$ python RTTrPMtoOSC.py [-h] [-udpIP UDP_IP] [-udpPort UDP_PORT] [-oscIP OSC_IP] [-oscPort OSC_PORT] 
```

optional arguments:

    -h, --help         show this help message and exit
    -oscIP OSC_IP      ip of OSC client
    -oscPort OSC_PORT  port of OSC client
    -udpIP UDP_IP      ip of network adapter to listen for tracking data
    -udpPort UDP_PORT  port where to listen for tracking data

## Usage example
```
$ python RTTrPMtoOSC.py -udpIP 192.168.8.102 -udpPort 24220 -oscIP 127.0.0.1 -oscPort 9000
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

## Dependencies

python-osc [PiPy - python-osc](https://pypi.org/project/python-osc/)

```
$ pip install python-osc
```

