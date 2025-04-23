Here's a breakdown of answers for Sets 9 through 16, ideal for interview prep or practical exams:

---

### **Set 9**

1. **Jira Cloud Instance (User Creation & Role Assignment):**
   - Go to **Jira Admin > User Management > Invite Users**.
   - Enter the emails of new members and select the product access.
   - After they accept, go to **Project Settings > People** to add them to the project and assign roles like Developer, Admin, etc.

2. **Git Commit and Push:**
   ```bash
   git add .
   git commit -m "Updated multiple files"
   git push origin main
   ```

3. **JQL Search (Bugs created in last 7 days):**
   ```jql
   labels = Bug AND created >= -7d
   ```

---

### **Set 10**

1. **GitHub Repository Setup:**
   - Go to GitHub > New Repository.
   - Fill in details, select a license from the dropdown.
   - After creation, go to **Settings > Branches**, add a rule for `main` to protect it (e.g., require pull request review).

2. **Jira Sprint Creation:**
   - Go to the board > Backlog view.
   - Click **Create Sprint**.
   - Drag backlog items into the sprint and click **Start Sprint** with a name and duration.

3. **Git Branch Creation:**
   ```bash
   git checkout -b feature-branch
   git push -u origin feature-branch
   ```

---

### **Set 11**

1. **Git Installation and Configuration:**
   ```bash
   sudo apt install git        # or use installer for Windows/Mac
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

2. **Jira Issue Creation:**
   - Click **Create Issue**.
   - Select project, issue type (Bug/Task), enter summary/details.
   - Set **Priority = High**, assign to a developer, and click **Create**.

3. **Jira Dashboard Setup:**
   - Go to Dashboards > Create Dashboard.
   - Add gadgets like *Sprint Health*, *Two-Dimensional Filter Statistics*.
   - Configure gadgets to filter by project/sprint/status.

---

### **Set 12**

1. **Local Git Initialization:**
   ```bash
   git init
   git remote add origin https://github.com/user/repo.git
   git pull origin main
   ```

2. **Git Pull and Merge:**
   ```bash
   git pull origin main
   # If conflicts, resolve them in files
   git add .
   git commit -m "Resolved merge conflicts"
   ```

3. **Jira Filter Creation:**
   - Use JQL: `assignee = currentUser() AND status != Done`
   - Click **Save as filter**, name it, and click **Details > Share with project/team**.

---

### **Set 13**

1. **Jira Project Setup:**
   - Go to Projects > Create Project > Scrum.
   - Name the project and select a template.
   - Go to **Project Settings > Permissions** to add the client with appropriate access.

2. **Git Add and Commit:**
   ```bash
   git add file1.txt file2.js
   git commit -m "Updated specific files"
   git push origin main
   ```

3. **Git Merge without Fast-Forward:**
   ```bash
   git checkout main
   git merge --no-ff feature-branch -m "Merge feature branch"
   ```

---

### **Set 14**

1. **GitHub Repository Collaboration:**
   - Go to repository > **Settings > Collaborators & Teams**.
   - Invite the developer by GitHub username/email.
   - Assign appropriate access (Read/Write/Admin).

2. **Jira Epic and Story Linking:**
   - Create an Epic from the backlog.
   - When creating stories, select the Epic Link field and choose the epic.

3. **Git Branch Deletion:**
   ```bash
   git branch -d feature-branch       # locally
   git push origin --delete feature-branch  # remotely
   ```

---

### **Set 15**

1. **Git Configuration Update:**
   ```bash
   git config --global user.email "newemail@example.com"
   ```

2. **Jira Sprint Management:**
   - Go to active sprint > **Complete Sprint**.
   - Jira will prompt to move incomplete issues to the next sprint or backlog.

3. **JQL Advanced Search:**
   ```jql
   assignee = currentUser() AND status != Done
   ```

---

### **Set 16**

1. **Jira Filter Creation:**
   - Same as Set 12 Q3. Use the JQL and share via **Details > Edit Permissions**.

2. **Jira Kanban Board Configuration:**
   - Create a new Kanban board via **Boards > Create board**.
   - Customize columns via **Board Settings > Columns** and map statuses accordingly.

3. **Jira Issue Creation:**
   - Repeat steps from Set 11 Q2.

---

Need flashcards or mock questions for these sets?
