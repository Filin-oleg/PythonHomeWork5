# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def delete_words(text, delete_str):
    text = list(filter(lambda x: (delete_str) not in x, text.split()))
    return " ".join(text)


print("Введите текст ")
text = input()
print("Введите комбинацию букв для удаления из текста слов с данной комбинацией букв ")
delete_str = input()
result_text = delete_words(text, delete_str)
print("Текст после удаления слов содержащих заданную Вами комбинацию букв ")
print(result_text)
