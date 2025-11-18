<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dilay'a Mektup</title>
    <style>
        /* Mobil Uyumlu ve Güvenilir Stil */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f0f0; /* Açık Gri Arka Plan */
            color: #333; /* Koyu Metin */
            padding: 15px;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .mektup-container {
            width: 100%;
            max-width: 500px; /* Mobil Ekran için maksimum genişlik */
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        /* Kaydırılabilir Metin Alanı (Akan Yazı) */
        .mektup-icerik {
            height: 70vh; /* Ekran yüksekliğinin %70'ini kapla */
            overflow-y: scroll; /* Dikey kaydırmayı etkinleştir */
            line-height: 1.6;
            font-size: 16px;
            margin-bottom: 20px;
            padding-right: 10px; /* Kaydırma çubuğu için boşluk */
            white-space: pre-wrap; /* Satır sonlarını koru */
        }

        .tarih {
            font-style: italic;
            text-align: right;
            display: block;
            margin-bottom: 10px;
        }

        .selamlama {
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 15px;
            display: block;
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
            background-color: #e74c3c; /* Kırmızı Buton */
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 18px;
            cursor: pointer;
            margin-top: 15px;
            font-weight: bold;
            transition: background-color 0.2s;
        }

        #playButton:hover {
            background-color: #c0392b;
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
        
        <div class="imza">Sevgilerle.</div>
    </div>
    
    <button id="playButton" onclick="openMusic()">Hatırla beni...</button>

</div>

<script>
    function openMusic() {
        var musicUrl = "https://www.youtube.com/watch?v=9bcO0yIUNkQ&list=RD9bcO0yIUNkQ&start_radio=1";
        // Müzik linkini yeni sekmede açar
        window.open(musicUrl, '_blank');
    }
</script>

</body>
</html>
