import streamlit as st

# Sayfa yapılandırması
st.set_page_config(page_title="Sevgili Dilay", page_icon="💌", layout="centered")

# CSS stilleri
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 700px;
    }
    
    .letter-container {
        background: #f9f7f4;
        padding: 40px 30px;
        border-radius: 10px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        font-family: Georgia, serif;
        border-top: 8px solid #667eea;
    }
    
    .date-style {
        text-align: right;
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
        font-style: italic;
    }
    
    .salutation-style {
        font-size: 22px;
        color: #333;
        margin-bottom: 25px;
        font-weight: bold;
    }
    
    .content-style {
        color: #444;
        line-height: 1.8;
        font-size: 16px;
        text-align: justify;
    }
    
    .content-style p {
        margin-bottom: 20px;
    }
    
    [data-testid="stButton"] button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 18px;
        border-radius: 50px;
        width: 100%;
        font-family: Georgia, serif;
        font-weight: bold;
        margin-top: 20px;
        transition: all 0.3s ease;
    }
    
    [data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Mektup içeriği
letter_content = """
<div class="letter-container">
    <div class="date-style">17.11.2025</div>
    <div class="salutation-style">Sevgili Dilay,</div>
    
    <div class="content-style">
        <p>Bir gün kapattığım bu siteye gireceksin. Buraya girdiğinde, bazı acılarla girmiş olduğunu biliyorum. Bu acılar; hayattan, sağlıktan, aileden ya da geçmiş ilişkimizden kaynaklanıyor olabilir. Ne olursa olsun...</p>
        
        <p>O gün geldiğinde burada bir huzur bulabilmen için, seninle tanışmamızın yıl dönümü olan 24 Kasım'a bir hafta kala bu mektubu buraya bırakıyorum. Ben artık olmasam da sana iyi gelecektir.</p>
        
        <p>Senden bir karşılık görmek için değil, sana olan sevgimin bir gerekliliği olarak iyi olmanı istediğim için bu mektubu bırakıyorum. Ne zaman güçsüz hissedersen burada sana iyi gelecek bir mektubun olsun istedim.</p>
        
        <p><strong>Bugün</strong><br>
        İnan bana, seni suçlamak, bir şeyleri zorlamak ya da seni kararından döndürmeye çalışmak için yazmıyorum. Sadece içimde biriken bir farkındalığı paylaşmak istiyorum.</p>
        
        <p>Bizim ilişkimizi geriye sardığımda, bugün bazı şeyleri daha net görüyorum: Sen duygularını güçlü yaşayan biriydin, sevgiyi derinden hissediyordun ama aynı zamanda o sevginin sana ağır geldiği anlar da vardı. Bu, senin kötü ya da yetersiz olmandan değildi; kendi içindeki yükler, geçmişte taşıdığın kırgınlıklar ve zaman zaman kimse tarafından tam anlaşılamama korkusu seni yoruyordu.</p>
        
        <p>Benim sevgim çoğu zaman sana iyi geliyordu fakat bazı anlarda seni korkuttu. Çünkü karşılık vermek zorundaymışsın gibi hissettin. Sanki bir adım geri çekildiğinde sevgi azalacakmış gibi kaygı duydun. Bu yüzden kaçtığın anlar oldu. Bu bir tercih değildi; içgüdüsel bir savunmaydı.</p>
        
        <p>Ben sevgimi verirken iyi etmek, güçlendirmek istedim. Ama belki de bazı anlarda fazlası oldu. Ben de o dönem bazı şeyleri yanlış yorumladım. Seni daha çok sarınca iyileşirsin sandım, oysa bazen senin nefes almaya ihtiyacın vardı. Bunları şimdi fark edebiliyorum.</p>
        
        <p>O günlerde ikimiz de kendi eksiklerimizle savaşıyorduk. Niyetim hep güzeldi ama herkesin kaldırabileceği yük farklıdır. Ben seni gerçekten bir insan olarak sevdim. Eksiklerinle, güçlü yanlarınla, bazen içine kapanmanla... Ve bugün şunu da görüyorum: Ben de iyi bir insanım. Severken elimden geleni yaptım, karşılık beklemeden emek verdim. Hiçbir anında seni yormak için değil, yanında olmak için çabaladım.</p>
        
        <p>Bunu artık kendime yük etmiyorum. Sevmek benim suçum değildi. Niyetim temizdi. Sana kızgın değilim, kırgın da değilim. Hatta bugün, beni değil kendini korumaya çalıştığını hissedebiliyorum. Bu ilişki senin için sadece bir 'sevgi' meselesi değildi; kendiyle olan mücadeleni de içine katıyordu. Bu yüzden ağırlık hissettin, bu yüzden yoruldun. Bunu anlıyorum.</p>
        
        <p>Bu mesajı yazmamın sebebi seni geri döndürmek değil. Bir gün geçmişe dönüp kendini suçlamanı istemiyorum. Çünkü bu hikâyede sen kötü biri değildin, ben de değilim. Sadece farklı yaralarla sevmeye çalışan iki insandık. Sen elinden geleni yaptın, ben de yaptım. Bazen iki iyi niyet, bir ilişkiyi ayakta tutmaya yetmiyor.</p>
        
        <p>Sana teşekkür ederim. Paylaştığımız her iyi an için, büyüdüğüm her duygu için, kalbime bıraktığın her iz için. Bunlar bende güzel bir yer olarak kalacak. Senin de kendi yolunda huzuru bulmanı dilerim. Sadece seni anladığımı bil istedim.</p>
        
        <p>Bana yaşattığın güzel anlar için teşekkür ederim. Bende güzel bir yerin olacak. Umarım sen de kendi yolunda huzuru bulursun. Zor zamanlarında şarkılarını dinle; sana güç ve huzur vereceklerdir.</p>
    </div>
</div>
"""

st.markdown(letter_content, unsafe_allow_html=True)

# Müzik butonu
if st.button("♪ Hatırla Beni ♪"):
    st.markdown(
        '<meta http-equiv="refresh" content="0; url=https://www.youtube.com/watch?v=9bcO0yIUNkQ" />',
        unsafe_allow_html=True
    )
    st.link_button("🎵 Müziği Açmak İçin Tıkla", "https://www.youtube.com/watch?v=9bcO0yIUNkQ")
