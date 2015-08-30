###PyGmail
PyGmail is a Pen-Testing BruteForce program.

###Passwords
Currently PyGmail has an intergrated passlist. 

###Run PyGmail
```
ozylol@devbot:~/Desktop/PyGmail# python pygmail.py

 /$$$$$$$             /$$$$$$                          /$$ /$$
| $$__  $$           /$$__  $$                        |__/| $$
| $$  \ $$ /$$   /$$| $$  \__/ /$$$$$$/$$$$   /$$$$$$  /$$| $$
| $$$$$$$/| $$  | $$| $$ /$$$$| $$_  $$_  $$ |____  $$| $$| $$
| $$____/ | $$  | $$| $$|_  $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$
| $$      | $$  | $$| $$  \ $$| $$ | $$ | $$ /$$__  $$| $$| $$
| $$      |  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$
|__/       \____  $$ \______/ |__/ |_/ |__/ \_______/|__/|__/ 
           /$$  | $$                                          
          |  $$$$$$/                                          
           \______/ 											
					Version [0.1.0]




Gmail Account: 
```

###Install
```` 
ozylol@devbot:~/Desktop/PyGmail# sudo pip install colorama
```

###Adding more passwords
The current passlist is fairly tiny so I will be adding more passwords in the future.

###Contribute
If you want to add more passwords to the passlist, by all means. That means less work for me!

###Timeouts
I'm using ```smtplib``` so timeouts in the session happen after around 8-9 times for one email. But the other than that, the script works fine. Also ```smtpserver``` sucks, so later updates will fix that problem too.

###Other shit
You dont need the wordlist, I just put it in there because slowly I will add more and more passwords to the current ```passlist```.