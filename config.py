#DBpath = 'sqlite:////mnt/sda1/termocontrol.db'
DBpath = 'sqlite:////Users/amenoni/Desarrollo/TermocontrolV2/termocontrol.db'
apiURL = 'http://192.168.1.107:8000/api/v1'
maxTemp = 50 #todo construct this value from usageLog or get it from arduino
#LINUX SIDE GLOBAL VARIABLES ---ARDUINO SIDE VARIABLES ARE STORED IN THE SQLITE DATABASE ---
minUsagesForStatics = 30  # how many usages we must log before start building the use statistics
bufferTimeToNextHourUse = 15 # how many minutes after the hour change we must consider to prepare the water temp