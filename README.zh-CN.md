<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo/lockup-dark.svg" />
  <img alt="video-to-notebook" src="assets/logo/lockup-light.svg" width="460" />
</picture>

**为 Claude Code 和 OpenAI Codex 设计。** 把一摞公开课视频整合成一份笔记：一本教材加一部概念百科，输出是单个静态站点。

把同主题的几个 **YouTube 或 B 站**播放列表丢给它，剩下的活由你的 coding agent 接手：爬视频、按你提供的本体给每条字幕片段打概念标签、聚类出概念图谱、按教学顺序排出章节、逐章逐概念把正文写出来。**不需要单独的 Anthropic API key**，所有 LLM 阶段都跑在 agent 已有的 Claude Code 或 Codex 会话里。Pagefind 搜索、中英双语输出默认带上。

[![CI](https://github.com/LinZhuoChen/video-to-notebook/actions/workflows/ci.yml/badge.svg)](https://github.com/LinZhuoChen/video-to-notebook/actions/workflows/ci.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Astro](https://img.shields.io/badge/Astro-5-FF5D01?logo=astro&logoColor=white)](https://astro.build/)
[![Built for Claude Code](https://img.shields.io/badge/built_for-Claude_Code-D97757?logo=anthropic&logoColor=white)](https://claude.com/claude-code)
[![Built for OpenAI Codex](https://img.shields.io/badge/built_for-OpenAI_Codex-10A37F?logo=openai&logoColor=white)](https://github.com/openai/codex)

[**在线 demo：Diffusion Models 教材**](https://linzhuochen.github.io/video-to-notebook/textbook/) · [**快速上手**](#-快速上手) · [**工作原理**](#-工作原理) · [**与各类 agent 配合**](#-用-ai-coding-agent-驱动) · [**Roadmap**](#-roadmap)

[English](README.md) · **中文**

---

</div>

> 🚧 **早期项目，遇到问题请反馈。** `video-to-notebook` 还在频繁迭代，v2.0.0 是从 `course-merger` 改名后的首个公开版本。撞上 bug、看到可疑的 prompt、生成的章节跑题、或者爬虫在某个真实播放列表上失败，请[**开 issue**](https://github.com/LinZhuoChen/video-to-notebook/issues/new/choose)并附上失败命令和几行日志，这样修起来最快。也欢迎提需求、贡献其它领域的本体文件，以及 YouTube 和 B 站之外（Coursera / edX / MIT-OCW…）的爬虫适配器。

## ✨ 成品长什么样

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://linzhuochen.github.io/video-to-notebook/textbook/">
  <img src="assets/screenshots/textbook-toc.png" alt="教材目录——5 个模块共 21 章" />
</a>
<sub><b>📖 教材目录</b>：21 章 / 5 个模块 / 按教学顺序编排</sub>
</td>
<td width="50%" valign="top" align="center">
<a href="https://linzhuochen.github.io/video-to-notebook/concepts/">
  <img src="assets/screenshots/concepts-grid.png" alt="概念百科——33 个图文详解" />
</a>
<sub><b>💡 概念百科</b>：33 个图文详解，每个模块独立强调色</sub>
</td>
</tr>
<tr>
<td colspan="2" align="center">
<a href="https://linzhuochen.github.io/video-to-notebook/textbook/1/">
  <img src="assets/screenshots/textbook-chapter.png" alt="章节阅读视图——左侧目录、TL;DR 块、右侧 mini-map、源视频深链" />
</a>
<sub><b>📐 章节阅读视图</b>：左侧目录、TL;DR、右侧 mini-map、源视频深链</sub>
</td>
</tr>
</table>

## 🧭 设计原则

和"把播放列表丢给 ChatGPT 让它写个 summary"的区别只有三点：

1. **源材料保真优先。** 每一章、每个概念页都要忠实再现讲师本人怎么讲：原话措辞、白板推导步骤、用过的比喻、点名引用的论文。自己加的延伸要打上 `🟡 教材外补充` 标签。两门课对同一概念给出不同比喻？两个都保留并注明来源。看过原视频的读者认不出这一章，就是写得太概括。

2. **不准编造，卡住就回去 debug pipeline。** 某一章的源 chunk 凑得稀疏时（比如 20 个全是课程后勤闲聊、或被字母序靠前的某门课吃掉了 LIMIT），agent 必须**停下来诊断**，不能用训练数据糊弄过去。常见 bug：chunk 选择 SQL 写成 `LIMIT 20 ORDER BY course_slug`（已用深度优先分配修复）、按讲座标题关键词匹配但概念本身没被讨论、`--max-source-chunks` 设得过低。

3. **教科书深度，不是杂志摘要深度。** 每章正文目标 5000–8000 中文字，需要包含：TL;DR 块、8–14 个编号小节（一二三四…）、每行附 `**Why**:` 注解的逐步公式推导、保留讲师所有独特比喻、3–5 个不同色 callout（info / note / warning / tip / quote）、工程细节内嵌成 callout 而非放到结尾、引入模型时给出完整可运行的 PyTorch 骨架、5–7 条锚定讲师具体例子的 takeaway。低于 4000 字算没写够。

三条规则写进了 [synthesize](src/video_to_notebook/synthesize/prompts.py) 和 [explain](src/video_to_notebook/explain/prompts.py) 的风格指南，任何驱动 pipeline 的 agent 都自动继承。

## 📸 功能展示

<table>
<tr>
<td width="50%" valign="top">

### 📖 合并教材

章节按教学顺序排，新手能从头读到尾拿到一条完整学习弧线，不是一堆零散片段。

- 内嵌 SVG 图和 CSS 动画
- KaTeX 渲染 LaTeX 公式
- 带时间戳的源视频片段
- 反偏见开场，每章末尾 3 条 takeaway
- 键盘 ← / → 翻章，侧栏 mini-map

</td>
<td width="50%" valign="top">

### 💡 概念百科

每个重要概念有独立页面，方便就单点深挖。

- 定义 / 公式 / 易错点 **quickref 卡片**
- 交互组件：滑块、step-button、动画 SVG
- 带等式链的手算示例
- 3 条带反例的常见误区
- 相关概念交叉链接
- 源视频片段深链

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌓 暗色模式与模块强调色

```
Module 1  · 数学直觉              🟢 绿
Module 2  · 训练直觉              🔵 蓝
Module 3  · 视觉起源              🟣 紫
Module 4  · 现代深度学习          🟡 琥珀
Module 5  · 现代架构与未来        🌸 玫红
```

通过 `data-module-idx` 套到布局根节点，卡片、侧栏、drop cap、进度条全部继承 `--module-accent`。

</td>
<td width="50%" valign="top">

### 📱 移动优先，不依赖 JS 框架

```
@media (max-width: 900px)
  → 左侧滑入式汉堡抽屉
  → 抽屉镜像教材侧栏
  → 阅读列展开占满视窗
```

没有 React，也没有 Vue。Astro 加 200 行原生 JS。一个概念页（含 SVG 和交互）gzip 后约 30 KB。

</td>
</tr>
</table>

## 🚀 快速上手

### 路线 A：无 API key，由 AI agent 驱动（默认）

每个 LLM 阶段（`tag` / `cluster` / `curriculum` / `synthesize` / `explain`）默认走 in-session：CLI 把待办工作以 prompt envelope 写到 `<state_dir>/prompts/<step>.json` 后退出；你（agent）把决策写到同目录的 `.decisions.json`，再用 `--apply` 重跑一次就把结果落到 DB。**Claude Code**、**OpenAI Codex**、**Cursor**、**Continue** 或你自己的脚本都行，都不需要单独的 API key。详见下方 [**§ 用 AI coding agent 驱动**](#-用-ai-coding-agent-驱动) 一节。

### 路线 B：带 Anthropic API key 跑

```bash
# 装 Python CLI（3.12+）
pip install video-to-notebook      # 或者：uv tool install video-to-notebook
brew install node yt-dlp           # Node 20+ 给最后的 Astro 构建用；yt-dlp 给爬虫用

# 跑 pipeline
export ANTHROPIC_API_KEY=sk-ant-...
mkdir my-study-site && cd my-study-site

video-to-notebook init --language zh                                # 或 `--language en`

# YouTube 播放列表
video-to-notebook crawl "https://www.youtube.com/playlist?list=PLxxx" --name cs336

# B 站，单视频 / 季选集 / 合集都行，需要 cookies（看下面 § B 站 一节）
video-to-notebook crawl "https://www.bilibili.com/video/BVxxx/" --name vizuara-llm --cookies-from chrome

video-to-notebook tag      --ontology examples/ontology-llm.yaml --use-api  # 每门课约 $0.10
video-to-notebook cluster  --ontology examples/ontology-llm.yaml --use-api  # 每跑一次约 $0.30
video-to-notebook build
video-to-notebook serve    # http://localhost:4321
```

> `--use-api` 显式启用 Anthropic SDK 路径，不加就是默认的 in-session（路线 A）。

5 门课语料首跑总成本约 **$2–4**，重跑因每个 chunk 幂等，免费。

## 🏗 工作原理

所有状态都在 `.video-to-notebook/` 下的**单个 SQLite 文件**里，每个阶段从这个文件读写。各阶段是独立的 CLI 命令，任何一个都能单独重跑，不影响其它。

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/cbb6a6b5-3762-4184-9c5e-aec6e4e48c13" />

每个子命令都做到了**幂等可恢复**：

- 加一门新课，只有这门课被爬和打标
- 重跑 `cluster`，新出现的 proposed tags 会被处理，已决策的不动
- `build --incremental`，只重渲染变化的部分

**输出是静态站**，任何地方都能托管（GitHub Pages、S3、Vercel、Netlify、自建 nginx）。

## 📦 安装

```bash
# 1. Python CLI（3.12+）
pip install video-to-notebook
# 或：uv tool install video-to-notebook

# 2. 外部依赖
brew install node yt-dlp       # Node 20+ 给 HTML 构建；yt-dlp 给爬虫
playwright install chromium    # 仅 e2e 测试需要

# 3.（可选）无字幕视频的 Whisper 后备
pip install 'video-to-notebook[whisper]'   # macOS 上用 mlx-whisper，其它平台用 faster-whisper
```

### 🎤 爬没有字幕的视频

视频没有官方字幕时，给 `crawl` 加 `--whisper`，pipeline 会下载音频、本地转写（Apple Silicon 走 `mlx-whisper`，Linux / Windows 走 `faster-whisper`），把生成的 VTT 喂进同一套 chunk 流程。不要 API key，音频下载完不再有任何网络往返。

```bash
video-to-notebook crawl "https://www.bilibili.com/video/BV..." \
  --name my-course \
  --cookies-from edge \
  --whisper \
  --whisper-lang zh        # 可选：跳过自动检测，强指定中文
# 完成：12 个 OK，8 个通过 whisper，0 个没字幕，0 个错误
```

`--whisper-model` 可覆盖默认。mlx 默认是 **`mlx-community/whisper-large-v3-turbo`**：large-v3 的蒸馏版，权重约 800 MB，M 系列上接近 2× 实时。实测这是双语讲座的甜蜜点，能产出带自然标点的简体中文（`small` 模型容易吐繁体、丢标点）。对英文术语精度要求极高可改用 `--whisper-model mlx-community/whisper-large-v3-mlx`（约 3 GB，约 1× 实时）。faster-whisper 默认 `small`，传 `large-v3` 拿到同等质量。

### 📺 B 站：季选集 / 合集 加 cookie 鉴权

B 站爬虫接受三种 URL 形式，`crawl` 都能正确枚举：

| URL 形式 | 例子 | 行为 |
|---|---|---|
| 单视频（多 P） | `https://www.bilibili.com/video/BVxxx/` | 每个 `?p=N` 成为一节课 |
| 空间季选集 | `https://space.bilibili.com/<uid>/lists/<id>?type=season` | 每条是独立 BV，解析到对应的标准视频页 |
| 系列 / 合集 | `https://space.bilibili.com/<uid>/channel/seriesdetail?sid=<id>` | 同季选集 |

**鉴权**：B 站枚举播放列表和下载音频都要登录 cookie。两种方式：

```bash
# A) 从浏览器 session 读 cookie（如果能跑通，最省事）
video-to-notebook crawl "<bilibili-url>" --name <slug> --cookies-from chrome --whisper

# B) 用手动导出的 cookies.txt（移植性最好，绕开 macOS Keychain 阻止
#    yt-dlp 解 Chrome v10 cookie 的问题，也能对抗 B 站的反爬
#    （那个反爬会用 HTTP 412 把未鉴权请求挡掉）
video-to-notebook crawl "<bilibili-url>" --name <slug> \
    --cookies-file ~/path/to/bilibili-cookies.txt --whisper
```

走 B 路线需要装一个 Chrome 扩展，比如 **"Get cookies.txt LOCALLY"**，登录 `bilibili.com` 后导出 Netscape 格式 cookies。保存路径**避开** `~/Downloads`、`~/Desktop`、`~/Documents`（macOS 上这几个有 TCC 保护，yt-dlp 读不到），`~/note/`、`~/code/` 或 `~/Documents/` 的任何子文件夹（注意不是 `~/Documents/` 本身）都可以。

### 从 `course-merger`（v1.x）升级

**v2.0.0** 把项目从 `course-merger` 改名为 `video-to-notebook`。已有项目三条命令完成迁移，不需要重爬、不需要重打标，SQLite schema 没变：

```bash
# 在项目目录里
mv .course-merger .video-to-notebook       # 改 marker 目录名
uv tool upgrade video-to-notebook          # 或：pip install -U video-to-notebook
video-to-notebook build                    # 继续干活
```

`course-merger` 命令作为向后兼容 shim 保留，调用时打印一行 deprecation 提示后转发到 `video-to-notebook`，计划在 v3.0.0 移除。完整说明见 [`CHANGELOG.md`](CHANGELOG.md#200--2026-05-15)。

## 🤖 用 AI coding agent 驱动

每个 LLM 阶段默认就是两段式 in-session（v2.3+）：CLI 把待办工作以 JSON envelope 写到 `<state_dir>/prompts/<step>.json` 后退出；agent 读、推理、把决策 JSON 写到同目录的 `.decisions.json`；用 `--apply` 重跑一次就把结果应用到 SQLite。这套协议**和具体 agent 无关**，schema 与约定在 [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md)。

<table>
<tr>
<td width="50%" valign="top">

### 🟠 Claude Code

```bash
git clone https://github.com/LinZhuoChen/video-to-notebook.git
bash video-to-notebook/skills/video-to-notebook/scripts/install-locally.sh
```

然后在 Claude Code 里说：

> 用这几门课给我搭一个学习站：`<playlist1>` `<playlist2>` `<playlist3>`，本体用 `examples/ontology-llm.yaml`。

完整 skill 清单在 [`skills/video-to-notebook/SKILL.md`](skills/video-to-notebook/SKILL.md)。Claude Max 用户彻底不需要 Anthropic API key，in-session 流程覆盖 tag / cluster / curriculum / synthesize / explain 全部阶段。

</td>
<td width="50%" valign="top">

### 🔵 OpenAI Codex

```bash
git clone https://github.com/LinZhuoChen/video-to-notebook.git
cd my-study-site
bash video-to-notebook/skills/video-to-notebook/scripts/install-codex.sh
codex                  # Codex 读 AGENTS.md
```

或者全局装一份，让 Codex 在任意目录都能识别 video-to-notebook：

```bash
bash video-to-notebook/skills/video-to-notebook/scripts/install-codex.sh --global
```

Codex 读 [`AGENTS.md`](AGENTS.md)（对应 Claude 的 `CLAUDE.md`）和 [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md)，走同一套 in-session 流程。

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🟣 Cursor / Continue / Aider / 你自己的脚本

任何会读 JSON、推理、写 JSON 的 agent 都能驱动 pipeline。[`AGENTS.md`](AGENTS.md) 加 [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md) 这一对是契约，里面没有 Claude 专属假设。

写决策 envelope 时，把 agent-id 字段（`tagger_model_id`、`synthesizer` 等）填一个能标识来源的字符串：`cursor:v1`、`continue:v1`、`my-script:v1`。这些会持久化到 DB 方便审计。

</td>
<td width="50%" valign="top">

### ⚙️ 纯 API key 模式

不想用 agent 时，`export ANTHROPIC_API_KEY=...`，给 `tag` 和 `cluster` 加 `--use-api`。会直接走 Anthropic API（带 prompt caching），每门课约 $0.30–0.80。

教材生成阶段（`curriculum` / `synthesize` / `explain`）**只支持 in-session 模式**，它们是为 agent 的逐步推理设计的，不适合一次性 API 调用。

</td>
</tr>
</table>

### 📋 In-session 流程（任意 agent 通用，新默认）

```
agent 说    "爬这个播放列表，用 examples/ontology-llm.yaml 打标。"

CLI 循环：
  video-to-notebook init && video-to-notebook crawl <url>
  for batch in chunks_of(20):
    video-to-notebook tag --limit 20                # 写 prompts/tag.json
    agent 读 prompts/tag.json，
      写  prompts/tag.decisions.json
    video-to-notebook tag --apply
  video-to-notebook cluster                         # 写 prompts/cluster.json
  agent 读 + 写 prompts/cluster.decisions.json
  video-to-notebook cluster --apply
  curriculum / synthesize（逐章）/ explain（逐概念）同样的两段式
  video-to-notebook build
```

（端到端示例：[`examples/frontier-notebook/RUNBOOK.md`](examples/frontier-notebook/RUNBOOK.md)。）

### 成本与速度对比

|                          | API key 模式 | In-session 模式 |
|--------------------------|--------------|------------------|
| 需要 API key             | ✅ 是（`--use-api`） | ❌ 否            |
| 5 门课语料成本           | ~$2-4       | $0 额外（你 agent 的订阅已包） |
| 1000 chunk 速度          | ~5-10 分钟  | ~1-2 小时        |
| 100 chunk 速度           | ~30 秒      | ~5-10 分钟       |
| Curriculum / synthesize / explain | ❌ 不可用 | ✅ 仅此模式可用 |
| 最适合                   | 大语料一次性批跑 | 中小语料 + 教材生成 |

## 📖 教材生成（v1.2+）

跑完 `tag` 和 `cluster` 之后，把语料合成一本统一教材：

```bash
# 1. 在 Claude Code 里设计章节顺序（in-session）
video-to-notebook curriculum                              # 写 prompts/curriculum.json
# Claude 读它、设计章节顺序、写 prompts/curriculum.decisions.json
video-to-notebook curriculum --apply

# 2. agent 问你：整本批量做，还是一章一章来？
#    - 整本批量：循环跑完所有 N 章，每章生成后立即 apply，最后 build 一次。
#                适合已经信任风格之后的重跑。
#    - 一章一章：合成第 1 章 → build → 把控制权交还给你检查 /textbook/1/ →
#                给反馈后再做第 2 章。适合新语料的首跑。
# 3. 每一章（两种模式都一样）：
video-to-notebook synthesize --chapter N                  # 写 prompts/synthesize/chapter-N.json
# Agent 读 + 写 /tmp/chN.html，遵循 v3 风格指南：
#   - 顶部 TL;DR + 8–14 个编号小节（一二三四…）
#   - 逐步推导，每行带 **Why**: 注解
#   - 保留讲师所有独特比喻（不能塌缩成一个）
#   - 3–5 个 callout 块（info/note/warning/tip/quote）内嵌
#   - 工程细节做成 callout 内嵌，不延后讨论
#   - 引入模型时给完整 PyTorch 骨架
#   - 5–7 条 takeaway，锚定到讲师给的具体例子
#   - 目标正文长度：每章 5,000–8,000 中文字
video-to-notebook synthesize --chapter N --apply

# 4. 构建 + 查看
video-to-notebook build
video-to-notebook serve  # http://localhost:4321/textbook/
```

每章是自包含的 HTML 片段，含内嵌 SVG、CSS 动画、带时间戳的源视频 iframe、KaTeX 渲染的 LaTeX 数学、彩色 callout。v3 风格指南（`src/video_to_notebook/synthesize/prompts.py`）会注入"源材料保真加教科书深度"原则，任何驱动 pipeline 的 agent 都自动继承。

## 💡 概念百科（v1.3+）

线性教材给从头读的人用。概念百科给想就**单个**概念深挖的人用：

```bash
video-to-notebook explain --concept linear-algebra        # 写 prompts/explain/linear-algebra.json
# Claude 写 /tmp/la.html，遵循 v2 风格指南：
#   - 每个概念 CSS namespace 前缀（la-）
#   - 仅用 CSS 变量颜色（暗色模式 + 模块强调色都通用）
#   - 9 个固定章节顺序
#   - 3 种交互组件模板任选一
video-to-notebook explain --concept linear-algebra --apply

video-to-notebook build  # /concepts/<slug>/ 立刻有了图文详解
```

[`src/video_to_notebook/explain/prompts.py`](src/video_to_notebook/explain/prompts.py) 里的 v2 风格指南强制：

- **反偏见开场**：每个条目必须先指出一个常见误解然后纠正它
- **一不变量规则**：每个动画 / 交互只可视化一个不变量
- **等式链规则**：每个公式都要展示代入链（不准只说"可以推出 X"）
- **反例误区**：3 条误区每条都要附具体的数值或视觉反例
- **see-also 约束**：所有交叉链接 slug 都必须出现在 envelope 的 `related_concepts` 字段里

## 🎨 站点特性

构建出来的站点（`video-to-notebook build && video-to-notebook serve`）自带：

| 特性 | 干嘛用的 |
|---|---|
| 🌓 **暗色模式** | `html.dark` 类加 `prefers-color-scheme` 回退；header 切换按钮；`localStorage` 持久化 |
| 🎨 **每模块强调色** | 绿 / 蓝 / 紫 / 琥珀 / 玫红，通过 `data-module-idx` 范围化；卡片、侧栏、drop cap 都继承 |
| 📊 **章节 mini-map** | 右栏用 `IntersectionObserver` 跟踪 `h2`/`h3`；点击锚点滚动 |
| ⌨️ **键盘导航** | `←` / `→` 切换章节；输入框中失效；右下角浮动提示 |
| 📱 **移动端抽屉** | <900 px 显示汉堡按钮，左侧滑入；镜像教材侧栏；Esc / 背板点击关闭 |
| 🔍 **搜索** | 客户端 [Pagefind](https://pagefind.app/) |
| 🧮 **LaTeX 数学** | [KaTeX](https://katex.org/) 自动渲染 `$...$` 行内 / `$$...$$` 块级 |
| 🎬 **视频深链** | 每个概念页都列出源视频片段，带时间戳的 iframe |

## 💵 成本

每门课（50–100 段 lecture，约 1500 个 chunk）：

| 阶段 | 模型 | 成本 |
|------|------|------|
| Crawl | 无（yt-dlp） | $0 |
| Tag | Claude Haiku（prompt caching） | ~$0.10-0.30 |
| Cluster | Claude Sonnet | ~$0.20-0.50 |
| Curriculum | in-session Claude | $0 额外 |
| Synthesize（每章） | in-session Claude | $0 额外 |
| Explain（每概念） | in-session Claude | $0 额外 |
| Build | 无（Astro） | $0 |
| **每课总计** | | **~$0.30-0.80** |

5 门课语料首跑约 $2–4，重跑因每 chunk 幂等，免费。

## 📐 用自己的语料

`examples/frontier-notebook/` 是推荐起点：

```bash
cp -r examples/frontier-notebook examples/my-corpus
# 编辑 examples/my-corpus/courses.toml 和 examples/my-corpus/ontology.yaml
bash examples/my-corpus/build.sh
```

build 脚本串起 crawl / tag / cluster / build，读 `courses.toml`，最后把可用站点放到 `examples/my-corpus/.video-to-notebook-project/site/dist/`。

## 🗺 Roadmap

**已发布**

- v1.0：基础
- v1.1：in-session 模式
- v1.2：教材生成器
- v1.3：概念百科加设计系统打磨
- v1.4：多 agent 支持（Codex、Cursor、Continue 和 Claude Code 并列）
- v2.0：项目改名 `video-to-notebook`、源材料保真和教材深度纳入质量纪律、章节 chunk 选择回归 bug 修复、prompt 与 Astro UI 完整 zh / en i18n、每次 `build` 自动模板叠加同步
- v2.1：Whisper 后备，没有官方字幕的视频通过 `mlx-whisper`（Apple Silicon）或 `faster-whisper`（跨平台）本地转写，生成的 VTT 喂进同一套 chunk 流程
- **v2.1.1：B 站健壮支持**，季 / 合集 / 系列 URL 现在正确解析到每个 BV 对应的标准视频页（修复了所有条目变成同一段音频的静默去重 bug）；新增 `--cookies-file <path>` 接 Netscape 格式 cookies.txt，绕开 macOS Keychain 阻拦，对抗 B 站 412 反爬；在一门真实的 14 段视频、8 小时 B 站课上端到端验证（详见 [CHANGELOG.md](CHANGELOG.md)）

**未完成**

- [ ] **对比视图实时过滤**：客户端 `?courses=cs336,gpu-mode` 选择
- [ ] **`review` CLI**：给 `ambiguous` 聚类决策做人工分流
- [ ] **概念多语别名**：中英概念名独立对齐（目前 i18n 覆盖 UI 和生成正文，不覆盖 slug 级别的别名）

## 🏛 架构与设计

- 设计 spec：[`docs/specs/2026-05-09-video-to-notebook-skill-design.md`](docs/specs/2026-05-09-video-to-notebook-skill-design.md)
- 实施计划（TDD 拆解）：
  - Plan 1：[基础和爬虫](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md)
  - Plan 2：[Tag 和 Cluster](docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md)
  - Plan 3：[Build 和 HTML](docs/superpowers/plans/2026-05-09-plan-3-build-and-html.md)
  - Plan 4：[Demo、Deploy、Skill](docs/superpowers/plans/2026-05-09-plan-4-demo-deploy-skill.md)
  - Plan 6：[教材生成器](docs/superpowers/plans/2026-05-13-plan-6-textbook-generator.md)
  - Plan 7：[双语 demo](docs/superpowers/plans/2026-05-19-plan-7-bilingual-demo.md)

## ⚖️ 免责声明

`video-to-notebook` 是个**工具**。使用者自己负责，确保对喂进 pipeline 的内容拥有抓取、处理、再分发的权利。这包括 YouTube 和 B 站关于程序化访问内容的服务条款、原作者对讲座内容的授权、以及使用者所在司法辖区的合理使用 / 转化性使用判定。

工具作者对用户生成的内容免责。**个人学习风险普遍较低；公开再分发或商用合成内容则未必。** 超出个人使用范围前，请先核对源材料的授权条款。

## 🤝 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎 PR，尤其欢迎新爬虫适配器和非 AI / CS 领域的本体文件。

## 📄 License

[MIT](LICENSE)。

---

<div align="center">

由 🤖 加 ☕ 在 [chenlinzhuo](https://github.com/chenlinzhuo) 手中做出。
站在 [Claude Code](https://claude.com/claude-code)、[Astro](https://astro.build/)、[yt-dlp](https://github.com/yt-dlp/yt-dlp)、[Pagefind](https://pagefind.app/)、[KaTeX](https://katex.org/) 的肩膀上。

如果 `video-to-notebook` 帮你省下了一个本来要狂刷 YouTube 或 B 站的周末，欢迎点个 ⭐。

</div>
