import os
#kutubhonani olish

olam = True
while olam:
    print (f'''
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ███████╗██╗██████╗ ██████╗  █████╗ ██╗   ██╗███████╗   │
│  ██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔════╝   │
│  █████╗  ██║██████╔╝██║  ██║███████║██║   ██║███████╗   │
│  ██╔══╝  ██║██╔══██╗██║  ██║██╔══██║╚██╗ ██╔╝╚════██║   │
│  ██║     ██║██║  ██║██████╔╝██║  ██║ ╚████╔╝ ███████║   │
│  ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝   │
 ─────────────────────────────────────────────────────────
    \033[1;33m____FIRDAVS_____________________
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
    |\033[1;32m  [ 10 ] \033[1;32mPrem yutganini tekshirish
    |\033[1;32m  [ 11 ] \033[1;32mKOD OLISH
    |\033[1;32m  [ 12 ] \033[1;32mKONKURS BOSISH IDEAL
    |\033[1;32m  [ 13 ] \033[1;32mSpamdan chqarishga zayafka.
    |\033[1;32m  [ 14 ] \033[1;32mPm Urish
    |\033[1;32m  [ 15 ] \033[1;32mHabar yuborish
    |\033[1;32m  [ 16 ] \033[1;32mRasm Qoyish
    |\033[1;32m  [ 17 ] \033[1;32mBan filter
    |\033[1;32m  [ 18 ] \033[1;32mUser almashtirish
    |\033[1;32m  [ 19 ] \033[1;32mBio almashtirish
    |\033[1;32m  [ 20 ] \033[1;32mPasswd
    |\033[1;32m 
    |\033[1;33m________IBRAGIMOV_________\033''')
    
    bf = (f'''/0,33[1;32\nTanlang>>>:''')
    
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
        os.system("python3 code1.py")
    elif jm == "10":
        os.system("python3 premtest.py")
    elif jm == "11":
        os.system("python3 code1.py")
    elif jm == "12":
        os.system("python3 kk.py")
    elif jm == "13":
        os.system("python3 spam.py")
    elif jm == "14":
        os.system("python3 view.py")
    elif jm == "15":
        os.system("python3 Send_msg.pyc")
    elif jm == "16":
        os.system("python3 Rasmlarim.pyc")
    elif jm == "17":
        os.system("python3 BanFilter.py")
    elif jm == "18":
        os.system("python3 username.py")
    elif jm == "19":
        os.system("python3 biochange.py")
    elif jm == "20":
        os.system("python3 changepswd.py")
        olam = False