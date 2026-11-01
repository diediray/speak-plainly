# 说人话 · Speak Plainly

[English](README.md)

有依据地判断，把话说清楚，把事情做实在。

一个用于改善 AI 回答和协作的轻量 skill：听懂当前问题，接续已有成果，作出有用的判断，删掉平凡真和重复解释，保留决定结论的事实与条件。

中文名是 **说人话**，英文名为 **Speak Plainly**，GitHub仓库名为 **`speak-plainly`**。技能调用名沿用 **`useful-judgment`**。

## 使用

在支持技能的工具里，直接说：

> 说人话，告诉我你怎么判断。

或：

> 不要防御，把这段改清楚，有用的条件留下。

技能描述也匹配“少说废话”及相近的表达、协作改进要求。需要直接指定时，可以写：

> 本次对话使用 $useful-judgment。

自动选用由宿主工具根据请求与技能描述决定。它按任务启用；安装不等于在每个新对话中全程加载。

## 安装

**通过 Codex 安装：** 将本仓库地址交给 Codex，要求使用 `$skill-installer` 安装仓库中的 `skills/useful-judgment`。

**手动安装：** [下载技能ZIP](https://raw.githubusercontent.com/diediray/speak-plainly/v1.2.0/downloads/useful-judgment-v1.2.0.zip)，解压后将整个 `useful-judgment` 文件夹放进技能目录。Codex 可使用 `~/.agents/skills/`；已有安装使用 `~/.codex/skills/` 时也可沿用。技能列表更新后即可使用。

## 它怎样工作

- 找回底稿、已有结果和已确认的决定，再接着完成本轮任务。
- 按用户所问的尺度作判断，把关键依据放在判断旁边。
- 先接清材料分别支持的关系，再提炼概括；新证据会改变正文或方案。
- 按句子承担的作用合并重复，保留实验条件、因果衔接与角色关系。

主体保持五段。复杂说明可借助只读校订；简单回答直接完成。

## 文件

- [技能主体](skills/useful-judgment/SKILL.md)
- [让证据改变决定](skills/useful-judgment/references/evidence-to-decision.md)
- [校订方法](skills/useful-judgment/references/reply-editing.md)
- [交付示例](skills/useful-judgment/references/accepted-examples.md)
- [验证说明](EVALUATION.md)
- [更新记录](CHANGELOG.md)

## 贡献

欢迎用具体问题改进：提供原请求、实际答复，以及答复漏掉或多加了什么。优先修改已有方法，让改进体现在答案里。

## 许可

[MIT](LICENSE)。
