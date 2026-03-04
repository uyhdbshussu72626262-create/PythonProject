
Chinese：
第四版图书管理系统
变化：

1.相比以前第一大变化是连接了sqlite3数据库，数据存储方法有字典->为数据库
从而实现数据的长久保存
2.加入权限管理文件permission.py，当是某个特定的对象时才能使用某个指令码
3.加入README.md文件实现版本迭代的内容告知

待加入以及改进的地方：
1.图书管理系统暂时未加入用户借阅，归还图书的功能，
2.用户借阅后会生成对应的借阅书籍列表，用户，管理员均可查看
3.黑名单计划，用户违约严重将被取消一段时间的借阅资格
4.根据用户借阅书籍情况生成借阅排行榜
5.加入第三方库matplotlib生成借阅曲线图
6.UI界面准备使用streamlit，做出简洁美观的图像画界面
7.sqlite3数据库性能孱弱，后续将使用MySQL数据库
8.接入AI，实现连接AI的功能，与AI对话的功能


注意：作者还在大学读书期间，版本迭代缓慢，主要利用下午或周末更新项目
且项目质量，水平还待进步，有意见的viewer可以给我发送谷歌电子邮件，
AI发展迅速，本人利用GPT.Claude等AI对项目进行多次重构，修改

English：

Library Management System v4.0

Key Updates
Database Migration (SQLite3): 
The most significant change is the transition from in-memory dictionary storage 
to a SQLite3 database. 
This enables data persistence, ensuring information is preserved across sessions.

Access Control Layer: Introduced permission.py to handle Role-Based Access Control (RBAC). 
Command execution is now restricted based on specific user permissions and roles.

Version Tracking: Added a README.md file to document the development lifecycle 
and provide clear version iteration notes.




Roadmap & Future Improvements
Core Features: Implement the core logic for borrowing and returning books.

Tracking System: Generate detailed borrowing lists accessible to both users and administrators.

Penalty System (Blacklist): 
Develop a "Blacklist" feature to temporarily suspend borrowing privileges 
for users with serious violations or overdue returns.

Data Analytics: Create a Borrowing Leaderboard based 
on user activity and book popularity.

Visualization: Integrate matplotlib to generate dynamic borrowing trend charts.

Frontend Upgrade: Transition to a sleek, modern GUI using Streamlit for a more intuitive user experience.

Scalability: Migrate from SQLite3 to MySQL to handle higher concurrency and larger datasets.

AI Integration: Implement LLM-powered features, allowing users to interact with the system via an AI assistant.



Author's Note
I am currently a university student, 
so development moves at a "student pace"—mostly during afternoons and weekends. 
This project is a work in progress, and I am constantly striving to improve the code quality.

I welcome any constructive feedback or suggestions; 
please feel free to reach out via Gmail. 
In the spirit of modern development, 
I have utilized AI tools like GPT and Claude to assist with code refactoring and architecture optimization. 
Thank you for following my journey!
