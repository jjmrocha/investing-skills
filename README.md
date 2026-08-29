# investing-skills

Agent skills for investing research, used with [Claude](https://claude.com/claude).

Each directory is a self-contained skill: a `SKILL.md` the agent loads, plus a `README.md` for humans browsing here.

## The skills

| Skill | Use it when |
|-------|-------------|
| [company-research](company-research/) | You need to understand a company — one you don't know, or one you know and suspect you're missing something about. Evidence only, never a verdict. |

## Install

Skills live in `~/.claude/skills/`. Clone once, then symlink the ones you want:

```bash
git clone https://github.com/jjmrocha/investing-skills.git ~/SOURCES/investing-skills

mkdir -p ~/.claude/skills
ln -s ~/SOURCES/investing-skills/company-research ~/.claude/skills/
```

Symlinks mean `git pull` updates the installed skills. To install all of them:

```bash
for d in ~/SOURCES/investing-skills/*/; do
  [ -f "$d/SKILL.md" ] && ln -sfn "${d%/}" ~/.claude/skills/
done
```

Restart Claude Code, or run `/doctor` to confirm they loaded.

Project-scoped instead of personal: put them in `.claude/skills/` inside the repo and commit them, so the whole team gets them.

## Using them

Skills load automatically when the agent judges the description to match what you're doing. You can also invoke one by name — `/company-research`.

## License

[MIT](LICENSE)
