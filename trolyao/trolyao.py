#truy cập, xử lí file hệ thống
import os
#Chuyển văn bản thành âm thanh
from gtts import gTTS
#Mở âm thanh
import playsound
#Chuyển âm thanh thành văn bản
import speech_recognition
from time import strftime
import time
import datetime
from datetime import date 
#Chọn ngẫu nhiên 
import random
#Truy cập web, trình duyệt
import re
import webbrowser
#Lấy thông tin từ web
import requests
import json
#Truy cập web, trình duyệt, hỗ trợ tìm kiếm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
#Thư viện Tkinter hỗ trợ giao diện
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
import urllib.request as urllib2
#truy cập, xu ly file he thong 
import ctypes 
#khai bao bien 
path=ChromeDriverManager().install()
root = Tk()
text_area = Text(root, height=26, width=45)
scroll = Scrollbar(root, command=text_area.yview)

#chuc năng chuyen van ban thanh am thanh 
def speak(text):
    print("AI:  {}".format(text))
    text_area.insert(INSERT,"AI: "+text+"\n")
    output = gTTS(text=text, lang='vi', slow=False) 
    output.save("output.mp3")
    playsound.playsound('output.mp3', True)
    os.remove("output.mp3")

#chuc nang chuyen am thanh thanh van ban 
def get_audio():
    playsound.playsound("Ping.mp3", False)
    time.sleep(1)
    print("\nAi:  Đang nghe ...")
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("You: ")
        audio = r.listen(source, phrase_time_limit=6)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower() #tra ve chu thuong 
        except:
            print("\n")
            return ""
#chuc nang giao tiep, chao hoi 

def hello():
    image1 = Image.open("image\\hacker1.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    day_time = int(strftime('%H'))
    if day_time < 11:
        speak("Chào buổi sáng tốt lành.AI có thể giúp gì được cho bạn.")
    elif 11 <= day_time < 13:
        speak("Chào buổi trưa tốt lành.AI có thể giúp gì được cho bạn.")
    elif 13 <= day_time < 18:
        speak("Chào buổi chiều tốt lành.AI có thể giúp gì được cho bạn.")
    else:
        speak("Chào buổi tối tốt lành.AI có thể giúp gì được cho bạn.")
    root.update()
    time.sleep(1)
#chuc nang hien thi thoi gian 

def get_time(text):
    image1 = Image.open("image\\thoigian.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    yesterday = now + datetime.timedelta(days=-1)
    today = date.today() 
    now3 = "Chủ nhật"
    if "giờ" in text:
        speak("Bây giờ là %d giờ %d phút %d giây"%(now.hour, now.minute, now.second))
    elif "hôm nay" in text and "là ngày"in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
    elif "ngày mai" in text:
        speak("Ngày mai là ngày %d tháng %d năm %d" % (tomorrow.day, tomorrow.month, tomorrow.year))
    elif "hôm qua" in text:
        speak("Hôm qua là ngày %d tháng %d năm %d" % (yesterday.day, yesterday.month, yesterday.year))
    elif "thứ" in text and today.weekday()!=6:
        speak("hôm nay là thứ %d" % (today.weekday() + 2))
    elif "thứ" in text and today.weekday()==6:
        speak("Hôm nay là %s" % (now3)) 
    else:
        speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không ?")
        time.sleep(1)
    root.update()
    time.sleep(1)
#chuc nang mở video tren youtube 

def play_song():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    speak('nội dung bạn muốn tìm là gì ?')
    root.update()
    time.sleep(3)
    mysong = get_audio()
    text_area.insert(INSERT,"You: "+mysong+"\n")
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Nội dung bạn yêu cầu đã được mở.")
    #print(result) 
    time.sleep(6)
    root.update()
    time.sleep(6)
#chuc nang mơ ung dung he thong 
def open_application(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "word" in text:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        speak( "Word đã được mở")
    elif "excel" in text:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        speak("Excel đã được mở")
    elif "powerpoint" in text:
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
        speak("PowerPoint đã được mở")
    elif "chrome" in text:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        speak("Google chrome đã được mở")
    
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    root.update()
    time.sleep(6)
#chuc nang mơ website 
def open_website(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    reg_ex = re.search('mở website (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        print(domain) 
        return True
    else:  
        return False 
    root.update()
    time.sleep(6)
#chuc nang mo google va tim kiem 
def open_google_and_search(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    search_for = text.split("kiếm", 1)[1]
    speak('AI đang tìm kiếm giúp bạn')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    root.update()
    time.sleep(5)
    root.update()
    time.sleep(5)
#chuc nang thay doi hinh nen may tinh 
def change_wallpaper():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    api_key = "DN_AGNS78lg1BPVxKIy9odxXvvSAvj4--XXe1sEYyCE"
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
          api_key  
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "C:\\Users\\nguye\\Documents\\Code\\python\\image\\imagechange.png")
    image = os.path.join("C:\\Users\\nguye\\Documents\\Code\\python\\image\\imagechange.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    speak("Hình nền máy tính bạn đã được thay đổi.")
    time.sleep(1)
    root.update()
    time.sleep(1)
#chuc nang hien thi thoi gian bieu  

#mở file csv,mode=w:để viết,r:đọc, utf-8-sig:đọc tiếng việt 
file = open("dulieu.csv", mode = "r",encoding="utf-8-sig")

#dong dau tien
header = file.readline()
header_list = header.split(";")

#dong 2
row2 = file.readline()
row2_list = row2.split(";")
row3 = file.readline()
row3_list = row3.split(";")
row4 = file.readline()
row4_list = row4.split(";")
row5 = file.readline()
row5_list = row5.split(";")
row6 = file.readline()
row6_list = row6.split(";")
row7 = file.readline()
row7_list = row7.split(";")
row8 = file.readline()
row8_list = row8.split(";")

thu2 = row2_list[0]+", "+header_list[1]+", "+row2_list[1] +", "+ header_list[2]+ " "+ row2_list[2]+", "+ header_list[3]+" "+ row2_list[3]
thu3 = row3_list[0]+", "+header_list[1]+", "+row3_list[1] +", "+ header_list[2]+ " "+ row3_list[2]+", "+ header_list[3]+" "+ row3_list[3]
thu4 = row4_list[0]+", "+header_list[1]+", "+row4_list[1] +", "+ header_list[2]+ " "+ row4_list[2]+", "+ header_list[3]+" "+ row4_list[3]
thu5 = row5_list[0]+", "+header_list[1]+", "+row5_list[1] +", "+ header_list[2]+ " "+ row5_list[2]+", "+ header_list[3]+" "+ row5_list[3]
thu6 = row6_list[0]+", "+header_list[1]+", "+row6_list[1] +", "+ header_list[2]+ " "+ row6_list[2]+", "+ header_list[3]+" "+ row6_list[3]
thu7 = row7_list[0]+", "+header_list[1]+", "+row7_list[1] +", "+ header_list[2]+ " "+ row7_list[2]+", "+ header_list[3]+" "+ row7_list[3]
cn = row8_list[0]+", "+header_list[1]+", "+row8_list[1] +", "+ header_list[2]+ " "+ row8_list[2]+", "+ header_list[3]+" "+ row8_list[3]
def week1(x):
    switcher={
            0:cn,
            1:thu2, 
            2:thu3,
            3:thu4,
            4:thu5,
            5:thu6,
            6:thu7,
        }
    return switcher.get(x, "nothing")
def subject(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now1 = datetime.datetime.now().strftime("%w")
    if "hôm nay" in text:
        now2 = int(now1)
        speak("Hôm nay "+week1(now2))
        root.update()
        sleep_time(now2)
    elif "ngày mai" in text:
        now2 = int(now1)+1
        if now2 >6:
            now2=0
        speak("Ngày mai "+week1(now2))
        root.update()
        sleep_time(now2)
def subject_day(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "thứ hai" in text:
        speak(thu2)
        root.update()
        sleep_time(0.5)
    elif "thứ ba" in text:
        speak(thu3)
        root.update()
        sleep_time(0.5)
    elif "thứ tư" in text:
        speak(thu4)
        root.update()
        sleep_time(0.5)
    elif "thứ năm" in text:
        speak(thu5)
        root.update()
        sleep_time(0.5)
    elif "thứ sáu" in text:
        speak(thu6)
        root.update()
        sleep_time(0.5)
    elif "thứ 7" in text:
        speak(thu7)
        root.update()
        sleep_time(0.5)
    elif "chủ nhật" in text:
        speak(cn)
        root.update()
        sleep_time(0)
# buổi sáng hôm nay, ngày mai, sáng thứ 2, sáng thứ 3...
st2 = row2_list[1]
st3 = row3_list[1]
st4 = row4_list[1]
st5 = row5_list[1]
st6 = row6_list[1]
st7 = row7_list[1]
scn = row8_list[1]

def week2(x):
    switcher={
            0:scn,
            1:st2, 
            2:st3,
            3:st4,
            4:st5,
            5:st6,
            6:st7,
        }
    return switcher.get(x, "nothing")
def subject2(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now1 = datetime.datetime.now().strftime("%w")
    if "sáng hôm nay" in text:
        now2 = int(now1)
        speak("sáng hôm nay "+week2(now2))
        root.update()
        sleep_time(now2)
    elif "sáng ngày mai" in text:
        now2 = int(now1)+1
        if now2 >6:
            now2=0
        speak("sáng ngày mai "+week2(now2))
        root.update()
        sleep_time(now2)
def subject_day2(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "sáng thứ hai"  in text:
        speak("sáng thứ hai "+st2)
        root.update()
        sleep_time(0.5)
    elif "sáng thứ ba" in text:
        speak("sáng thứ ba "+st3)
        root.update()
        sleep_time(0.5)
    elif "sáng thứ tư" in text:
        speak("sáng thứ tư "+st4)
        root.update()
        sleep_time(0.5)
    elif "sáng thứ năm"in text:
        speak("sáng thứ 5 "+st5)
        root.update()
        sleep_time(0.5)
    elif "sáng thứ sáu"  in text:
        speak("sáng thứ sáu "+st6)
        root.update()
        sleep_time(0.5)
    elif "sáng thứ bảy"  in text:
        speak("sáng thứ bảy "+st7)
        root.update()
        sleep_time(0.5)
    elif "sáng chủ nhật" in text:
        speak("sáng chủ nhật "+scn)
        root.update()
        sleep_time(0)
#chiều hôm nay, ngày mai, thứ 2, thứ 3...
ct2 = row2_list[2]
ct3 = row3_list[2]
ct4 = row4_list[2]
ct5 = row5_list[2]
ct6 = row6_list[2]
ct7 = row7_list[2]
ccn = row8_list[2]

def week3(x):
    switcher={
            0:ccn,
            1:ct2, 
            2:ct3,
            3:ct4,
            4:ct5,
            5:ct6,
            6:ct7,
        }
    return switcher.get(x, "nothing")
def subject3(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now1 = datetime.datetime.now().strftime("%w")
    if "chiều hôm nay" in text:
        now2 = int(now1)
        speak("chiều hôm nay "+week3(now2))
        root.update()
        sleep_time(now2)
    elif "chiều ngày mai" in text:
        now2 = int(now1)+1
        if now2 >6:
            now2=0
        speak("chiều ngày mai "+week3(now2))
        root.update()
        sleep_time(now2)
def subject_day3(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "chiều thứ 2"  in text:
        speak("chiều thứ hai "+ct2)
        root.update()
        sleep_time(0.5)
    elif "chiều thứ ba"  in text:
        speak("chiều thứ ba "+ct3)
        root.update()
        sleep_time(0.5)
    elif "chiều thứ tư"  in text:
        speak("chiều thứ tư "+ct4)
        root.update()
        sleep_time(0.5)
    elif "chiều thứ năm" in text:
        speak("chiều thứ năm "+ct5)
        root.update()
        sleep_time(0.5)
    elif "chiều thứ sáu" in text:
        speak("chiều thứ sáu "+ct6)
        root.update()
        sleep_time(0.5)
    elif "chiều thứ bảy" in text:
        speak("chiều thứ bảy "+ct7)
        root.update()
        sleep_time(0.5)
    elif "chiều chủ nhật" in text:
        speak("chiều chủ nhật "+ccn)
        root.update()
        sleep_time(0)

#tối hôm nay, mai, thứ 2, thứ 3...
tt2 = row2_list[3]
tt3 = row3_list[3]
tt4 = row4_list[3]
tt5 = row5_list[3]
tt6 = row6_list[3]
tt7 = row7_list[3]
tcn = row8_list[3]

def week4(x):
    switcher={
            0:tcn,
            1:tt2, 
            2:tt3,
            3:tt4,
            4:tt5,
            5:tt6,
            6:tt7,
        }
    return switcher.get(x, "nothing")
def subject4(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now1 = datetime.datetime.now().strftime("%w")
    if "tối hôm nay" in text:
        now2 = int(now1)
        speak("tối hôm nay "+week4(now2))
        root.update()
        sleep_time(now2)
    elif "tối ngày mai" in text:
        now2 = int(now1)+1
        if now2 >6:
            now2=0
        speak("tối ngày mai "+week4(now2))
        root.update()
        sleep_time(now2)
def subject_day4(text):
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "tối thứ hai"  in text:
        speak("tối thứ hai "+tt2)
        root.update()
        sleep_time(0.5)
    elif "tối thứ ba" in text:
        speak("tối thứ ba "+tt3)
        root.update()
        sleep_time(0.5)
    elif "tối thứ tư"  in text:
        speak("tối thứ tư "+tt4)
        root.update()
        sleep_time(0.5)
    elif "tối thứ 5" in text:
        speak("tối thứ năm "+tt5)
        root.update()
        sleep_time(0.5)
    elif "tối thứ sáu"in text:
        speak("tối thứ sáu "+tt6)
        root.update()
        sleep_time(0.5)
    elif "tối thứ 7" in text:
        speak("tối thứ bảy "+tt7)
        root.update()
        sleep_time(0.5)
    elif "tối chủ nhật" in text:
        speak("tối chủ nhật "+tcn)
        root.update()
        sleep_time(0)




#chuc nang hien thi thoi tiet 
def weather(text):
    temp="Trời quang mây tạnh"
    if "moderate rain" in text:
        temp="Trời hôm nay có mưa vừa, bạn ra ngoài nhớ mang theo áo mưa" 
    elif "heavy intensity rain" in text or "thunderstorm with light rain" in text or "very heavy rain" in text:
        temp="Trời hôm nay có mưa rất lớn kèm theo giông sét, bạn nhớ đem ô dù khi ra ngoài" 
    elif "light rain" in text:
        temp="Trời hôm nay mưa nhẹ, rải rác một số nơi" 
    elif "heavy intensity shower rain" in text:
        temp="Trời hôm nay có mưa rào với cường độ lớn"
    elif "broken clouds" in text or "few clouds" in text:
        temp="Trời hôm nay có mây rải rác, không mưa"
    elif "overcast clouds" in text:
        temp="Trời hôm nay nhiều mây, u ám, dễ có mưa"
    elif "scattered clouds" in text:
        temp="Trời hôm nay có nắng, có mây rải rác"   
    
    if "rain" in text:
        image1 = Image.open("image\\thoitiet2.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
    else :
        image1 = Image.open("image\\thoitiet1.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

    return temp

def temperature(text):
    temp="mát mẻ"
    if text<15:
        temp="lạnh buốt giá"
    elif text<20:
        temp="khá lạnh"
    elif text<30:
        temp="mát mẻ"
    elif text<33:
        temp="khá nóng"
    else:
        temp="nóng bức"

    return temp

def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu vậy.")
    root.update()
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_audio()
    text_area.insert(INSERT,"You: "+city+"\n")
    if city=="":
        current_weather()
    else:
        api_key = "005a04eefd0c96ac9b6e6a015836601f"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        #print(data)
        if data["cod"] != "404":
            city_res = data["main"]
            current_humidity = city_res["humidity"]
            current_temperature = city_res["temp"]
            temperature1=temperature(current_temperature)
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

            weather_description = data["weather"][0]["description"]
            weather1=weather(weather_description)
            content = """
    -Thời tiết hôm nay {temperature} có nhiệt độ trung bình là {temp} độ C 
    -Độ ẩm là {humidity}%
    -{weather}
    -Mặt trời mọc vào {hourrise} giờ {minrise} phút
    -Mặt trời lặn vào {hourset} giờ {minset} phút.""".format(hourrise = sunrise.hour, minrise = sunrise.minute,
                                                            weather=weather1,temperature=temperature1,
                                                            hourset = sunset.hour, minset = sunset.minute, 
                                                            temp = current_temperature, humidity = current_humidity)
            speak(content)
            root.update()
            time.sleep(2)
        else:
            speak("Không tìm thấy địa chỉ của bạn")
            root.update()
            time.sleep(2)
            current_weather()

def sleep_time(x):
    if x==1:
        time.sleep(1)
    elif x==2:
        time.sleep(2)
    elif x==3:
        time.sleep(3)
    elif x==4:
        time.sleep(4)
    elif x==5:
        time.sleep(5)
    elif x==6:
        time.sleep(10)
    else :
        time.sleep(7)

def func():
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    content="""
    Tôi có những chức năng sau đây:
    1.Chào hỏi
    2.Thông báo thời gian 
    3.Dự báo thời tiết 
    4.Thay đổi ảnh nền máy tính 
    5.Mở ứng dụng
    6.Mở website 
    7.Tìm kiếm thông tin trên google 
    8.Mở nhạc,phim trên youtube 
    9.Tạm biệt"""
    speak(content)
    root.update()
    time.sleep(23)

def color():
    mylist = ["#009999","black","green","grey","blue","orange","#cc0099","#00ff00","brown"]
    aa=random.choice(mylist)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here", background = aa)
    root.update()

def color1():
    mylist1 = ["yellow","#0000ff","white","#00ff00","black"]
    bb=random.choice(mylist1)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here",foreground = bb)
    root.update()

def info():
    mbox.showinfo("Giới thiệu", "-Nhấn Micro để bắt đầu thực hiện nói với AI.\n-Nhấn Làm mới để xóa toàn bộ cuộc trò chuyện.\n-Bạn có thể thay đổi màu nền hoặc màu chữ ngẫu nhiên.\n-Tiếng Pip xuất hiện là lúc AI đang nghe bạn nói.\n-Nói 'dừng lại' để tạm hoãn cuộc trò chuyện. \n-Nhấn Thoát để tắt chương trình.")

def r_set():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    text_area.delete("1.0", "1000000000.0")

def ham_main():
    r = speech_recognition.Recognizer() #nghe nguoi dung noi 
    you=""
    ai_brain=""
    while True:
        with speech_recognition.Microphone() as source:
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            print("AI:  Dang nghe ...")
            audio = r.listen(source, phrase_time_limit=6)
            print("AI:  ...")
        try:
            you = r.recognize_google(audio, language="vi-VN")
            print("\nYou: "+ you)   
            you = you.lower()
        except:
            ai_brain = "Tôi nghe không rõ. Bạn nói lại được không"
            print("\nAI: " + ai_brain)

        text_area.insert(INSERT,"You: "+you+"\n")
        root.update()

        if "xin chào" in you or "hello" in you:
            hello()
        elif "thời tiết" in you:
            current_weather()
        elif "ngày mấy" in you or "mấy giờ" in you or "thứ mấy" in you:
            get_time(you)
        
        elif "mở ứng dụng" in you:
            open_application(you)
        elif "mở website" in you:
            open_website(you)
        elif "mở google và tìm kiếm" in you:
            open_google_and_search(you)
        elif "nghe nhạc" in you or "xem phim" in you or "mở youtube" in you or "bài hát" in you:
            play_song()
        elif "thay đổi hình nền" in you:
            change_wallpaper()
        elif "gửi email" in you or "mail" in you or "gmail" in you:
            send_email()
        elif ("sáng hôm nay" in you and "môn" in you) or ("sáng ngày mai" in you and "môn" in you):
            subject2(you)
        elif ("sáng thứ" in you and "môn" in you) or ("sáng chủ nhật" in you and "môn" in you):
            subject_day2(you) 
        elif ("chiều hôm nay" in you and "môn" in you) or ("chiều ngày mai" in you and "môn" in you):
            subject3(you)
        elif ("chiều thứ" in you and "môn" in you) or ("chiều chủ nhật" in you and "môn" in you):
            subject_day3(you)
        elif ("tối hôm nay" in you and "môn" in you) or ("tối ngày mai" in you and "môn" in you):
            subject4(you)
        elif ("tối thứ" in you and "môn" in you) or ("tối chủ nhật" in you and "môn" in you):
            subject_day4(you)
        elif ("hôm nay" in you and "môn" in you) or ("ngày mai" in you and "môn" in you):
            subject(you)
        elif ("thứ" in you and "môn" in you) or ("chủ nhật" in you and "môn" in you):
            subject_day(you)
        
        elif "bạn có" in you and "chức năng" in you:
            func()
        elif "đổi màu nền" in you:
            color()
        elif "đổi màu chữ" in you:
            color1()
        elif "dừng lại" in you:
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            break
        elif "hẹn gặp lại" in you or "tạm biệt" in you or "cảm ơn" in you:
            ai_brain="Rất vui khi giúp đỡ bạn. Hẹn gặp lại bạn sau."
            speak(ai_brain)
            root.update()
            time.sleep(2)
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            exit()
        else:
            ai_brain = "Tôi không nghe rõ gì cả !!!"
            speak(ai_brain)
            root.update()
            time.sleep(2)

        text_area.insert(INSERT,"_____________________________________________")
        you=""

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent) 
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Trợ lí AI")
        self.style = Style()
        self.style.theme_use("default")
        
        scroll.pack(side=RIGHT, fill=Y)
        text_area.configure(yscrollcommand=scroll.set)
        text_area.pack(side=RIGHT)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        image3 = Image.open("image\\micro.png")
        image_3 = ImageTk.PhotoImage(image3)  
        label = Label(image=image_3)
        label.image = image_3
        label.place(x=430, y=477)

        closeButton = Button(self, text="Thoát",command = exit,width=10,fg="white", bg="#009999",bd=3)
        closeButton.pack(side=RIGHT, padx=11, pady=10)
        okButton = Button(self, text="Micro",command = ham_main,width=10,fg="white", bg="#009999",bd=3)
        okButton.pack(side=RIGHT, padx=11, pady=10)
        doimau = Button(self,text="Đổi màu nền",command = color,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        doimau = Button(self,text="Đổi màu chữ",command = color1,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        thongtin = Button(self,text="Giới thiệu",command = info,width=10,fg="white", bg="#009999",bd=3)
        thongtin.pack(side=RIGHT,padx=11, pady=10)
        lammoi = Button(self,text="Làm mới",command = r_set,width=10,fg="white", bg="#009999",bd=3)
        lammoi.pack(side=RIGHT,padx=11, pady=10)
    
        image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
        label1 = Label(self, image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

        l = Label(root, text='Lịch sử trò chuyện', fg='White', bg='blue')
        l.place(x = 750, y = 10, width=120, height=25)
        l1 = Label(root, text='Hình ảnh minh họa', fg='yellow', bg='black')
        l1.place(x = 250, y = 11, width=120, height=25)

root.geometry("1000x510+250+50")
root.resizable(False, False)
app = Example(root)
root.mainloop()


