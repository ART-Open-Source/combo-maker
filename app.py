from random import choice as a

print('by 6u15_ on Instagram ')

print(' ----- \n 1 = combo user \n 2 = combo email \n ----- ') combo = int(input(''))

if combo == 1 : a4 = int(input('number of letters : \n')) user_a = 'qwertyuiopAsdfghkLlzxcvbnm._1234567890' pass_a = ['11221122','123123123123','Aa123123','Aa121212','1234512345' , '1234554321' , 'password'] while True: username_a =str(''.join((a(user_a) for i in range(a4)))) password_a = a(pass_a) combo_a = username_a+':'+password_a print(combo_a) open ('user_combo.txt', 'a').write(combo_a+'\n')

if combo == 2 : a1 = input(' DOMIN : \n') a4 = int(input('number of letters : \n')) user_a = 'qwertyuiopAsdfghkLlzxcvbnm_1234567890' pass_a = ['11221122','123123123123','Aa123123','Aa121212','1234512345' , '1234554321' , 'password'] while True: username_a =str(''.join((a(user_a) for i in range(a4)))) password_a = a(pass_a) combo_a = username_a+a1+':'+password_a print(combo_a) open ('email_combo.txt', 'a').write(combo_a+'\n')
