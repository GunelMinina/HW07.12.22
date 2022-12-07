# Напишите программу, удаляющую из текста слова, содержащие 'абв'

my_text = 'аьвдфва gcgndfx вапрспрв мчтсщ'
my_text_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, my_text.split()))
print(my_text_list)