print("Kayıt Olma Ekranına Hoş Geldiniz.".upper())

kullaniciid = str(input("Kullanıcı İD'nizi Giriniz:"))
kullanicisifre = str(input("Kullanıcı Şifrenizi Giriniz:"))

print("Kaydınız Tamamlandı. Lütfen sizi doğrulayabilmemiz için tekrar giriş yapın.")

uid = str(input("Varolan Kullanıcı İD'nizi Giriniz:"))
usi = str(input("Varolan Kullanıcı Şifrenizi Giriniz:"))

if uid != kullaniciid or kullanicisifre != usi:
    print("Kullanıcı Adınızı veya Şifrenizi Yanlış Girdiniz, Tekrar Giriş Yapın.")
    uid = str(input("Varolan Kullanıcı İD'nizi Giriniz:"))
    usi = str(input("Varolan Kullanıcı Şifrenizi Giriniz:"))
    if uid != kullaniciid or kullanicisifre != usi:
        print("Kullanıcı Adınızı veya Şifrenizi Yanlış Girdiniz, Tekrar Giriş Yapın.")
        uid = str(input("Varolan Kullanıcı İD'nizi Giriniz:"))
        usi = str(input("Varolan Kullanıcı Şifrenizi Giriniz:"))
        if uid == kullaniciid and kullanicisifre == usi:
            print("Sisteme Girişin Başarılı Rakılardan Banada Ayır.")
        else:
            print("Çok fazla hatalı giriş denemesinde bulundun daha sonra tekrar gel.")

else:
    print("Sisteme Girişin Başarılı Rakılardan Banada Ayır.")