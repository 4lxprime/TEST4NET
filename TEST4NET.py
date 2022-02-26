import speedtest
import time
                                                                    #--------------------COMMENTS--------------------#
                                                                    
f = open("connection.log" ,'a')                                                 #set the log file
log = "---------------------------------------------LOG-NET---------------------------------------------"
temp = time.localtime()                                                         #set time
t = time.asctime(temp)                                                          #set legible time
template = f"[+]-[{t}]-"
box = "box-name"                                                                #set your box name (for the style)
value = "mo"                                                                    #values is : go, mo, ko
logo = f"""
 _______  _______  _______  _______  _____   _______  _______  _______
|_     _||    ___||     __||_     _||  |  | |    |  ||    ___||_     _|
  |   |  |    ___||__     |  |   |  |__    ||       ||    ___|  |   |   {box}
  |___|  |_______||_______|  |___|     |__| |__|____||_______|  |___|    
"""

def main():
    try:
        st = speedtest.Speedtest()
        up = st.upload()                                                        #get the upload
        dw = st.download()                                                      #get the download
        if value == "mo":
            up = up / 8                                                         #convert bits in octets
            up = up / 1000000                                                   #convert octets in mo
            up = round(up, 2)                                                   #round the result
            dw = dw / 8                                                         #convert bits in octets
            dw = dw / 1000000                                                   #convert octets in mo
            dw = round(dw, 2)                                                   #round the result
            stat = f"online (upload : {up} Mo/s, download : {dw} Mo/s)"
            temp = time.localtime()                                             #reset time
            t = time.asctime(temp)                                              #reset legible time
            template = f"[+]-[{t}]-"
            f.write(f"\n{template}network stat : {stat}")
            print(f"{template}network stat : {stat}")
            time.sleep(120)                                                     #wait 120 seconds
            main()
        elif value == "go":
            up = up / 8                                                         #convert bits in octets
            up = up / 1000000000                                                #convert octets in go
            up = round(up, 5)                                                   #round the result
            dw = dw / 8                                                         #convert bits in octets
            dw = dw / 1000000000                                                #convert octets in go
            dw = round(dw, 5)                                                   #round the result
            stat = f"online (upload : {up} Go/s, download : {dw} Go/s)"
            temp = time.localtime()                                             #reset time
            t = time.asctime(temp)                                              #reset legible time
            template = f"[+]-[{t}]-"
            f.write(f"\n{template}network stat : {stat}")
            print(f"{template}network stat : {stat}")
            time.sleep(120)                                                     #wait 120 seconds
            main()
        elif value == "ko":
            up = up / 8                                                         #convert bits in octets
            up = up / 1000                                                      #convert octets in ko
            up = round(up, 1)                                                   #round the result
            dw = dw / 8                                                         #convert bits in octets
            dw = dw / 1000                                                      #convert octets in ko
            dw = round(dw, 1)                                                   #round the result
            stat = f"online (upload : {up} Ko/s, download : {dw} Ko/s)"
            temp = time.localtime()                                             #reset time
            t = time.asctime(temp)                                              #reset legible time
            template = f"[+]-[{t}]-"
            f.write(f"\n{template}network stat : {stat}")
            print(f"{template}network stat : {stat}")
            time.sleep(120)                                                     #wait 120 seconds
            main()
    except:
        stat = "offline"
        temp = time.localtime()                                                 #reset time
        t = time.asctime(temp)                                                  #reset legible time
        template = f"[+]-[{t}]-"
        f.write(f"\n{template}network stat : {stat}")
        print(f"{template}network stat : {stat}")
        time.sleep(120)                                                         #wait 120 seconds
        main()

print(logo)                                                                     #display the logo in the console
f.write(logo)                                                                   #display the logo in the log file
print(" ")
print(f"time : {t}")                                                            #display the time in the console
f.write(f"\ntime : {t}\n")                                                      #display the time in the log file
print(" ")
print(log)                                                                      #display the log message in the console
f.write(log)                                                                    #display the log message in the log file

main()
