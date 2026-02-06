import sqlalchemy as sa
import sqlalchemy.orm as so

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

    def get_user_name(self, user_id: int|None = None) -> 'str':
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

            if post is None:
                return None
        #TODO because this won't find posts actually there for some reason lowkey idk why but i intend to fix it and maybe could have actually fixed it in the time it took to write this but i didn't :(( anyway, yolo
        return post


if __name__ == '__main__':
    controller = Controller()
    controller.set_current_user_from_name('Alice')