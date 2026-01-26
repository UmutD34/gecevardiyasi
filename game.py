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
        
       
            
            <div class="paragraph">
                <strong>Bir gün bu siteye girersen...</strong><br>
                Aşkımızı hatırla.
            </div>
            
            
        </div>
        
        <div class="button-container">
            <button class="music-button" onclick="playMusic()">Hatıra</button>
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
