# Напишите программу, которая запрашивает строку до тех пор, пока пользователь не введет “хватит”.
# Т.е. программа запрашивает ввод, если вводится любое значение отличное от слова “хватит”,
# то программа запрашивает ввод снова.
data = input("Enter data: ")
stop =str("stop")
while data != stop :
    print (data)
    data = input("Enter data: ")
