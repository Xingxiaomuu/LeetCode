# LeetCode Solutions

This folder contains my personal solutions to problems on [LeetCode](https://leetcode.com/). The code is organized by problem number and title for easy reference and review.

## About

- All solutions are written as part of my algorithm and data structure practice.
- Covers common algorithm topics such as binary search, bucket sort, dynamic programming, backtracking, greedy algorithms, etc.

## Purpose

- Strengthen algorithm fundamentals
- Prepare for coding interviews
- Record solution approaches and optimizations

Continuously updating — feedback and suggestions are welcome!

# 将本地目录推送到 GitHub 仓库的步骤

**✅ 前提条件**  
1. 已安装 Git  
2. 已有一个 GitHub 账号，并新建了一个仓库（假设名为 `LeetCode`）

---

**🛠️ 一次性设置步骤**  

1. **打开终端**（PowerShell 或 CMD），导航到本地目录：  
   ```bash
   cd "C:\Users\User\OneDrive\Documents\GitHub\My-projects\LeetCode"

2. **初始化 Git 仓库（如果未初始化）：**
   ```bash
   git init

3. **添加远程仓库地址（替换链接中的用户名和仓库名）：**
   ```bash
   git remote add origin https://github.com/你的用户名/LeetCode.git

4. **添加并提交所有文件：**
   ```bash
   git add .
   git commit -m "Initial commit"

5. **首次推送到 GitHub 仓库：**
   ```bash
   git branch -M main
   git push -u origin main

6. **🔁 后续更新流程**
   每次修改文件后执行以下命令：
   ```bash
   git add .
   git commit -m "更新说明"
   git push