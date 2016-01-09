#DBpath = 'sqlite:////mnt/sda1/arduino/termocontrol.db'
DBpath = 'sqlite:////Users/amenoni/Desarrollo/TermocontrolV2/termocontrol.db'
minUsagesForStatics = 30  # how many usages we must log before start building the use statistics
bufferTimeToNextHourUse = 15 # how many minutes after the hour change we must consider to prepare the water temp
maxTemp = 55