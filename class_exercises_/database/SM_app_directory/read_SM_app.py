import sqlite3
conn = sqlite3.connect("SM_app.db")
cursor = conn.cursor()

select_posts = """
SELECT title, description
FROM posts
"""

select_text = """
SELECT text
FROM comments
WHERE text LIKE '%?';
"""

update_users = """
UPDATE users
SET name = 'Lizzy'
WHERE name = 'Elizabeth'
"""

show_user_posts = """
SELECT users.name, count(posts.id)
FROM users inner join posts on users.id = posts.user_id
GROUP BY posts.id;
"""

show_user_comments = """
SELECT users.name, GROUP_CONCAT(comments.text)
FROM users
LEFT JOIN comments on users.id = comments.user_id
GROUP BY users.id;
"""


posts = cursor.execute(select_posts).fetchall()
text = cursor.execute(select_text).fetchall()
update_users = cursor.execute(update_users).fetchall()
user_post_count = cursor.execute(show_user_posts).fetchall()
user_comments = cursor.execute(show_user_comments).fetchall()


print(posts)
print(text)
print(user_post_count)
print(user_comments)

conn.close()
