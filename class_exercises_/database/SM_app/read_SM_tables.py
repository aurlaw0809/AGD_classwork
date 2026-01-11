import sqlite3

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

select_users = """SELECT * FROM users;"""
with sqlite3.connect("SM_app.db") as conn:
    users = execute_read_query(conn, select_users)

for user in users:
    print(user)

print()

select_posts = """SELECT * FROM posts;"""
with sqlite3.connect("SM_app.db") as conn:
    posts = execute_read_query(conn, select_posts)

for post in posts:
    print(post)

print()

select_user_posts = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts INNER JOIN users ON users.id = posts.user_id;
"""

with sqlite3.connect("SM_app.db") as conn:
    users_posts = execute_read_query(conn, select_user_posts)

for user_post in users_posts:
    print(user_post)

print()

select_posts_comments_users = """
SELECT
    posts.description as post,
    comments.text as comment,
    users.name
FROM
    posts INNER JOIN comments ON posts.id = comments.post_id INNER JOIN users on users.id = comments.user_id;
"""
with sqlite3.connect("SM_app.db") as conn:
    posts_comments_users = execute_read_query(conn, select_posts_comments_users)

for posts_comments_user in posts_comments_users:
    print(posts_comments_user)

print()

conn = sqlite3.connect('SM_app.db')
cursor = conn.cursor()
cursor.execute(select_posts_comments_users)
cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)