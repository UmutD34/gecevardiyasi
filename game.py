import streamlit as st

# Sayfa yapılandırması
st.set_page_config(page_title="Sevgili Dilay", page_icon="💌", layout="centered")

# CSS stilleri
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .letter-container {
        background: #f9f7f4;
        padding: 40px 30px;
        border-radius: 10px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        margin: 20px auto;
        max-width: 600px;
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
        font-family: Georgia, serif;
    }
    
    .content {
        color: #444;
        line-height: 1.8;
        font-size: 16px;
        text-align: justify;
        font-family: Georgia, serif;
    }
    
    .paragraph {
        margin-bottom: 20px;
    }
    
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 18px;
        border-radius: 50px;
        width: 100%;
        font-family: Georgia, serif;
    }
    
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Mektup içeriği
st.markdown("""
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
</div>
""", unsafe_allow_html=True)

# Müzik butonu
if st.button("♪ Hatırla Beni ♪"):
    st.markdown("""
        <script>
            window.open('https://www.youtube.com/watch?v=9bcO0yIUNkQ&list=RD9bcO0yIUNkQ&start_radio=1', '_blank');
        </script>
    """, unsafe_allow_html=True)
    st.success("Müzik yeni sekmede açılıyor...")
