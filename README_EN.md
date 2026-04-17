<h1 align="center">Hi 👋, I'm Hari</h1>
<h3 align="center">Senior Frontend Engineer / Full-Stack Engineer (Web3 & AI)</h3>

<p align="center">
  <a href="mailto:song52wow@gmail.com"><img src="https://img.shields.io/badge/song52wow@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://github.com/song52wow"><img src="https://img.shields.io/badge/song52wow-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://img.shields.io/badge/Experience-8%2B_Years-blue?style=for-the-badge" alt="Experience" />
  <img src="https://img.shields.io/badge/Location-Shenzhen-success?style=for-the-badge" alt="Location" />
</p>

---

## 👨‍💻 About Me

A **full-stack engineer with 8+ years** of experience in frontend and full-stack development, deeply involved in **AI data engineering, Web3 multi-chain ecosystems, and Telegram/Chrome cross-platform development**.
- 🚀 Led or contributed to **30+ commercial and open-source projects**, covering large-scale Monorepo architecture design and NPM SDK publishing.
- 🤖 Proficient in AI large model application scenarios (data annotation engines, AI-assisted toolchains), with a strong ability to rapidly engineer cutting-edge technologies.
- ⛓️ Delivered products across **10+ blockchain networks** in the Web3 space, with ongoing focus on AI Agents, LLM toolchains, and on-chain data integration.

---

## 🛠️ Tech Stack

### 💻 Frontend Engineering
![Vue.js](https://img.shields.io/badge/-Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)
![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/-Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tailwind](https://img.shields.io/badge/-Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)
- **Core Stack:** Vue 3 (20+ large-scale projects) / React (18-19) / TypeScript (advanced type gymnastics & API client auto-generation)
- **Build Tooling:** Webpack / Vite 6 / Turborepo / pnpm workspace + Changesets
- **UI Design Systems:** Element Plus / Radix UI / Reka UI / UnoCSS / Vant

### 🌐 Web3 & Blockchain
![Ethereum](https://img.shields.io/badge/-Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white)
![Web3.js](https://img.shields.io/badge/-ethers.js-F16822?style=flat-square&logo=web3dotjs&logoColor=white)
- **Chain Ecosystem:** 10+ heterogeneous chains (Ethereum, Cosmos, Tron, Avalanche, Arbitrum, BSC, etc.)
- **Core Libraries:** ethers.js (v5/v6) / viem / CosmJS / TronWeb / Axelar SDK / TypeChain
- **Wallet Integration:** WalletConnect / MetaMask / Ledger (USB, BLE, HID) / Privy / Reown AppKit

### 🤖 AI & Cross-Platform Development
- **Graphics & Interaction:** Konva (high-performance Canvas) / Three.js / Pixi.js / Tesseract.js (browser-side private OCR) / GSAP
- **Cross-Platform:** Chrome Extension (Popup/Content/Worker advanced architecture) / Telegram Mini App (full lifecycle)

### ⚙️ Backend
![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Deno](https://img.shields.io/badge/-Deno-000000?style=flat-square&logo=deno&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- **Server Runtime:** Node.js (Express) / Deno (Oak, grammy) / GraphQL (Apollo)
- **Cloud Deployment:** Docker

---

## 🏆 Core Projects

### 1. 🏢 AI Data Crowdsourcing Collaboration Platform (Large-Scale Monorepo)
> **Domain:** AI Infrastructure / Data Engineering &nbsp; | &nbsp; **Scale:** `8 Apps + 7 Packages`

A core data annotation workstation for LLM training, supporting multimodal (text/image/audio) workflows with Web3 Token-based economic incentives.
- 🌟 **Key Contributions:**
  - Built a high-frequency Canvas annotation engine based on **Konva**, supporting complex skeleton points and polygon cropping, achieving **3x rendering performance** improvement over traditional SVG approaches.
  - Integrated **Tesseract.js** for client-side OCR inference, protecting data privacy and significantly reducing cloud request overhead.
  - Designed a high-cohesion, low-coupling **pnpm Monorepo boundary strategy**, enabling seamless cross-platform component reuse and boosting CI/CD build cache hit rate to **85%+**.
  - Injected **TypeChain** strong typing across the full stack for smart contract interactions, eliminating runtime ABI parameter mismatch errors.
- 🛠 **Tags:** <kbd>Vue 3</kbd> <kbd>Konva</kbd> <kbd>Tesseract.js</kbd> <kbd>viem</kbd> <kbd>Vite</kbd>

### 2. 🧩 Multi-Chain Unified Connection SDK
> **Domain:** Web3 Core Infrastructure &nbsp; | &nbsp; **Format:** Internal NPM core open-source library

An enterprise-grade multi-network, multi-wallet bridging solution extracted and abstracted to address the fragmented Web3 dApp connection layer.
- 🌟 **Key Contributions:**
  - Maintained up to 11 atomic modules with **Turborepo**, integrating Changesets for fully automated version management and changelog traceability.
  - Built a ~1,000-line core dispatcher engine that abstracts signing differences across `10+` heterogeneous chains (Cosmos, Tron, EVM, etc.) such as `eth_requestAccounts` and `cosmos_signAmino`.
  - Overcame hardware security sandbox limitations, achieving full coverage of Ledger device communication via `USB/BLE/HID` protocols.
- 🛠 **Tags:** <kbd>TypeScript</kbd> <kbd>pnpm Workspaces</kbd> <kbd>Vitest</kbd> <kbd>ethers.js</kbd>

### 3. 🤖 AI-Assisted Smart Browser Extension Suite
> **Domain:** AI Toolchain Extension &nbsp; | &nbsp; **Format:** Chrome Extension Monorepo

An advanced extension assistant enabling intelligent capture, in-page annotation, and closed-loop data feedback within any webpage sandbox.
- 🌟 **Key Contributions:**
  - Redesigned the architecture with a three-layer separation: `Popup / Content Script / Background Worker`. Replaced legacy request libraries with **ky**, reducing bundle size by `40%+` and avoiding memory-related review rejections.
  - Used **mark.js** to intercept the virtual DOM tree for high-speed text addressing, fully compatible with highly dynamic pages (React SPA / Vue SSR).
  - Integrated **GSAP** industrial-grade animation library into injected panel feedback, elevating the plugin-level UX.
- 🛠 **Tags:** <kbd>Vue 3</kbd> <kbd>mark.js</kbd> <kbd>GSAP</kbd> <kbd>ky</kbd>

### 4. 🚀 Cross-Platform Full-Stack Ecosystem (Telegram Bot + Mini App Matrix)
> **Domain:** Telegram Global Traffic Platform &nbsp; | &nbsp; **Format:** Telegram Web App (TWA) + Microservices

Capturing Telegram's open platform traffic opportunities, building decentralized interactive social systems and gaming ecosystems (e.g., BaaSheep nurturing economy).
- 🌟 **Key Contributions:**
  - Adopted **Deno** with **Oak** framework to replace legacy Node.js for Bot orchestration, leveraging built-in TypeScript security sandbox and interceptor decorators (`@Logger/@Trycatch`) for a high-availability middleware gateway.
  - Broke through Mini App UI limitations by introducing **Pixi.js** / **Konva** for rich interactive immersive interfaces (cross-platform touch operations and game farm rendering).
  - Solved cross-platform layout fragmentation with a single **postcss** configuration, achieving seamless layout across Telegram iOS / Android / Windows embedded WebViews.
- 🛠 **Tags:** <kbd>Deno</kbd> <kbd>grammy</kbd> <kbd>Pixi.js</kbd> <kbd>Vue/React</kbd>


---

## 🎯 Core Technical Breakthroughs

| ⚔️ Challenges | 🛡️ Solutions |
| :--- | :--- |
| ⚡️ **Multi-chain signing protocol fragmentation** | Designed a unified **Connector** abstraction layer with a single API wrapping `eth_requestAccounts` / `cosmos_signAmino` / `tron_requestAccounts` across 10+ chains, enabling chain-agnostic business logic. |
| 🔐 **Hardware wallet cross-channel access** | Overcame browser security sandbox limitations, supporting Ledger's `USB` / `BLE` / `HID` physical communication protocols for full enterprise cold wallet coverage. |
| 👁️ **Client-side private OCR** | Pushed OCR inference entirely to the client with **Tesseract.js**, eliminating server-side relay, keeping data local for privacy compliance and low latency. |
| 🧱 **Cross-framework ecosystem fragmentation** | Bridged Vue 3 and React 19 via **Veaury**, enabling Privy (React-exclusive Web3 auth library) to run seamlessly within Vue projects. |
| 📱 **Multi-platform layout fragmentation** | Achieved cross-platform layout with a single `postcss-px-to-viewport` config and zero media queries, covering Telegram iOS / Android / Windows WebView. |

---

