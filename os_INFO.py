import platform

# This script is written with help from OStechnix

""" linux_distribution function is depreciated from python 3.5
    It will be (is) removed on version 3.8 """

#print('Uname:', platform.uname())
#print()

print('Distribution :', platform.linux_distribution())
print('Machine :', platform.machine())
print('Node :', platform.node())
print('Processor :', platform.processor())
print('Release :', platform.release())
print('System :', platform.system())
print('Version :', platform.version())
print('Platform :', platform.platform())
