for _ in range(int(input())):
    s = input()
    d = int(s[:2])
    m = int(s[3:])
    if d<12 and d!=0 :
        print(s+ " AM")
    elif d==12:
        print(s + " PM")
    elif d == 0 and m!=0:
        if m<=9:
            print("12:0" + str(m) +" AM")
        else:
            print("12:" + str(m) +" AM")

    elif d == 0 and m == 0:
        print("12:00 AM")
    elif d>12:
        d -= 12
        if  d<=9:
            if m <=9:
                print( "0" + str(d)+ ":0"+ str(m) + " PM")
            else:
                print("0" +str(d)+ ":"+ str(m) + " PM")

        else:
            if m <= 9:
                print(str(d)+ ":0"+ str(m) + " PM")
            else:
                print(str(d)+ ":"+ str(m) + " PM")
 