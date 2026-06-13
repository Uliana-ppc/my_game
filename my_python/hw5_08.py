file = input("какой файл стереть?\n")
open(file, "w").close()
print("файл почистился")
