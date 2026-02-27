import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped
import pyinputplus as pyip
import random

from class_exercises_.database.SM_app_sqlalchemy.models import User, Post, Comment


class Controller:
    def __init__(self, db_location = 'sqlite:///social_media.db'):
        self.current_user_id: int|None = None
        self.viewing_post_user_id: int|None = None
        self.engine = sa.create_engine(db_location)

    def set_current_user_from_name(self, name:str) -> User|None:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()

            if user is None:
                # Fallback behaviour: clear current user and return None
                self.current_user_id = None
                return None

            self.current_user_id = user.id
        return user

    def get_user_name(self, user_id: int|None = None) -> Mapped[str]:
        if user_id is None:
            user_id = self.current_user_id
        with so.Session(bind=self.engine) as session:
            name = session.get(User, user_id).name
        return name

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(User.name).order_by(User.name)).all()
        return list(user_names)

    def create_account(self, username, age, gender, nationality):
        with so.Session(bind=self.engine) as session:
            new_user = User(name=username, age=age, gender=gender, nationality=nationality)
            session.add(new_user)
            session.commit()

    def search_posts_by_title(self, title:str) -> Post:
        with so.Session(bind=self.engine) as session:
            post = session.scalars(sa.select(Post).where(Post.title == title)).one_or_none()
        return post

    def search_posts_by_description(self, desc: str) -> Post:
        with so.Session(bind=self.engine) as session:
            post = session.scalars(sa.select(Post).where(Post.description == desc)).one_or_none()
        return post

    def search_users(self, username: str) -> User:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == username)).one_or_none()
        return user

    def search_comments(self, comment):
        with so.Session(bind=self.engine) as session:
            the_comment = session.scalars(sa.select(Comment).where(Comment.comment == comment)).one_or_none()
        return the_comment

    def find_comments(self, post_id):
        with so.Session(bind=self.engine) as session:
            comments = session.scalars(sa.select(Comment).where(Comment.post_id == post_id)).all()
            for thing in comments:
                print(f'{thing.comment} - {self.get_user_name(thing.user_id)}')

    def find_no_likes(self, post_id: int) -> int:
        with so.Session(bind=self.engine) as session:
            post = session.scalars(sa.select(Post).where(Post.id == post_id)).one_or_none()
            return post.number_of_likes()

    def find_no_user_posts(self, user_id: int) -> int:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.id == user_id)).one_or_none()
            return user.number_of_posts()

    def find_no_user_comments(self, user_id: int) -> int:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.id == user_id)).one_or_none()
            return user.number_of_comments()

    def find_no_user_liked_posts(self, user_id: int) -> int:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.id == user_id)).one_or_none()
            return user.number_of_posts_liked()

    def get_post_name(self, post_id):
        with so.Session(bind=self.engine) as session:
            post = session.scalars(sa.select(Post).where(Post.id == post_id)).one_or_none()
            return post.title

    def find_newest_post(self):
        with so.Session(bind=self.engine) as session:
            max = len(session.scalars(sa.select(Post).order_by(Post.title)).all())
            post = session.scalars(sa.select(Post).where(Post.id == max)).one_or_none()
            return post

    def find_random_post(self):
        with so.Session(bind=self.engine) as session:
            max = len(session.scalars(sa.select(Post).order_by(Post.title)).all())
            num = random.randint(1, max)
            post = session.scalars(sa.select(Post).where(Post.id == num)).one_or_none()
            return post

    def view_post(self, post):
        print(f'View post - {post.title}')
        print(f'Author: {self.get_user_name(post.user_id)}')
        print(f'Likes: {self.find_no_likes(post.id)}')
        print(f'Description: {post.description}')
        print('Comments:')
        print(f'{self.find_comments(post.id)}')

    def view_comment(self, comment):
        print(f'View comment')
        print(f'{comment.comment}')
        print(f'Author: {self.get_user_name(comment.user_id)}')
        print(f'Post: {self.get_post_name(comment.post_id)}')

    def view_user(self, user):
        print(f'View user - {user.name}')
        print(f'Age: {user.age}')
        print(f'Gender: {user.gender}')
        print(f'Nationality: {user.nationality}')
        print(f'NO. posts: {self.find_no_user_posts(user.id)}')
        print(f'NO. comments: {self.find_no_user_comments(user.id)}')
        print(f'NO. likes made: {self.find_no_user_liked_posts(user.id)}')

#TODO view user
if __name__ == '__main__':
    controller = Controller()
    controller.set_current_user_from_name('Alice')