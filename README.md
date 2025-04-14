Set 1
Q1. Git - Project Initialization (InvoiceApp) Steps:
1.	mkdir InvoiceApp && cd InvoiceApp
2.	git init
3.	git remote add origin https://github.com/username/InvoiceApp.git
4.	git add .
5.	git commit -m "Initial commit"
6.	git push -u origin main
Q2. JQL - Advanced Search
a.	created >= -10d AND resolution = EMPTY
b.	due <= 3d
c.	issuetype = Bug AND resolved >= -5dDifference:
-	resolution = EMPTY: Not resolved
-	status != Done: Status is not 'Done'
-	
Set 2
Q1. GitHub - Team Collaboration
1.	Create repo
2.	Add README.md
3.	Settings > Collaborators > Invite
4.	Settings > Branch Protection
Q2. JQL - Transitions
a.	status CHANGED FROM "To Do" TO "In Progress" AFTER -7d
b.	assignee = currentUser() AND due < now()
c.	status CHANGED TO Done AFTER -2dCHANGED: Tracks status transitions

Set 3
Q1. Git - Branching & PR
1.	git checkout -b search-feature
2.	git add . && git commit -m "search feature" && git push origin search-feature
3.	Open PR & assign reviewer
4.	Merge PR
Q2. JQL
a.	created >= "2025-03-01" AND created <= "2025-03-10"
b.	updated >= -3d
c.	status CHANGED FROM "In Progress" TO "Testing" AFTER "2025-04-01"updated vs created: updated includes edits

Set 4
Q1. Git - Merge Conflict
1.	git pull origin branch-name
2.	Edit file manually
3.	git add filename && git commit && git push
Q2. JQL
a.	component = Frontend AND resolution = EMPTY
b.	labels IN (urgent, production-fix)
c.	sprint in openSprints() AND assignee in membersOf("team-name")
Labels: Tags | Components: Modules

Set 5
Q2. JQL - Release Readiness
a.	fixVersion = "v2.0"
b.	fixVersion = "v2.0" AND issuetype = Bug AND resolution = EMPTY
c.	fixVersion = "v2.0" AND issuetype = Task AND resolved >= -7d

Set 6
Q1. Git - Tag & Release
1.	git tag v1.0
2.	git push origin v1.0
3.	GitHub > Releases > New Release
Q2. JQL - SLA
a.	due <= -2d AND resolution = EMPTY
b.	labels = "SLA-48hrs" AND resolution = EMPTY
c.	due >= startOfWeek() AND due <= endOfWeek()

Set 7
Q1. Jira - Scrum Setup
1.	Create project
2.	Auto board setup
3.	Add backlog items
4.	Start sprint
Q2. JQL
a.	assignee in membersOf("Team-A") AND resolution = EMPTY
b.	status = Blocked AND status CHANGED TO Blocked BEFORE -2d
c.	issuetype = Bug AND assignee = currentUser() AND status = "In Review"

Set 8
Q1. GitHub - Fork & Contribute
1.	Fork repo
2.	git clone https://github.com/yourname/repo.git
3.	git checkout -b patch-1, commit, push
4.	Open PR
5.	
Q2. JQL
a.	created >= startOfWeek()
b.	resolved >= startOfQuarter(-1) AND resolved <= endOfQuarter(-1)
c.	due <= 7d AND resolution = EMPTY AND assignee in membersOf("team-name")
# chetan04Demo
