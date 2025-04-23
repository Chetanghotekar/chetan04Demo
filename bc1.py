Here’s a comprehensive yet concise answer key for all the Git, GitHub, and Jira practical scenarios provided in Sets 1–8. Each answer is framed clearly and simply for exam or interview-style use:

---

### **Set 1**

**1. Jira Setup:**
- Sign up at [https://www.atlassian.com/software/jira](https://www.atlassian.com/software/jira)
- Create a new site and choose **"Jira Software."**
- Create a new project and choose a template (Scrum or Kanban).
- Navigate to **Projects > Your Project > Board** to access the project board.

**2. Basic Git Operations:**
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

**3. JQL Search:**
```sql
assignee = currentUser() AND status = "In Progress"
```

---

### **Set 2**

**1. GitHub Repository:**
- Go to [https://github.com](https://github.com)
- Click **"New repository"**
- Fill in details and click **"Create repository"**
- Share the **repository link** or add your teammate as a **collaborator** via **Settings > Collaborators**.

**2. Jira Scrum Project:**
- In Jira, click **Create Project > Scrum template**
- Name your project and choose whether to use a team-managed or company-managed project
- Configure board, sprints, and backlog settings under **Project Settings**.

**3. Git Branching:**
```bash
git checkout -b feature-branch
# Make changes
git add .
git commit -m "Added new feature"
git checkout main
git merge feature-branch
```

---

### **Set 3**

**1. Git Installation & GitHub Link:**
```bash
# Install Git (from git-scm.com)
git config --global user.name "YourUsername"
git config --global user.email "you@example.com"
```

**2. Jira Issue Creation:**
- Click **Create Issue**
- Choose **Bug** type, assign it under the appropriate **Epic**, set priority and assign it to a developer.

**3. Jira Filter Creation:**
- Use JQL: `priority = High`
- Click **Save as Filter**, give it a name, and optionally **share it with the team**.

---

### **Set 4**

**1. Local Git Initialization:**
```bash
cd your-project-folder
git init
git remote add origin https://github.com/username/repo.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

**2. Git Push and Pull:**
```bash
git stash       # Save your work temporarily
git pull origin main
git stash pop   # Reapply your work
```

**3. Jira Dashboard:**
- Go to **Dashboards > Create Dashboard**
- Add gadgets like **Filter Results**, **Sprint Burndown**, and **Assigned to Me**
- Use saved filters to configure each gadget.

---

### **Set 5**

**1. Jira Navigation:**
- Go to **Projects > Your Project**
- Click **Backlog** for sprint backlog
- Click **Board > Active Sprints** for the active sprint board.

**2. Git Commit:**
```bash
git add filename
git commit -m "Descriptive commit message"
```

**3. Git Merge:**
```bash
git checkout main
git pull origin main
git merge feature-branch
git push origin main
```

---

### **Set 6**

**1. GitHub Setup:**
- On GitHub, create a new repo
- Check **"Add a README.md"** and add a `.gitignore` template for Java
- Clone and start working.

**2. Jira Epic Creation:**
- Go to **Backlog > Create Issue > Change Type to Epic**
- Create stories, then drag them under the Epic or set **Epic Link** in each story.

**3. JQL Search:**
```sql
sprint in openSprints() AND status != Done
```

---

### **Set 7**

**1. Git Commit:**
```bash
git add filename
git commit -m "Descriptive message"
```

**2. Git Pull (Avoid Conflicts):**
```bash
git stash
git pull origin main
git stash pop
```

**3. Jira Kanban Board Configuration:**
- Create a new **Kanban** project or board
- Go to **Board Settings > Columns**
- Add or rename columns like **To Do, In Progress, Testing, Done**.

---

### **Set 8**

**1. JQL Search:**
```sql
assignee = currentUser() AND status = "In Progress"
```

**2. Jira Story Creation:**
- Click **Create Issue**
- Set type to **Story**, enter summary, description, priority, and assign to developer
- Optionally link it to an Epic.

**3. Git Branching for Hotfix:**
```bash
git checkout main
git pull origin main
git checkout -b hotfix-branch
# Apply fix
git commit -am "Hotfix applied"
git checkout main
git merge hotfix-branch
```

---

Let me know if you want printable notes or flashcards for these!
