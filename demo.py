**Set 1**

**Q1. Git Scenario – Recover Deleted Local Changes**
- **If staged:**
  ```bash
  git reset HEAD <file>
  git checkout -- <file>
  ```
- **If only modified:**
  ```bash
  git checkout -- <file>
  ```
- **Deleted after last commit:**
  ```bash
  git checkout HEAD -- <file>
  ```

**Q2. JQL – Tracking Creation & Reopened Issues**
a. `assignee = currentUser() AND created >= -14d`
b. `status CHANGED FROM Done TO Reopened`
c. `issuetype = Bug AND status != Done AND reporter in membersOf("qa-team")`

**Explanation:**
`status CHANGED` helps in identifying transitions like reopening issues, making it ideal for tracking workflow regressions.

---

**Set 2**

**Q1. GitHub Scenario – Manage Repo Access**
- **Add collaborator:** Go to repo > Settings > Collaborators > Add by username/email.
- **Prevent force push to main:** Settings > Branches > Add branch protection > Enable "Prevent force pushes".
- **Required PR reviews:** Same section > Enable "Require pull request reviews before merging".

**Q2. JQL – Priority, Due Dates, and Overdue Items**
a. `priority = Critical AND assignee in membersOf("team-name")`
b. `due <= 3d AND status != Done`
c. `created >= -20d AND due < now() AND status != Done`

**Explanation:**
Dynamic dates like `<= 3d` adjust in real-time, while fixed ones need manual updates.

---

**Set 3**

**Q1. Jira Scenario – Add Custom Workflow Status**
- **Add status:** Go to Workflows > Edit > Add Status "Code Review"
- **Update transitions:** Add transitions from "In Progress" to "Code Review" and from "Code Review" to "Done"
- **Reflect on board:** Map "Code Review" in board column settings.

**Q2. JQL – Workflow Transition Metrics**
a. `status CHANGED TO "Code Review" AFTER -5d`
b. `status CHANGED FROM "In Progress" TO "Blocked"`
c. `issuetype = Story AND status WAS NOT "Testing"`

**Explanation:**
Use `NOT status WAS` to find issues that skipped a stage.

---

**Set 4**

**Q1. Git Scenario – Clean Up Commits Before Push**
- **Squash:**
  ```bash
  git rebase -i HEAD~n  # choose squash
  ```
- **Rewrite message:** Done in rebase interactive mode.
- **Push safely:**
  ```bash
  git push origin main --force-with-lease
  ```

**Q2. JQL – Epic, Sprint & FixVersion Filters**
a. `"Epic Link" = "Checkout Redesign"`
b. `sprint in openSprints() AND status != Done`
c. `issuetype = Story AND fixVersion = v1.1`

**Explanation:**
`fixVersion` tracks what is shipping when—critical for planning releases.

---

**Set 5**

**Q1. GitHub Scenario – Using GitHub Issues for Planning**
- **Enable issues:** Repo Settings > Features > Enable Issues
- **Create labels:** Issues > Labels > New label
- **Assign & close:** Issues > Click issue > Assign > Close with comment

**Q2. JQL – Label, Component, and Reporter Filters**
a. `labels = security AND status != Done`
b. `component = API AND created >= -7d`
c. `reporter = devops@example.com`

**Explanation:**
Use **components** for system parts (API, UI), **labels** for tags (urgent, enhancement).

---

**Set 6**

**Q1. Git Scenario – Clone and Contribute to a Repo**
- Clone:
  ```bash
  git clone <repo-url>
  cd <repo-folder>
  ```
- Branch:
  ```bash
  git checkout -b feature-contact-form
  ```
- Commit and push:
  ```bash
  git add .
  git commit -m "Added contact form"
  git push origin feature-contact-form
  ```
- Pull request: Go to GitHub > Compare & pull request > Submit PR.

**Q2. JQL – Bug Analysis Over Time**
a. `issuetype = Bug AND status != Done AND created <= -10d`
b. `issuetype = Bug AND resolved - created <= 3d`
c. `issuetype = Bug AND status CHANGED TO Reopened`

**Explanation:**
`created`, `resolved`, and `status changed` track bug timelines and fix efficiency.

---

**Set 7**

**Q1. Jira Scenario – Dashboard Customization**
- **Filter:** `issuetype = Bug AND status != Done`
- **Pie chart:** Dashboard > Add gadget > Pie Chart > Configure with filter and Priority
- **Table:** Add Filter Results gadget, group by Assignee

**Q2. JQL – Assignee, Due Date, Priority Filters**
a. `assignee = currentUser() AND status != Done`
b. `priority = High AND due >= startOfWeek() AND due <= endOfWeek()`
c. `assignee IS EMPTY`

**Explanation:**
Unassigned tasks may be overlooked—important for workload balance.

---

**Set 8**

**Q1. Git Scenario – Work with Remote Branches**
- **Track branch:** `git branch -u origin/report-gen`
- **Pull teammate's changes:** `git pull origin report-gen`
- **Delete remote branch:** `git push origin --delete report-gen`

**Q2. JQL – User, Status, and Date Combinations**
a. `assignee = john.doe AND status = "In Progress"`
b. `creator = currentUser() AND created >= startOfMonth()`
c. `status CHANGED TO Done AFTER "2025-04-01"`

**Explanation:**
`startOfMonth()` simplifies monthly reports without hardcoding dates.

