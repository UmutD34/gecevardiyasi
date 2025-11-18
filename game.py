import os

html_icerigi = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sevgili Dilay'a Mektup</title>
    <style>
        /* Mobil Dostu ve Duygusal Tasarım */
        body {
            font-family: 'Georgia', serif;
            background-color: #1c1c1c; /* Koyu arka plan */
            color: #dcdcdc; /* Açık metin */
            padding: 10px;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }

        .mektup-container {
            width: 95%;
            max-width: 600px; /* Mobil ve tablet için uygun maksimum genişlik */
            margin-top: 20px;
            padding: 20px;
            background-color: #2a2a2a;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.7);
        }

        /* Kaydırma Efekti (Akan Yazı) */
        .mektup-icerik {
            height: 65vh; /* Mobil ekranın %65'i kadar yükseklik */
            overflow-y: scroll; /* Dikey kaydırmayı etkinleştirir */
            line-height: 1.6;
            white-space: pre-wrap; /* Satır sonlarını korur ve metni sarar */
            font-size: 16px;
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #444;
            border-radius: 4px;
        }

        .tarih {
            font-style: italic;
            text-align: right;
            display: block;
            margin-bottom: 15px;
            color: #bbb;
        }

        .selamlama {
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 15px;
            display: block;
            color: #e5e5e5;
        }

        .imza {
            text-align: right;
            font-style: italic;
            margin-top: 20px;
            display: block;
        }

        /* Buton Stili */
        #playButton {
            width: 100%;
            padding: 15px;
            background-color: #c0392b; /* Kırmızımsı kontrast renk */
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s;
            font-weight: bold;
            text-transform: uppercase;
        }

        #playButton:hover {
            background-color: #e74c3c;
        }
    </style>
</head>
<body>

<div class="mektup-container">
    <div class="mektup-icerik" id="mektupIcerik">
        <span class="tarih">17.11.2025</span>
        <span class="selamlama">Sevgili Dilay,</span>
        
        Bir gün kapattığım bu siteye gireceksin. Buraya girdiğinde, bazı acılarla girmiş olduğunu biliyorum. Bu acılar; hayattan, sağlıktan, aileden ya da geçmiş ilişkimizden kaynaklanıyor olabilir. Ne olursa olsun...

        O gün geldiğinde burada bir huzur bulabilmen için, seninle tanışmamızın yıl dönümü olan 24 Kasım’a bir hafta kala bu mektubu buraya bırakıyorum. Ben artık olmasam da sana iyi gelecektir.
        
        Senden bir karşılık görmek için değil, sana olan sevgimin bir gerekliliği olarak iyi olmanı istediğim için bu mektubu bırakıyorum. Ne zaman güçsüz hissedersen burada sana iyi gelecek bir mektubun olsun istedim.

        **Bugün**

        İnan bana, seni suçlamak, bir şeyleri zorlamak ya da seni kararından döndürmeye çalışmak için yazmıyorum. Sadece içimde biriken bir farkındalığı paylaşmak istiyorum.

        Bizim ilişkimizi geriye sardığımda, bugün bazı şeyleri daha net görüyorum:

        Sen duygularını güçlü yaşayan biriydin, sevgiyi derinden hissediyordun ama aynı zamanda o sevginin sana ağır geldiği anlar da vardı. Bu, senin kötü ya da yetersiz olmandan değildi; kendi içindeki yükler, geçmişte taşıdığın kırgınlıklar ve zaman zaman kimse tarafından tam anlaşılamama korkusu seni yoruyordu.
        
        Benim sevgim çoğu zaman sana iyi geliyordu fakat bazı anlarda seni korkuttu. Çünkü karşılık vermek zorundaymışsın gibi hissettin. Sanki bir adım geri çekildiğinde sevgi azalacakmış gibi kaygı duydun. Bu yüzden kaçtığın anlar oldu. Bu bir tercih değildi; içgüdüsel bir savunmaydı.
        
        Ben sevgimi verirken iyi etmek, güçlendirmek istedim. Ama belki de bazı anlarda fazlası oldu. Ben de o dönem bazı şeyleri yanlış yorumladım. Seni daha çok sarınca iyileşirsin sandım, oysa bazen senin nefes almaya ihtiyacın vardı. Bunları şimdi fark edebiliyorum.
        
        O günlerde ikimiz de kendi eksiklerimizle savaşıyorduk. Niyetim hep güzeldi ama herkesin kaldırabileceği yük farklıdır.
        
        Ben seni gerçekten bir insan olarak sevdim. Eksiklerinle, güçlü yanlarınla, bazen içine kapanmanla... Ve bugün şunu da görüyorum: Ben de iyi bir insanım. Severken elimden geleni yaptım, karşılık beklemeden emek verdim. Hiçbir anında seni yormak için değil, yanında olmak için çabaladım.
        
        Bunu artık kendime yük etmiyorum. Sevmek benim suçum değildi. Niyetim temizdi.
        
        Sana kızgın değilim, kırgın da değilim. Hatta bugün, beni değil kendini korumaya çalıştığını hissedebiliyorum. Bu ilişki senin için sadece bir ‘sevgi’ meselesi değildi; kendiyle olan mücadelesini de içine katıyordu. Bu yüzden ağırlık hissettin, bu yüzden yoruldun. Bunu anlıyorum.
        
        Bu mesajı yazmamın sebebi seni geri döndürmek değil. Bir gün geçmişe dönüp kendini suçlamanı istemiyorum.
        
        Çünkü bu hikâyede sen kötü biri değildin, ben de değilim. Sadece farklı yaralarla sevmeye çalışan iki insandık. Sen elinden geleni yaptın, ben de yaptım. Bazen iki iyi niyet, bir ilişkiyi ayakta tutmaya yetmiyor.
        
        Sana teşekkür ederim. Paylaştığımız her iyi an için, büyüdüğüm her duygu için, kalbime bıraktığın her iz için. Bunlar bende güzel bir yer olarak kalacak.
        
        Senin de kendi yolunda huzuru bulmanı dilerim. Sadece seni anladığımı bil istedim.
        
        Bana yaşattığın güzel anlar için teşekkür ederim. Bende güzel bir yerin olacak. Umarım sen de kendi yolunda huzuru bulursun. Zor zamanlarında şarkılarını dinle; sana güç ve huzur vereceklerdir.
        
        <span class="imza">Sevgilerle.</span>
    </div>
    
    <button id="playButton" onclick="openMusic()">Hatırla beni...</button>

</div>

<script>
    function openMusic() {
        var musicUrl = "https://www.youtube.com/watch?v=9bcO0yIUNkQ&list=RD9bcO0yIUNkQ&start_radio=1";
        window.open(musicUrl, '_blank');
    }
</script>

</body>
</html>
"""

# HTML dosyasını oluştur ve kaydet
dosya_adi = "Dilaya_Mektup.html"
try:
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(html_icerigi)
    print(f"Mektup başarıyla oluşturuldu: {os.path.abspath(dosya_adi)}")
    print("Bu dosyayı herhangi bir tarayıcıda (mobil dahil) açarak mektubu görebilirsiniz.")
except Exception as e:
    print(f"Dosya yazılırken bir hata oluştu: {e}")
