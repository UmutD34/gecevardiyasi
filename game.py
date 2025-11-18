import streamlit as st
import streamlit.components.v1 as components

# Sayfa yapılandırması
st.set_page_config(page_title="Sevgili Dilay", page_icon="💌", layout="wide")

# HTML içeriği
html_code = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .letter-container {
            background: #f9f7f4;
            max-width: 600px;
            width: 100%;
            padding: 40px 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            border-radius: 10px;
            position: relative;
            overflow: hidden;
        }

        .letter-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 8px;
            background: linear-gradient(90deg, #667eea, #764ba2);
        }

        .date {
            text-align: right;
            color: #666;
            font-size: 14px;
            margin-bottom: 20px;
            font-style: italic;
        }

        .salutation {
            font-size: 20px;
            color: #333;
            margin-bottom: 25px;
            font-weight: bold;
        }

        .content {
            color: #444;
            line-height: 1.8;
            font-size: 16px;
            text-align: justify;
            max-height: 60vh;
            overflow-y: auto;
            padding-right: 10px;
            margin-bottom: 30px;
        }

        .content::-webkit-scrollbar {
            width: 8px;
        }

        .content::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }

        .content::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 10px;
        }

        .content::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        .paragraph {
            margin-bottom: 20px;
            opacity: 0;
            animation: fadeIn 1s ease-in forwards;
        }

        .paragraph:nth-child(1) { animation-delay: 0.2s; }
        .paragraph:nth-child(2) { animation-delay: 0.4s; }
        .paragraph:nth-child(3) { animation-delay: 0.6s; }
        .paragraph:nth-child(4) { animation-delay: 0.8s; }
        .paragraph:nth-child(5) { animation-delay: 1s; }
        .paragraph:nth-child(6) { animation-delay: 1.2s; }
        .paragraph:nth-child(7) { animation-delay: 1.4s; }
        .paragraph:nth-child(8) { animation-delay: 1.6s; }
        .paragraph:nth-child(9) { animation-delay: 1.8s; }
        .paragraph:nth-child(10) { animation-delay: 2s; }
        .paragraph:nth-child(11) { animation-delay: 2.2s; }
        .paragraph:nth-child(12) { animation-delay: 2.4s; }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .button-container {
            text-align: center;
            margin-top: 30px;
            opacity: 0;
            animation: fadeIn 1s ease-in 2.6s forwards;
        }

        .music-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 18px;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            font-family: 'Georgia', serif;
        }

        .music-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }

        .music-button:active {
            transform: translateY(0);
        }

        @media (max-width: 600px) {
            .letter-container {
                padding: 30px 20px;
            }

            .content {
                font-size: 15px;
            }

            .salutation {
                font-size: 18px;
            }
        }
    </style>
</head>
<body>
    <div class="letter-container">
        <div class="date">17.11.2025</div>
        <div class="salutation">Sevgili Dilay,</div>
        
        <div class="content">
            <div class="paragraph">
                Bir gün kapattığım bu siteye gireceksin. Buraya girdiğinde, bazı acılarla girmiş olduğunu biliyorum. Bu acılar; hayattan, sağlıktan, aileden ya da geçmiş ilişkimizden kaynaklanıyor olabilir. Ne olursa olsun...
            </div>
            
            <div class="paragraph">
                O gün geldiğinde burada bir huzur bulabilmen için, seninle tanışmamızın yıl dönümü olan 24 Kasım'a bir hafta kala bu mektubu buraya bırakıyorum. Ben artık olmasam da sana iyi gelecektir.
            </div>
            
            <div class="paragraph">
                Senden bir karşılık görmek için değil, sana olan sevgimin bir gerekliliği olarak iyi olmanı istediğim için bu mektubu bırakıyorum. Ne zaman güçsüz hissedersen burada sana iyi gelecek bir mektubun olsun istedim.
            </div>
            
            <div class="paragraph">
                <strong>Bugün</strong><br>
                İnan bana, seni suçlamak, bir şeyleri zorlamak ya da seni kararından döndürmeye çalışmak için yazmıyorum. Sadece içimde biriken bir farkındalığı paylaşmak istiyorum.
            </div>
            
            <div class="paragraph">
                Bizim ilişkimizi geriye sardığımda, bugün bazı şeyleri daha net görüyorum: Sen duygularını güçlü yaşayan biriydin, sevgiyi derinden hissediyordun ama aynı zamanda o sevginin sana ağır geldiği anlar da vardı. Bu, senin kötü ya da yetersiz olmandan değildi; kendi içindeki yükler, geçmişte taşıdığın kırgınlıklar ve zaman zaman kimse tarafından tam anlaşılamama korkusu seni yoruyordu.
            </div>
            
            <div class="paragraph">
                Benim sevgim çoğu zaman sana iyi geliyordu fakat bazı anlarda seni korkuttu. Çünkü karşılık vermek zorundaymışsın gibi hissettin. Sanki bir adım geri çekildiğinde sevgi azalacakmış gibi kaygı duydun. Bu yüzden kaçtığın anlar oldu. Bu bir tercih değildi; içgüdüsel bir savunmaydı.
            </div>
            
            <div class="paragraph">
                Ben sevgimi verirken iyi etmek, güçlendirmek istedim. Ama belki de bazı anlarda fazlası oldu. Ben de o dönem bazı şeyleri yanlış yorumladım. Seni daha çok sarınca iyileşirsin sandım, oysa bazen senin nefes almaya ihtiyacın vardı. Bunları şimdi fark edebiliyorum.
            </div>
            
            <div class="paragraph">
                O günlerde ikimiz de kendi eksiklerimizle savaşıyorduk. Niyetim hep güzeldi ama herkesin kaldırabileceği yük farklıdır. Ben seni gerçekten bir insan olarak sevdim. Eksiklerinle, güçlü yanlarınla, bazen içine kapanmanla... Ve bugün şunu da görüyorum: Ben de iyi bir insanım. Severken elimden geleni yaptım, karşılık beklemeden emek verdim. Hiçbir anında seni yormak için değil, yanında olmak için çabaladım.
            </div>
            
            <div class="paragraph">
                Bunu artık kendime yük etmiyorum. Sevmek benim suçum değildi. Niyetim temizdi. Sana kızgın değilim, kırgın da değilim. Hatta bugün, beni değil kendini korumaya çalıştığını hissedebiliyorum. Bu ilişki senin için sadece bir 'sevgi' meselesi değildi; kendiyle olan mücadeleni de içine katıyordu. Bu yüzden ağırlık hissettin, bu yüzden yoruldun. Bunu anlıyorum.
            </div>
            
            <div class="paragraph">
                Bu mesajı yazmamın sebebi seni geri döndürmek değil. Bir gün geçmişe dönüp kendini suçlamanı istemiyorum. Çünkü bu hikâyede sen kötü biri değildin, ben de değilim. Sadece farklı yaralarla sevmeye çalışan iki insandık. Sen elinden geleni yaptın, ben de yaptım. Bazen iki iyi niyet, bir ilişkiyi ayakta tutmaya yetmiyor.
            </div>
            
            <div class="paragraph">
                Sana teşekkür ederim. Paylaştığımız her iyi an için, büyüdüğüm her duygu için, kalbime bıraktığın her iz için. Bunlar bende güzel bir yer olarak kalacak. Senin de kendi yolunda huzuru bulmanı dilerim. Sadece seni anladığımı bil istedim.
            </div>
            
            <div class="paragraph">
                Bana yaşattığın güzel anlar için teşekkür ederim. Bende güzel bir yerin olacak. Umarım sen de kendi yolunda huzuru bulursun. Zor zamanlarında şarkılarını dinle; sana güç ve huzur vereceklerdir.
            </div>
        </div>
        
        <div class="button-container">
            <button class="music-button" onclick="playMusic()">Hatırla Beni ♪</button>
        </div>
    </div>

    <script>
        function playMusic() {
            window.open('https://www.youtube.com/watch?v=9bcO0yIUNkQ&list=RD9bcO0yIUNkQ&start_radio=1', '_blank');
        }
    </script>
</body>
</html>
"""

# HTML'i render et
components.html(html_code, height=800, scrolling=True)
