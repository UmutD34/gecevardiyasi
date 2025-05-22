import streamlit as st

st.set_page_config(page_title="Flappy Dilay", page_icon="🌻", layout="centered")

GAME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Flappy Dilay</title>
<style>
  * { margin:0; padding:0; overflow:hidden; }
  canvas { background: #70c5ce; display: block; margin: auto; }
</style>
</head>
<body>
<canvas id="gameCanvas" width="400" height="600"></canvas>
<script>
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let frames = 0;

// Load images
const bird = new Image();
bird.src = 'https://i.imgur.com/6Xz5KZC.png';
const pipeNorth = new Image();
pipeNorth.src = 'https://i.imgur.com/6FLFQnh.png';
const pipeSouth = new Image();
pipeSouth.src = 'https://i.imgur.com/AU0XwK6.png';

// Game variables
let birdX = 50, birdY = 150, birdV = 0;
const gravity = 0.4, flap = -8;
const gap = 150;
let pipes = [];
let score = 0;

// Controls
document.addEventListener('keydown', e => {
  if(e.code === 'Space') birdV = flap;
});

// Draw loop
function loop(){
  frames++;
  ctx.fillStyle = "#70c5ce";
  ctx.fillRect(0,0,canvas.width,canvas.height);

  // pipes
  if(frames % 100 === 0){
    let y = Math.floor(Math.random()*(canvas.height - gap - 200)) + 50;
    pipes.push({ x: canvas.width, yNorth: y, ySouth: y + gap });
  }
  for(let i=0; i<pipes.length; i++){
    let p = pipes[i];
    ctx.drawImage(pipeNorth, p.x, p.yNorth - pipeNorth.height);
    ctx.drawImage(pipeSouth, p.x, p.ySouth);
    p.x -= 2;

    // collision
    if(birdX > p.x && birdX < p.x + pipeNorth.width){
      if(birdY < p.yNorth || birdY + bird.height > p.ySouth){
        return gameOver();
      }
    }

    // scoring
    if(p.x === birdX) score++;
  }

  pipes = pipes.filter(p => p.x > -pipeNorth.width);

  // bird physics
  birdV += gravity;
  birdY += birdV;
  ctx.drawImage(bird, birdX - bird.width/2, birdY - bird.height/2);

  // boundaries
  if(birdY + bird.height/2 > canvas.height || birdY - bird.height/2 < 0){
    return gameOver();
  }

  // score display
  ctx.fillStyle = "#fff";
  ctx.font = "40px Arial";
  ctx.fillText(score, canvas.width/2 - 10, 50);

  requestAnimationFrame(loop);
}

function gameOver(){
  ctx.fillStyle = "rgba(0,0,0,0.5)";
  ctx.fillRect(0,0,canvas.width,canvas.height);
  ctx.fillStyle = "#fff";
  ctx.font = "30px Arial";
  ctx.fillText("Oyun Bitti!", 110, canvas.height/2 - 20);
  ctx.font = "20px Arial";
  ctx.fillText("Yeniden yüklemek için F5", 80, canvas.height/2 + 20);
}

bird.onload = () => {
  pipeNorth.onload = () => {
    pipeSouth.onload = () => {
      loop();
    };
  };
};
</script>
</body>
</html>
"""

st.components.v1.html(GAME_HTML, height=650)
