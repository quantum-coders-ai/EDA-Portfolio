# Contributing Guide

## Workflow
1. Create an issue for each task.
2. Create a branch from `main`:
   - `feat/<short-name>` for new features
   - `fix/<short-name>` for bug fixes
   - `chore/<short-name>` for tooling/infra
3. Commit using **Conventional Commits**:
   - `feat: add user login`
   - `fix: handle null in signup`
   - `docs: update readme`
4. Open a Pull Request; link the issue (`Closes #123`), pass CI, request review.
5. Merge via **Squash & Merge** after at least **1 approval**.

## Commit Message Format (Conventional Commits)
```
<type>(optional scope): <short summary>

[optional body]

[optional footer(s)]
```
**Types**: feat, fix, docs, style, refactor, perf, test, build, ci, chore