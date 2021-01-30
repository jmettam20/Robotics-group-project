import time
import board
import busio
import adafruit_ccs811

i2c = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c)

#If sensor isnt ready pass
while not ccs811.data_ready:
    pass
#Print out CO2 in PPM and the TVOC(Total volotile orgo#anic compounds)  , asically toxic particles
while True:
    print("CO2: {} PPM, TVOC: {} PPB, Baseline: {}, data_ready: {}, eco2: {}, error: {}, error_code: {}, reset: {}".format(ccs811.eco2,ccs811.tvoc,ccs811.baseline, ccs811.data_ready,ccs811.eco2,ccs811.error,ccs811.error_code,ccs811.reset))

    time.sleep(0.5)