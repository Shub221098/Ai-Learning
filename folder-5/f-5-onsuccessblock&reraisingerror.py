# Folder 5: Video - 9 : On success block and re-raising errors in python


class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr(self):
        return f"<User {self.name}>"

def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError as e:
        print(f"Key error: {e}")
    else:
        if user.score > 50:
            send_engagement_notificatio(user)

def perform_calculation(metrics):
    result = metrics['clicks'] * 5 + metrics['hits'] * 2
    return result

def send_engagement_notificatio(user):
    print(f'Notification sent to {user.name} with engagement score.')

my_user = User("John", {"clicks": 10, "hits": 5})
email_engaged_user(my_user) # Notification sent to John with engagement score.
