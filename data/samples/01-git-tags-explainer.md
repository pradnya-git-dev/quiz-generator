---
id: git-tags-explainer
source: Written by Pradnya Kandarkar
---

# What is a Git tag?

A tag is a named pointer to a specific commit. Tags permanently mark a point in history, typically used to indicate release versions. Unlike branches, tags don't move. Every new commit on a branch advances the branch pointer forward. Tags don't do that. Once you tag a commit, the tag always points to that exact commit, no matter how many commits come after it.

Tags are a core **Git** feature. They work the same on GitLab, Bitbucket, or any Git host.

# Types of tags

**Lightweight**: Just a pointer, no extra metadata.
```bash
git tag v0.1.0
```

**Annotated**: Includes tagger name, date, and a message. Recommended for releases.
```bash
git tag -a v0.1.0 -m "Initial release"
```

# Common commands

**Create a tag:**
```bash
git tag -a v0.1.0 -m "Initial release"
```

**List all tags:**
```bash
git tag
```

**Tag a past commit:**
```bash
git tag -a v0.1.0 <commit-hash> -m "Initial release"
```

**Push a tag to remote:**
```bash
git push origin v0.1.0
```

**Push all tags to remote:**
```bash
git push origin --tags
```

**Delete a local tag:**
```bash
git tag -d v0.1.0
```

**Delete a remote tag:**
```bash
git push origin --delete v0.1.0
```

# Versioning convention

Tags typically follow [Semantic Versioning](https://semver.org/): `vMAJOR.MINOR.PATCH`

| Part | When to increment |
|------|-------------------|
| MAJOR | Breaking changes |
| MINOR | New features, backwards compatible |
| PATCH | Bug fixes |

# Tags on GitHub

GitHub surfaces tags under the **Tags** tab and lets you promote them to full Releases with release notes and downloadable assets.
