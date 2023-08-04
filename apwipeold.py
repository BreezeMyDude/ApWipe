import serial

import time



serialPort = serial.Serial(

    port="COM5", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE

)

serialString = ""  # Used to hold data coming over UART

while 1:

    # Wait until there is data waiting in the serial buffer

    if serialPort.in_waiting > 0:



        # Read data out of the buffer until a carraige return / new line is found

        serialString = serialPort.readline()



        # Print the contents of the serial data

        for word in serialString.split():

            try:

                if word.decode("Ascii") == "<Enter>":

                    time.sleep(3)

                    print("Enter Found")

                    payload = "\r\n"

                    payload.encode("Ascii")



                    serialPort.write(payload)

                print(word.decode("Ascii"))

            except:

                pass




        try:

            print(serialString.decode("Ascii"))

        except:

            pass