# 2026.09.06—09.12 周报证据地图

## 最新版本：图文与视频深化版（37 页）

在 30 页版本基础上增加 7 页机制 / 证据分析：研究 Agent 人工干预、监控层次、数学探索工作流、三维预演约束、DaVinci 调色验收、图像编辑保持约束、Sketch 与模板。观点推演明确标作编辑分析，没有新增未经来源支持的内部实现声明。

视频均从原公众号 HTML 的 video_page_infos 提取原始媒体地址下载，本地播放、保留原声但不自动播放，离开页面自动暂停。已用 ffmpeg 解码生成独立 poster，并在隔离 Chrome 中逐个确认元数据和播放进度。

| 最新页码 | 原始媒体 | 时长 | 原文 |
|---|---|---|---|
| 14 | demo-video-0.mp4：剑斗成品 | 27.47 秒 | https://mp.weixin.qq.com/s/QYn2OeBXhsO2O7XLwE0lfA |
| 14、15 | demo-video-1.mp4：Blender 预演与生成对照 | 28.05 秒 | 同上 |
| 16 | demo-video-7.mp4：DaVinci 调色展示 | 14.97 秒 | 同上 |
| 30 | images-extra-video-0.mp4：Images 2.5 展示 | 57.96 秒 | https://mp.weixin.qq.com/s/37bo6MT5K2tfCZjVtA3eWQ |
| 31 | images-extra-video-1.mp4：Sketch | 33.52 秒 | 同上 |
| 31 | images-extra-video-2.mp4：模板 | 27.71 秒 | 同上 |

下文的 30 页补充审查保留为历史记录，其页码以该次版本为准。当前使用独立 v3 浏览器编辑存储，避免旧节点编号错贴。修改前 30 页备份：index-before-media-depth.html。

> 本文件用于编辑与核验，不在幻灯片中展示。数字均保留来源口径；无法从官方材料确认的内容不升级为确定事实。

| 候选项 | 组织 / 作者 | 核心证据 | 类型与路由 | 原始来源 | 视觉 | 置信度 |
|---|---|---|---|---|---|---|
| Agents API | OpenAI | 托管模型—工具循环、会话、压缩与恢复；执行环境和持久文件仍由应用负责 | brief → 前沿公司 | [官方发布](https://openai.com/index/introducing-the-agents-api/) / [官方架构](https://developers.openai.com/api/docs/guides/agents-api/architecture) / [AINLP](https://mp.weixin.qq.com/s/MlV92tRKoMTA1CVpY7RHwQ) | 官方流程截图 | 高 |
| AI 加速 AI 研究 | OpenAI | 截至 8 月中旬，每 1 个人类研究日对应 3.1 个 Agent 工作日；中位数与 P90 每日推理资源按 API 标价超过 600 / 7,000 美元；4—8 小时任务的成功案例过半仍有人介入 | article-deep-read → 公司研究 | [官方文章](https://openai.com/index/research-acceleration-view-inside-openai/) / [AINLP 译文](https://mp.weixin.qq.com/s/NjCOtCiK62_9MiGQzlx9LA) | 工作日曲线、人工介入图 | 高 |
| 电商 Agent 配方 | Anthropic | 单 Agent + Skills；高频规则进 prompt、长尾进 Skill；工具复用既有业务系统，Harness 执行边界 | article-deep-read → Agent 工程 | [Claude Blog](https://claude.com/blog/the-anatomy-of-effective-commerce-agents) / [PaperAgent](https://mp.weixin.qq.com/s/W8LAP0vPqeBnB6C9qjnV2g) | Prompt / Skills 分层图、缓存结构 | 高 |
| AlphaGenome Atlas | Google DeepMind | 公司披露：覆盖约 90 亿单碱基变异、每种约 27,000 项预测，合计逾 240 万亿数值、约 1 PB | brief → 前沿公司 / 科研基础设施 | [DeepMind 公告信号](https://x.com/googledeepmind/status/2097325048109384166) / [新智元](https://mp.weixin.qq.com/s/P1MtqQ15A8p4KNTH1ARiyw) | 官方演示与数据库截图 | 中高 |
| tgrep | Microsoft | 本地 trigram 索引减少大仓库重复扫描；报道口径最高约 52 倍，并已进入 GitHub Copilot CLI | brief → 前沿公司 | [报道](https://mp.weixin.qq.com/s/tct_TRhUW4zWNylBoKtixA) | 编辑重绘检索流程 | 中 |
| DeepSeek V4.1 Flash | DeepSeek | 552B MoE；输入 / 输出激活 8B / 16B；CED 非对称架构；缓存 HBM / SSD 需求为上一代的 1/4 / 1/8；主 KV 压至 FP4 | technical-report → 国产模型 | [技术报告](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf) / [量子位](https://mp.weixin.qq.com/s/-a3MXvHw4PtZNlfNjMtaig) | 原报告架构、缓存历史 | 高 |
| LLaDA-Image | InclusionAI | 6B DiT；累计生成训练样本 2.2 亿、超过 90% 为纯图片监督；Qwen-Image-Bench 英 / 中 53.53 / 53.38；Turbo 2—4 步 | technical-report → 国产模型 | [论文](https://arxiv.org/pdf/2609.03796) / [模型集合](https://huggingface.co/collections/inclusionAI/llada-image) / [机器之心](https://mp.weixin.qq.com/s/6vfgiKelrm5IxWujwNiHew) | 训练配方、生成样例、榜单 | 高 |
| S-Space | MirroS | VLM 内部存在可线性读出的水平 / 垂直 / 距离坐标；定向干预会选择性改变空间判断；外部坐标变换显著优于原生回答 | paper-deep-read 01 | [技术报告](https://mirros.ai/report/s-space.pdf) / [代码](https://github.com/MirroS-Lab/S-Space) / [机器之心](https://mp.weixin.qq.com/s/gHkDFBsw0tfTUwsK7UfmDA) | 原始机制图、干预图、视角变换结果 | 高 |
| Stolen Thoughts | Panfilov 等 | 同厂商加密推理块可跨会话 / 用户 / 模型重放；弱模型越狱可恢复强模型推理；6,708 条公开轨迹重建 315,320 个推理块，并发现隐私材料 | paper-deep-read 02 | [项目页](https://stolen-thoughts.com/) / [论文](https://arxiv.org/abs/2608.09867) / [报道](https://mp.weixin.qq.com/s/px2bGiL0wwfi1NOHO3ux9g) | 官方三厂商提取一致性图 | 高 |
| Action Map Policy | Huang 等 | 将 3D 动作投影为多视角像素轨迹并以交叉熵分类；真机早餐任务中报告成功率提升约 50%—70%，13.80ms 对 DiffPo 93.53ms，224px 下约 1mm 误差 | paper-deep-read 03 / 具身智能 | [项目](https://haojhuang.github.io/amp_page/) / [论文](https://arxiv.org/abs/2607.10706) / [机器之心](https://mp.weixin.qq.com/s/h05elhMfbmVewWxKeCFEFA) | 原论文框架、架构、真机表格 | 高 |
| Skild S1 / 具身 ICL | Skild AI | 报道称一次任务演示视频可作为上下文，让机器人尝试未见任务；长任务可达约 10 分钟 | brief → 具身智能 | 本周本地摘录（原链接缺失） | 编辑重绘上下文学习回路 | 低，显著标注“报道 / 待补原始链接” |
| GPT Images 2.5 | OpenAI | 报道与公开演示：精准编辑、多轮一致性、Sketch 输入；公司称延迟最多降低 50%；总生成量每周约 30 亿张来自公司披露 | demo → 生成媒体 | [APPSO](https://mp.weixin.qq.com/s/LnUELzf0IyALtS4sCoEolw) / [相关规模披露](https://mp.weixin.qq.com/s/37bo6MT5K2tfCZjVtA3eWQ) | 编辑前后、Sketch、递归生成 | 中高 |
| H3 Lightning | RunningHub / MiniMax | 项目方测试：5 秒视频从 348.8 秒降至 28.7 秒，约 12 倍；媒体实测 15 秒视频约 54 秒；测试硬件口径不同 | demo → 生成媒体 / 推理工程 | [开源项目](https://github.com/RH-RunningHub/MiniMax-H3-MultiGPU-Lightning) / [智东西](https://mp.weixin.qq.com/s/_LoP2CgrMlzSLheRxNBomA) | 工作流、测试画面 | 中高 |
| 中美 AI 公司结构 | RAND 研究转述 | 样本中美 743 / 438 家；美国应用软件集中于知识行业，中国更多落在制造、交通、能源；结论依赖分类口径 | article-deep-read → 商业化 / 产业结构 | [虎嗅解读](https://mp.weixin.qq.com/s/Bv1w-1DuWlKdJVN6JcN1rQ) | 原报告表格、行业分布图 | 中 |
| 订阅与推理经济 | OpenAI / Anthropic / 媒体 | Pro 20X 停止新增订阅、企业大客户销售与高强度 Agent 推理共同说明“单位结果成本”正在替代单 token 成本 | commercial | [OpenAI 订阅报道](https://mp.weixin.qq.com/s/3a4XdRaZxpOnDOq9DL2QcA) / [Anthropic 销售报道](https://mp.weixin.qq.com/s/heNKavi56U2pMNNFhnV4MA) | 编辑数据卡 | 中，媒体披露 |

## 本期精读选择

只把 S-Space、Stolen Thoughts、Action Map Policy 放进可见的“本周论文精读”章节。DeepSeek V4.1 Flash 与 LLaDA-Image 保留为国产模型技术报告；OpenAI 研究加速与 Anthropic 电商 Agent 配方作为公司研究 / Agent 工程专题；RAND 解读作为产业结构文章精读。

## 2026-09-13 OpenAI 覆盖补充审查

修订后 30 页。原有置信度不能当成官方网页已直读的证明；本轮 web 工具不可用，直接请求 OpenAI 公告、Images 发布与开发者指南均返回 403。下列新页依据完整公众号正文及其嵌入图像，已在页面中标注报道口径。

| 来源文件 | 补充主题与原文 | 页码 | 内容 / 证据与边界 | 视觉 |
|---|---|---|---|---|
| 00_NLP应用/topc-chatgpt.md | [研究加速全文译文](https://mp.weixin.qq.com/s/NjCOtCiK62_9MiGQzlx9LA) | 5—6 | article-deep-read；六阶段研究流程、支持频道下降、人工干预；运行时长不能当作生产率倍数，同期算力增长构成混杂因素 | 内部支持曲线原图 |
| 同上 | [An Alien Mind 解读](https://mp.weixin.qq.com/s/f_5eMcbaZSs2vbK4JQ4nzA) | 7 | article-deep-read；作者观点：对齐、监控与研发节奏；没有把建议写成已生效政策 | 报道引用的运行时长图、编辑归纳回路 |
| 同上 | [N–S 成果与署名报道](https://mp.weixin.qq.com/s/pVKhiX3SrcI59P1Sjsl6yQ) | 8—9 | research claim；约万名 Agent / 88 小时均为转述；有外力 N–S、无外力 Euler 与他人有外力 Euler 严格区分；未独立核验证明、代码与双方时间线 | 涡旋示意原图、条件对照表 |
| 同上 | [Astra 指南译文](https://mp.weixin.qq.com/s/PndMcyDwl_0Ev-pAL2ykNg) | 10 | article-deep-read；异步工具、执行中追加指令、推理强度与缓存、Skills 规则；仅作本周指南摘要，官方页面本轮访问受限 | 功能 / 应用责任对照表 |
| 同上 | [跨软件创作原文](https://mp.weixin.qq.com/s/QYn2OeBXhsO2O7XLwE0lfA) | 11 | demo；第三方工作流示例，生成归 Seedance，预演归 Blender；不推断插件/API或普遍成功率 | 已查看 8 段视频元数据，下载前两段原视频封面，保留观看原文入口 |
| 同上 | [评测争议报道](https://mp.weixin.qq.com/s/CFE_wh9TaUt15aEMcxgB2Q) | 12 | disputed brief；未独立核验历史快照，不下作弊结论；版本 / 条件 / 成本作为复核标准 | 报道数字变化与复现条件表 |
| 同上 | [Images 两档与规模报道](https://mp.weixin.qq.com/s/37bo6MT5K2tfCZjVtA3eWQ) | 24—25 | product brief；每周 30 亿为产品与 API 合计；Flare / Sunburst 定位按报道；没有绝对价格，因此不推断价格高低 | APPSO 原始样例 |
| 同上 | Pro 20X 订阅与额度 | 28 | commercial；补充报道中的 5X / 20X 对应每周 50 / 200 条；非当前账户权限承诺 | 订阅卡片 |

### 其余候选的处理

- Brockman AGI 访谈：观点性采访，与研发进展页重叠，不单开页面，不把“AGI 没有发布日期”写成技术认定。
- GPT-6 Sol 内测：第 12 页保留待观察信号，不按正式发布计入。
- 验证码游戏：第三方娱乐性个例，与跨软件示例重复，暂不纳入；不能推成真实验证系统通用破解率。
- 果蝇接 ChatGPT：第三方项目，缺少映射有效性证据，不纳入 OpenAI 公司成果。
- S-Space：MirroS 研究，继续保留在论文精读，不能作为 OpenAI 自身成果。
- 陶哲轩的文章与数学共同体讨论：数学验证页吸收正确性、可读性和理解价值的编辑视角；本轮未直读陶哲轩原文，不新增对其个人观点的直接归因。
- BSD / 霍奇、后续 AGI 发布日期与“蒸馏税”收入比例：证据不足，排除确定性结论。
