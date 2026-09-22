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

I am a **Payments Operations Professional with 7+ years of experience** specializing in card-transaction disputes, customer investigations, claims processing, and compliance-focused workflows[span_0](start_span)[span_0](end_span). Currently at **Walmart**, I own complex, high-value chargeback cases end-to-end—applying Mastercard and Visa scheme rules, investigating root causes, and implementing AI-assisted workflow automations[span_1](start_span)[span_1](end_span).

- 💳 **Domain Depth:** Card disputes, chargeback representment, risk pattern analysis, scheme rules[span_2](start_span)[span_2](end_span).
- 🛠 **Tools & Tech:** SQL, Advanced Excel, Salesforce Service Cloud, Accertify, Genesys, Oracle[span_3](start_span)[span_3](end_span).
- 🤖 **Automation:** AI-assisted workflow optimization and process gap reduction[span_4](start_span)[span_4](end_span).

---

## Core Skills & Systems

| Domain | Systems & Tools |
|:---|:---|
| **Dispute & Case Systems** | Accertify Dispute Management, Salesforce Service Cloud, Siebel CRM, Genesys, Oracle[span_5](start_span)[span_5](end_span) |
| **Data & Analytics** | SQL, Advanced Excel, Root-Cause Analysis, Trend Reporting[span_6](start_span)[span_6](end_span) |
| **Operations & Compliance** | Mastercard & Visa Scheme Rules, KYC/AML Support, Escalation Management, SLA Tracking[span_7](start_span)[span_7](end_span) |
| **Automation** | AI-assisted Workflow Automation, Process Improvement[span_8](start_span)[span_8](end_span) |

---

## Professional Experience

### **Senior Resolution Coordinator — Chargebacks & Disputes** · Walmart
*Bangalore, India | Feb 2026 – Present*[span_9](start_span)[span_9](end_span)
- Own card-transaction dispute cases end-to-end across the full lifecycle applying Mastercard and Visa scheme rules[span_10](start_span)[span_10](end_span).
- Investigate complex customer concerns, manage escalations, and maintain strict SLA compliance[span_11](start_span)[span_11](end_span).
- Conducted workflow gap analysis and implemented corrective plans that reduced error rates by **15%**[span_12](start_span)[span_12](end_span).
- Leverage AI-assisted workflow automation and SQL analysis to streamline dispute operations[span_13](start_span)[span_13](end_span).

### **Underwriting & Operations Specialist** · Roc360
*Chennai, India | Mar 2022 – Nov 2024*[span_14](start_span)[span_14](end_span)
- Reviewed financial-claim documentation, maintained a centralized decision framework, and supported KYC/AML compliance[span_15](start_span)[span_15](end_span).

### **Senior Associate — Technical & Billing Support** · Sutherland
*Chennai, India | Jan 2019 – Feb 2022*[span_16](start_span)[span_16](end_span)
- Handled escalations for complex billing cases maintaining **95%+ SLA performance**[span_17](start_span)[span_17](end_span).

### **Process Associate — Group Benefits Claims** · Cognizant
*Chennai, India | Jan 2019 – Feb 2022*[span_18](start_span)[span_18](end_span)
- Processed U.S. benefits claims using the Oracle Disability Claims system under strict data-privacy standards[span_19](start_span)[span_19](end_span).

---

## Education & Certifications

- **B.Sc. Biotechnology** — Pondicherry University[span_20](start_span)[span_20](end_span)
- **Diploma in Business Administration** — UniAthena (FEDE)[span_21](start_span)[span_21](end_span)
- **Google AI Professional Certificate**[span_22](start_span)[span_22](end_span)
- **Project Management Foundations** — Google / Coursera[span_23](start_span)[span_23](end_span)

---

## Contribution Graph & Snake Game

<div align="center">

<img src="https://raw.githubusercontent.com/your-username/your-username/output/github-contribution-grid-snake.svg" alt="GitHub Contribution Grid Snake" />

</div>

<details>
<summary><b>⚙️ GitHub Actions Automation Code for Snake Game (.github/workflows/snake.yml)</b></summary>

```yaml
name: Generate Snake Animation

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  generate:
    permissions:
      contents: write
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: generate-github-user-contribution-grid-snake-svg
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark

      - name: push github-contribution-grid-snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

