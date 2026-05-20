<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo/lockup-dark.svg" />
  <img alt="video-to-notebook" src="assets/logo/lockup-light.svg" width="460" />
</picture>

**专为 Claude Code 与 OpenAI Codex 打造。** 把成串的公开课视频读成一份合并笔记——教材 + 概念百科，静态站一站搞定。

把同主题的几个 **YouTube 或 B 站** 播放列表喂给它。你的 coding agent 负责干活——爬视频、按你的本体把每个字幕片段打概念标签、聚类成干净的概念图、按教学法排出章节顺序、逐章逐概念把文章写出来。**不需要单独的 Anthropic API key**：所有 LLM 阶段都通过你 agent 现有的 Claude Code 或 Codex 订阅在会话里跑。开关一拨，Pagefind 搜索和双语（中文 / English）输出都自带。

[![CI](https://github.com/LinZhuoChen/video-to-notebook/actions/workflows/ci.yml/badge.svg)](https://github.com/LinZhuoChen/video-to-notebook/actions/workflows/ci.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Astro](https://img.shields.io/badge/Astro-5-FF5D01?logo=astro&logoColor=white)](https://astro.build/)
[![Built for Claude Code](https://img.shields.io/badge/built_for-Claude_Code-D97757?logo=anthropic&logoColor=white)](https://claude.com/claude-code)
[![Built for OpenAI Codex](https://img.shields.io/badge/built_for-OpenAI_Codex-10A37F?logo=openai&logoColor=white)](https://github.com/openai/codex)

[**在线 demo：Diffusion Models 教材**](https://linzhuochen.github.io/video-to-notebook/textbook/) · [**快速上手**](#-快速上手) · [**工作原理**](#-工作原理) · [**与 Claude Code / Codex / 任意 agent 配合**](#-用-ai-coding-agent-驱动) · [**Roadmap**](#-roadmap)

[English](README.md) · **中文**

---

</div>

> 🚧 **早期项目——遇到磕磕绊绊请上报。** `video-to-notebook` 处于活跃开发期；v2.0.0 是从 `course-merger` 重命名后的首个公开版。如果你撞上 bug、看见令人困惑的 prompt、生成出主题跑偏的章节、或者哪个爬虫在某个真实播放列表上罢工，请[**开一个 issue**](https://github.com/LinZhuoChen/video-to-notebook/issues/new/choose)，附上失败的命令和几行日志——这是修复速度最快的路径。也欢迎提交新需求、其它领域的本体文件，以及超出 YouTube + B 站之外（Coursera / edX / MIT-OCW……）的爬虫适配器。

## ✨ 你会得到什么

<table>
<tr>
<td width="50%" valign="top" align="center">
<a href="https://linzhuochen.github.io/video-to-notebook/textbook/">
  <img src="assets/screenshots/textbook-toc.png" alt="教材目录——5 个模块共 21 章" />
</a>
<sub><b>📖 教材目录</b>——21 章 / 5 个模块 / 按教学法排序</sub>
</td>
<td width="50%" valign="top" align="center">
<a href="https://linzhuochen.github.io/video-to-notebook/concepts/">
  <img src="assets/screenshots/concepts-grid.png" alt="概念百科——33 个图文详解" />
</a>
<sub><b>💡 概念百科</b>——33 个图文详解、每个模块独立强调色</sub>
</td>
</tr>
<tr>
<td colspan="2" align="center">
<a href="https://linzhuochen.github.io/video-to-notebook/textbook/1/">
  <img src="assets/screenshots/textbook-chapter.png" alt="章节阅读视图——左侧目录、TL;DR 块、右侧 mini-map、源视频深链" />
</a>
<sub><b>📐 章节阅读视图</b>——左侧目录 · TL;DR · 右侧 mini-map · 源视频深链</sub>
</td>
</tr>
</table>

## 🧭 设计原则

`video-to-notebook` 区别于"把播放列表喂给 ChatGPT 让它写个 summary"的三件事：

1. **源材料保真优先。** 每一章、每一个概念页都必须忠实传达讲师"实际是怎么讲"的——确切的类比、白板推导步骤、原话措辞、点过名的引用。你自己加的延伸要用显式的 `🟡 教材外补充` 标出来。两门课对同一概念给了不同比喻？两个都保留并标注。如果一个看过原视频的读者认不出这一章，说明系统过度概括了。

2. **不准编造——卡住就回去 debug pipeline。** 当某一章的源 chunk 凑得很稀（比如 20 个全是课程后勤闲聊，或者按字母序靠前的某门课吃掉了 LIMIT），agent 必须**停下来诊断**，而不是用训练数据里的知识糊弄过去。常见 bug：chunk 选择 SQL 写成 `LIMIT 20 ORDER BY course_slug`（已通过深度优先分配修复）、按讲座标题关键词匹配但概念本身没被讨论、`--max-source-chunks` 太低。

3. **教科书级笔记深度，不是杂志摘要深度。** 每章目标 5,000–8,000 中文字，包含：TL;DR 块、8–14 个编号小节（一二三四……）、每行带 `**Why**:` 注解的逐步公式推导、所有讲师独特类比都保留、3–5 个不同色 callout（info/note/warning/tip/quote）、工程细节内嵌成 callout 而不是延后讨论、引入模型时给完整可运行的 PyTorch 骨架、5–7 条锚定到讲师具体例子的 takeaway。低于 4,000 字 = 没写够。

这三条规则写进了 [synthesize](src/video_to_notebook/synthesize/prompts.py) 和 [explain](src/video_to_notebook/explain/prompts.py) 的风格指南——任何驱动 pipeline 的 agent 都会自动继承。

## 📸 功能展示

<table>
<tr>
<td width="50%" valign="top">

### 📖 合并教材

章节按教学法编排——小白从头读到尾能拿到一条完整弧线，不是一堆碎片化的片段。

- 内嵌 SVG 图 + CSS 动画
- KaTeX 渲染 LaTeX 数学公式
- 带时间戳的源视频片段嵌入
- 反偏见开场 + 每章 3 条 takeaway
- ← / → 键盘翻章 · 📊 侧栏 mini-map

</td>
<td width="50%" valign="top">

### 💡 概念百科

每个重要概念都有自己的丰富页面——给想就某一概念深挖的读者。

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

### 🌓 暗色模式 + 每模块强调色

```
Module 1  · 数学直觉              🟢 绿
Module 2  · 训练直觉              🔵 蓝
Module 3  · 视觉起源              🟣 紫
Module 4  · 现代深度学习          🟡 琥珀
Module 5  · 现代架构与未来         🌸 玫红
```

通过 `data-module-idx` 自动应用到布局根节点。卡片、侧栏、drop cap、进度条都继承 `--module-accent`。

</td>
<td width="50%" valign="top">

### 📱 移动端优先，不依赖 JS 框架

```
@media (max-width: 900px)
  → 左侧滑入式汉堡抽屉
  → 抽屉镜像教材侧栏
  → 阅读列展开占满视窗
```

没有 React、没有 Vue。Astro + 200 行原生 JS。一个概念页（含 SVG + 交互）gzipped 仅 ~30 KB。

</td>
</tr>
</table>

## 🚀 快速上手

### 路线 A——不要 API key，靠 AI agent 驱动

每个 LLM 阶段（`tag` / `cluster` / `curriculum` / `synthesize` / `explain`）都有 `--print-prompts` / `--apply-results` 两个标志。在 **Claude Code**、**OpenAI Codex**、**Cursor**、**Continue** 或你自己的脚本里驱动整套 pipeline——不需要单独的 API key。详见下面 [**§ 用 AI coding agent 驱动**](#-用-ai-coding-agent-驱动) 段落。

### 路线 B——配 Anthropic API key

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

# B 站——单视频、季选集、合集都行。需要 cookies（看下面 § B 站 一节）
video-to-notebook crawl "https://www.bilibili.com/video/BVxxx/" --name vizuara-llm --cookies-from chrome

video-to-notebook tag      --ontology examples/ontology-llm.yaml  # 每门课 ~$0.10
video-to-notebook cluster  --ontology examples/ontology-llm.yaml  # 每跑一次 ~$0.30
video-to-notebook build
video-to-notebook serve    # http://localhost:4321
```

5 门课的语料首跑总成本：**~$2-4**，重跑 **$0**（每个 chunk 幂等）。

## 🏗 工作原理

所有东西都围着 `.video-to-notebook/` 下的**一个 SQLite 文件**转——每个阶段都从这个文件读、向它写。各阶段是独立 CLI 命令，所以你可以单独重跑任何一个而不影响其它。

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/cbb6a6b5-3762-4184-9c5e-aec6e4e48c13" />

每个子命令都**幂等 + 可恢复**：

- 加一门新课 → 只有这门课被爬 / 打标
- 重跑 `cluster` → 接住新出现的 proposed tags，不重新处理已决策好的
- `build --incremental` → 只重新渲染发生变化的部分

**输出是静态站**——任何地方都能托管（GitHub Pages、S3、Vercel、Netlify、自家 nginx）。

## 📦 安装

```bash
# 1. Python CLI（3.12+）
pip install video-to-notebook
# 或：uv tool install video-to-notebook

# 2. 外部依赖
brew install node yt-dlp       # Node 20+ 给 HTML 构建；yt-dlp 给爬虫
playwright install chromium    # 仅 e2e 测试需要

# 3.（可选）给无字幕视频准备的 Whisper 后备
pip install 'video-to-notebook[whisper]'   # macOS 上用 mlx-whisper，其它平台用 faster-whisper
```

### 🎤 爬没有字幕的视频

视频没有官方字幕时，给 `crawl` 加 `--whisper` 标志，pipeline 会下载音频、本地转写（Apple Silicon 上用 `mlx-whisper`，Linux/Windows 上用 `faster-whisper`），把生成的 VTT 喂进同一套 chunk 流程。不要 API key、音频下载后没有任何网络往返。

```bash
video-to-notebook crawl "https://www.bilibili.com/video/BV..." \
  --name my-course \
  --cookies-from edge \
  --whisper \
  --whisper-lang zh        # 可选：跳过自动检测，强指定中文
# 完成：12 个 OK，8 个通过 whisper，0 个没字幕，0 个错误
```

`--whisper-model` 可覆盖默认。mlx 上默认是 **`mlx-community/whisper-large-v3-turbo`**——large-v3 蒸馏版，~800 MB 权重，M 系列上 ~2× 实时。经验上这是双语讲座的甜蜜区：能产出带自然标点的简体中文（对比 `small` 倾向于吐繁体中文、丢标点）。如果对英文专业术语精度要求极高，传 `--whisper-model mlx-community/whisper-large-v3-mlx`（~3 GB，~1× 实时）。faster-whisper 上默认是 `small`；传 `large-v3` 拿到同等质量提升。

### 📺 B 站：季选集 / 合集 + cookie 鉴权

B 站爬虫接受三种 URL 形式，全都被 `crawl` 正确枚举：

| URL 形式 | 例子 | 行为 |
|---|---|---|
| 单视频（多 P） | `https://www.bilibili.com/video/BVxxx/` | 每个 `?p=N` 成为一节课 |
| 空间季选集 | `https://space.bilibili.com/<uid>/lists/<id>?type=season` | 每条是一个独立 BV，解析到对应的标准视频页 |
| 系列 / 合集 | `https://space.bilibili.com/<uid>/channel/seriesdetail?sid=<id>` | 同季选集 |

**鉴权**：B 站对枚举播放列表 + 下载音频都要求登录 cookie。两种方式：

```bash
# A) 从浏览器 session 读 cookie（如果能跑通，最省事）
video-to-notebook crawl "<bilibili-url>" --name <slug> --cookies-from chrome --whisper

# B) 用手动导出的 cookies.txt（移植性最好——绕开 macOS Keychain 阻止
#    yt-dlp 解 Chrome v10 cookie 的问题，也能对抗 B 站的反爬
#    （那个反爬会用 HTTP 412 把未鉴权请求挡掉）
video-to-notebook crawl "<bilibili-url>" --name <slug> \
    --cookies-file ~/path/to/bilibili-cookies.txt --whisper
```

走 B 路线的话，装个 Chrome 扩展比如 **"Get cookies.txt LOCALLY"**，登录 `bilibili.com` 后导出 Netscape 格式的 cookies。保存路径**避开** `~/Downloads`、`~/Desktop`、`~/Documents`（这几个在 macOS 上有 TCC 保护，yt-dlp 读不到）——`~/note/`、`~/code/` 或 `~/Documents/` 的任何子文件夹（注意不是 `~/Documents/` 本身）都行。

### 从 `course-merger`（v1.x）升级？

**v2.0.0** 把项目从 `course-merger` 改名为 `video-to-notebook`。已有项目三条命令迁移完——不需要重爬、不需要重打标，SQLite schema 没变：

```bash
# 在项目目录里
mv .course-merger .video-to-notebook       # 改 marker 目录名
uv tool upgrade video-to-notebook          # 或：pip install -U video-to-notebook
video-to-notebook build                    # 继续干活
```

`course-merger` 命令仍作为向后兼容 shim 存在——打印一行 deprecation 提示再转发到 `video-to-notebook`。计划在 v3.0.0 移除。完整 rationale 见 [`CHANGELOG.md`](CHANGELOG.md#200--2026-05-15)。

## 🤖 用 AI coding agent 驱动

每个 LLM 阶段都支持 **`--print-prompts` / `--apply-results`** 两段式流程。CLI 把待办工作以 JSON envelope 输出到 stdout；agent 读、推理、写一份结果 JSON；CLI 把结果应用到 SQLite。这套协议是**与 agent 无关的**——schema 和约定都在 [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md) 里。

<table>
<tr>
<td width="50%" valign="top">

### 🟠 Claude Code

```bash
git clone https://github.com/LinZhuoChen/video-to-notebook.git
bash video-to-notebook/skills/video-to-notebook/scripts/install-locally.sh
```

然后在 Claude Code 里：

> 用这几门课给我搭一个学习站：`<playlist1>` `<playlist2>` `<playlist3>`，用 `examples/ontology-llm.yaml`。

完整 skill 清单在 [`skills/video-to-notebook/SKILL.md`](skills/video-to-notebook/SKILL.md)。Claude Max 用户彻底不需要 Anthropic API key——in-session 流程覆盖 tag/cluster/curriculum/synthesize/explain。

</td>
<td width="50%" valign="top">

### 🔵 OpenAI Codex

```bash
git clone https://github.com/LinZhuoChen/video-to-notebook.git
cd my-study-site
bash video-to-notebook/skills/video-to-notebook/scripts/install-codex.sh
codex                  # Codex 读 AGENTS.md
```

或者全局装一份，让 Codex 在任意目录都知道 video-to-notebook：

```bash
bash video-to-notebook/skills/video-to-notebook/scripts/install-codex.sh --global
```

Codex 读 [`AGENTS.md`](AGENTS.md)（Codex 的 CLAUDE.md 对应物）和 [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md)。同一套 in-session 流程。

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🟣 Cursor / Continue / Aider / 你自己的脚本

任何会读 JSON、推理、写 JSON 的 agent 都能驱动 pipeline。[`AGENTS.md`](AGENTS.md) + [`docs/AGENT_PROTOCOL.md`](docs/AGENT_PROTOCOL.md) 这一对是契约——没有 Claude 专属假设。

写结果 envelope 时给 agent-id 字段（`tagger_model_id`、`synthesizer` 等）填一个能标识你的字符串——`cursor:v1`、`continue:v1`、`my-script:v1`。会持久化到 DB，方便审计。

</td>
<td width="50%" valign="top">

### ⚙️ 纯 API key

如果你不用 agent，直接 `export ANTHROPIC_API_KEY=...`，然后 `tag` + `cluster` 都不加 `--print-prompts` 跑。它们会直接调用 Anthropic API（带 prompt caching），每门课 ~$0.30-0.80。

教材生成阶段（`curriculum` / `synthesize` / `explain`）目前**仅支持 in-session 模式**——它们是为 agent 的逐步推理设计的，不适合一次性 API 调用。

</td>
</tr>
</table>

### 📋 In-session 流程（任意 agent 通用）

```
agent 说    "爬这个播放列表，用 examples/ontology-llm.yaml 打标。"

CLI 循环：
  video-to-notebook init && video-to-notebook crawl <url>
  for batch in chunks_of(20):
    video-to-notebook tag --print-prompts --limit 20 > p.json
    agent 读 p.json、写 r.json
    video-to-notebook tag --apply-results r.json
  video-to-notebook cluster --print-prompts > c.json
  agent 读 c.json、写 c-apply.json
  video-to-notebook cluster --apply-results c-apply.json
  curriculum / synthesize（逐章）/ explain（逐概念）同样的两段式
  video-to-notebook build
```

### 成本与速度取舍

|                          | API key 模式 | In-session 模式 |
|--------------------------|--------------|------------------|
| 需要 API key             | ✅ 是        | ❌ 否            |
| 5 门课语料成本           | ~$2-4       | $0 额外（你 agent 的订阅已包） |
| 1000 chunk 速度          | ~5-10 分钟  | ~1-2 小时        |
| 100 chunk 速度           | ~30 秒      | ~5-10 分钟       |
| Curriculum / synthesize / explain | ❌ 不可用 | ✅ 仅此模式可用 |
| 最适合                   | 大语料一次性批跑 | 中小语料 + 教材生成 |

## 📖 教材生成（v1.2+）

跑完 `tag` + `cluster` 后，把语料合成一本统一的教材：

```bash
# 1. 在 Claude Code 里设计章节顺序（in-session）
video-to-notebook curriculum --print-prompts > curr.json
# Claude 读 curr.json、设计章节顺序、写 curr-results.json
video-to-notebook curriculum --apply-results curr-results.json

# 2. agent 问你：整本批量做，还是一章一章来？
#    - 整本批量：循环跑完所有 N 章，每章生成后立即 apply，最后 build 一次。
#                适合你已经信任风格之后的重跑。
#    - 一章一章：合成第 1 章 → build → 把控制权交还给你检查 /textbook/1/ →
#                给反馈后再做第 2 章。适合新语料的首跑。
# 3. 每一章（两种模式都一样）：
video-to-notebook synthesize --chapter N --print-prompts > chN.json
# Agent 读 + 写 /tmp/chN.html，遵循 v3 风格指南：
#   - 顶部 TL;DR + 8–14 个编号小节（一二三四……）
#   - 逐步推导，每行带 **Why**: 注解
#   - 所有讲师独特类比都保留（不能塌缩成一个）
#   - 3–5 个 callout 块（info/note/warning/tip/quote）内嵌
#   - 工程细节做成 callout 内嵌，不延后讨论
#   - 引入模型时给完整 PyTorch 骨架
#   - 5–7 条 takeaway，锚定到讲师给的具体例子
#   - 目标正文长度：每章 5,000–8,000 中文字
video-to-notebook synthesize --chapter N --apply-results apply-chN.json

# 4. 构建 + 查看
video-to-notebook build
video-to-notebook serve  # http://localhost:4321/textbook/
```

每一章都是自包含的 HTML 片段，含内嵌 SVG、CSS 动画、带时间戳的源视频 iframe、LaTeX 数学（KaTeX 渲染）、彩色 callout 块。v3 风格指南（`src/video_to_notebook/synthesize/prompts.py`）自动注入"源材料保真 + 教科书深度"原则——任何驱动 pipeline 的 agent 都会继承。

## 💡 概念百科（v1.3+）

线性教材给首次阅读者用。概念百科给想就**单个**概念深入的人用：

```bash
video-to-notebook explain --concept linear-algebra --print-prompts > la.json
# Claude 写 /tmp/la.html，遵循 v2 风格指南：
#   - 每个概念 CSS namespace 前缀（la-）
#   - 仅用 CSS 变量颜色（暗色模式 + 模块强调色都通用）
#   - 9 个固定章节顺序
#   - 3 种交互组件模板任选一
video-to-notebook explain --concept linear-algebra --apply-results la-results.json

video-to-notebook build  # /concepts/<slug>/ 立刻有了图文详解
```

[`src/video_to_notebook/explain/prompts.py`](src/video_to_notebook/explain/prompts.py) 里的 v2 风格指南强制：

- **反偏见开场** 每个条目必须从指出一个常见误解然后纠正它开始
- **一不变量规则** 每个动画/交互必须可视化恰好一个不变量
- **等式链规则** 每个公式都要展示代入链（不准"可以推出 X"）
- **反例误区** 3 条误区中每条都要有具体的数值或视觉反例
- **see-also 约束** 所有交叉链接 slug 都必须存在于 envelope 的 `related_concepts` 字段里

## 🎨 站点特性

构建出来的站点（`video-to-notebook build && video-to-notebook serve`）自带：

| 特性 | 干嘛用的 |
|---|---|
| 🌓 **暗色模式** | `html.dark` 类 + `prefers-color-scheme` 回退；header 切换按钮；`localStorage` 持久化 |
| 🎨 **每模块强调色** | 绿 / 蓝 / 紫 / 琥珀 / 玫红，通过 `data-module-idx` 范围化；卡片、侧栏、drop cap 都继承 |
| 📊 **章节 mini-map** | 右栏用 `IntersectionObserver` 跟踪 `h2`/`h3`；点击锚点滚动 |
| ⌨️ **键盘导航** | `←` / `→` 切换章节；输入框中失效；右下角浮动提示 |
| 📱 **移动端抽屉** | <900 px 显示汉堡按钮，左侧滑入；镜像教材侧栏；Esc / 背板点击关闭 |
| 🔍 **搜索** | 客户端 [Pagefind](https://pagefind.app/) |
| 🧮 **LaTeX 数学** | [KaTeX](https://katex.org/) 自动渲染 `$...$` 行内 / `$$...$$` 块级 |
| 🎬 **视频深链** | 每个概念页都列出源视频片段，带时间戳的 iframe |

## 💵 成本现实

每门课（50-100 个 lecture，~1500 个 chunk）：

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

5 门课的语料首跑 ~$2-4。重跑因为每 chunk 幂等，所以免费。

## 📐 给你的语料定制

`examples/frontier-notebook/` 目录是推荐起点：

```bash
cp -r examples/frontier-notebook examples/my-corpus
# 编辑 examples/my-corpus/courses.toml 和 examples/my-corpus/ontology.yaml
bash examples/my-corpus/build.sh
```

build 脚本会串起 crawl / tag / cluster / build，读 `courses.toml`，最后把可用的站点放到 `examples/my-corpus/.video-to-notebook-project/site/dist/`。

## 🗺 Roadmap

**已发布：** v1.0 基础 · v1.1 in-session 模式 · v1.2 教材生成器 · v1.3 概念百科 + 设计系统打磨 · v1.4 多 agent 支持（Codex + Cursor + Continue 与 Claude Code 并列） · v2.0 项目重命名为 `video-to-notebook`、源材料保真 + 教材深度质量纪律、章节 chunk 选择回归 bug 修复、prompt + Astro UI 完整 zh/en i18n、每次 `build` 自动模板叠加同步 · v2.1 Whisper 后备——没有官方字幕的视频通过 `mlx-whisper`（Apple Silicon）或 `faster-whisper`（跨平台）本地转写，生成的 VTT 喂进同一套 chunk 流程 · **v2.1.1 健壮 B 站支持**——季 / 合集 / 系列 URL 现在正确解析到每个 BV 的标准视频页（修复了所有条目变成同一段音频的静默去重 bug）；新增 `--cookies-file <path>` 接 Netscape 格式 cookies.txt，绕开 macOS Keychain 阻止 + 抗 B 站 412 反爬；在一门真实的 14 段视频 / 8 小时 B 站课上端到端测过（详见 [CHANGELOG.md](CHANGELOG.md)）。

**未完成：**
- [ ] **对比视图实时过滤** 客户端 `?courses=cs336,gpu-mode` 选择
- [ ] **`review` CLI** 给 `ambiguous` 聚类决策做人工分流
- [ ] **概念多语别名** 中英概念名独立对齐（目前的 i18n 覆盖 UI + 生成正文，不覆盖 slug 级别的别名）

## 🏛 架构与设计

- 设计 spec：[`docs/specs/2026-05-09-video-to-notebook-skill-design.md`](docs/specs/2026-05-09-video-to-notebook-skill-design.md)
- 实施计划（TDD 拆解）：
  - Plan 1：[基础 + 爬虫](docs/superpowers/plans/2026-05-09-plan-1-foundation-and-crawl.md)
  - Plan 2：[Tag + Cluster](docs/superpowers/plans/2026-05-09-plan-2-tag-and-cluster.md)
  - Plan 3：[Build + HTML](docs/superpowers/plans/2026-05-09-plan-3-build-and-html.md)
  - Plan 4：[Demo + Deploy + Skill](docs/superpowers/plans/2026-05-09-plan-4-demo-deploy-skill.md)
  - Plan 6：[教材生成器](docs/superpowers/plans/2026-05-13-plan-6-textbook-generator.md)
  - Plan 7：[双语 demo](docs/superpowers/plans/2026-05-19-plan-7-bilingual-demo.md)

## ⚖️ 免责声明

`video-to-notebook` 是个**工具**。使用者负责确保对喂进这套 pipeline 的内容拥有抓取、处理、再分发的权利。包括 YouTube / B 站 关于程序化访问内容的服务条款、原创作者对讲座内容的授权、以及使用者所在司法辖区的合理使用 / 转化性使用判定。

工具作者对用户生成的内容免责。**个人学习用风险普遍较低。公开再分发或商用合成内容可能不低。** 超出个人使用范围前，请查阅源材料的授权条款。

## 🤝 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎 PR——尤其欢迎新爬虫适配器、非 AI/CS 领域的本体文件。

## 📄 License

[MIT](LICENSE)——详情见文件。

---

<div align="center">

由 🤖 + ☕ 在 [chenlinzhuo](https://github.com/chenlinzhuo) 手中做出。
站在 [Claude Code](https://claude.com/claude-code)、[Astro](https://astro.build/)、[yt-dlp](https://github.com/yt-dlp/yt-dlp)、[Pagefind](https://pagefind.app/)、[KaTeX](https://katex.org/) 的肩膀上。

如果 `video-to-notebook` 帮你省下了一个用来狂刷 YouTube / B 站 的周末，就在 GitHub 上点个 ⭐。

</div>
