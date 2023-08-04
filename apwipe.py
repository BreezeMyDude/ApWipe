from turtle import clear
import serial
import time




# while(comEntered == False):
#     COM = "COM" + input("What com number are you on?(Just enter the number it is not COM then the number): ")
#     comEntered = True
serialPort = serial.Serial(
    port= "COM5", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
serialString = ""  # Use66d to hold data coming over UART
# while 1:
#     # Wait until there is data waiting in the serial buffer
#     try:
#         if serialPort.in_waiting > 0:

#             # Read data out of the buffer until a carraige return / new line is found
#             serialString = serialPort.readline()

#             # Print the contents of the serial data
#             print(serialString.decode("Ascii"))
            # for word in serialString.split():
            #     try:
            #         if word.decode("Ascii") == "<Enter>":
            #             print("Enter Found")
            #             time.sleep(1)
            #             serialPort.write("\r".encode('utf-8'))
            #         print(word.decode("Ascii"))
            #     except:
            #         pass
            # if "<Enter>" in serialString.decode("Ascii"):
            #     print("Enter Found")
            #     time.sleep(1)
            #     serialPort.write("\r".encode('utf-8'))
def Readline():
    try:
        if serialPort.in_waiting > 0:
            time.sleep(.1)
            # Read data out of the buffer until a carraige return / new line is found
            Serial_Port_String = serialPort.readline()

            # Print the contents of the serial data
            data  = Serial_Port_String.decode("Ascii")
            print(data)
            return data
    except:
        time.sleep(10)
        return None

def Readlines():
    line = Readline()
    if Readline != line:
        print(line)
        print(Readline)

def SendWordsUntil(Input,Wait):
    print(f"Sending {Input} until we recive {Wait} as a response")
    LineOut = Readline()
    print(LineOut)
    if Wait not in LineOut:
        serialPort.write(Input.encode('Ascii'))
        serialPort.write("\r".encode('Ascii'))
        serialPort.flush()
        time.sleep(.10)
    else:
        print("Desired Response was found")




def clearAP():
    reset = False
    saved = False
    apDone = False
    found = False


    while(apDone == False):
        try:
            if serialPort.in_waiting > 0:

                # Read data out of the buffer until a carraige return / new line is found
                serialString = serialPort.readline()

                # Print the contents of the serial data
                print(serialString.decode("Ascii"))
            # APboot found so it will stop spamming enter ONLY if it has not been found

            # Hitting enter to enter thing.
            while(found == False):
                SendWordsUntil("","apboot>")
                #serialPort.write("\r".encode('Ascii'))
                print("Enter hit!")
                break

            while(reset == False):
                # check if reset was truly completed: 
                if "done" in serialString.decode("Ascii"):
                    print("Access point sent")
                    reset = True 
                            

                if "apboot>" in serialString.decode("Ascii"):
                    print("---Resetting AP---")
                    print("AP Boot Found, Now attempting to send Factory reset command")
                    found = True

                #  print(serialPort.write("factory_reset".encode('Ascii')))
                    #print(serialPort.write("\r".encode('Ascii')))
                # serialPort.flush()
                    print("Factory reset command sent, Flushed serial Port, Waiting for response")
                    SendWordsUntil("factory_reset","apboot>")
                    reset = True 
                break  
                

            while(saved == False and reset == True):
                if(reset == True and "apboot>" in serialString.decode("Ascii")):
                    print("---Saving AP---")
                    #Readline()
                    
                # Readline()
                    SendWordsUntil("save","apboot>")
                    #Readline()
                    print("Ap Saved")
                    saved = True
                    apDone = True
                break
        except:
            pass

        # except:
        #     pass

print("Waiting for an AP to be connected")
while True:
    
    if serialPort.in_waiting > 0:
        print("Clearing AP ")
        clearAP()
        print("AP has been cleared")
        time.sleep(3)
    else:
        time.sleep(.1)