Set 1
Q1: Git Scenario – Project Initialization
You’re starting a new project called InvoiceApp. Here's how to initialize Git, connect to GitHub, and push your project:

✅ Step-by-step Git Commands:
Initialize Git in the project folder:

bash
Copy
Edit
cd InvoiceApp     # Go to your project directory
git init          # Initialize the Git repository
Create a remote GitHub repo and connect it:

Go to GitHub → Click New repository → Name it InvoiceApp → Create.

Now connect it using:

bash
Copy
Edit
git remote add origin https://github.com/your-username/InvoiceApp.git
Add files, commit, and push:

bash
Copy
Edit
git add .                              # Stage all files
git commit -m "Initial commit"        # Commit with a message
git branch -M main                    # Rename branch to main (if needed)
git push -u origin main               # Push code to GitHub
Q2: JQL Advanced Search – Created, Due, and Resolution Filters
a. Issues created in the last 10 days that are still unresolved
sql
Copy
Edit
created >= -10d AND resolution = EMPTY
b. Issues due in the next 3 days
sql
Copy
Edit
due <= 3d
c. Bugs resolved in the last 5 days
sql
Copy
Edit
issuetype = Bug AND resolutiondate >= -5d
🔍 Explanation: resolution = EMPTY vs status != Done
resolution = EMPTY means the issue has never been resolved, regardless of status.

status != Done means the issue's current workflow state is not 'Done', but it might have been resolved before (e.g., re-opened).

📌 Example:

An issue can have status = In Progress but resolution = Done (reopened issue).

resolution = EMPTY is more reliable for checking truly unresolved issues.

✅ Set 1 is complete!
Would you like to move on to Set 2 now?








You said:
all set 


ChatGPT said:
Awesome! Let's continue step-by-step through all 8 sets. Here's a clear and concise breakdown for each scenario:

Set 1
Q1: Git – Project Initialization for InvoiceApp
bash
Copy
Edit
cd InvoiceApp                     # Navigate to project folder
git init                          # Initialize Git
git remote add origin https://github.com/your-username/InvoiceApp.git
git add .                         # Stage all files
git commit -m "Initial commit"    # Commit files
git branch -M main                # Set main as default branch
git push -u origin main           # Push to GitHub
Q2: JQL – Created, Due, Resolution
a. created >= -10d AND resolution = EMPTY

b. due <= 3d

c. issuetype = Bug AND resolutiondate >= -5d

Resolution = EMPTY checks if the issue hasn’t been resolved.
Status != Done checks if the issue is not in the “Done” column, even if it was resolved before.

Set 2
Q1: GitHub – Team Collaboration
Create a GitHub repo via UI or:

bash
Copy
Edit
gh repo create TeamProject --public --source=. --remote=origin
Add README.md:

bash
Copy
Edit
echo "# TeamProject" > README.md
git add README.md
git commit -m "Add README"
git push
Invite collaborators: Go to Settings → Collaborators → Add team members

Set branch protection:

Settings → Branches → main → Add Rule

Require PRs before merging

Require status checks

Q2: JQL – Transitions, Assignee, Due
a. status CHANGED FROM "To Do" TO "In Progress" AFTER -7d

b. assignee = currentUser() AND duedate < now()

c. status CHANGED TO "Done" AFTER -2d AND issuetype = Task

CHANGED tracks workflow transitions between statuses over time.

Set 3
Q1: Git – Branching & Pull Request
bash
Copy
Edit
git checkout -b search-feature      # Create branch
# Make code changes
git add .
git commit -m "Add search feature"
git push origin search-feature      # Push branch

# Go to GitHub → Open Pull Request → Assign Reviewer → Click "Create Pull Request"
# After review, click "Merge Pull Request"
Q2: JQL – Created/Updated/Transitioned
a. created >= "2025-03-01" AND created <= "2025-03-10"

b. updated >= -3d

c. status CHANGED FROM "In Progress" TO "Testing" AFTER "2025-04-01"

updated >= -3d is for recently modified issues.
created >= -3d is for newly added issues.

Set 4
Q1: Git – Resolve Merge Conflict
Pull and see conflict:

bash
Copy
Edit
git pull origin main
# Git will show conflict in file (marked by <<<<<<< HEAD)
Open the file and manually fix it, then:

bash
Copy
Edit
git add filename
git commit -m "Resolve merge conflict"
Q2: JQL – Component, Labels, Sprint
a. component = Frontend AND resolution = EMPTY

b. labels IN (urgent, production-fix)

c. sprint IN openSprints() AND assignee in membersOf("team-name")

Labels are flexible tags; components are for grouping based on technical ownership.

Set 5
Q1: GitHub – Team Collaboration
(Same steps as Set 2 Q1.)

Q2: JQL – Release Readiness
a. fixVersion = "v2.0"

b. fixVersion = "v2.0" AND issuetype = Bug AND resolution = EMPTY

c. fixVersion = "v2.0" AND issuetype = Task AND resolutiondate >= -7d

fixVersion links issues to a specific release milestone, helping in planning and tracking releases.

Set 6
Q1: Git – Tag and Release
bash
Copy
Edit
git tag -a v1.0 -m "Release version 1.0"
git push origin v1.0
Then go to GitHub → Releases → Draft a new release → Choose v1.0 tag.

Q2: JQL – Overdue & SLA
a. duedate <= -2d

b. labels = SLA-48hr OR "Time to resolution" <= "2d"

c. duedate >= startOfWeek() AND duedate <= endOfWeek()

JQL helps track SLAs by filtering time-bound tasks, ensuring teams meet deadlines.

Set 7
Q1: Jira – Scrum Setup
Create Project → Type: Scrum

Create board → Configure sprints

Add backlog items → Click Create Issue

Start sprint → Go to backlog → Click Start Sprint → Manage via active sprint view

Q2: JQL – Team Assignment and Status
a. assignee in membersOf("Team-A") AND resolution = EMPTY

b. status = Blocked AND updated <= -2d

c. issuetype = Bug AND assignee = currentUser() AND status = "In Review"

Team filters improve dashboards for sprint focus and workload visibility.

Set 8
Q1: GitHub – Fork & Contribute
Fork: Go to the repo → Click Fork

Clone:

bash
Copy
Edit
git clone https://github.com/your-username/original-repo.git
cd original-repo
Create a branch:

bash
Copy
Edit
git checkout -b fix-typo
# Make changes
git add .
git commit -m "Fix typo"
git push origin fix-typo
Open a pull request from fix-typo → Choose original repo and submit PR.

Q2: JQL – Time Filters
a. created >= startOfWeek()

b. resolutiondate >= startOfQuarter(-1) AND resolutiondate <= endOfQuarter(-1)

c. duedate <= 7d AND resolution = EMPTY AND assignee in membersOf("team-name")

startOfWeek(): Current week's start

startOfQuarter(-1): Previous quarter

<= 7d: Due within next 7 days

These help teams plan by week/quarter and handle urgent workload.

