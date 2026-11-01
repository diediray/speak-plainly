# Speak Plainly · 说人话

[中文说明](README.zh-CN.md)

Make a clear call. Explain what matters. Follow through.

A lightweight agent skill for answering the actual question, making reasoned judgments, and continuing work from what already exists. It cuts empty caveats and repeated explanations while keeping the facts, conditions, and connections that make an answer useful.

**Speak Plainly** is the English name of **说人话**. The skill ID remains **`useful-judgment`**. Its instructions and examples are currently written in Chinese.

## Use

In a tool that supports skills, ask naturally:

> 说人话，告诉我你怎么判断。

> 不要防御，把这段改清楚，有用的条件留下。

The description also covers similar requests to improve an answer or the way the assistant works with you. To select it explicitly:

> Use $useful-judgment for this conversation.

The host selects skills from their descriptions. Installation makes the skill available; requests determine when it is loaded.

## Install

**With Codex:** give Codex this repository's address and ask it to use `$skill-installer` to install `skills/useful-judgment`.

**Manually:** [download the skill ZIP](https://raw.githubusercontent.com/diediray/speak-plainly/v1.2.0/downloads/useful-judgment-v1.2.0.zip) and place the extracted `useful-judgment` folder in your skills directory. Codex supports `~/.agents/skills/`; an existing `~/.codex/skills/` setup can also be used. Use it once the skill list refreshes.

## How it works

- Recover the current draft, existing results, and agreed decisions before continuing the task.
- Judge the question at the level asked, with the deciding evidence beside the judgment.
- Connect the relationships supported by the material before summarizing; let new evidence change the answer or plan.
- Merge repeated wording by its function, keeping useful conditions, transitions, and relationships.

The core instructions take five paragraphs. Longer explanations can use a separate reader; simple answers stay simple.

## Contents

- [Core instructions](skills/useful-judgment/SKILL.md)
- [Let evidence change the decision](skills/useful-judgment/references/evidence-to-decision.md)
- [Editing method](skills/useful-judgment/references/reply-editing.md)
- [Examples](skills/useful-judgment/references/accepted-examples.md)
- [Evaluation notes](EVALUATION.md)
- [Changelog](CHANGELOG.md)

## Contribute

Bring a concrete example: the request, the actual answer, and what it missed or added. Prefer a useful change to the existing method, demonstrated in the resulting answer.

## License

[MIT](LICENSE).
