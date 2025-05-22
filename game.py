
import streamlit as st

st.set_page_config(page_title="Dilay'ı Koru", layout="centered")

st.markdown("""
    <style>
        canvas {
            background-color: #fdfcdc;
            border: 3px solid #333;
            border-radius: 12px;
        }
        .title {
            font-size: 28px;
            color: #d32f2f;
            font-weight: bold;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎮 Dilay'ı Koru: Gece Vardiyası Başlıyor!</div>', unsafe_allow_html=True)

# HTML5 Canvas + PyScript ile Python üzerinden oyun kontrolü
st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
<canvas id="gameCanvas" width="350" height="550"></canvas>
<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let hero = { x: 150, y: 450, w: 50, h: 50 };
let enemies = [];
let bullets = [];
let score = 0;
let health = 100;

function spawnEnemy() {
    enemies.push({ x: Math.random() * 300, y: 0, w: 40, h: 40, speed: 2 });
}

function drawHero() {
    ctx.fillStyle = "#1976d2";
    ctx.fillRect(hero.x, hero.y, hero.w, hero.h);
    ctx.fillStyle = "#fff";
    ctx.fillText("UMUT", hero.x + 5, hero.y + 30);
}

function drawEnemies() {
    ctx.fillStyle = "#d84315";
    enemies.forEach(e => {
        ctx.fillRect(e.x, e.y, e.w, e.h);
    });
}

function moveEnemies() {
    enemies.forEach(e => e.y += e.speed);
    enemies = enemies.filter(e => {
        if (e.y + e.h > canvas.height) {
            health -= 10;
            return false;
        }
        return true;
    });
}

function shoot() {
    bullets.push({ x: hero.x + 20, y: hero.y, w: 10, h: 20 });
}

function drawBullets() {
    ctx.fillStyle = "#00c853";
    bullets.forEach(b => ctx.fillRect(b.x, b.y, b.w, b.h));
}

function moveBullets() {
    bullets.forEach(b => b.y -= 4);
    bullets = bullets.filter(b => b.y > 0);
}

function checkCollisions() {
    bullets.forEach((b, bi) => {
        enemies.forEach((e, ei) => {
            if (b.x < e.x + e.w && b.x + b.w > e.x && b.y < e.y + e.h && b.y + b.h > e.y) {
                enemies.splice(ei, 1);
                bullets.splice(bi, 1);
                score += 10;
            }
        });
    });
}

function drawHUD() {
    ctx.fillStyle = "#000";
    ctx.fillText("Skor: " + score, 10, 20);
    ctx.fillText("Can: " + health, 10, 40);
}

function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawHero();
    drawEnemies();
    drawBullets();
    moveEnemies();
    moveBullets();
    checkCollisions();
    drawHUD();
    if (health <= 0) {
        ctx.fillStyle = "#d32f2f";
        ctx.fillText("Gece Vardiyasını Yendik!", 60, 250);
    } else {
        requestAnimationFrame(gameLoop);
    }
}

setInterval(spawnEnemy, 1500);
setInterval(shoot, 500);
ctx.font = "16px sans-serif";
gameLoop();
</script>
</body>
</html>
""", height=580)
