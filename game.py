import streamlit as st

# ----------------------
# State Yönetimi
# ----------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
    st.session_state.section_step = 0
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.score = 0

# ----------------------
# Yardımcı Fonksiyonlar
# ----------------------
def restart_game():
    st.session_state.stage = 'intro'
    st.session_state.section_step = 0
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.score = 0


def next_event():
    st.session_state.section_step += 1
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    # 3 macera sonra sonraki bölüme geç
    if st.session_state.section_step >= 3:
        order = ['intro', 'gece_mail', 'ogrenciler', 'veliler', 'fare', 'su', 'asansor', 'lavabo', 'finished']
        idx = order.index(st.session_state.stage)
        st.session_state.stage = order[idx + 1]
        st.session_state.section_step = 0


def render_bars():
    st.progress(st.session_state.player_health / 100, text="Can")
    st.progress(st.session_state.enemy_health / 100, text="Düşman Can")

# ----------------------
# Uygulama Başlığı
# ----------------------
st.title("🌻 DİLAY'I KORU GECE VARDİYASI EDITON BY UMUTD34 ")
st.write(f"**Skor:** {st.session_state.score}")
st.write("---")
stage = st.session_state.stage

# ----------------------
# Intro
# ----------------------
if stage == 'intro':
    st.write("**Gece vardiyasına hoş geldiniz!**\n\nBu gece vardiyasını yenmek için yeterince cesur musun? 🤔")
    c1, c2 = st.columns(2)
    if c1.button("Evet, hazırım! 💪"):
        st.session_state.stage = 'gece_mail'
        st.session_state.section_step = 0
    if c2.button("Hayır, korkuyorum 😱"):
        st.error("Korkuya yenik düştün! Oyunu kaybettin. 😔")
        if st.button("Tekrar Dene"):
            restart_game()

# ----------------------
# Dinamik Bölüm İşleyici
# ----------------------
else:
    render_bars()
    step = st.session_state.section_step

    # Bölüm 1: Mail Saldırısı
    if stage == 'gece_mail':
        st.subheader(f"Bölüm 1: Mail Saldırısı (Adım {step+1}/3)")
        if step == 0:
            st.write("Dilay'ın gelen kutusu patlamak üzere! İlk hamle? 📧")
            c1, c2 = st.columns(2)
            if c1.button("Spam filtresi uygula 🛡️"):
                st.success("Spam filtresi canavarı engelledi! 🎉")
                st.session_state.score += 10
                next_event()
            if c2.button("Hepsini oku 📖"):
                st.error("Okurken kaosa davetiye çıkardın, kaybettin.")
                st.session_state.player_health = 0
        elif step == 1:
            st.write("CC: Herkes faciası başladı! Nasıl durdurursun? 🔄")
            c1, c2 = st.columns(2)
            if c1.button("Yanıtları kapat🔇"):
                st.success("Sessiz spam başarıyla filtrelendi.")
                st.session_state.score += 15
                next_event()
            if c2.button("Cevabı okula gönder🏫"):
                st.error("Yanlış okulu etiketledin, kaybettin.")
                st.session_state.player_health = 0
        else:
            st.write("Son aşama: Mail saldırısına son hamle? 🚀")
            c1, c2 = st.columns(2)
            if c1.button("Hepsini arşive at📂"):
                st.success("Mail faciasını durdurdun! 🏆")
                st.session_state.score += 20
                next_event()
            if c2.button("Hemen sil🗑️"):
                st.error("Yanlışlıkla önemli maili sildin, kaybettin.")
                st.session_state.player_health = 0

    # Bölüm 2: Sorunlu Öğrenciler
    elif stage == 'ogrenciler':
        st.subheader(f"Bölüm 2: Sorunlu Öğrenciler (Adım {step+1}/3)")
        if step == 0:
            st.write("Öğrenciler dersin ortasında dans etmeye başladı! Ne yaparsın? 💃🕺")
            c1, c2 = st.columns(2)
            if c1.button("Zil çal🔔"):
                st.success("Zil öğeleri susturdu! 📚")
                st.session_state.score += 8
                next_event()
            if c2.button("Onlara DJ ol🎧"):
                st.error("Dansa daha çok başladılar, kaybettin.")
                st.session_state.player_health = 0
        elif step == 1:
            st.write("Masanın altından hayalet sesleri geliyor! Ne yaparsın? 👻")
            c1, c2 = st.columns(2)
            if c1.button("Maske tak🦹‍♂️"):
                st.success("Hayaletleri korkuttun! 👻➡️🏃")
                st.session_state.score += 12
                next_event()
            if c2.button("Şarkı söyle🎤"):
                st.error("Hayaletler konsere katıldı, kaybettin.")
                st.session_state.player_health = 0
        else:
            st.write("Son adım: Motivasyon konuşması yap! 🎓")
            c1, c2 = st.columns(2)
            if c1.button("Konuşmayı başlat📢"):
                st.success("Öğrenciler motive oldu! 🌟")
                st.session_state.score += 15
                next_event()
            if c2.button("Selfie iste🤳"):
                st.error("Selfie süreci sınıfı böldü, kaybettin.")
                st.session_state.player_health = 0

    # Bölüm 3: Sorunlu Veliler
    elif stage == 'veliler':
        st.subheader(f"Bölüm 3: Sorunlu Veliler (Adım {step+1}/3)")
        if step == 0:
            st.write("Veliler öğretmeni sorguluyor! İlk hamle? 🧔👩‍🦰")
            c1, c2 = st.columns(2)
            if c1.button("Çay daveti ☕"):
                st.success("Çay molası herkesi rahatlattı.")
                st.session_state.score += 10
                next_event()
            if c2.button("Sözlü sınav yap✏️"):
                st.error("Veliler notu beğenmedi, kaybettin.")
                st.session_state.player_health = 0
        elif step == 1:
            st.write("Veliler Whatsapp'ta grup kurdu! Ne yaparsın? 📱")
            c1, c2 = st.columns(2)
            if c1.button("Sessize al🔇"):
                st.success("Grup suskun kaldı.")
                st.session_state.score += 12
                next_event()
            if c2.button("GIF gönder🎬"):
                st.error("Yanlış GIF, ortam gerildi, kaybettin.")
                st.session_state.player_health = 0
        else:
            st.write("Son adım: Velilere hediye seç! 🎁")
            c1, c2 = st.columns(2)
            if c1.button("Kalem seti al✏️"):
                st.success("Hediye çok beğenildi! 🎉")
                st.session_state.score += 15
                next_event()
            if c2.button("Çiçek gönder🌸"):
                st.error("Alerjisi çıktı, kaybettin.")
                st.session_state.player_health = 0

    # Bölüm 4: Fare İstilası
    elif stage == 'fare':
        st.subheader(f"Bölüm 4: Fare İstilası (Adım {step+1}/3)")
        if step == 0:
            st.write("Fareler okulun her yerine yayıldı! İlk strateji? 🐭")
            c1, c2 = st.columns(2)
            if c1.button("Kedi maması koy🥫"):
                st.success("Fareler kedinin yolunu tuttu! 🐱")
                st.session_state.score += 10
                next_event()
            if c2.button("Sesli kovala🔊"):
                st.error("Daha çok toplandılar, kaybettin.")
                st.session_state.player_health = 0
        elif step == 1:
            st.write("Fareler bilgisayara saldırıyor! Ne yaparsın? 💻")
            c1, c2 = st.columns(2)
            if c1.button("Kapan kur🪤"):
                st.success("En büyük fare bile takıldı! 🏅")
                st.session_state.score += 12
                next_event()
            if c2.button("Ses aç🔊"):
                st.error("Fareler rave partisine dönüştürdü, kaybettin.")
                st.session_state.player_health = 0
        else:
            st.write("Son adım: Fare tuzağı mı yoksa kedi çağır? 🐈")
            c1, c2 = st.columns(2)
            if c1.button("Tuzak kur🪤"):
                st.success("Fareler prangaya kapandı! 🎉")
                st.session_state.score += 15
                next_event()
            if c2.button("Kedi ara📞"):
                st.error("Kedi kayboldu, kaybettin.")
                st.session_state.player_health = 0

    # Bölüm 5: Su Basması
    elif stage == 'su':
        st.subheader(f"Bölüm 5: Su Basması (Adım {step+1}/3)")
        if step == 0:
            st.write("Okul koridorları göle döndü! İlk hamle? 🌊")
            c1, c2 = st.columns(2)
            if c1.button("Pompa çalıştır🔧"):
                st.success("Su çekiliyor! 🚰")
                st.session_state.score += 10
                next_event()
            if c2.button("Kano kirala🛶"):
                st.error("Kano battı, kaybettin.")
                st.session_state.player_health = 0
        elif step == 1:
            st.write("Su basıncı tehlikeli! Ne yaparsın? 💥")
            c1, c2 = st.columns(2)
            if c1.button("Vanayı kapat🚰"):
                st.success("Basınç azaldı.")
                st.session_state.score += 12
                next_event()
            if c2.button("Selfie çek🤳"):
                st.error("Selfie emeğini su götürdü, kaybettin.")
                st.session_state.player_health = 0
        else:
            st.write("Son adım: Havuz mu kovamı? 🪣")
            c1, c2 = st.columns(2)
            if c1.button("Kova getir🪣"):
                st.success("Kova işe yaradı! 🎉")
                st.session_state.score += 15
                next_event()
            if c2.button("Havuz kur🏊‍♂️"):
                st.error("Havuz sızıntı yaptı, kaybettin.")
                st.session_state.player_health = 0

    # Bölüm 6: Asansör Saldırısı
    elif stage == 'asansor':
        st.subheader(f"Bölüm 6: Asansör Saldırısı (Adım {step+1}/3)")
        if step == 0:
            st.write("Asansör birden hızlandı! İlk hamle? 🚀")
            c1, c2 = st.columns(2)
            if c1.button("Acil fren🛑"):
                st.success("Asansör durdu! 👍")
                st.session_state.score += 10
                next_event()
            if c2.button("Atla🦘"):
                st.error("Düşerken kaybettin.")
                st.session_state.player_health = 0
        elif step == 1:
            st.write("Kablo kopmak üzere! Ne yaparsın? 🛠️")
            c1, c2 = st.columns(2)
            if c1.button("Kablo onar🔧"):
                st.success("Kablo tamir edildi.")
                st.session_state.score += 12
                next_event()
            if c2.button("Asansörle konuş🗣️"):
                st.error("Asansör susturuldu, kaybettin.")
                st.session_state.player_health = 0
        else:
            st.write("Son adım: Kat kontrol mü yoksa ip iniş? 🪜")
            c1, c2 = st.columns(2)
            if c1.button("Kat şifresini gir🔢"):
                st.success("Kapılar açıldı! 🎉")
                st.session_state.score += 15
                next_event()
            if c2.button("İple in🧗‍♂️"):
                st.error("Yarı yolda indik, kaybettin.")
                st.session_state.player_health = 0

    # Bölüm 7: Lavabo Düşmesi
    elif stage == 'lavabo':
        st.subheader(f"Bölüm 7: Lavabo Düşmesi (Adım {step+1}/3)")
        if step == 0:
            st.write("Lavabo sabit durmuyor! İlk seçenek? 🚰")
            c1, c2 = st.columns(2)
            if c1.button("Kayışı sıkıştır🔩"):
                st.success("Kayış işe yaradı! 👍")
                st.session_state.score += 10
                next_event()
            if c2.button("Instagram canlı📱"):
                st.error("Lavabo düştü, kaybettin.")
                st.session_state.player_health = 0
        elif step == 1:
            st.write("Lavabo titreşim yapıyor! Ne yaparsın? 📉")
            c1, c2 = st.columns(2)
            if c1.button("Destek ayağı ekle🦵"):
                st.success("Stabilite arttı.")
                st.session_state.score += 12
                next_event()
            if c2.button("Havaya kaldır🎈"):
                st.error("Havada düştü, kaybettin.")
                st.session_state.player_health = 0
        else:
            st.write("Son adım: Su tahliyesi mi yoksa yerleştir? 🛠️")
            c1, c2 = st.columns(2)
            if c1.button("Boru bağla🔧"):
                st.success("Tesisat tamamlandı! 🎉")
                st.session_state.score += 15
                next_event()
            if c2.button("Dans et💃"):
                st.error("Dans ederken düştü, kaybettin.")
                st.session_state.player_health = 0

    # Bitiş
    elif stage == 'finished':
        st.balloons()
        st.success(f"Tebrikler! Tüm bölümleri tamamladın. Skorun: {st.session_state.score} 🌟")
        if st.button("Yeniden Başla"):
            restart_game()

    # Kaybetme Durumu
    if st.session_state.player_health <= 0:
        st.error("Kaybettin! 🙁")
        if st.button("Baştan Başla"):
            restart_game()
