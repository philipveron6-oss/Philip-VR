<div align="center">

<a href="https://capsule-render.vercel.app/">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0071CE,50:4C1D95,100:312E81&height=180&section=header&text=M.%20Philip%20Veron%20Raj&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35" />
</a>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=20&duration=3000&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=Payments+Operations+Professional;Card+Disputes+%26+Chargebacks;Mastercard+%26+Visa+Scheme+Rules;AI-Assisted+Workflow+Automation" alt="Typing animation" />
</a>

<br />

<img src="https://img.shields.io/badge/Organization-Walmart-0071CE?style=for-the-badge&logo=walmart&logoColor=white" alt="Organization Walmart" />
<img src="https://img.shields.io/badge/Location-Bangalore%2C%20India-312E81?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Location" />
<img src="https://img.shields.io/badge/Followers-400%2B-5B21B6?style=for-the-badge&logo=github&logoColor=white" alt="Followers" />

<br /><br />

<a href="mailto:philipveron6@gmail.com"><img src="https://img.shields.io/badge/Email-6D28D9?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
<a href="https://linkedin.com/in/philipveronraj" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-4C1D95?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>

</div>

---

## About Me

I am a **Payments Operations Professional with 7+ years of experience** specializing in card-transaction disputes, customer investigations, claims processing, and compliance-focused workflows. Currently at **Walmart**, I own complex, high-value chargeback cases end-to-end—applying Mastercard and Visa scheme rules, investigating root causes, and implementing AI-assisted workflow automations.

- 💳 **Domain Depth:** Card disputes, chargeback representment, risk pattern analysis, scheme rules.
- 🛠 **Tools & Tech:** SQL, Advanced Excel, Salesforce Service Cloud, Accertify, Genesys, Oracle.
- 🤖 **Automation:** AI-assisted workflow optimization and process gap reduction.

---

## Core Skills & Systems

| Domain | Systems & Tools |
|:---|:---|
| **Dispute & Case Systems** | Accertify Dispute Management, Salesforce Service Cloud, Siebel CRM, Genesys, Oracle |
| **Data & Analytics** | SQL, Advanced Excel, Root-Cause Analysis, Trend Reporting |
| **Operations & Compliance** | Mastercard & Visa Scheme Rules, KYC/AML Support, Escalation Management, SLA Tracking |
| **Automation** | AI-assisted Workflow Automation, Process Improvement |

---

## Professional Experience

### **Senior Resolution Coordinator — Chargebacks & Disputes** · Walmart
*Bangalore, India | Feb 2026 – Present*
- Own card-transaction dispute cases end-to-end across the full lifecycle applying Mastercard and Visa scheme rules.
- Investigate complex customer concerns, manage escalations, and maintain strict SLA compliance.
- Conducted workflow gap analysis and implemented corrective plans that reduced error rates by **15%**.
- Leverage AI-assisted workflow automation and SQL analysis to streamline dispute operations.

### **Underwriting & Operations Specialist** · Roc360
*Chennai, India | Mar 2022 – Nov 2024*
- Reviewed financial-claim documentation, maintained a centralized decision framework, and supported KYC/AML compliance.

### **Senior Associate — Technical & Billing Support** · Sutherland
*Chennai, India | Jan 2019 – Feb 2022*
- Handled escalations for complex billing cases maintaining **95%+ SLA performance**.

### **Process Associate — Group Benefits Claims** · Cognizant
*Chennai, India | Jan 2019 – Feb 2022*
- Processed U.S. benefits claims using the Oracle Disability Claims system under strict data-privacy standards.

---

## Education & Certifications

- **B.Sc. Biotechnology** — Pondicherry University
- **Diploma in Business Administration** — UniAthena (FEDE)
- **Google AI Professional Certificate**
- **Project Management Foundations** — Google / Coursera

---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neon Defender - GitHub Single File Game</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      background: #0a0c16;
      color: #fff;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      overflow: hidden;
    }
    #game-container {
      position: relative;
      box-shadow: 0 0 35px rgba(0, 255, 204, 0.25);
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid rgba(0, 255, 204, 0.2);
    }
    canvas {
      background: #05070f;
      display: block;
    }
    .ui-layer {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background: rgba(5, 7, 15, 0.88);
      backdrop-filter: blur(6px);
      text-align: center;
      padding: 20px;
    }
    h1 {
      font-size: 2.8rem;
      color: #00ffcc;
      text-shadow: 0 0 12px #00ffcc;
      margin-bottom: 12px;
      letter-spacing: 2px;
    }
    p {
      color: #a0aec0;
      margin-bottom: 24px;
      font-size: 1.1rem;
      line-height: 1.5;
    }
    button {
      background: linear-gradient(135deg, #00ffcc, #0099ff);
      border: none;
      color: #05070f;
      padding: 14px 36px;
      font-size: 1.2rem;
      font-weight: bold;
      border-radius: 30px;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
    }
    button:hover {
      transform: scale(1.05);
      box-shadow: 0 0 25px rgba(0, 255, 204, 0.8);
    }
    .hidden {
      display: none !important;
    }
  </style>
</head>
<body>

  <div id="game-container">
    <canvas id="canvas" width="800" height="500"></canvas>
    
    <div id="start-screen" class="ui-layer">
      <h1>NEON DEFENDER</h1>
      <p>Use <b>Arrow Keys / WASD</b> or <b>Mouse</b> to control the ship.<br>Blasters auto-fire when active.</p>
      <button id="start-btn">START GAME</button>
    </div>

    <div id="game-over-screen" class="ui-layer hidden">
      <h1 style="color: #ff3366; text-shadow: 0 0 12px #ff3366;">GAME OVER</h1>
      <p>Final Score: <span id="final-score" style="color: #00ffcc; font-weight: bold;">0</span></p>
      <button id="restart-btn">PLAY AGAIN</button>
    </div>
  </div>

  <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const startScreen = document.getElementById('start-screen');
    const gameOverScreen = document.getElementById('game-over-screen');
    const finalScoreEl = document.getElementById('final-score');

    let gameActive = false;
    let score = 0;
    let frame = 0;

    const player = {
      x: canvas.width / 2,
      y: canvas.height - 60,
      size: 18,
      speed: 7
    };

    let bullets = [];
    let enemies = [];
    let particles = [];
    const keys = {};

    window.addEventListener('keydown', (e) => keys[e.code] = true);
    window.addEventListener('keyup', (e) => keys[e.code] = false);

    canvas.addEventListener('mousemove', (e) => {
      if (!gameActive) return;
      const rect = canvas.getBoundingClientRect();
      player.x = e.clientX - rect.left;
      player.y = e.clientY - rect.top;
    });

    function spawnEnemy() {
      const size = Math.random() * 18 + 14;
      enemies.push({
        x: Math.random() * (canvas.width - size * 2) + size,
        y: -size,
        size: size,
        speed: Math.random() * 2.5 + 1.5,
        color: `hsl(${Math.random() * 60 + 330}, 100%, 60%)`
      });
    }

    function createParticles(x, y, color) {
      for (let i = 0; i < 14; i++) {
        particles.push({
          x: x,
          y: y,
          dx: (Math.random() - 0.5) * 7,
          dy: (Math.random() - 0.5) * 7,
          size: Math.random() * 4 + 1.5,
          alpha: 1,
          color: color
        });
      }
    }

    function update() {
      if (!gameActive) return;
      frame++;

      // Keyboard Controls
      if (keys['ArrowLeft'] || keys['KeyA']) player.x -= player.speed;
      if (keys['ArrowRight'] || keys['KeyD']) player.x += player.speed;
      if (keys['ArrowUp'] || keys['KeyW']) player.y -= player.speed;
      if (keys['ArrowDown'] || keys['KeyS']) player.y += player.speed;

      // Keep Player within Canvas
      player.x = Math.max(player.size, Math.min(canvas.width - player.size, player.x));
      player.y = Math.max(player.size, Math.min(canvas.height - player.size, player.y));

      // Auto Shooting
      if (frame % 7 === 0) {
        bullets.push({ x: player.x, y: player.y - player.size, speed: 11 });
      }

      // Update Bullets
      for (let i = bullets.length - 1; i >= 0; i--) {
        bullets[i].y -= bullets[i].speed;
        if (bullets[i].y < 0) bullets.splice(i, 1);
      }

      // Spawn Enemies
      if (frame % 30 === 0) spawnEnemy();

      // Update Enemies & Collision Detection
      for (let eIdx = enemies.length - 1; eIdx >= 0; eIdx--) {
        const enemy = enemies[eIdx];
        enemy.y += enemy.speed;

        // Player Collision
        const distToPlayer = Math.hypot(player.x - enemy.x, player.y - enemy.y);
        if (distToPlayer < player.size + enemy.size) {
          endGame();
          return;
        }

        // Bullet Hit Collision
        for (let bIdx = bullets.length - 1; bIdx >= 0; bIdx--) {
          const bullet = bullets[bIdx];
          const dist = Math.hypot(bullet.x - enemy.x, bullet.y - enemy.y);
          if (dist < enemy.size) {
            createParticles(enemy.x, enemy.y, enemy.color);
            enemies.splice(eIdx, 1);
            bullets.splice(bIdx, 1);
            score += 10;
            break;
          }
        }

        if (enemy && enemy.y > canvas.height + enemy.size) {
          enemies.splice(eIdx, 1);
        }
      }

      // Update Particles
      for (let pIdx = particles.length - 1; pIdx >= 0; pIdx--) {
        const p = particles[pIdx];
        p.x += p.dx;
        p.y += p.dy;
        p.alpha -= 0.03;
        if (p.alpha <= 0) particles.splice(pIdx, 1);
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (!gameActive) return;

      // Draw Player Ship
      ctx.fillStyle = '#00ffcc';
      ctx.shadowBlur = 15;
      ctx.shadowColor = '#00ffcc';
      ctx.beginPath();
      ctx.moveTo(player.x, player.y - player.size);
      ctx.lineTo(player.x - player.size, player.y + player.size);
      ctx.lineTo(player.x + player.size, player.y + player.size);
      ctx.closePath();
      ctx.fill();

      // Draw Bullets
      ctx.fillStyle = '#00e5ff';
      ctx.shadowColor = '#00e5ff';
      bullets.forEach(b => {
        ctx.beginPath();
        ctx.arc(b.x, b.y, 3.5, 0, Math.PI * 2);
        ctx.fill();
      });

      // Draw Enemies
      enemies.forEach(e => {
        ctx.fillStyle = e.color;
        ctx.shadowColor = e.color;
        ctx.beginPath();
        ctx.arc(e.x, e.y, e.size, 0, Math.PI * 2);
        ctx.fill();
      });

      // Draw Particles
      particles.forEach(p => {
        ctx.save();
        ctx.globalAlpha = p.alpha;
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      });

      ctx.shadowBlur = 0;

      // Score Display
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 18px monospace';
      ctx.fillText(`SCORE: ${score}`, 20, 35);
    }

    function loop() {
      update();
      draw();
      if (gameActive) requestAnimationFrame(loop);
    }

    function startGame() {
      score = 0;
      frame = 0;
      bullets = [];
      enemies = [];
      particles = [];
      player.x = canvas.width / 2;
      player.y = canvas.height - 60;
      gameActive = true;

      startScreen.classList.add('hidden');
      gameOverScreen.classList.add('hidden');
      loop();
    }

    function endGame() {
      gameActive = false;
      finalScoreEl.innerText = score;
      gameOverScreen.classList.remove('hidden');
    }

    document.getElementById('start-btn').addEventListener('click', startGame);
    document.getElementById('restart-btn').addEventListener('click', startGame);
  </script>
</body>
</html>
