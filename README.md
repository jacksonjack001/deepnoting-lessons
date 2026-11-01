# deepnoting-lessons

DeepNoting 的深度学习、NLP 与大模型实验资料库。仓库同时包含可运行的 Python 教学示例、模型训练实验、视觉模型缓存对比实验，以及按周整理的 AI 进展演示文稿。

这里的脚本是相互独立的实验，不是一个已经打包发布的 Python 库；目前没有统一的 `requirements.txt`、`pyproject.toml` 或端到端训练流水线。

## 内容导航

### 课程示例 `lessons/`

从经典表示学习逐步过渡到 Transformer：

- [`1-wordembedding.pptx`](lessons/1-wordembedding.pptx)：词嵌入课程幻灯片。
- [`word_embedding.py`](lessons/word_embedding.py)：在一组中文句子上训练 Word2Vec、FastText，并加载 `bert-base-chinese`，比较“苹果”在水果/公司两种语义下的句向量相似度；运行后生成 `sentence_similarities.csv` 和 `disambiguation_ability.csv`。
- [`2-attention.py`](lessons/2-attention.py)：用 Matplotlib 动画演示注意力、Multi-Head Attention（MHA）、Multi-Query Attention（MQA）和 Grouped-Query Attention（GQA），输出 MP4 视频。
- [`3-transformer_train_demo.py`](lessons/3-transformer_train_demo.py)：使用 PyTorch 从零搭建一个极小的 Encoder-Decoder Transformer，在 6 组简单的“数字到字母”数据上训练并进行贪心解码。
- [`locagent_astropy.xlsx`](lessons/locagent_astropy.xlsx)：课程/实验相关的表格材料。

### 强化学习 `RL/`

- [`demo_ppo.py`](RL/demo_ppo.py)：基于 PyTorch 的 Actor-Critic PPO 教学实现，在 `CartPole-v1` 上训练。
- [`demo_ppo_llm.py`](RL/demo_ppo_llm.py)：以 GPT-2 文本生成为策略，使用“生成文本长度”作为简单奖励，演示 PPO 风格的语言模型更新过程。

### 记忆模块与微调 `memory-SFT/`

- [`train_engram.py`](memory-SFT/train_engram.py)：为 Qwen3 解码器层注入 Engram/N-gram 记忆模块，并结合 LoRA/监督微调训练。
- [`train_smft.py`](memory-SFT/train_smft.py)：将指定层的 MLP 替换为 Product Key Memory，只更新检索到的部分记忆参数，包含稀疏梯度掩码和 loss 曲线保存。

这两个脚本面向多 GPU 和真实数据集训练，默认模型、数据集和输出目录是作者机器上的绝对路径，需要先修改脚本顶部的配置。

### 视觉模型缓存实验 `vlm_cache/`

- [`compare_vlm_cache.py`](vlm_cache/compare_vlm_cache.py)：向多个视觉语言模型发送同一张图片，比较首次请求、复用会话缓存和重新上传图片三种情况下的耗时，并将结果追加写入 `vision_model_benchmark3.csv`。

### Vibe Coding 材料 `vibecoding/`

- [`locagent_astropy.xlsx`](vibecoding/locagent_astropy.xlsx)：与 `lessons/` 中对应的实验表格材料。
- [`demo.py`](vibecoding/demo.py)：实验占位文件，当前没有可执行的完整示例。

### AI 进展周报 `ainews/`

每个日期目录都包含一个可直接在浏览器打开的独立 HTML 演示文稿及其图片、视频资源；日期采用 `YYMMDD` 命名。当前已收录：

| 日期 | 内容 |
| --- | --- |
| [2026-08-23](ainews/260823/index.html) | 本周 AI 进展周报（2026.08.17–08.23） |
| [2026-08-29](ainews/260829/index.html) | AI 进展周报（2026.08.24–08.29） |
| [2026-09-06](ainews/260906/index.html) | AI 进展周报（2026.08.30–09.05） |
| [2026-09-12](ainews/260912/index.html) | AI 进展周报（2026.09.06–09.12） |
| [2026-09-26](ainews/260926/index.html) | 双周 AI 进展观察（2026.09.13–09.26） |
| [2026-10-11](ainews/261011/index.html) | 一周 AI 进展观察（2026.10.06–10.10） |
| [2026-10-16](ainews/261016/index.html) | 一周 AI 观察（2026.10.12–10.16） |
| [2026-10-23](ainews/261023/index.html) | 一周 AI 观察（2026.10.17–10.23） |
| [2026-10-30](ainews/261030/index.html) | 一周 AI 观察（2026.10.24–10.30） |

历史入口见 [`ainews/his/index.html`](ainews/his/index.html)，部分周报还附带 `audit-*.md`、`evidence-map.md` 等核查材料。

## 环境准备

建议使用 Python 3.10+，按要运行的实验分别安装依赖。常见依赖可以一次安装：

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install -U pip
python -m pip install torch numpy matplotlib jieba gensim transformers scikit-learn gym openai datasets peft tokenizers sympy
```

其中：

- `lessons/word_embedding.py` 需要 `jieba`、`gensim`、`transformers`、`torch` 和 `scikit-learn`，首次运行会下载 `bert-base-chinese`。
- `lessons/2-attention.py` 需要系统中的 FFmpeg 才能保存动画视频。
- `RL/demo_ppo.py` 使用 `gym` API；不同 Gym 版本可能存在兼容性差异。
- `RL/demo_ppo_llm.py` 首次运行会下载 GPT-2，并直接进入训练循环，建议先确认显存、磁盘和网络条件。
- `memory-SFT/` 通常需要 CUDA、多 GPU、较大的显存和本地模型/数据集；`flash_attention_2` 是否可用取决于硬件与安装环境。
- `vlm_cache/compare_vlm_cache.py` 依赖外部 API、图片网络访问和项目外部的 `openai_tools.client`，不能脱离原运行环境直接执行。

## 快速运行

以下命令均在仓库根目录执行：

```bash
# 词嵌入与中文语义消歧
python lessons/word_embedding.py

# 注意力机制动画（需要 FFmpeg）
python lessons/2-attention.py

# 极小 Transformer 训练与推理
python lessons/3-transformer_train_demo.py

# CartPole PPO
python RL/demo_ppo.py
```

训练类脚本的默认路径和超参数仅供示例。运行 [`train_engram.py`](memory-SFT/train_engram.py)、[`train_smft.py`](memory-SFT/train_smft.py) 或视觉缓存实验前，请先检查并替换模型路径、数据路径、API 客户端和输出目录；不要把密钥写入仓库。

## 输出文件

部分脚本会在当前工作目录或脚本目录写入实验产物，例如：

- `sentence_similarities.csv`、`disambiguation_ability.csv`
- `attention_mechanism_explained——3.mp4`
- `vision_model_benchmark3.csv`
- `memory-SFT` 训练产生的 checkpoint、loss CSV 和 `loss_curve.png`

这些输出可能较大，建议在独立的实验目录中运行，并根据需要加入 `.gitignore`。

## 说明

仓库中的代码主要用于教学、原理验证和实验记录。示例数据集很小，PPO/Transformer 代码也进行了极度简化，结果不代表生产模型或严谨基准测试；AI 周报 HTML 中的观点、价格和性能数字应以页面列出的原始来源为准。
