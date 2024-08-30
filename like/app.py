import os
#kutubhonani olish

olam = True
while olam:
    print (f'''
     \033[1;33m_________________________
    |
    |\033[1;33m  [ 1 ] \033[1;32mTekshirish.
    |\033[1;33m  [ 2 ] \033[1;32mNomer ulash reg.
    |\033[1;33m  [ 3 ] \033[1;32mKanal va grga a'zo.
    |\033[1;33m  [ 4 ] \033[1;32m 1ta Kanal va grdan chiqish.
    |\033[1;33m  [ 5 ] \033[1;32mBarcha kanalardan chiq.
    |\033[1;33m  [ 6 ] \033[1;32mBarcha guruhlarda chiq.
    |\033[1;33m  [ 7 ] \033[1;32mStart bot.
    |\033[1;33m  [ 8 ] \033[1;32mLike bosish.
    |\033[1;32m  [ 9 ] \033[1;32mChiqish.
    |\033[1;32m 
    |\033[1;33m________Jm7Uzgr__________\033''')
    
    bf = (f'''\033[1;32m\nTanlang>>>:''')
    
    jm = input(bf)
    if jm == "1":
        os.system("python3 login.py")
    elif jm == "2":
        os.system("python3 reg.py")
    elif jm == "3":
        os.system("python3 join.py")
    elif jm == "4":
        os.system("python3 leave.py")
    elif jm == "5":
        os.system("python3 allleave.py")
    elif jm == "6":
        os.system("python3 allleave2.py")
    elif jm == "7":
        os.system("python3 bot.py")
    elif jm == "8":
        os.system("python3 like.py")
    elif jm == "9":
        os.system("python3 code.py")
    elif jm == "10":
        olam = False

