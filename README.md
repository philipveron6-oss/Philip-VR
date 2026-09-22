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
  <title>Tic-Tac-Toe</title>
  <style>
    body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; background: #f0f2f5; }
    h1 { margin-bottom: 10px; }
    #status { font-size: 1.2rem; margin-bottom: 20px; }
    .board { display: grid; grid-template-columns: repeat(3, 100px); grid-gap: 5px; }
    .cell { width: 100px; height: 100px; background: #fff; border: 2px solid #333; font-size: 2.5rem; font-weight: bold; display: flex; align-items: center; justify-content: center; cursor: pointer; }
    .cell:hover { background: #e9e9e9; }
    button { margin-top: 20px; padding: 10px 20px; font-size: 1rem; cursor: pointer; }
  </style>
</head>
<body>
  <h1>Tic-Tac-Toe</h1>
  <div id="status">Player X's Turn</div>
  <div class="board" id="board">
    <div class="cell" data-index="0"></div>
    <div class="cell" data-index="1"></div>
    <div class="cell" data-index="2"></div>
    <div class="cell" data-index="3"></div>
    <div class="cell" data-index="4"></div>
    <div class="cell" data-index="5"></div>
    <div class="cell" data-index="6"></div>
    <div class="cell" data-index="7"></div>
    <div class="cell" data-index="8"></div>
  </div>
  <button id="reset">Reset Game</button>

  <script>
    const cells = document.querySelectorAll('.cell');
    const statusText = document.querySelector('#status');
    const resetBtn = document.querySelector('#reset');
    let board = ["", "", "", "", "", "", "", "", ""];
    let currentPlayer = "X";
    let isGameActive = true;

    const winConditions = [
      [0,1,2], [3,4,5], [6,7,8],
      [0,3,6], [1,4,7], [2,5,8],
      [0,4,8], [2,4,6]
    ];

    function handleCellClick(e) {
      const index = e.target.getAttribute('data-index');
      if (board[index] !== "" || !isGameActive) return;

      board[index] = currentPlayer;
      e.target.textContent = currentPlayer;
      checkWinner();
    }

    function checkWinner() {
      let won = false;
      for (let condition of winConditions) {
        let [a, b, c] = condition;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
          won = true;
          break;
        }
      }

      if (won) {
        statusText.textContent = `Player ${currentPlayer} Wins!`;
        isGameActive = false;
      } else if (!board.includes("")) {
        statusText.textContent = "Draw!";
        isGameActive = false;
      } else {
        currentPlayer = currentPlayer === "X" ? "O" : "X";
        statusText.textContent = `Player ${currentPlayer}'s Turn`;
      }
    }

    function resetGame() {
      board = ["", "", "", "", "", "", "", "", ""];
      currentPlayer = "X";
      isGameActive = true;
      statusText.textContent = "Player X's Turn";
      cells.forEach(cell => cell.textContent = "");
    }

    cells.forEach(cell => cell.addEventListener('click', handleCellClick));
    resetBtn.addEventListener('click', resetGame);
  </script>
</body>
</html>
