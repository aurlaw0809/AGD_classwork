import pyinputplus as pyip

from controller_student import Controller


class CLI:
    def __init__(self):
        self.controller = Controller()
        self.current_menu = self.login
        self.running = True
        self.run_menus()

    @staticmethod
    def show_title(title):
        print('\n' + title)
        print('-' * len(title) + '\n')

    def run_menus(self):
        while self.running:
            self.current_menu = self.current_menu()

    def exit_menus(self):
        self.running = False
        print("Goodbye")

    def login(self):
        self.show_title('Login Screen')
        users = self.controller.get_user_names()
        menu_items = ['Login',
                      'Create a new account',
                      'Exit',
                       ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Select user or create a new account\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'create a new account':
            next_menu = self.create_account
        elif menu_choice.lower() == 'exit':
            next_menu = self.exit_menus
        else:
            user_name = input('Enter your name: ')
            if user_name in users:
                self.controller.set_current_user_from_name(user_name)
                next_menu = self.user_home
            else:
                print(f'Name: "{user_name.title()}" not recognised')
                next_menu = self.login
        return next_menu

    def create_account(self):
        self.show_title('Create Account')

        user_name = input('Enter username: ')
        age = int(input('Enter age: '))
        gender = input('Enter gender: ')
        nationality = input('Enter nationality: ')

        self.controller.create_account(user_name, age, gender, nationality)
        self.controller.set_current_user_from_name(user_name)
        next_menu = self.user_home

        return next_menu

    def user_home(self):
        user_name = self.controller.get_user_name()
        self.show_title(f'User Home - {user_name.title()}')
        menu_items = ['Log out',
                      'Search',
                      'View posts',
                      'My account',
                      'New',
                      ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Select a menu\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'log out':
            next_menu = self.login
        elif menu_choice.lower() == 'search':
            next_menu = self.search
        elif menu_choice.lower() == 'view posts':
            next_menu = self.view_posts
        elif menu_choice.lower() == 'my account':
            next_menu = self.my_account
        elif menu_choice.lower() == 'new':
            next_menu = self.new
        else:
            next_menu = self.login
        return next_menu

    def search(self):
        self.show_title(f'Search')
        menu_items = ['Posts',
                      'Users',
                      'Comments',
                      'Exit',
                      ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Select what you want to search\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'posts':
            next_menu = self.search_posts
        elif menu_choice.lower() == 'users':
            next_menu = self.search_users
        elif menu_choice.lower() == 'comments':
            next_menu = self.search_comments
        else:
            next_menu = self.user_home
        return next_menu

    def search_posts(self):
        self.show_title(f'Search Posts')
        menu_items = ['Title',
                      'Description',
                      'Exit',
                      ]
        menu_choice = pyip.inputMenu(menu_items,
                                     prompt='Search by..\n',
                                     numbered=True,
                                     )
        if menu_choice.lower() == 'title':
            next_menu = self.search_posts_by_title
        elif menu_choice.lower() == 'description':
            next_menu = self.search_posts_by_desc
        else:
            next_menu = self.search
        return next_menu

    def search_posts_by_title(self):
        self.show_title(f'Search Posts by Title')

        title = input('Enter title: ')
        post = self.controller.search_posts_by_title(title)
        print(post)
        if post is None:
            print('No such post')
            next_menu = self.search_posts
        else:
            self.view_post(post)
        return self.search_posts()

    def search_posts_by_desc(self):
        self.show_title(f'Search Posts by Description')
        return self.search_posts()

    def search_users(self):
        return self.search()

    def search_comments(self):
        return self.search()

    def view_posts(self):
        return self.user_home()

    def my_account(self):
        return self.user_home()

    def new(self):
        return self.user_home()

    def view_post(self, post):
        print('youd view a post here if id done it already')
        pass


if __name__ == '__main__':
    cli = CLI()
# controller = Controller()