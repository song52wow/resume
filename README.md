<h1 align="center">Hi 👋, I'm Hari</h1>
<h3 align="center">资深前端工程师 / 全栈工程师（Web3 & AI 方向）</h3>

<p align="center">
  <a href="mailto:song52wow@gmail.com"><img src="https://img.shields.io/badge/song52wow@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://github.com/song52wow"><img src="https://img.shields.io/badge/song52wow-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <img src="https://img.shields.io/badge/Experience-8%2B_Years-blue?style=for-the-badge" alt="Experience" />
  <img src="https://img.shields.io/badge/Location-Shenzhen-success?style=for-the-badge" alt="Location" />
</p>

---

## 👨‍💻 关于我 (About Me)

拥有 **8 年以上**前端及全栈开发经验，深度参与 **AI 数据工程、Web3 多链生态、Telegram/Chrome 跨平台开发** 等前沿领域。
- 🚀 主导或深度参与过 **30+ 个商业/开源项目**，涵盖大型 Monorepo 架构设计、NPM SDK 发布、Kubernetes 多集群运维全链路。
- 🤖 熟悉 AI 大模型应用落地场景（数据标注引擎、AI 辅助工具链），具备将前沿技术快速工程化的卓越落地能力。
- ⛓️ 在 Web3 方向实现了跨 10+ 条公链的产品交付，持续关注 AI Agent、LLM 工具链与链上数据融合等方向。

---

## 🛠️ 技能栈 (Tech Stack)

### 💻 前端工程 (Frontend)
![Vue.js](https://img.shields.io/badge/-Vue.js-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)
![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/-Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tailwind](https://img.shields.io/badge/-Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)
- **核心体系：** Vue 3 (20+大型项目) / React (18-19) / TypeScript (深入类型体操与 API Client 自动生成)
- **工程化基建：** Webpack / Vite 6 / Turborepo / pnpm workspace + Changesets
- **UI 设计系统：** Element Plus / Radix UI / Reka UI / UnoCSS / Vant

### 🌐 Web3 & 区块链 (Blockchain)
![Ethereum](https://img.shields.io/badge/-Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white)
![Web3.js](https://img.shields.io/badge/-ethers.js-F16822?style=flat-square&logo=web3dotjs&logoColor=white)
- **公链生态：** 跨 10+ 条异构链 (Ethereum, Cosmos, Tron, Avalanche, Arbitrum, BSC 等)
- **核心组件：** ethers.js (v5/v6) / viem / CosmJS / TronWeb / Axelar SDK / TypeChain
- **钱包生态集成：** WalletConnect / MetaMask / Ledger(USB, BLE, HID) / Privy / Reown AppKit

### 🤖 AI & 跨端扩展开发 (AI & Cross-Platform)
- **图形学与交互：** Konva (高性能 Canvas) / Three.js / Pixi.js / Tesseract.js (私有化浏览器端 OCR) / GSAP
- **跨平台技术：** Chrome Extension (Popup/Content/Worker 高级架构) / Telegram Mini App (全闭环)

### ⚙️ 后端 & DevOps (Backend & Infra)
![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Deno](https://img.shields.io/badge/-Deno-000000?style=flat-square&logo=deno&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
- **服务端运行层：** Node.js (Express) / Deno (Oak, grammy) / GraphQL (Apollo)
- **云原生部署：** Docker / Kubernetes (EKS, 5+ 集群级) / Harbor / AWS / OpenResty

---

## 🏆 核心项目实战 (Core Projects)

### 1. 🏢 AI 数据众包协作平台 (大型超级 Monorepo)
> **领域：** AI 基础设施 / 数据工程 &nbsp; | &nbsp; **规模：** `8 Apps + 7 Packages`

面向大模型训练的数据标注核心工作站，支持多模态（文本/图像/音频）并结合 Web3 Token 经济模型激励流动性。
- 🌟 **核心贡献：**
  - 基于 **Konva** 构建底层高频 Canvas 标注引擎，支持复杂骨架点/多边形截取，渲染效率对比传统 SVG 数据 **跃升 3 倍**。
  - 前置 OCR 解析算力，集成 **Tesseract.js** 直接在浏览器端完成识别，保护数据隐私并极大降低云端请求开销。
  - 设计高内聚低耦合的 **pnpm Monorepo 边界策略**，实现跨终端组件完美复用，将 CI/CD 构建缓存命中率提升至 **85%+**。
  - **TypeChain** 强类型约束注入全栈与智能合约交互，从源头消灭运行时的 ABI 参数不对齐报错痛点。
- 🛠 **标签：** <kbd>Vue 3</kbd> <kbd>Konva</kbd> <kbd>Tesseract.js</kbd> <kbd>viem</kbd> <kbd>Vite</kbd>

### 2. 🧩 多链统一连接基建 SDK
> **领域：** Web3 核心基建 &nbsp; | &nbsp; **形态：** NPM 团队内部级核心开源库

针对 Web3 dApp 连接层碎片化的行业痛点，独立抽离并封装的企业级多网络、多钱包接入桥接基石方案。
- 🌟 **核心贡献：**
  - 使用 **Turborepo** 维护多达 11 个原子级模块，串联 Changesets 全自动化管理版本的平滑切角与 Changelog 溯源。
  - 产出近千行核心调度类引擎，完全封装并抹平内部跨越 `10+` 条异构主链（Cosmos、Tron、EVM等）的底层签名调用差异（如 `eth_requestAccounts`, `cosmos_signAmino`）。
  - 打通强隔离硬件安全边界限制，实现底层对 Ledger 实体设备的 `USB/BLE/HID` 多通信通道协议全面覆盖。
- 🛠 **标签：** <kbd>TypeScript</kbd> <kbd>pnpm Workspaces</kbd> <kbd>Vitest</kbd> <kbd>ethers.js</kbd>

### 3. 🤖 AI 辅助智能浏览器扩展套件 (AI Browser Extension)
> **领域：** AI 工具链拓展 &nbsp; | &nbsp; **形态：** Chrome Extension 体系 Monorepo

帮助用户逃离原生工作台，在任意网页沙箱环境内完成智能捕获、截取标注并完成闭环数据回流的高阶拓展助手。
- 🌟 **核心贡献：**
  - 推翻原生粗放型架构，基于 `Popup / Content Script / Background Worker` 范式进行三端分离。使用并接入 **ky** 组件接替老旧请求库，令包体积锐减 `40%+`，规避由于内存占用引发的审核拒批。
  - 使用 **mark.js** 侵入式接管虚拟 DOM 树并执行文本寻址极速关联，全面兼容市面上极度动态化的页面(React SPA / Vue SSR)。
  - 接入 **GSAP** 工业级流体动画库并植入于注入面板反馈中，拉高插件级应用体验天花板。
- 🛠 **标签：** <kbd>Vue 3</kbd> <kbd>mark.js</kbd> <kbd>GSAP</kbd> <kbd>ky</kbd>

### 4. 🚀 跨平台全栈生态 (Telegram Bot + Mini App 矩阵)
> **领域：** TG 全球亿级流量入口 &nbsp; | &nbsp; **形态：** Telegram Web App (TWA) + 微服务中台

抢占 Telegram 开放平台流量红利体系，深度定制去中心化互动社交系统与游戏生态（例如 BaaSheep 养成经济模型）。
- 🌟 **核心贡献：**
  - 大胆采用 **Deno** 搭配 **Oak** 框架接管陈旧的 Node.js 作为 Bot 调度节点，利用内置 TypeScript 安全沙箱和拦截装饰器（`@Logger/@Trycatch`）构建高可用中间件网关防御屏障。
  - 小程序侧突破局限性与表单展示，引入 **Pixi.js** / **Konva** 组合重新构筑出富交互沉浸界面（如大型跨端触控操作与游戏农场调度渲染）。
  - 解决原生各端异构割裂问题，用一套 **postcss** 配置层完美跑通 TG 原生 iOS / Android 以至于 Windows 客户端内嵌的多核 WebView 流畅布局。
- 🛠 **标签：** <kbd>Deno</kbd> <kbd>grammy</kbd> <kbd>Pixi.js</kbd> <kbd>Vue/React</kbd>


---

## 🎯 核心技术攻坚 (Core Technical Breakthroughs)

| ⚔️ 难题场景 (Challenges) | 🛡️ 解决方案 (Solutions) |
| :--- | :--- |
| ⚡️ **多链签名协议割裂** | 设计统一 **Connector** 抽象层，以单一 API 封装 `eth_requestAccounts` / `cosmos_signAmino` / `tron_requestAccounts` 等 10+ 条链的底层差异，实现上层业务零感知切链。 |
| 🔐 **硬件钱包跨通道接入** | 突破浏览器安全沙箱限制，同时打通 Ledger 的 `USB` / `BLE` / `HID` 三种物理通信协议，实现企业级冷钱包全覆盖。 |
| 👁️ **浏览器端隐私 OCR** | 以 **Tesseract.js** 将 OCR 推理完全下沉到客户端，消除服务端中转，数据不出本地，兼顾识别时延与隐私合规。 |
| 🧱 **跨框架生态割裂** | 通过 **Veaury** 桥接层在 Vue 3 中直接挂载 React 19 组件树，使 Privy（React 专属 Web3 认证库）无缝运行于 Vue 项目中。 |
| 📱 **多端布局碎片化** | 仅用一套 `postcss-px-to-viewport` 配置且无媒体查询，跑通 Telegram iOS / Android / Windows 客户端内嵌 WebView，消除平台差异。 |

---

## 🎖 教育经历 (Education)

- **广东工程职业技术学院** · 软件信息工程 · 大专学历 · _2013 - 2016_

