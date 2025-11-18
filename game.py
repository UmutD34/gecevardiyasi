import streamlit as st
import webbrowser

# Sayfa yapılandırması
st.set_page_config(page_title="Sevgili Dilay", page_icon="💌", layout="centered")

# CSS stilleri
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .letter-box {
        background: #f9f7f4;
        padding: 40px 30px;
        border-radius: 10px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        font-family: Georgia, serif;
    }
    
    .date-text {
        text-align: right;
        color: #666;
        font-size: 14px;
        margin-bottom: 20px;
        font-style: italic;
    }
    
    .salutation-text {
        font-size: 22px;
        color: #333;
        margin-bottom: 25px;
        font-weight: bold;
    }
    
    .letter-text {
        color: #444;
        line-height: 1.8;
        font-size: 16px;
        text-align: justify;
    }
    
    .paragraph-space {
        margin-bottom: 20px;
    }
    
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        padding: 15px 40px !important;
        font-size: 18px !important;
        border-radius: 50px !important;
        width: 100% !important;
        font-family: Georgia, serif !important;
        margin-top: 20px !important;
    }
    
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

# Mektup başlangıcı
st.markdown('<div class="letter-box">', unsafe_allow_html=True)
st.markdown('<p class="date-text">17.11.2025</p>', unsafe_allow_html=True)
st.markdown('<p class="salutation-text">Sevgili Dilay,</p>', unsafe_allow_html=True)
st.markdown('<div class="letter-text">', unsafe_allow_html=True)

# Paragraflar
paragraphs = [
    "Bir gün kapattığım bu siteye gireceksin. Buraya girdiğinde, bazı acılarla girmiş olduğunu biliyorum. Bu acılar; hayattan, sağlıktan, aileden ya da geçmiş ilişkimizden kaynaklanıyor olabilir. Ne olursa olsun...",
    
    "O gün geldiğinde burada bir huzur bulabilmen için, seninle tanışmamızın yıl dönümü olan 24 Kasım'a bir hafta kala bu mektubu buraya bırakıyorum. Ben artık olmasam da sana iyi gelecektir.",
    
    "Senden bir karşılık görmek için değil, sana olan sevgimin bir gerekliliği olarak iyi olmanı istediğim için bu mektubu bırakıyorum. Ne zaman güçsüz hissedersen burada sana iyi gelecek bir mektubun olsun istedim.",
    
    "**Bugün**\n\nİnan bana, seni suçlamak, bir şeyleri zorlamak ya da seni kararından döndürmeye çalışmak için yazmıyorum. Sadece içimde biriken bir farkındalığı paylaşmak istiyorum.",
    
    "Bizim ilişkimizi geriye sardığımda, bugün bazı şeyleri daha net görüyorum: Sen duygularını güçlü yaşayan biriydin, sevgiyi derinden hissediyordun ama aynı zamanda o sevginin sana ağır geldiği anlar da vardı. Bu, senin kötü ya da yetersiz olmandan değildi; kendi içindeki yükler, geçmişte taşıdığın kırgınlıklar ve zaman zaman kimse tarafından tam anlaşılamama korkusu seni yoruyordu.",
    
    "Benim sevgim çoğu zaman sana iyi geliyordu fakat bazı anlarda seni korkuttu. Çünkü karşılık vermek zorundaymışsın gibi hissettin. Sanki bir adım geri çekildiğinde sevgi azalacakmış gibi kaygı duydun. Bu yüzden kaçtığın anlar oldu. Bu bir tercih değildi; içgüdüsel bir savunmaydı.",
    
    "Ben sevgimi verirken iyi etmek, güçlendirmek istedim. Ama belki de bazı anlarda fazlası oldu. Ben de o dönem bazı şeyleri yanlış yorumladım. Seni daha çok sarınca iyileşirsin sandım, oysa bazen senin nefes almaya ihtiyacın vardı. Bunları şimdi fark edebiliyorum.",
    
    "O günlerde ikimiz de kendi eksiklerimizle savaşıyorduk. Niyetim hep güzeldi ama herkesin kaldırabileceği yük farklıdır. Ben seni gerçekten bir insan olarak sevdim. Eksiklerinle, güçlü yanlarınla, bazen içine kapanmanla... Ve bugün şunu da görüyorum: Ben de iyi bir insanım. Severken elimden geleni yaptım, karşılık beklemeden emek verdim. Hiçbir anında seni yormak için değil, yanında olmak için çabaladım.",
    
    "Bunu artık kendime yük etmiyorum. Sevmek benim suçum değildi. Niyetim temizdi. Sana kızgın değilim, kırgın da değilim. Hatta bugün, beni değil kendini korumaya çalıştığını hissedebiliyorum. Bu ilişki senin için sadece bir 'sevgi' meselesi değildi; kendiyle olan mücadeleni de içine katıyordu. Bu yüzden ağırlık hissettin, bu yüzden yoruldun. Bunu anlıyorum.",
    
    "Bu mesajı yazmamın sebebi seni geri döndürmek değil. Bir gün geçmişe dönüp kendini suçlamanı istemiyorum. Çünkü bu hikâyede sen kötü biri değildin, ben de değilim. Sadece farklı yaralarla sevmeye çalışan iki insandık. Sen elinden geleni yaptın, ben de yaptım. Bazen iki iyi niyet, bir ilişkiyi ayakta tutmaya yetmiyor.",
    
    "Sana teşekkür ederim. Paylaştığımız her iyi an için, büyüdüğüm her duygu için, kalbime bıraktığın her iz için. Bunlar bende güzel bir yer olarak kalacak. Senin de kendi yolunda huzuru bulmanı dilerim. Sadece seni anladığımı bil istedim.",
    
    "Bana yaşattığın güzel anlar için teşekkür ederim. Bende güzel bir yerin olacak. Umarım sen de kendi yolunda huzuru bulursun. Zor zamanlarında şarkılarını dinle; sana güç ve huzur vereceklerdir."
]

for i, para in enumerate(paragraphs):
    st.markdown(f'<p class="paragraph-space">{para}</p>', unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# Müzik butonu
st.markdown('<br>', unsafe_allow_html=True)
if st.button("♪ Hatırla Beni ♪"):
    st.markdown("""
        <meta http-equiv="refresh" content="0; url=https://www.youtube.com/watch?v=9bcO0yIUNkQ&list=RD9bcO0yIUNkQ&start_radio=1" />
    """, unsafe_allow_html=True)
    st.link_button("🎵 Müziği Dinle", "https://www.youtube.com/watch?v=9bcO0yIUNkQ&list=RD9bcO0yIUNkQ&start_radio=1")
