# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import random


def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as flow:
        result = flow.read()
        return result


def writing_file(user_string: str, user_file: str):
    with open(user_file, 'w', encoding='utf-8') as flow:
        flow.writelines(user_string)


def cleared(comprssed_file, recovered_file):
    if input('Для очистки рабочих файлов введите "0".\n'
             'Для сохранения - другое число: ') == '0':
        cleared_data = ''
        cleared_file = comprssed_file
        writing_file(cleared_data, cleared_file)
        cleared_file = recovered_file
        writing_file(cleared_data, recovered_file)


def data_flow_generator(user_file: str):
    number_characters = random.randint(5, 20)
    simbol_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    data_flow = ''
    for i in range(number_characters):
        simbol_flow = random.choice(simbol_str)
        number_repetitions = random.randint(1, 50)
        for j in range(number_repetitions):
            data_flow += simbol_flow
    writing_file(data_flow, user_file)
    return data_flow


def rle_encoding(data):
    encode_rle = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encode_rle += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encode_rle += str(count) + prev_char
    return encode_rle


def rle_decoding(data):
    decode_rle = ''
    count = ''
    for char in data:
        if char in data:
            if char.isdigit():
                count += char
            else:
                decode_rle += char * int(count)
                count = ''
    return decode_rle


work_file = 'source_data.txt'
comprssed_file = 'compressed_data.txt'
recovered_file = 'recovered_data.txt'
cleared(comprssed_file, recovered_file)

way = input('Если Вы хотите сгенерировать новый поток данных, введите "1",\n'
            'если нет - введите любое другое число: ')
if way == '1':
    data_flow_generator(work_file)

incoming_stream = read_file(work_file)
compressed_data = rle_encoding(incoming_stream)
writing_file(compressed_data, comprssed_file)
restored_data = rle_decoding(compressed_data)
writing_file(restored_data, recovered_file)
cleared(comprssed_file, recovered_file)
