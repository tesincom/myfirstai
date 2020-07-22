import os
import random
import webbrowser

i = 1
while i == 1:

    ismi = "Esse"
    print("Buyrun Ben {}?".format(ismi))

    mtn1e = input()

    if mtn1e == "Adını Değiştirmek İstiyorum":
        ismi = input("Adımın ne olmasını istersiniz?:")
        cvp = input("İsmim artık {}. Nasıl Yardımcı Olabilirim?".format(ismi))

    if mtn1e == "Adın Ne?":
        print("Adım {}".format(ismi))

    if mtn1e == "Oyun Önerisinde Bulun":
        oyun_listesi = ["CS:GO'yu denemelisin.", "Zula'yı Denemelisin.", "League of Legends'i Denemelisin."]
        print(random.choice(oyun_listesi))

    if mtn1e != "sajkdsabevewmaksiyonlarkaenyumrukemelkem":
        gili = "https://github.com/tesincom/"
        print("Geliştirici Topluluğumuza {} katılmaya ne dersin?".format(gili))
        mhmt = input("Katılmak İstiyorsanız Evet Yazın.")
        if mhmt == "Evet":
            webbrowser.open("https://github.com/tesincom/")

    if mtn1e == "İnstagram sayfasını ziyaret et":
        insta = input("Hangi İnstagram Sayfasını Ziyaret Etmek İstersiniz: @ koymadan kullanıcı adınızı belirtiniz")
        webbrowser.open('https://instagram.com/{}'.format(insta))

    if mtn1e == "Youtube Kanalı'nı Ziyaret Et":
        ytb = input("Hangi Youtube Kanalını Ziyaret Etmek İstersiniz: URL'deki ismini belirtiniz")
        webbrowser.open('https://youtube.com/{}'.format(ytb))

    if mtn1e == "Fatih Kalemi Aç":
        print("Fatih Kalem Açılıyor...")
        os.startfile("C:\Program Files (x86)\Fatih Kalem\Fatih Kalem.exe")
