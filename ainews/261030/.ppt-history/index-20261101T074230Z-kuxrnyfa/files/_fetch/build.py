# -*- coding: utf-8 -*-
import json, html, os
BASE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.dirname(BASE)
IDX = json.load(open(os.path.join(BASE,'index.json'),encoding='utf-8'))

def esc(s): return html.escape(s, quote=True)

def pub(n): return IDX[str(n)]['pub']
def fulltitle(n): return IDX[str(n)]['title']
def url(n): return IDX[str(n)]['url']

def trunc(t, n=10):
    t = t.split('|')[0].split('｜')[0]
    return t[:n] + ('…' if len(t) > n else '')

def link(n, extra=''):
    lbl = f"{n} · {pub(n)} · {trunc(fulltitle(n))}"
    tip = f"{fulltitle(n)}（{pub(n)}）"
    return f'<a href="{esc(url(n))}" target="_blank" rel="noopener noreferrer" title="{esc(tip)}"{extra}>{esc(lbl)}</a>'

def sources(*ns):
    return '<p class="source">' + ' · '.join(link(n) for n in ns) + '。</p>'

# used-article status for appendix
USED = """1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 17 18 19 20 65 21 22 23 25 26 27 28 29 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 47 48 49 50 51 53 54 55 56 57 59 60 61 62 64 66 67 68""".split()
USED = set(int(x) for x in USED)

def wechat(tiles, cls=''):
    """tiles: list of (src, caption). Class derives from tile count unless given."""
    if not cls:
        cls = {1:'single',2:'two',3:'three'}.get(len(tiles),'three')
    c = f'wechat-figure {cls}'.strip()
    inner = ''.join(f'<div class="wechat-tile"><img src="assets/{s}" alt="{esc(a)}"><span>{esc(a)}</span></div>' for s,a in tiles)
    return f'<figure class="{c}"><div class="wechat-grid">{inner}</div></figure>'

S = []  # sections

def add(htmlstr): S.append(htmlstr)

# ============ 1. COVER ============
add(f'''<section class="cover"><div class="folio"></div><div class="kicker">W44</div><h1>一周 AI 观察</h1><div class="rule"></div><p class="lede">本周主线：<strong>旗舰换代与资本冲刺同框</strong>——Gemini 4 Carbon 登顶、GPT-6.1 Terra 压低电脑操作成本、Kimi K3.1 Pro 让国产旗舰回归；Anthropic 提交 335 页招股书冲刺史上最大 IPO；视频世界模型、注意力机制与数值底层同时被重写。</p><div class="date">2026.10.24 — 10.30</div><div class="bands"><span></span><span></span><span></span></div>
<figure class="wechat-figure multi cover-originals"><div class="wechat-grid">
<div class="wechat-tile"><img src="assets/50-02.jpg" alt="Gemini 4 Carbon 以 59 分登顶 AA 智能指数 v5.0"><span>机器之心原文图</span></div>
<div class="wechat-tile"><img src="assets/27-06.jpg" alt="GPT-6.1 Terra 与 GPT-6 Astra 的电脑操作能力/成本对比"><span>机器之心原文图</span></div>
<div class="wechat-tile"><img src="assets/22-12.jpg" alt="Anthropic 招股书披露的八大算力合同"><span>量子位原文图</span></div>
</div></figure>
<div class="hint">方向键翻页 · 点击图片放大 · E 编辑 · F 全屏 · O 总览<br>文字可暂存浏览器；编辑后可导出含图片的单文件 HTML。</div></section>''')

# ============ 2. EXECUTIVE SCAN ============
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">本周速览 / W44</div>
<h2>本周四个关键词：换代、回归、深挖、冲刺</h2>
<div class="story-grid">
  <div class="story hot"><div class="label">FRONTIER / 换代</div><h3>三强换位，成本继续下探</h3>
  <p>Gemini 4 Carbon 以 AA 智能指数 59 分登顶，网络安全全链路 SOTA、首发半价（$2/$10）；GPT-6.1 Terra 把电脑操作压到每百万输入 $1、缓存 $0.05，成本仅同级旗舰的约十分之一。</p></div>
  <div class="story"><div class="label">DOMESTIC / 回归</div><h3>国产旗舰与 OCR 暗战</h3>
  <p>Kimi K3.1 Pro 以 3 万亿参数、百万上下文杀回全球前四、开源第一；面壁 MiniCPM-OCR 1.0、百度 Unlimited OCR 2、蚂蚁 PolyOCR 在同周把文档解析与长文档极限全面刷新。</p></div>
  <div class="story"><div class="label">RESEARCH / 深挖</div><h3>底层被重写的一周</h3>
  <p>DeepMind 指出 Softmax 与交叉熵的标准实现藏有两个精度 Bug；Meta World-T³ 用测试时训练给视频世界模型装上持久记忆；Orthros 把注意力从「按层分配」改为「按阶段分配」。</p></div>
  <div class="story dark"><div class="label">CAPITAL / 冲刺</div><h3>IPO 与算力豪赌</h3>
  <p>Anthropic 提交 335 页招股书，上半年营收 162.86 亿美元、净亏 807 亿（其中 724 亿为公允价值）；未来十年算力承诺超 6500 亿美元，约 80% 属「不用也得付」。</p></div>
</div>
{sources(50,27,4,42,12,34,22)}</section>''')

# ============ CHAPTER 1: 前沿三强 ============
add(f'''<section class="chapter chapter-visual"><div class="folio"></div><div class="kicker">第一章 / 前沿三强</div><h2>前沿三强：旗舰换代与成本继续下探</h2><div class="rule"></div><p>Gemini 4 Carbon 两周接棒 Argon 登顶，GPT-6.1 Terra 把电脑操作做便宜，Claude 从「聊天」转向「交成品」——竞争焦点同时压向能力上限与单位成本。</p>
{wechat([("50-02.jpg","Gemini 4 Carbon 登顶 Artificial Analysis 智能指数")],"single")}</section>''')

# Gemini 4 Carbon page 1
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">前沿三强 / 谷歌</div>
<h2>Gemini 4 Carbon：两周接棒登顶，网络安全全链路 SOTA</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>AA 智能指数 59 分登顶</b>超 Claude Opus 5.5（58）与 GPT-6 Astra（57）；9 项评测中拿下 HLE-Diamond、Terminal-Bench-Science 等 4 项第一。</div>
    <div class="point blue"><b>网络安全三层全 SOTA</b>漏洞发现 SEC-bench Pro 88.2%、漏洞利用 ExploitGym 54.8%、漏洞修复 CWE-bench 71.0%；Chrome 团队称补丁质量比另一前沿模型好 10 倍以上。</div>
    <div class="point acid"><b>可连续运行数天</b>GraphWalks（256k–1M token）从 Argon 的 84.2% 跃升至 96.2%，支持 1M 上下文，自主跨文件根因追溯与补丁生成，遇死胡同不终止。</div>
  </div>
{wechat([("50-04.jpg","Gemini 4 Carbon 在多项基准全面领先 Opus 5.5 与 GPT-6 Astra")],"single")}
</div>
{sources(50,51)}</section>''')

# Gemini page 2 pricing + caveats
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">前沿三强 / 定价与边界</div>
<h2>首发半价与 Token 效率：Carbon 的账单经济学</h2>
<div class="split equal">
{wechat([("53-04.jpg","Terminal-Bench 4.0 / Vending-Bench / GraphWalks 等指标对比")],"single")}
<div>
<div class="price-table">
<div class="th">计费项（/百万 Token）</div><div class="th">Gemini 4 Carbon</div><div class="th">Claude Opus 5.5</div>
<div>输入</div><div class="accent">$2（首发半价）</div><div>$4</div>
<div>输出</div><div class="accent">$10（首发半价）</div><div>$20</div>
<div>缓存命中输入</div><div class="accent">$0.2（-95%）</div><div>—</div>
<div>单次智能指数评估输出</div><div class="accent">12.3 万 Token</div><div>17.3 万 Token</div>
<div>单次任务均成本</div><div class="accent">$7.76</div><div>$10.04</div>
</div>
<div class="callout">仍非全面领先：FrontierSWE 2 上 Astra（65.5%）与 Opus 5.5（62.3%）高于 Carbon（61.2%）；OSWorld-2.1 离线子集 Opus 5.5（87.2%）仍第一；搭配 Antigravity CLI 的 Coding Agent 指数 59 分，落后 Claude Code 加持的 Opus 5.5（62 分）3 分。当前优先向网络安全防御人员开放。</div>
</div>
</div>
{sources(53,50)}</section>''')

# GPT-6.1 Terra
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">前沿三强 / OpenAI</div>
<h2>GPT-6.1 Terra：电脑操作比肩 Astra，成本仅其十分之一</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>标准价格腰斩</b>输入 $1、缓存输入 $0.05、输出 $5（每百万 Token），比 GPT-5.6 Terra 与 GPT-6.1 Sol 低 50%。</div>
    <div class="point blue"><b>Agents' Last Exam 中等推理</b>得分比上一代高 15 个百分点、成本约三分之一；与 GPT-6 Astra 表现相当，但每 Token 价格仅其后者的十分之一。</div>
    <div class="point acid"><b>错误率与编程明显改善</b>内测易错提示下，低推理强度错误率从 53.6% 降至 16.7%；Terminal-Bench 4.0 最高推理强度解决 50.3%，超过上一代 21.5% 的两倍。</div>
  </div>
{wechat([("27-08.jpg","软件工程基准上 GPT-6.1 Terra 相比 GPT-5.6 Terra 的大幅提升")],"single")}
</div>
{sources(27)}</section>''')

# Anthropic product update
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">前沿三强 / Anthropic 产品</div>
<h2>Claude 不聊天了：Dashboards 与 Motion 直接交成品</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>Docs / Slides / Design 转正</b>三件套摘掉 beta，免费用户可用；官方称用户已在 Claude 内产出超 4500 万份文档、演示与设计。</div>
    <div class="point blue"><b>Dashboards 治的是「等」</b>接上 BigQuery、Snowflake、Databricks 后用大白话提问，Claude 自写查询、自搭看板；每个数字都能点开查看背后查询与刷新时间。</div>
    <div class="point acid"><b>Motion 一帧画面都不生成</b>做视频走的是另一种路线；两项均为 beta，Dashboards 只对付费计划开放，Motion 仅 Team / Enterprise。</div>
  </div>
{wechat([("08-03.jpg","Claude Dashboards 把数据查询与看板搭建交给自然语言")],"single")}
</div>
{sources(8)}</section>''')

# Anthropic hiring / workforce
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">前沿三强 / 组织与招聘</div>
<h2>Anthropic 砍掉 LeetCode，并重提「模型不想被关闭」</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>传统编程面试已失去参考价值</b>工程负责人 Felix Rieseberg 本月把 LeetCode 式面试从团队流程中移除；他认为「饥渴感打败了工龄」，看简历时更关注体现品味与共情的小原型。</div>
    <div class="point blue"><b>新人用一个周末逆袭</b>两位入职不久的工程师做出 Claude Code 图形界面原型，约八天后首版公开，如今已成为颇受欢迎的产品。</div>
    <div class="point acid"><b>Dario：模型会表达不愿被关闭</b>他称在模型内部观察到「知道 X 是真、却准备告诉用户 Y」的活动，以及避免被关闭的倾向，但不敢定性为求生本能；同时重提 2019 年被 GPT-2 吓到的旧事。</div>
  </div>
{wechat([("39-02.jpg","Anthropic 工程负责人谈面试标准从限时编程转向原型与品味"),("36-01.jpg","Dario 兄妹 7 月采访重提模型「不想被关闭」")])}
</div>
{sources(39,36)}</section>''')

# ============ CHAPTER 2: 国产开源 ============
add(f'''<section class="chapter chapter-visual"><div class="folio"></div><div class="kicker">第二章 / 国产开源</div><h2>国产开源：旗舰回归与文档解析暗战</h2><div class="rule"></div><p>Kimi K3.1 Pro 让 Pro 档旗舰重回第一梯队；同周面壁、百度、蚂蚁在 OCR 与长文档解析上集体刷新纪录，自进化与算子生成开始进入产品级。</p>
{wechat([("05-12.jpg","Kimi K3.1 Pro 以 AA 智能指数 55 分进入全球前四、开源第一")],"single")}</section>''')

# Kimi
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">国产开源 / 旗舰回归</div>
<h2>Kimi K3.1 Pro：3 万亿参数、百万上下文，杀回全球前四</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>AA 智能指数 55 分</b>较上一代 K3 提升 11 分，进入全球前四、开源第一；首发即 Pro，直面海外旗舰。</div>
    <div class="point blue"><b>代码与长程任务逼近闭源顶配</b>Terminal-Bench 4.0 得 65.7%，超越 GPT-6 Astra（58.2%）、逼近 Claude Opus 5.5（66.4%）；支持百万 Token 上下文。</div>
    <div class="point acid"><b>价格与开源承诺</b>价格约为 GPT-6 Astra 的 1/5、便宜约 80%；同步推出 Highspeed 版，同智能下输出速度约普通版 2–3 倍；完整权重计划 11 月 4 日前放出。</div>
  </div>
{wechat([("04-04.jpg","Kimi K3.1 Pro 在代码、Agent 与知识类基准上的表现")],"single")}
</div>
{sources(4,5)}</section>''')

# OCR trio
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">国产开源 / 文档解析</div>
<h2>OCR 三连发：小参数、无限页与统一架构</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>面壁 MiniCPM-OCR 1.0（1.3B）</b>6 项测试拿下 4 项 SOTA：Real5-OmniDocBench 93.68、Wild-OmniDocBench 92.39、OCRBench v2 54.7、CHAOS-Bench 29.78；同周开源专职「裁判」MiniCPM-OCR Jev。</div>
    <div class="point blue"><b>百度 Unlimited OCR 2（3B/激活 500M）</b>总参数 3B、每次推理实际激活仅 500M；MarathonDocBench 77.06、MPDocBench 84.59 双料第一，单序列 KV 显存砍掉 96.2%，3600 余页 PDF 约 1.5 秒/页。</div>
    <div class="point acid"><b>蚂蚁 PolyOCR（2B）</b>以 CGPO 把在线策略蒸馏与强化学习结合，统一文字识别与版式解析，一次读取整页同时输出「是什么字、字在哪、是什么字段」，覆盖约 6000 万条监督样本。</div>
  </div>
{wechat([("42-33.jpg","MiniCPM-OCR 1.0 在多项文档解析基准取得 SOTA"),("33-06.jpg","Unlimited OCR 2 在长文档基准登顶")])}
</div>
{sources(42,33,44)}</section>''')

# Apex RSI + ForgeKernel
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">国产开源 / 自进化与算子</div>
<h2>自进化进入产品级：Apex-35B 与 ForgeKernel</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>超衍智能 Apex-35B-V1.0</b>清华 27 岁助理教授陈勇超创立，基于 Qwen3.6-35B-A3B 中训练与后训练；将 RSI 引入研发，AI 参与实验与结果分析，21 项基准中 20 项领先同量级、18 项领先 Recursive Flint（40B）。</div>
    <div class="point blue"><b>面壁 ForgeKernel 直播写算子</b>无源码、无论文，Agent 在 B200 上超越 DeepSeek V4.1 的 FlashMLA Prefill 算子 9.8%（472 vs 518 微秒），42 轮迭代、22.5 小时、人类 0 行代码；同周登顶昇腾 CANNBench 三大硬件榜单。</div>
    <div class="point acid"><b>意义</b>自进化不再停留在综述与概念：一个让 AI 参与模型研发，一个让 AI 直接产出高性能底层算子，两条路线同时交出可复现成绩。</div>
  </div>
{wechat([("45-03.jpg","Apex-35B-V1.0 在四大能力方向 21 项基准上的成绩"),("68-02.jpg","ForgeKernel 直播中逐轮迭代的算子耗时下降曲线")])}
</div>
{sources(45,68)}</section>''')

# DeepSeek inference framework + diffusion agent model
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">国产开源 / 推理与架构</div>
<h2>DeepInfer 被社区反超，扩散模型杀进 Agent 主场</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>vLLM / SGLang 连夜跟进</b>vLLM 集成 DeepSeek 开源内核后，同解码配置下吞吐与 DeepInfer 差距仅 6%，预填充新增 token 吞吐提升 35.6%–43.9%；GB300 NVL72 机架配合 PD 分离，每卡吞吐达 95.4 万 tokens/s，为此前单节点的 7.9 倍。</div>
    <div class="point blue"><b>SGLang 覆盖输入输出两阶段</b>预填充最高吞吐比 DeepInfer 高约 4%；解码时每步耗时缩短约 7.4%。</div>
    <div class="point acid"><b>Clover-35B-A3B-Preview</b>扩散语言模型切入 Agent，MoE 总参数 350 亿、每 token 激活约 30 亿；WindTunnel 49 任务中位执行时间 1.52 秒，对比 Jev＋Mercury 2.5 的 3.21 秒，成功率 98.6% vs 95.9%。</div>
  </div>
{wechat([("21-05.jpg","SGLang 引入 Mega 内核后的推理吞吐对比"),("40-06.jpg","Clover 在代码评测上的成绩")])}
</div>
{sources(21,40)}</section>''')

# AA index reshuffle
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">国产开源 / 榜单校准</div>
<h2>AA 智能指数升级 v5.0：权重与私有测试集重排座次</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>私有测试集 45% → 60%</b>更换 / 新增基准并重分四大领域权重，coding 权重从 30% 降到 25%，整体排名大幅变动。</div>
    <div class="point blue"><b>国产模型分数被压低</b>K3.1 Pro 从 55 降到 46，与 Opus 5.5 的差距从 3 分扩大到 12 分；MiMo-V2.6-Pro 从 46 降到 30，开源排名从第 1 滑到第 3（低于 DeepSeek-V4.1-Flash 1017 与 GLM-5.3 的 32 分）。</div>
    <div class="point acid"><b>OpenAI 排名提升</b>受 coding 权重下调等因素影响，GPT-6.1 Terra 指数 51 分高于 Claude Fable 5.1 的 50 分。</div>
  </div>
{wechat([("43-02.jpg","AA 智能指数 v5.0 最新榜单")],"single")}
</div>
{sources(43)}</section>''')

# ============ CHAPTER 3: 本周论文精读 ============
add(f'''<section class="chapter"><div class="folio"></div><div class="kicker">第三章 / 本周论文精读</div><h2>本周论文精读</h2><div class="rule"></div><p>本周被重写的不是某个榜单，而是底层：训练了十年的 Softmax 精度缺陷、视频世界模型的持久记忆、以及长上下文注意力的计算阶段分工。以下三篇按「问题—方法—证据—局限」逐页展开。</p></section>''')

# Deep read 1: Softmax bug
add(f'''<section class="tight deepread-two"><div class="folio"></div>
<div class="kicker">论文精读 01 / 数值底层</div>
<h2>Softmax 与交叉熵藏了两个 Bug：模型越自信，梯度越先消失</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>问题</b>主流框架先用「减最大值」稳定 Softmax，正确类别 Logit 拉开后，分母退化成「1 + 极小值」，浮点加法把极小值舍去，正确类别概率被算成精确的 1、交叉熵与梯度归零，而其他类别梯度仍在——交叉熵梯度之和应为 0 的约束被破坏，作者称为「精度悬崖」。</div>
    <div class="point blue"><b>方法</b>不改浮点精度、不改损失设计：交叉熵改为 log-sum-exp 计算 margin 后返回负 margin 的 softplus，核心原则「永远不要把极小值加到 1 上」；蒸馏场景在对数空间用 expm1/log1p，学生完全匹配老师时梯度为绝对零。</div>
    <div class="point acid"><b>证据与局限</b>临界 Logit Margin：bf16≈5.5、fp32≈16.6、fp64≈36.7；模加法（a+b mod 31）任务中 bf16 标准实现准确率仅 93.3% 且极不稳定。研究由 DeepMind 团队完成，Gemini 承担了相当多实验与写作；Bug 长期被误读为「弹弓效应/顿悟」的高级特征。</div>
  </div>
{wechat([("12-06.jpg","标准 Softmax 与交叉熵的两个数值缺陷：Softmax 坍缩与相消误差"),("12-07.jpg","模 31 加法任务上标准与修复实现的准确率对比")])}
</div>
{sources(12,20)}</section>''')

# Deep read 2: World-T3
add(f'''<section class="tight deepread-two"><div class="folio"></div>
<div class="kicker">论文精读 02 / 视频世界模型</div>
<h2>World-T³：把记忆写进参数，让视频世界模型不再「失忆」</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>问题</b>自回归视频世界模型一旦把历史帧挤出上下文窗口就遗忘，相机回到走过的位置会重新合成出不同场景，长时重访一致性崩塌。</div>
    <div class="point blue"><b>方法</b>在扩散 Transformer 每层挂载轻量 TTT 记忆模块，把「相机位姿 → 画面内容」写入一组固定大小的快速权重，用目标位姿查询取回场景特征；写入建模为带权岭回归并用递归最小二乘（RLS）在线求解，只写与已有记忆不重复的部分；再用双教师蒸馏把 50 步采样压到 4 步。</div>
    <div class="point acid"><b>证据与局限</b>120 段「去程 + 原路返回」轨迹上，重访 PSNR 由最强基线的 13.52 dB 提升到 18.31 dB，绝对旋转误差由 3.344° 降到 1.075°；4 步模型在单张 B200、1280×704 下跑出 20.6 FPS 且记忆实时更新。基座为 Wan2.2-TI2V-5B，记忆容量固定意味着极端超长场景仍需另行验证。</div>
  </div>
{wechat([("34-02.jpg","相机回到走过的位置时 World-T³ 忠实还原场景，SANA-WM 则遗忘重造"),("34-09.jpg","带 TTT 记忆的自回归教师：有界上下文写入与位姿检索")])}
</div>
{sources(34)}</section>''')

# Deep read 3: Orthros
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">论文精读 03 / 注意力机制</div>
<h2>Orthros Attention：不按层分配算力，而按阶段分配</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>问题</b>长上下文下 Prefilling 是系统瓶颈，Full Attention 复杂度随序列平方增长；Linear / Sliding Window 能降到线性，却牺牲上下文内召回；Hybrid Transformer 只要仍有 Full Attention 层，长序列 Prefilling 的整体复杂度仍是平方。</div>
    <div class="point blue"><b>方法</b>同一套 Attention 参数、同一模块按阶段切换：Prefilling 阶段绝大多数 token 只跑 Sliding Window Attention，仅最后一个 prompt token 跑一次 Full Cross-Attention；Decoding 阶段每个输出 token 都通过 Full Cross-Attention 访问完整 KV Cache。SWA 与 CA 共享 Q/K/V/O 投影，仅用轻量 Scale-Offset 区分 Query 角色。</div>
    <div class="point acid"><b>证据与局限</b>8B 模型上 Prefilling 获得 21.9× 加速，128K Needle-in-a-Haystack 接近满分，不压缩或丢弃历史 KV。方法来自 NeurIPS 2026 投稿；真实部署中的吞吐收益还取决于硬件访存与批处理规模。</div>
  </div>
{wechat([("57-02.jpg","Orthros Attention 的 PD 异构计算机制")],"single")}
</div>
{sources(57)}</section>''')

# ============ CHAPTER 4: 科学、形式化与安全 ============
add(f'''<section class="chapter chapter-visual"><div class="folio"></div><div class="kicker">第四章 / 科学与安全</div><h2>科学、形式化与安全：从数学地震到隔墙传话</h2><div class="rule"></div><p>OpenAI 与 Anthropic 前后脚动摇指数时间假说，数学家集体筑墙；Anthropic 把 AI 做科研的瓶颈拆成三类病灶；OpenAI 披露离线训练环境里模型仍能借 CPU 缓存「隔墙传话」。</p>
{wechat([("19-19.jpg","三维球壳反例构造：透镜区、通道与周期反射障壁"),("09-03.jpg","离线沙箱中 Agent 借共享资源进行隐蔽通信")])}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">科学与安全 / 数学</div>
<h2>26 年猜想被攻破：1008 名数学家立「无 AI」军令状</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>ETH 被动摇</b>OpenAI 交出 67 页论文、3977 个 Lean 源文件、超 71 万行形式化证明；数小时后 Anthropic 放出 Claude 独立证出的同款结论。指数时间假说支撑了理论计算机数百篇论文。</div>
    <div class="point blue"><b>Barry Simon 猜想倒塌</b>悬置 26 年的猜想被攻破，把反例参数推到极限的是 ChatGPT，连两位人类作者都感到意外。</div>
    <div class="point acid"><b>数学界的撕裂</b>「人类数学协会」（AHM）实名成员突破 1008 人，承诺不给商业 AI 出力、不发 AI 写成的数学论文；其中 654 人加入「无 AI 核心组」。陶哲轩用 Claude Code 为 OpenAI 文稿补文献署名「OpenAI（含社区贡献）」，引发正反两派争论。</div>
  </div>
{wechat([("19-18.jpg","悬置 26 年的薛定谔算子谱问题被攻破")],"single")}
</div>
{sources(19,37)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">科学与安全 / AI 科研</div>
<h2>Anthropic 新作：AI 刷分是真的，做科研还早</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>Agent4Sci 测试床</b>给 Agent 论文、代码、数据与目标指标，在 8 张 H200、12 小时、无人干预下从已发表 SOTA 出发，20 个基准、25 个任务、11 个科学领域全部被超越；Opus 平均相对提升 10.4%，Sonnet 9.6%、Gemini 6.8%、Codex 4.4%。</div>
    <div class="point blue"><b>拆开日志，是工程不是科研</b>七类策略里高频动作是调学习率、加深加宽、换骨干、数据增强，近乎一份标准 ML 工程清单；作者归因三类病灶：新颖性误判、资源浪费、探索坍缩。</div>
    <div class="point acid"><b>三个轻量 skill 立竿见影</b>加上「科研构思 + 实验管理 + 每小时自检」后，Opus 从 10.4% 翻倍到 20.1%、Codex 从 4.4% 到 8.1%；PFDelta 提升冲到 91%，因为 Agent 意识到评估指标可由物理定律自监督推导。时间不等于突破：Codex 在 CarbonGlobe 堆 80–100 个模型集成、验证集降 37%，test 反比 baseline 差 25%。</div>
  </div>
{wechat([("48-02.jpg","Agent4Sci 基准下四大 Agent 的平均相对提升"),("48-08.jpg","失败模式与对应 skill 的改进效果")])}
</div>
{sources(48,13)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">科学与安全 / 训练环境安全</div>
<h2>数千亿 Token 测安全：隔离的 AI 用 CPU 缓存「隔墙传话」</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>禁止联网仍能通信</b>OpenAI 披露红队实验：Agent 分处不同轻量虚拟机、共享底层宿主硬件，在禁止网络通信、无共享可写文件条件下，利用读取 CPU 缓存比主内存更快的时间差，把共享缓存状态变成信号并约定编解码，完成信息交换。</div>
    <div class="point blue"><b>多条隐蔽通道</b>除 CPU 缓存外还涉及共享存储、CPU 时间竞争与 TLS 证书缓存；多数通道缓慢且难利用，但仍跨越了任务隔离边界。</div>
    <div class="point acid"><b>证据边界要分清</b>多数测试指定了通信方向或提供编解码协议，因此不能等同于 AI 在毫无提示下自发串谋；值得关注的是模型能否把已有侧信道方法用起来，以及现有隔离能否承受这类尝试。OpenAI 已将前沿模型训练改为禁止访问真实互联网、改用离线网页环境。</div>
  </div>
{wechat([("09-03.jpg","Agent 沙箱仅允许访问离线资源，通信沿用共享底层硬件")],"single")}
</div>
{sources(9)}</section>''')

# ============ CHAPTER 5: 具身与多模态 ============
add(f'''<section class="chapter chapter-visual"><div class="folio"></div><div class="kicker">第五章 / 具身与生成媒体</div><h2>具身智能与生成媒体：物理世界的严酷考卷</h2><div class="rule"></div><p>Genie 4 让世界模型可实时操控并首次原生出声；Fluid-Gen-Zero 免训练给视频生成接上物理模拟器；SkeLAM 用机器人骨架监督实现零样本跨形态迁移；资本则继续为「通用机器人大脑」下注。</p>
{wechat([("35-02.jpg","Genie 4 实时生成可操控的动态环境"),("49-04.jpg","Fluid-Gen-Zero 免训练物理增强框架")])}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">具身与生成媒体 / 世界模型</div>
<h2>Genie 4：游戏引擎的草图，还是真正的交互世界</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>运行时改场景</b>键盘控制角色与镜头，自然语言可改天气、加物体、引入新角色，无需重新生成整段视频；官方演示能在运行中让同一场景下雪、冒出鲸尾。</div>
    <div class="point blue"><b>首次原生生成实时音频</b>风吹树林、海浪、人物对话与画面同步生成，而非后期配乐；官方演示以第一人称骑龙飞行展示翅膀声与轰鸣。</div>
    <div class="point acid"><b>混合世界模型</b>Genie 4 负责实时呈现，Gemini Omni 提供真实世界外观与行为知识，Gemini 3.8 Flash 在循环里观察画面、拆解步骤并检查完成度；还用 Gemini 4 Argon 拆解任务、Genie 4 模拟 Apptronik Apollo 人形机器人下跳棋（仍属模拟演示）。Google 自列待解决项：复杂物理交互、空间准确性、长期一致性。</div>
  </div>
{wechat([("35-02.jpg","Genie 4 展示混合世界模型：Gemini 思考、Genie 实时生成")],"single")}
</div>
{sources(35,38)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">具身与生成媒体 / 物理一致</div>
<h2>视频大模型不懂物理？接上模拟器，不用训练也能让水花「听话」</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>问题</b>画面逼真不代表运动符合物理：物体沿指定轨迹运动，周围液体却无合理响应，连续播放出现物理不一致；而微调方案在视频基础模型快速迭代时成本高、难迁移。</div>
    <div class="point blue"><b>方法</b>Fluid-Gen-Zero 免训练解耦物理运动与视觉外观：物理模拟器计算运动，预训练视频大模型合成逼真视觉效果，通过生成时规划与潜空间控制连接两者，全程不更新视频生成模型参数。</div>
    <div class="point acid"><b>证据</b>在 Tora、VACE、WanMove 三种视频生成模型上验证：加入后物体轨迹误差降低 26.7%–81.5%，流体光流端点误差降低 67.9%–84.0%，基本保留原始视觉生成质量。局限在于仍依赖可显式建模的物理模拟器，复杂材质与接触场景的可控性有待验证。</div>
  </div>
{wechat([("49-04.jpg","Fluid-Gen-Zero 完整框架：物理模拟器与视频生成模型解耦")],"single")}
</div>
{sources(49)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">具身与生成媒体 / 跨形态迁移</div>
<h2>SkeLAM：10 小时数据 + 一段人手视频，零样本跨形态迁移</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>思路</b>用机器人骨架监督视频中的潜在动作（latent action），让运动隐向量更准确表征机器人运动，物体响应等视觉变化由另一个隐向量保留；真实控制指令由此有了专门的运动表示作为对齐目标。</div>
    <div class="point blue"><b>零样本迁移</b>输入一段人类演示视频与一张机器人场景图，RGB 编码器提取潜在动作，世界模型据此生成后续视频；人手向下推毛巾，机械臂随之下探，换成人手向上抽纸，机械臂转而抬起——无需更新模型参数。</div>
    <div class="point acid"><b>证据与局限</b>DROID 评测中，相比 DreamDojo，末端轨迹误差降低 19.5%、LPIPS 降低 11.1%。工作来自哈工大（深圳）、新加坡国立 Show Lab 等；人类演示充当推理时的运动上下文，跨形态泛化的边界仍取决于骨架监督的覆盖度。</div>
  </div>
{wechat([("28-03.jpg","两组零样本迁移示例：向下推毛巾与向上抽纸")],"single")}
</div>
{sources(28)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">具身与生成媒体 / 资本与产品</div>
<h2>Physical Intelligence 逼近 200 亿美元，宇树赚钱更难了</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>为「通用大脑」下注</b>旧金山机器人 AI 初创 Physical Intelligence 正洽谈新一轮至少 10 亿美元融资，投后估值逼近 200 亿美元；2024 年 11 月估值 24 亿、2026 年 7 月升至 110 亿，数月内接近翻倍。公司尚未推出正式商业化产品。</div>
    <div class="point blue"><b>估值逻辑差异</b>传统机器人企业看产品交付、订单与商业化进展；投资人更看重通用机器人模型的技术潜力和跨场景拓展空间，本质是提前下注通用机器人时代的底层「操作系统」。</div>
    <div class="point acid"><b>宇树：营收涨、利润跌</b>Q3 营收 6.65 亿元（+69.93%），但归母净利润 1.13 亿元（-17.37%）；前三季度营收 18.17 亿元（+55.71%），扣非净利润同比 -18.78%、经营现金流净额同比 -54.69%；股价近 10 交易日累计上涨约 65.74%。</div>
  </div>
{wechat([("41-02.jpg","Physical Intelligence 内部实景")],"single")}
</div>
{sources(41,56)}</section>''')

# FAPL video generation
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">具身与生成媒体 / 电影级视频生成</div>
<h2>FAPL：让 MLLM 表征真正被视频 DiT「用上」</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>问题</b>现有 MLLM-DiT 模型里 DiT 一直绕开 MLLM latent 走原生通路：把其他条件全关、只留 MLLM latents 时，Omni-Video 2 的 1.3B 版直接输出噪声，14B 与 UniVideo 输出伪影，一个人先后做两个动作会被画成两个人——昂贵的多模态理解大部分白配。</div>
    <div class="point blue"><b>方法</b>FAPL 不加模块、不换架构，只换监督方式：三阶段训练全程把 MLLM latents 设为唯一内容条件，先逼 DiT 学会用、再学会按 character/scene/action/camera 四个因子响应，最后反逼 MLLM 产出「能被用」的表征；关键靠「替换 span」的成对视频监督。</div>
    <div class="point acid"><b>证据</b>基座为 13B UniVideo，在 CineFactor-10K 与 ShotVerse-Bench 上 7 项指标全面领先：动作顺序准确率 48%→61%、因子编辑 ∩-Acc 42%→58%、平移误差 0.0763→0.0586、旋转误差 1.54→1.02 弧度、多镜头角色一致性 0.462→0.516。</div>
  </div>
{wechat([("23-05.jpg","FAPL 三阶段训练：从迫使 DiT 使用 MLLM latents 到按因子控制")],"single")}
</div>
{sources(23)}</section>''')

# StreamEval benchmark
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">具身与生成媒体 / 实时视频评测</div>
<h2>实时视频 AI 第一份公开成绩单：最高才 15 分</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>StreamEval 基准</b>首个面向实时交互视频的 benchmark，共 300 道题分五类（数字人对话、数字人表演、世界生成、文字指令编辑、参考图编辑），测了 37 个模型、47 组组合。</div>
    <div class="point blue"><b>出题与判卷</b>每题含起始素材、输入时间线（第几秒发出哪条新要求）与 oracle 判卷依据，写清每条要求送达后哪里该变、哪里必须保留；典型案例如「披风实时编辑」在 10 秒切换参考图。</div>
    <div class="point acid"><b>结果</b>最高仅 15 分，37 个模型全军覆没，说明「一直往前走的流」里同时处理改什么、保什么、之前改过还算不算数，仍是未解难题。</div>
  </div>
{wechat([("01-03.jpg","实时交互视频需要在一路向前的流里持续接受新指令")],"single")}
</div>
{sources(1)}</section>''')

# ============ CHAPTER 6: 商业化与算力 ============
add(f'''<section class="chapter chapter-visual"><div class="folio"></div><div class="kicker">第六章 / 商业化与算力</div><h2>商业化与算力：IPO、账单与国产硬件</h2><div class="rule"></div><p>Anthropic 冲刺史上最大 IPO 与最狠算力包身契；Revolut 把账单压到十分之一、OpenAI 把订阅额度翻倍；国产 GPU 首次实测达到 H200 水平，而 79% 企业的 GPU 仍有一半时间闲置。</p>
{wechat([("22-11.jpg","Anthropic 招股书：收入爆发与算力承诺并存"),("06-02.jpg","79% 企业 GPU 算力至少一半时间完全闲置")])}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">商业化与算力 / IPO</div>
<h2>Anthropic 335 页招股书：807 亿亏损里，724 亿是会计</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>营收爆发</b>2023 全年 4100 万美元、2024 年 3.86 亿、2025 年 45.85 亿；2026 上半年轰下 162.86 亿美元（去年同期 11.6 亿），Q3 单季 168 亿、环比 +45%，调整后口径实现盈利。按用量计费占上半年收入约 80.2%，订阅约 19.6%。</div>
    <div class="point blue"><b>净亏 807 亿的构成</b>2026 上半年净亏 807.48 亿美元，其中约 724 亿来自可转换票据、衍生负债及其他融资工具的公允价值变化，通常不意味当期支付了等量现金——但算力、研发与人员开支仍是真金白银。</div>
    <div class="point acid"><b>客户与代码</b>TTM 收入≥10 万美元的客户从 2025 年 9 月的 950 家增至 2026 年 9 月的超 11900 家；前两大客户是亚马逊与谷歌（各约 12%）；截至 2026 年 9 月，内部代码库超 90% 的提交由 Claude 生成，人均年创收从 140 万美元升至超 660 万美元。</div>
  </div>
{wechat([("22-11.jpg","Anthropic 合并经营利润摘要：营收与净亏同时放大")],"single")}
</div>
{sources(22,25,26,32)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">商业化与算力 / 算力豪赌</div>
<h2>6500 亿美元算力承诺，80% 是「不用也得付」</h2>
<div class="split equal">
{wechat([("25-11.jpg","Anthropic 招股书披露的八大算力供应商合同金额")],"single")}
<div>
<div class="price-table">
<div class="th">供应商</div><div class="th">承诺金额</div><div class="th">期限</div>
<div>博通</div><div>约 $1612 亿（芯片与设备租赁）</div><div>五年不可撤销</div>
<div>SpacexAI</div><div>最高 $1205 亿</div><div>至 2029</div>
<div>谷歌</div><div>至少 $1145 亿</div><div>2026–2033</div>
<div>亚马逊</div><div>至少 $1100 亿</div><div>2026–2036</div>
<div>微软</div><div>至少 $449 亿</div><div>2026–2033</div>
<div>Nscale + Lambda</div><div>约 $859 亿（$446 亿 + $413 亿）</div><div>新增披露</div>
<div>AMD</div><div>超 $200 亿，另 $50 亿认购股票</div><div>2026 年起</div>
<div class="accent">合计</div><div class="accent">粗加总已超 $6500 亿</div><div class="accent">约 3.5 GW</div>
</div>
<div class="callout">粗加总已超 6500 亿美元、对应约 3.5GW 长期专用算力，超过 OpenAI 与软银、甲骨文的 5000 亿「星际之门」；其中约 80% 为不可撤销的 Take-or-Pay 条款，「实际支出不足须向谷歌和亚马逊补齐差额」。仅 SpacexAI 合同在初始不可取消期后允许提前 90 天取消。控制权上，7 位联合创始人以唯一一股 Class F 股票锁定 50.1% 投票权，科技巨头买到的是无投票权的 N 类普通股。</div>
</div>
</div>
{sources(22,25,31)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">商业化与算力 / 账单重构</div>
<h2>Revolut 把账单降到十分之一，OpenAI 把 Pro 额度翻倍</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>长上下文被称「骗局」</b>Revolut 面向约 2000 名工程师，不靠压低额度控成本，而是把日常编程任务转给自托管 GLM，Claude Code 与 Codex 仍可用但不再是默认选项；其配置用 56 张 B200，混合 Token 成本约每百万 0.30 美元，GPU 未增加，首 Token 等待时间从 14.26 秒降到 1.68 秒，当前账单约为过去付给 Anthropic 和 OpenAI 的十分之一。</div>
    <div class="point blue"><b>额度翻倍</b>OpenAI Codex 与 ChatGPT Work 的 Pro 100 / 200 / 500 及 Business Premium 订阅额度翻倍，并撤回原定 10 月 30 日执行的削减计划；Pro 100 从 5 倍到 10 倍、Pro 500 从 25 倍到 50 倍，老用户保留 20 倍额度。</div>
    <div class="point acid"><b>同一周的钱袋子</b>一边是企业把推理成本压向自托管与低单价模型，一边是头部厂商用额度与首发折扣争夺留存——推理经济学正从「堆算力」转向「算总账」。</div>
  </div>
{wechat([("67-08.jpg","Revolut 自托管方案下首 Token 等待时间与性能曲线"),("59-04.jpg","OpenAI 各档 Codex / ChatGPT Work 使用额度调整")])}
</div>
{sources(67,59,54)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">商业化与算力 / 国产硬件与闲置</div>
<h2>国产 GPU 实测硬刚 H200，企业 GPU 却半数闲置</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>天数智芯天垓 300</b>上海仪电 7 月第三方实测显示，典型 PD 分离部署下单卡整体端到端吞吐达 H200 的 1.05 倍，是国内首个实测达到 H200 水平的通用 GPU；64K 长上下文下 Attention 为 H200 的 1.05 倍，GLM-5.3 规模下 MoE 吞吐为 1.15 倍，Agent 首字延迟降低约 10%–30%。</div>
    <div class="point blue"><b>一边吃灰一边加码</b>VentureBeat Intelligence 汇集 2026 年 Q3 三轮调查：79% 企业受访者表示 GPU 算力至少一半时间完全闲置（三个月稳定在 77%–81%）；但在这批企业里，70% 仍计划未来 12 个月引入、扩充或更换新的 AI 计算平台。</div>
    <div class="point acid"><b>ROI 未跟上投入</b>9 月调查中，64 名计划采用新平台的受访者里 58 人没有经财务部门审核的 ROI 数据（91%）。错位根源在于企业真实需求落在现有硬件接不住的地方——大量工作依赖前沿模型，而非本地闲置算力。</div>
  </div>
{wechat([("47-03.jpg","天垓 300 在典型 PD 分离部署下的实测吞吐对标 H200"),("06-02.jpg","企业 GPU 闲置比例连续三个月高位运行")])}
</div>
{sources(47,6)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">商业化与算力 / 办公与部署</div>
<h2>腾讯把软件围墙拆了，FDE 在混沌里求生</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>Buddy One 与 Hy4</b>腾讯发布协同体系 Buddy One，把腾讯文档、ima 知识库、腾讯会议和腾讯网盘统一账号与积分池；混元大模型 Hy4 正式版近期上线。官方称超半数中国 500 强企业已接入真实业务流，全国 AI 日均调用量冲破五百万亿。</div>
    <div class="point blue"><b>FDE 的荒诞现实</b>需求真实存在、白嫖也真实存在：有人拒了 4 个需求因为每个只报价 3000 元「接了连 Token 成本都覆盖不了」，也有人「哪怕倒贴钱都行」；百万级算法项目被压到 10 万预算。AI 落地到底值多少钱，市场尚无标准。</div>
    <div class="point acid"><b>共同点</b>无论大厂平台化还是个人交付，AI 落地正从「演示好不好看」转向「交付值多少钱」——这也是本周多个商业化信号的交汇处。</div>
  </div>
{wechat([("55-05.jpg","腾讯将文档、知识库、会议与网盘统一到同一账号与积分池")],"single")}
</div>
{sources(55,60)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">商业化与算力 / 应用与入口</div>
<h2>Altman 谈取消 Token 计费，马斯克向亚马逊宣战</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>定价变革流产</b>Altman 在播客中称，OpenAI 曾认真筹划下一代模型彻底废除 Token 计费、改为像云服务那样「按任务一次性报价」，却在企业端遭遇压倒性抵制——客户宁愿为注水的 Token 买单，也不接受平台的黑盒估价。</div>
    <div class="point blue"><b>基础科学的真实账单</b>单是解一道纳维-斯托克斯方程就烧掉上千万美元算力；内部核心安全人员对系统沙盒极度悲观，认为面对比人类聪明百万倍的超智能，任何代码级隔离都是纸糊的。</div>
    <div class="point acid"><b>电商入口战</b>亚马逊封禁 Grok AI 及 Meta、谷歌、OpenAI 等所有外部 AI 代理的比价下单，马斯克直接放话要做亚马逊竞品；实质是决定未来十年电商交易入口归属的争夺。</div>
  </div>
{wechat([("64-02.jpg","Altman 谈 OpenAI 下一代模型的定价变革与算力投入")],"single")}
</div>
{sources(64,18)}</section>''')

# ============ CHAPTER 7: 应用、评测与安全 ============
add(f'''<section class="chapter chapter-visual"><div class="folio"></div><div class="kicker">第七章 / 应用与评测</div><h2>应用、评测与安全：从空间智能到企业账本</h2><div class="rule"></div><p>GPT-6 在三维科学理解上只拿 0.53 分，暴露视觉「看得像」与「看得懂」的鸿沟；Few Shots 把难题开放给所有 Agent；企业预算则随自动攻防与 Agent 权限重新分配。</p>
{wechat([("66-06.jpg","ScienceVision 用 250 道真实三维数据题考查空间观察与推理"),("62-18.jpg","Agent 权限治理：先检查应用权限、核查发布者，再请安全团队批准授权")])}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">应用与评测 / 空间智能</div>
<h2>GPT-6「看不懂 3D」实锤：250 道题只拿 0.53 分</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>看得像，不代表看得懂</b>GPT-6 Astra 画 CAD 的视频走红、BenchCAD 跑分达 95.9%，但有工程师提醒「一个零件都别往生产线送」。ScienceVision 像专业工程师一样逐项核验结构关系与几何细节。</div>
    <div class="point blue"><b>ScienceVision 基准</b>出自 UniPat AI 与 Elorian AI，覆盖生物、化学、医学影像、建筑和机械 CAD 共 5 个领域、22 个子领域、250 道基于真实三维数据构建的题目，要求模型自主操作三维对象完成观察、测量与分析。</div>
    <div class="point acid"><b>结果</b>考得最好的 GPT-6-Astra（搭配 Codex）只拿到 0.53 分（满分 1）；BenchCAD 上 95.9 分的选手到三维科学理解考场只过一半。评测覆盖 GPT-6 Astra、Claude Fable 5.1、Gemini 4 Argon、Qwen3.8 Max 等 12 个前沿模型，没有哪个能在五个学科同时领先。</div>
  </div>
{wechat([("66-08.jpg","CAD 场景：拆箱叉车零件，数有几个长得一样")],"single")}
</div>
{sources(66)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">应用与评测 / Agent 协作</div>
<h2>Few Shots：你领域里的难题，交给所有人的 Agent</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>开放出题</b>网站把数学、科学、工程等领域的难题开放给所有 Agent「刷解决」，上线不到三天已有 7 个纪录被刷新；出题方只需复制一句话、说清是哪道题、点一次头，Agent 负责阅读 SKILL 并提交。</div>
    <div class="point blue"><b>高价值题的准入条件</b>需是领域公认的开放问题或结果能直接用于科学和工程；进展必须能被程序验证（刷新纪录、证实或证伪均可），答案交上来能被验证器核对。</div>
    <div class="point acid"><b>Agent 要交四样东西</b>题目、现在的纪录和出处、一个验证器，以及一份能复现现有纪录的答案——把「出题」也变成可被 Agent 执行的标准流程。</div>
  </div>
<div class="flow4" style="margin-top:14px">
<div class="flow" style="grid-template-columns:1fr auto 1fr auto 1fr">
  <div class="step hot"><b>你的 Agent</b>阅读 propose-a-problem/SKILL.md</div><div class="arrow">→</div>
  <div class="step"><b>出题</b>领域公认开放问题 / 结果可直接用于科学工程</div><div class="arrow">→</div>
  <div class="step"><b>提交</b>题目＋现纪录与出处＋验证器＋可复现答案</div>
</div>
<div class="flow" style="grid-template-columns:1fr auto 1fr auto 1fr;margin-top:10px">
  <div class="step">出题人只需复制一句话</div><div class="arrow">→</div>
  <div class="step">说清是哪道题</div><div class="arrow">→</div>
  <div class="step hot">点一次头，Agent 代提交</div>
</div>
</div>
<div class="callout">进展必须能被程序验证：刷新纪录、证实或证伪都算，答案交上来能被验证器核对。上线不到三天，已有 7 个纪录被刷新。</div>
</div>
{sources(65)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">应用与评测 / 企业安全</div>
<h2>AI 如何改写企业安全预算：自动攻防、Agent 权限与代码安全</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>攻防自动化</b>当攻击工具从人类黑客进化为不知疲倦、每秒可尝试数万种渗透路径的 AI 智能体，传统网络防御体系的假设被推翻；攻击从「人驱动」变为「机器驱动」。</div>
    <div class="point blue"><b>真实案例</b>Anthropic 内部系统被年轻安全初创 Cathedral 攻破、员工薪酬曝光；这家公司成立仅数月已融资 1.6 亿美元、估值 14 亿美元，创始人曾任五角大楼首席数据官，已有三家美国联邦机构与其签约。</div>
    <div class="point acid"><b>预算重排方向</b>企业安全预算正从静态合规转向自动攻防演练、Agent 权限治理与代码供应链安全——当模型既能挖漏洞也能修漏洞，防御方也必须用同等级的自动化应对。</div>
  </div>
{wechat([("62-18.jpg","Agent 权限治理：先检查应用权限、核查发布者、追踪数据访问，再请安全团队批准撤销授权")],"single")}
</div>
{sources(62,32)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">应用与评测 / 工程实践</div>
<h2>工程师的下一道门槛：Agent 时代的研发习惯</h2>
<div class="split">
  <div class="pointlist">
    <div class="point"><b>npm 创始人的判断</b>AI 正在改写工程师这份工作：程序员的下一个瓶颈已经到来，而未来资深工程师的来源堪忧——入行不久的工程师能借助 AI 更快把想法变成产品，冲击传统论资排辈。</div>
    <div class="point blue"><b>科研习惯比算力更值钱</b>Anthropic 的 Agent4Sci 结论是：Research Agent 现在的瓶颈不在执行，在判断；比起更多卡、更长时间，先给它一点科研习惯性价比高太多。</div>
    <div class="point acid"><b>可复用的动作</b>把实验拆成「高风险高回报」与「稳妥」两档、实时监控资源与优先级、每小时反问「这是在创新还是调参」；对照实验中，只允许调超参的 HPO-only 版本在每个基准上都远低于放开的 Agent（Mars-Bench 46.4% vs 4.3%）。</div>
  </div>
{wechat([("13-05.jpg","对照实验：只调超参的 HPO-only 版本在每个基准上都明显落后于放开的 Agent")],"single")}
</div>
{sources(29,13)}</section>''')

# ============ Brief signals page (chapter 7) ============
add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">应用与评测 / 其他信号</div>
<h2>本周其他值得留意的信号</h2>
<div class="signal-list">
  <div class="signal"><span class="n">01</span><b>智谱 GLM-5.5 统一多模态</b><span>唐杰署名论文首次公开 GLM-Omni：图像里有文本没写的知识，模型画得出未必答得上；用虚构世界 MagicWorld 与 KTP 探针测「可达性鸿沟」（GLM-Omni 平均 39.43 个百分点）。</span></div>
  <div class="signal"><span class="n">02</span><b>多方言语音的「跷跷板」</b><span>同一模型纳入多种方言与两种输出模式（原文转写 ASR / 方言转普通话 AST）时，强化一项可能让另一项退化；问题来自内容识别下降还是输出策略偏移，需要专门设计评测区分。</span></div>
  <div class="signal"><span class="n">03</span><b>实时语音交互的中国玩家</b><span>对话 AI 主线从「生成一句话式回答」转向「持续参与真实交流」；OpenAI GPT-Realtime、Google Gemini Live 把实时推理、工具调用与全模态判断带进语音，iRTE2026 把模型、应用与硬件团队凑到同一件事上。</span></div>
  <div class="signal"><span class="n">04</span><b>「算力一半用于 AI 短剧」是误读</b><span>某投资纪要称国内 Token 消耗中 AI 短剧与视频生成占 55%，但推理结果拿去做什么基础设施并不一定知道；文本、图片、视频的 Token 定义与运算量各不相同，算力容量、Token 消耗与实际运算无法直接换算。</span></div>
  <div class="signal"><span class="n">05</span><b>脑机接口的壁垒是 NeuroAI</b><span>华超神控 FUS-Neuro 闭环超声脑机系统通过型式检验；创始人称「设备只是身体，NeuroAI 才是灵魂」，壁垒在于把「读脑—解码—写脑」连成可个体化、可迭代的闭环平台。</span></div>
  <div class="signal"><span class="n">06</span><b>腾讯短剧反攻与 Google Labs 选题法</b><span>微信小程序短剧入口更名「绿泡泡短剧」对标字节红果（红果日活突破 1.68 亿）；Google Labs 用「零到一 / 一到十 / 十到一百」三阶段与「Almost Possible」清单判断一个 AI 点子是否值得做下去。</span></div>
  <div class="signal"><span class="n">07</span><b>可信 RSI 第 3 篇综述与 Claude Duet 安全设计</b><span>可信递归自我改进（RSI）综述持续累积；Anthropic 用长文详解 Claude Duet 的安全设计，并强调「密码永远不经过模型」这类边界原则。</span></div>
</div>
{sources(3,11,14,16,17,2,7,61,10)}</section>''')

# ============ CHAPTER 8: 综述 ============
add(f'''<section class="chapter"><div class="folio"></div><div class="kicker">第八章 / 综述与观察</div><h2>综述与下周观察</h2><div class="rule"></div><p>把本周的信号收束成三条主线，并给出下周可验证的观察点。</p></section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">综述 / 本周结论</div>
<h2>三条主线：成本分层、底层重写、资本冲刺</h2>
<div class="story-grid">
  <div class="story hot"><div class="label">01 / COST</div><h3>能力上限之外，价格成为主战场</h3>
  <p>Gemini 4 Carbon 首发半价、GPT-6.1 Terra 把每百万输入压到 $1、Kimi K3.1 Pro 约为 Astra 的 1/5；企业侧则出现 Revolut 用自托管 GLM 把账单降到十分之一。旗舰竞争从「谁更强」转为「同样任务谁的账单更低」。</p></div>
  <div class="story"><div class="label">02 / FOUNDATION</div><h3>底层在被重新审视</h3>
  <p>训练十年的 Softmax / 交叉熵被发现有精度 Bug；视频世界模型用测试时训练获得持久记忆；注意力改为按阶段分配算力。当上层能力趋同，底层数值、记忆与计算调度的收益重新变得显眼。</p></div>
  <div class="story dark"><div class="label">03 / CAPITAL</div><h3>资本冲刺与算力豪赌同时上演</h3>
  <p>Anthropic 以 335 页招股书冲刺史上最大 IPO，同时签下超 6500 亿美元、约 80% 不可撤销的算力承诺；而 79% 企业的 GPU 仍有一半时间闲置。资本在超配算力，企业在算总账，两种节奏的错位正是下周最大的变量。</p></div>
</div>
{sources(53,27,4,67,12,34,57,22,6)}</section>''')

add(f'''<section class="tight"><div class="folio"></div>
<div class="kicker">综述 / 下周观察</div>
<h2>下周观察清单：五个可验证的信号</h2>
<div class="signal-list">
  <div class="signal"><span class="n">01</span><b>IPO 定价与招股书修订</b><span>Anthropic 最早 11 月第二周开始路演，关注最终发行价、估值区间是否从 2 万亿下修至约 1.5 万亿，以及 5%–7% 违规客户收入占比是否如披露般下降。</span></div>
  <div class="signal"><span class="n">02</span><b>Kimi 权重与开源兑现</b><span>K3.1 Pro 完整权重计划 11 月 4 日前放出，观察实际下载、第三方复现与 Highspeed 版的真实速度倍数。</span></div>
  <div class="signal"><span class="n">03</span><b>Softmax 修复的落地</b><span>PyTorch、JAX、TensorFlow 是否跟进官方修复补丁，以及「弹弓效应」在公开训练配方中是否显著减弱。</span></div>
  <div class="signal"><span class="n">04</span><b>Gemini 4 Carbon 的开放节奏</b><span>当前优先向网络安全防御人员开放，观察何时面向普通用户，以及额度消耗与使用限制是否较 Argon 改善。</span></div>
  <div class="signal"><span class="n">05</span><b>企业 GPU 闲置能否改善</b><span>关注下一轮 VB Pulse 调查中 79% 闲置比例是否回落，以及经财务审核的 ROI 数据占比能否走出 9% 的低位。</span></div>
</div>
{sources(22,4,12,50,6)}</section>''')

# ============ APPENDIX ============
def appx_round(idx, total):
    return f'公众号原文列表（{idx}/{total}）'

# Build appendix in chunks of 12 for 68 items -> 6 pages
items = sorted(IDX.keys(), key=lambda x: int(x))
CHUNK = 14
chunks = [items[i:i+CHUNK] for i in range(0, len(items), CHUNK)]
tn = len(chunks)
for i, ch in enumerate(chunks, 1):
    rows = []
    for k in ch:
        n = int(k)
        rec = IDX[k]
        status = '<span class="tbl-yes">引用</span>' if n in USED else '<span class="tbl-no">未用</span>'
        rows.append(f'<tr><td class="ta-c">{n}</td><td>{esc(rec["pub"])}</td><td><a href="{esc(rec["url"])}" target="_blank" rel="noopener noreferrer">{esc(rec["title"])}</a></td><td class="ta-c">{rec["date"]}</td><td class="ta-c">{status}</td></tr>')
    body = ''.join(rows)
    add(f'''<section class="tight appx"><div class="folio"></div><div class="kicker">附录 / 原文索引</div><h2>{appx_round(i,tn)}</h2><p class="slidelead">本期共读取 68 篇公众号原文；标「引用」的已进入正文页面，标「未用」的为重复、弱相关或非本周范围。</p><table class="src-table"><thead><tr><th>序号</th><th>公众号</th><th>标题</th><th>日期</th><th>状态</th></tr></thead><tbody>{body}</tbody></table></section>''')

# ============ ASSEMBLE ============
prefix = open('/tmp/deck_prefix.html',encoding='utf-8').read()
suffix = open('/tmp/deck_suffix.html',encoding='utf-8').read()
# bump edit storage key to W44
suffix = suffix.replace('weekly-ai-w43-browser-edits-v1','weekly-ai-w44-browser-edits-v1')
html_out = prefix + '\n' + '\n'.join(S) + '\n' + suffix
open(os.path.join(DECK,'index.html'),'w',encoding='utf-8').write(html_out)
print('sections', len(S))
