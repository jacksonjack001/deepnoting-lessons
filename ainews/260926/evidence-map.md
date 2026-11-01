# 双周 AI 进展：证据与取舍

范围：2026-09-13 至 2026-09-26。以 9 月 12 日已覆盖版本为边界，核对 `git log`、`git diff --name-status` 和实际新增段落。来源库在 9 月 26 日集中提交，不能把提交日期当成每篇报道的发布日期。该文件供编辑复核，不进入可见幻灯片。

原始论文页面与摘要已访问；所用图从论文 PDF 提取。微信文章在普通请求中曾返回验证码；改用浏览器请求头后，已访问本期所用的完整文章正文与配图。媒体披露的榜单、演示与价格仍按“报道”“团队披露”或“待核”标注，不升级为独立实测结论。

| 候选 | 素材文件 | 原始来源 | 主体 / 类型 | 核心信息与关键数字 | 图片 | 信度与处理 |
|---|---|---|---|---|---|---|
| GPT-6 Sol / Luna | `00_NLP应用/topc-chatgpt.md` | [发布报道](https://mp.weixin.qq.com/s/9BVUcYJLIBFbwlLTcKFn-A) | OpenAI / brief, commercial | Sol 输入/输出 US$2/10；Luna US$0.10/0.50，均每百万 token；AutomationBench Sol 33.2%、约 US$0.27/任务 | 价格表 | 中：媒体转述 9/22 发布；独立官方价目访问受限。单页。 |
| Opus 5.5 | `00_NLP应用/topc-claude.md` | [发布报道](https://mp.weixin.qq.com/s/cqLAQYWQkoVTPk6JiVyLsA)、[定价传闻](https://mp.weixin.qq.com/s/VPaUV8AI-XX5-yNbegmDdg) | Anthropic / brief, commercial | 68 万行迁移案例、网页任务 39/40、典型任务成本约降 40%；US$4/20、缓存 US$0.20/5 为待核口径 | 任务流程与数据卡 | 中低：案例为公司转述，价格传闻标待核。单页。 |
| Magenta RealTime 2 | `00_NLP应用/topc-google_deepmind.md` | [报道](https://mp.weixin.qq.com/s/EjwpzflEVGi_TdmzTBF0pw) | Google / brief | 实时音乐生成发布信号 | 公司扫描数据项 | 中低：仅短讯，不推断普遍质量。合并。 |
| Muse / 字节蒸馏 | `00_NLP应用/meta.md` | [Muse 报道](https://mp.weixin.qq.com/s/vM5iiwIScwX5IpxHN5HNOQ)、[字节蒸馏报道](https://mp.weixin.qq.com/s/TYIhhnunyokGKkT_AcQVzA) | Meta / article, research | 长期个人 Agent 状态与字节训练单位 | 公司扫描数据项 | 中低：只保留议题，未采用未核实增益。合并。 |
| GLM 推理服务 / Infra Agent | `00_NLP应用/0_chatglm专题.md` | [报道](https://mp.weixin.qq.com/s/gwu2NvcUdeQuVA5bqVdIEg) | 智谱 / article-deep-read, commercial | 国产卡部署、团队披露端到端吞吐约 3.2 倍；Agent 参与优化骨架复用 | 反馈闭环图 | 中：团队报告，没有公开可复现实验。单页，放国产模型工程。 |
| 智谱融资 | `00_NLP应用/0_chatglm专题.md` | [报道](https://mp.weixin.qq.com/s/k0jnzEhPF-xg2HdDZX8fPw) | 智谱 / commercial | 募资用于模型与算力基础设施；金额来自报道与公告转述 | 国产模型资本卡 | 中低：不展示可能受汇率、结构影响的合并金额。合并。 |
| ZCode 数据争议 | `00_NLP应用/0_chatglm专题.md` | [报道](https://mp.weixin.qq.com/s/PAc9mO0Jloex7jqpT-cmSg) | 智谱 / brief, reliability | 客户端上传边界、致歉、开源与第三方审计 | 国产模型治理卡 | 中低：以报道描述为准，未独立核查历史版本。合并。 |
| Qwen 手机 Agent | `00_NLP应用/0_chatgpt-qwen.md` | [报道](https://mp.weixin.qq.com/s/pa4ytH21qLpBFMwZarTDtw) | 阿里 / demo, commercial | Planner / Use / Creative；API 优先、GUI 兜底；荣耀合作 | 输入-动作-反馈图 | 中：产品路线为发布口径，具体应用覆盖和权限未披露。单页。 |
| Qwen 企业上下文 | `00_NLP应用/0_chatgpt-qwen.md` | [报道](https://mp.weixin.qq.com/s/Zh1lczla_3TLyM37SdWnhQ) | 阿里 / commercial | Enterprise Context 与 QwenNote A2，补充线下会话输入 | 手机页补充卡 | 中：发布报道；未采用 Glean 估值/ARR 作因果证据。合并。 |
| Qwen-Image-2.1 | `00_NLP应用/0_chatgpt-qwen.md` | [报道](https://mp.weixin.qq.com/s/V8Bl3qkpSWA3qImyeeZTxA) | 阿里 / brief, generative media | 文生图与编辑一体、透明图、多参考图 | 生产流程对照 | 中：产品功能按报道，不采用未经独立核验的排名。合并。 |
| DSec | `00_NLP应用/deepseek.md` | [原论文](https://arxiv.org/abs/2609.22978) | DeepSeek / paper-deep-read | 统一四类沙箱后端；约 160 节点、每天约 300 万实例、峰值超 38 万并发、每秒超 5000 创建 | 原论文图 1 | 高：原论文核对；数字为作者报告。单页，论文精读。 |
| VBVR-Pro | `00_NLP应用/0_chatgpt-qwen.md` | [原论文](https://arxiv.org/abs/2608.26105) | NTU 等 / paper-deep-read | 300 程序化任务、30 余生成器、7 项外部迁移评测；任务评分器支持 RL | 原论文图 1 | 高：原论文核对；迁移结论为作者报告。单页，论文精读。 |
| RSIAgent | `00_NLP应用/ASI.md`、`topc-chatgpt.md` | [原论文](https://arxiv.org/abs/2609.15364) | Aether AI 等 / paper-deep-read | 课程、执行、验证 Agent；先广后深探索，冻结并复用记忆，不更新权重 | 原论文图 2 | 高：原论文核对；跨模型对比只按论文条件陈述。单页，论文精读。 |
| SearchGEO | `02_创业计划/AI搜索.md` | [原论文](https://arxiv.org/abs/2606.16821) | KAUST 等 / paper-backed applied reliability | 13 后端 × 308 案例；ASR 0.0%–31.4%，脚手架影响风险 | 原论文图 1–2 | 高：原论文核对。为保持精读章节聚焦，放 Agent 可靠性单页。 |
| Jev | `调研报告/claudeopenclaw.md` | [官方发布](https://typesafe.ai/blog/introducing-system-one-models-and-jev)、[机器之心报道](https://mp.weixin.qq.com/s/rphPh91aHpcOovORbAo2Kw) | TypeSafe AI / Agent engineering | 结构化概率判断；官方输入价 US$0.042/百万 token、输出免费；报道转述 LangChain 小规模评分约 0.44 秒、US$0.00035/次；724 条广告约 40 秒 | 公众号原文 LangChain 实验截图 | 中：机制由官方发布核对，案例和费用为转述。独立单页。 |
| 机器人 SO-101 | `00_NLP应用/topc-chatgpt.md` | [演示报道](https://mp.weixin.qq.com/s/wRkb8qsZkgSn38VqxkhriA) | OpenAI / demo | 报道附测试表：入碗 19/20，拼图 2/20；跨任务表现差异大 | 原文演示帧与测试表 | 中：报道转述测试，未独立复现。合并具身。 |
| Simate / RoboDojo | `00_NLP应用/topc-chatgpt.md` | [报道](https://mp.weixin.qq.com/s/fMbm9PqjABhFGOJfeCO5eQ) | Simate / brief, embodied | AutoResearch 系统榜单表现 | 证据等级对照 | 中低：媒体榜单，不归属 OpenAI。合并具身。 |
| MiniMax H3 / FastH3 | `03_多模态/文生视频.md` | [报道](https://mp.weixin.qq.com/s/Ue4Uiv_VATM1i3Essqs4rA) | MiniMax、vLLM-Omni、FastVideo / article-deep-read | 八卡 B300，10.125 秒完整 MP4 约 8.7 秒就绪；非首帧流式 | 生产链流程 | 中：特定系统配置报告。合并生成媒体。 |
| 剪映生成+剪辑 | `03_多模态/文生视频.md` | [报道](https://mp.weixin.qq.com/s/yRZJMQoFCwRD8uIE-DOXHA) | 剪映 / brief | 生成视频接入编辑工作流 | 生产链流程 | 中低：短讯，只描述连接关系。合并。 |
| AI 硬件留存 | `5.1_新行业调研/XR.md` | [报道](https://mp.weixin.qq.com/s/Y3s0tbrQXslSFOiqBdoNtQ) | Mooni 等 / commercial | 预订、销量报道；10/30/180 天留存更关键 | 商业化矩阵 | 中低：没有独立销量核验，不把预订当收入。合并。 |
| AI 长剧热度 | `03_多模态/文生视频.md` | [报道](https://mp.weixin.qq.com/s/0xPW0LXVahvg8QFqQXNBGQ) | 芒果等 / commercial | 热度与股价叙事 | 商业化矩阵 | 低：不把股价波动解释为内容收入。合并。 |

## 未选入的长文与重复项

- `topc-chatgpt.md` 的 GPT-6 Astra 架构长文、GPT-Live 工程报告、数学成果报道，以及 `LLM规则和记忆.md` 的记忆综述均有分析价值；受 20 页上限和本期主线约束未纳入。数学成果尚不宜以报道标题当已验证定理。
- `0_chatgpt_badcase.md` 的 Pain Axis 论文可作为安全研究；报道对“痛苦”与自我意识的拟人化解释超过实验可证明范围，未纳入。
- `topc-google_deepmind.md` 中 Gemini 4 偷跑、Mathematica 泄露、RSI“已破解”等题材证据不足，未纳入。
- `ASI.md` 的 MetaRSI、AI4AI、CAITLY，`03_多模态/文生视频.md` 的 OmniHarness，以及 `01_NLP模型/LLM面试.md` 的随机 KV 淘汰，均按方法类候选复核；本期不扩张论文精读集合。
- 其他与 AI 主线关系弱的地理常识、硬件配置、出行、行业人物稿未进入候选池。

## 本版图像说明

- 公众号相关页面优先使用完整原文中的价格、基准、架构、演示和成本配图。原始图片文件保存在 `assets/wechat-*`；页面只缩放显示，点击可查看完整本地原图。每张图片在幻灯片中只出现一次。
- 论文精读与 SearchGEO 页面使用论文原图的局部裁切；精读分隔页选用与详情页不同的 DSec、VBVR-Pro、RSIAgent 图表局部。
- 结论与观察页保留标明“编辑归纳”的图，因为它们跨越多篇来源，单篇公众号配图无法准确覆盖整页论证。

| 页码 | 公众号原文配图 | 原文 |
|---|---|---|
| 1–3 | OpenAI 工作流与价格图、智谱 Kernel 优化图、千问图像样例与手机现场、Jev 批量判断案例、Anthropic 成本曲线、Magenta 界面；各图不重复 | [OpenAI](https://mp.weixin.qq.com/s/9BVUcYJLIBFbwlLTcKFn-A)、[智谱](https://mp.weixin.qq.com/s/gwu2NvcUdeQuVA5bqVdIEg)、[千问](https://mp.weixin.qq.com/s/pa4ytH21qLpBFMwZarTDtw)、[Jev](https://mp.weixin.qq.com/s/rphPh91aHpcOovORbAo2Kw)、[Anthropic](https://mp.weixin.qq.com/s/cqLAQYWQkoVTPk6JiVyLsA)、[Magenta](https://mp.weixin.qq.com/s/EjwpzflEVGi_TdmzTBF0pw) |
| 4 | AutomationBench 分数与任务成本原图 | [OpenAI 产品报道](https://mp.weixin.qq.com/s/9BVUcYJLIBFbwlLTcKFn-A) |
| 5 | 代码迁移与网页优化案例截图、FrontierCode 成本曲线 | [Opus 5.5 报道](https://mp.weixin.qq.com/s/cqLAQYWQkoVTPk6JiVyLsA) |
| 6–7 | GLM 推理吞吐曲线、ZCode 整改声明、Infra Agent 密集反馈原图 | [智谱推理服务](https://mp.weixin.qq.com/s/gwu2NvcUdeQuVA5bqVdIEg)、[ZCode](https://mp.weixin.qq.com/s/PAc9mO0Jloex7jqpT-cmSg) |
| 8 | 荣耀 Magic9 / Robot Phone 与 Qwen Agent Harness 发布现场 | [千问手机 Agent 报道](https://mp.weixin.qq.com/s/pa4ytH21qLpBFMwZarTDtw) |
| 9 | LangChain 使用 Jev 给 Agent 结果评分的原文截图 | [机器之心 Jev 报道](https://mp.weixin.qq.com/s/rphPh91aHpcOovORbAo2Kw) |
| 15 | SO-101 机械臂操作画面与入碗/拼图测试表 | [机器人演示报道](https://mp.weixin.qq.com/s/wRkb8qsZkgSn38VqxkhriA) |
| 16 | Qwen-Image-2.1 局部编辑样例、MiniMax H3 音视频处理架构 | [千问生图](https://mp.weixin.qq.com/s/V8Bl3qkpSWA3qImyeeZTxA)、[H3 服务](https://mp.weixin.qq.com/s/Ue4Uiv_VATM1i3Essqs4rA) |
| 17 | 《后西游记》制作成本构成信息图 | [虎嗅报道](https://mp.weixin.qq.com/s/0xPW0LXVahvg8QFqQXNBGQ) |
