# Algorithm and Programming 102

- Course repository for weekly lecture notes, code snippets, and class discussion stories.
- The repository grows every week in a predictable structure.

## Goal of This Repo
- Keep all curriculum material in one place.
- Give students short, practical algorithm/data-structure examples.
- Make weekly teaching content easy to follow and update.

## Repository Structure
- `weeks/week-XX/`
  - `README.md` -> lecture notes for that week
  - `story.md` -> class discussion story/context
  - `src/` -> in-class code snippets

## Current Weeks
- `weeks/week-01`
  - Topics: Stack, Queue, Singly Linked List
- `weeks/week-02`
  - Topics: Trees, Binary Search Trees (BST)

## How Students Should Use This Repo
- Start from the current week folder in `weeks/`.
- Read that week's `README.md` first (concepts, workflows, homework).
- Read `story.md` for class discussion context.
- Open the files in `src/` and review code line by line.

## Quick Run Examples
- Week 01:
  - `python3 -i weeks/week-01/src/1-stack.py`
  - `python3 -i weeks/week-01/src/2-queue.py`
  - `python3 -i weeks/week-01/src/3-linked_list.py`
- Week 02:
  - `python3 -i weeks/week-02/src/1-trees.py`
  - `python3 -i weeks/week-02/src/2-binary_search_tree.py`

## How We Add New Weeks
- Keep the same pattern each week:
  - `README.md` for lecture notes
  - `story.md` for class discussion
  - `src/` for code snippets
- Create a new week folder with:

```bash
mkdir -p weeks/week-03/src
touch weeks/week-03/README.md weeks/week-03/story.md
```
