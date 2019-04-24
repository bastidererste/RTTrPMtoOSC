import socket
import binascii
import struct
import thirdParty_motion
import traceback
import RTTrP
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-oscIP", dest='OSC_IP', default="127.0.0.1",help="ip of OSC client")
parser.add_argument("-oscPort", dest='OSC_PORT', default=9000, type=int, help="port of OSC client")
parser.add_argument("-udpIP", dest='UDP_IP', default="192.168.8.102", help="ip of tracking server")
parser.add_argument("-udpPort",dest='UDP_PORT',  type=int, default=24220, help="port of tracking server")
args = parser.parse_args()

OSC_IP = args.OSC_IP
OSC_PORT =args.OSC_PORT

UDP_IP = args.UDP_IP
UDP_PORT = args.UDP_PORT




sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("RTTrPM to OSC conversion started on "+args.UDP_IP+" port "+str(args.UDP_PORT)+ " to "+ args.OSC_IP + " port " +str(args.OSC_PORT))
while True:
	data, addr = sock.recvfrom(65535)
	if(data != None and addr != None):
		pkt = RTTrP.RTTrP(data)
		try:
			# If we have an RTTrPM packet, begin to extract the components
			if (hex(pkt.fltHeader) == "0x4334" or hex(pkt.fltHeader) == "0x3443"):
				pkt = thirdParty_motion.RTTrPM(pkt)
				# print(pkt.rttrp_head.numMods)
				# After determining the number of trackables (listed in the RTTrP header) we begin to extract
				# each trackable from the packet and return it to the GUI
				for i in range(pkt.rttrp_head.numMods):
					module = thirdParty_motion.Trackable(pkt.data, pkt.rttrp_head.intHeader, pkt.rttrp_head.fltHeader)
					pkt.trackable = module
					
					# For each trackable, we need to extract each module. Keep in mind when dealing with LED modules, each
					# individual LED is considered it's own separate module, so we don't need to worry about
					# modules within modules, except in the case of a Trackable.
					
					for i in range(module.numMods):
						if (module.data[0] == 2):
							pkt.centroidMod = thirdParty_motion.CentroidMod(module.data, module.intSig, module.fltSig)
							module.data = pkt.centroidMod.data
						elif (module.data[0] == 3):
							pkt.quatMod = thirdParty_motion.QuatModule(module.data, module.intSig, module.fltSig)
							module.data = pkt.quatMod.data
			
						elif (module.data[0] == 4):
							pkt.eulerMod = thirdParty_motion.EulerModule(module.data, module.intSig, module.fltSig)
							module.data = pkt.eulerMod.data
						elif (module.data[0] == 6):
							# print(pkt.trackable.name+" 06 was executed")
							pkt.ledMod[pkt.trackable.name]=thirdParty_motion.LEDModule(module.data, module.intSig, module.fltSig, pkt.trackable.name)
							#print(pkt.ledMod)
							#module.data = pkt.ledMod[len(pkt.ledMod)-1].data
							#print(len(pkt.ledMod)-1)
						elif (module.data[0] == 32):
							pkt.centroidAccVelMod = thirdParty_motion.CentroidAccVelMod(module.data, module.intSig, module.fltSig)
							module.data = pkt.centroidAccVelMod.data
						elif (module.data[0] == 33):
							# print("33 was executed")
							pkt.LEDAccVelMod.append(thirdParty_motion.LEDAccVelMod(module.data, module.intSig, module.fltSig))
							module.data = pkt.LEDAccVelMod[len(pkt.LEDAccVelMod)-1].data
						else:
							# unknwon packet type, da fuq is this
							exit()
					pkt.data = pkt.data[pkt.trackable.size:]
					pkt.sendOSC(OSC_IP, OSC_PORT)
			elif (hex(pkt.fltHeader) == "0x4434" or hex(pkt.fltHeader) == "0x3444"): # TODO: Create the RTTrPL code that reads an RTTrPL packet
				print("RRTrPL not implemented")
				# pkt = RTTrPL(pkt)
				#sock.close()
				exit()
			
		except Exception as e:
			print(traceback.print_exc(None))
			continue
	# print("================#######################================#######===========")

sock.close()
