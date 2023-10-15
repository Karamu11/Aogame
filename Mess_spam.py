from emoji.core import emoji_count
import requests, os
import socket
from time import sleep
import emoji
import os

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = "\033[1m"
    TAU = "\U0001f680"
print(style.RED  'Tool By AoGame')

ip=socket.gethostbyname(socket.gethostname())
th='- - - - - - - - - - - - - - - - - - - - - - - - -'
print(style.HEADER +emoji.emojize(':red_heart:  SPAM MESSENGER :red_heart:'))
print(style.BLUE+'----------------------------')
id=input(style.OKGREEN + '\U0001f4aa NHẬP ID MỤC TIÊU \U0001f64a :')
print(style.BLUE+'----------------------------')
while True:
  ck=input(style.GREEN + '\U0001f58a\uFE0F  NHẬP COOKIE FACEBOOK \U0001f4dc :')
  print(style.BLUE+'----------------------------')
  try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        break
  except:
        print(style.RED +'SAI COOKIE RỒI NGU QUÁ \U0001f602')



nd=input(style.GREEN + '\u270D\uFE0F Nhập nội dung : ')
print(style.BLUE+'----------------------------')
so_luong=int(input(style.GREEN +'\U0001f525Nhập số lần spam : '))
print(style.BLUE+'----------------------------')
delay=int(input('\u23F1\uFE0F Nhập delay: '))
print(style.BLUE+'----------------------------')
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    # Requests sorts cookies= alphabetically
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

params = {
    'icm': '1',
}

data = {
    f'ids[{id}]': id,
    'body': nd,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
}
for i in range(1,so_luong+1):
    response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
    print(style.GREEN + f'{i}. \u2694\uFE0F  Mục Tiêu Đã Bị Tấn Công \U0001f680 | {nd} \U0001f3f9')
    sleep(delay)
print(style.BLUE+'----------------------------')
print(style.HEADER +'__[KẾT THÚC TẤN CÔNG]__')
print(style.BLUE+'----------------------------')
