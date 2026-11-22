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

**Manually:** [download the current repository ZIP](https://github.com/diediray/speak-plainly/archive/refs/heads/main.zip), then copy `skills/useful-judgment` from the extracted repository into your skills directory. Keep the existing installation location when updating.

## How it works

- Choose steps for the current task, reuse existing results, and skip work that adds no useful result.
- Recover the current draft, existing results, and agreed decisions before continuing the task.
- Put the requested scope in the judgment and keep deciding evidence and useful conditions beside it.
- Compare choices by the effect the user wants, addressing differences that change the direction before local details.
- Connect the relationships supported by the material before summarizing; let new evidence change the answer or plan.
- Review answers, notes, captions, and text inside figures for added information. Remove self-commentary and production notes that add no facts, explanation, judgment, or practical use; retain useful methods and conditions.
- Merge repeated wording by its function, keeping useful conditions, transitions, and relationships.

The core instructions cover everyday answers and collaboration. Editing, revision, and detailed examples are loaded when relevant. Separate review is used when the content needs it.

## Contents

- [Core instructions](skills/useful-judgment/SKILL.md)
- [Let evidence change the decision](skills/useful-judgment/references/evidence-to-decision.md)
- [Editing method](skills/useful-judgment/references/reply-editing.md)
- [Editing scope](skills/useful-judgment/references/editing-guide.md)
- [Revision and selective undo](skills/useful-judgment/references/revision.md)
- [Examples](skills/useful-judgment/references/accepted-examples.md)
- [Evaluation notes](EVALUATION.md)
- [Changelog](CHANGELOG.md)

## Contribute

Bring a concrete example: the request, the actual answer, and what it missed or added. Prefer a useful change to the existing method, demonstrated in the resulting answer.

## Source and adaptation

The editing foundation adapts [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua), with Speak Plainly's methods for judgment, continued work, and removing empty caveats. Both contributions are retained under the [MIT license](LICENSE).

## License

[MIT](LICENSE).
