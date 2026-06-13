"""
1. спросить длину пароля, сделать проверку(только числа)
2. спросить у пользователя, какой это пароль(состоит только из букв и чисел или должен содержать особые символы) 
3. составляем шаблон буд. пароля()
4. генерируем сам пороль с помощью перебора символов
5. показываем пользователю пароль перед глазами
6. спрашиваем, сохранить или нет
7. спрашиваем сайт и логин для него
8. выводим готовый результат
"""
import string
import random



while True:
	dlina = input("введите длину пароля\n")
	if dlina.isdigit():
		dlina = int(dlina)
		break
	else:
		print("введите число")



while True:
	sloznost = input("сложный ли нужен пароль?(easy/hard)\n")
	if sloznost == "easy" or sloznost == "hard":
		break
	else:
		print("выбери easy или hard")



if sloznost == "easy":
	shablon = string.ascii_lowercase + string.ascii_uppercase + string.digits
else:
	shablon = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation



password = ""
for i in range(dlina):
	password += random.choice(shablon)




print(f"готовый пароль\n====================\n{password}\n====================")



safe = input("сохранить пароль? (да/нет)\n")
if safe == "да":
	site=input("введите сайт, для которого будет использоваться пароль: \n")
	login=input(f"введите логин на сайте {site}: \n")
	with open("password.txt", "a") as f:
		f.write(site + "\n") 
		f.write("логин:  " + login + "\n")
		f.write("пароль:  " + password + "\n" )
		f.write("\n")
	print("пароль сохранен в password.txt")
else:
	print("пароль не сохранен")
