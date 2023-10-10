import requests
import os
import platform
print("[*] Checking Required Packages: - \n")
print("[*] Checking Requirements Module")
if platform.system().startswith("Linux"):
    try:
        import requests
    except ImportError:
        os.system("python3 -m pip install requests -q -q -q")
        import requests
    try:
        import pyfiglet
    except ImportError:
        os.system("python3 -m pip install pyfiglet -q -q -q")
        import pyfiglet
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
        from termcolor import colored
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        import pyuseragents as pyuseragents
    except:
        os.system("python3 -m pip install pyuseragents -q -q -q")
        import pyuseragents as pyuseragents


elif platform.system().startswith("Windows"):
    try:
        import requests
    except ImportError:
        os.system("python -m pip install requests -q -q -q")
        import requests
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        import pyuseragents as pyuseragents
    except:
        os.system("python -m pip install pyuseragents -q -q -q")
        import pyuseragents as pyuseragents


colorama.deinit()
banner = Center.XCenter("""
   ___   _ ____ _____ ____       _____ _ _   _ ____  _____ ______
  / / | | / ___|___ /|  _ \     |  ___/ | \ | |  _ \| ____|  _ \ \`
 | || | | \___ \ |_ \| |_) |____| |_  | |  \| | | | |  _| | |_) | |
< < | |_| |___) |__) |  _ <_____|  _| | | |\  | |_| | |___|  _ < > >
 | | \___/|____/____/|_| \_\    |_|   |_|_| \_|____/|_____|_| \_\ |
  \_\                                                          /_/          
                            \n\n
""")




user_agent = pyuseragents.random()
blu = "\033[96m"
red = "\033[91m"
grn = "\033[32m"
ylw = "\033[93m"
res = "\033[0;m"
HEADER = '\033[95m'
lred = "\033[2;31;5m"
def facebook(target):
    url=f"https://www.facebook.com/{target}"
    inp = requests.get(f"{url}").text
    if "The link you followed may be broken" in inp:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Facebook Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Facebook Found: {url}")
def tiktok(target):
    url=f"https://www.tiktok.com/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}TikTok Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Tiktok Found: {url}")
def youtube(target):
    url=f"https://www.youtube.com/{target}"
    inp = requests.get(f"{url}").text
    if "Not Found" in inp:
        print(f" {ylw}[ {red}✖{ylw} ] {red}YouTube Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}YouTube Found: {url}")
def blogspot(target):
    url = f"https://{target}.blogspot.com"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Blogspot Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Twitter Found: {url}")
def twitter(target):
    inp = {"input": target}
    header = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
              "x-requested-with": "XMLHttpRequest"}
    inp = requests.post(f"https://tweeterid.com/ajax.php", data=inp, headers=header).text
    if "error" in inp:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Twitter Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Twitter Found: {target}")
def mix(target):
    url="https://mix.com/"
    inp = requests.get(f"{url}{target}").status_code
    if inp == 301:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Mix Found: {url}")

    else:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Mix Not Found")
def basecamp(target):
    url="https://launchpad.37signals.com/session/profile?username="
    inp = requests.get(f"{url}{target}").text
    if 'password' in inp:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Basecamp Found: {url}")

    else:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Basecamp Not Found")
def wordpress(target):
    url=f"https://{target}.wordpress.com"
    inp = requests.get(f"{url}").text
    if "Do you want to register" in inp:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Wordpress Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Wordpress Found: {url}")
def reddit(target):
    url=f"https://en.reddit.com/user/{target}"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    inp = requests.get(f"{url}/about.json?jsonp=_jqjsp&_1661423588377=",
                        headers=header).status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Reddit Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Reddit Found: {url}")
def github(target):
    url=f"https://www.github.com/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Github Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Github Found: {url}")
def pintrest(target):
    url=f"https://www.pinterest.com/{target}"
    inp = requests.get(f"{url}", allow_redirects=False).status_code
    if inp == 301:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Pinterest Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Pinterest Found: {url}")
def vimeo(target):
    url=f"https://vimeo.com/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Vimeo Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Pinterest Found: {url}")

def med(target):
    url = f"https://medium.com/@{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Medium Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Medium Found: {url}")
def about(target):
    url=f"https://about.me/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}About Me Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}About me Found: {url}")
def spot(target):
    url=f"https://open.spotify.com/user/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Spotify Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Spotify Found: {url}")

def scribd(target):
    url=f"https://www.scribd.com/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Scrbid Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Scrbid Found: {url}")

def bit(target):
    url=f"https://bitbucket.org/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}BitBucket Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}BitBucket Found: {url}")
def daily(target):
    url=f"https://www.dailymotion.com/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Daily Motion Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Daily Motion Found: {url}")
def cash(target):
    url=f"https://cash.me/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Cash Me Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Cash Me Found: {url}")
def keybase(target):
    url=f"https://keybase.io/{target}"
    inp = requests.get(f"{url}").status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}keybase Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}keybase Found {url}")
def code(target):
    url=f"https://www.codecademy.com/{target}"
    inp = requests.get(f"{url}", headers={"user-agent": user_agent}).status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Code Academy Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Code Academy Found: {url}")
def paste(target):
    url=f"https://pastebin.com/u/{target}"
    inp = requests.get(f"{url}", headers={"user-agent": user_agent}).status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Pastebin Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Pastebin Found: {url}")
def wiki(target):
    url=f"https://www.wikipedia.org/wiki/User:{target}"
    inp = requests.get(f"{url}", headers={"user-agent": user_agent}).status_code
    if inp == 404:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Wikipedia Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Wikipedia Found: {url}")

def ebay(target):
    url=f"https://www.ebay.com/usr/{target}"
    inp = requests.get(f"{url}", headers={"user-agent": user_agent}).text
    if "The User ID you entered was not found. Please check the User ID and try again." in inp:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Ebay Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Ebay Found: {url}")
def slack(target):
    url=f"https://{target}.slack.com"
    inp = requests.get(f"{url}", headers={"user-agent": user_agent}).status_code
    if inp != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Slack Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Slack Found: {url}")

def proton(target):
    url=f"https://account.protonmail.com/api/users/available?Name={target}"
    inp = requests.get(f"{url}",
                        headers={"user-agent": user_agent}).status_code
    if inp != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}ProtonVPN Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}ProtonVPN Found: {url}")
def xbox(target):
    url=f"https://playerdb.co/api/player/xbox/{target}"
    inp = requests.get(f"{url}", headers={"user-agent": user_agent}).status_code
    if inp != 200:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Xbox Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Xbox Found: {url}")
def hackernews(target):
    url=f"https://news.ycombinator.com/user?id={target}"
    inp = requests.get(f"{url}", headers={"user-agent": user_agent}).text
    if "No such user." in inp:
        print(f" {ylw}[ {red}✖{ylw} ] {red}Hacker News Not Found")

    else:
        print(f" {ylw}[ {grn}✔{ylw} ] {grn}Hacker News Found: {url}")


def catc():
    try:
        if platform.system().startswith("Windows"):
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            target = input(Fore.GREEN+'[*] Enter Username:- ')
            tiktok(target)
            youtube(target)
            blogspot(target)
            twitter(target)
            mix(target)
            basecamp(target)
            reddit(target)
            github(target)
            pintrest(target)
            vimeo(target)
            med(target)
            about(target)
            spot(target)
            scribd(target)
            bit(target)
            daily(target)
            cash(target)
            keybase(target)
            code(target)
            paste(target)
            wiki(target)
            ebay(target)
            slack(target)
            proton(target)
            xbox(target)
            hackernews(target)
        else:
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            target = target = input(Fore.GREEN+'[*] Enter Username:- ')
            tiktok(target)
            youtube(target)
            blogspot(target)
            twitter(target)
            mix(target)
            basecamp(target)
            reddit(target)
            github(target)
            pintrest(target)
            vimeo(target)
            med(target)
            about(target)
            spot(target)
            scribd(target)

            bit(target)
            daily(target)
            cash(target)
            keybase(target)
            code(target)
            paste(target)
            wiki(target)
            ebay(target)
            slack(target)
            proton(target)
            xbox(target)
            hackernews(target)
    except KeyboardInterrupt:
        print()
        print(termcolor.colored("\nYou Pressed The Exit Button!",'red'))
        quit()

catc()

