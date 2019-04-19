from faker import Faker
from app import db
from app.models import User, Post

fake = Faker()

#delete 
for user in User.query.all():
    db.session.delete(user)

for post in Post.query.all():
    db.session.delete(post)

u = User(username='fakeuser', email='fakeuser@gmail.com')
u.set_password('fakepassword')
db.session.add(u)

for _ in range(10):
    username = fake.user_name()
    email = fake.email()
    u = User(username=username, email=email)
    u.set_password('fakepassword')
    for _ in range(10):
        p = Post(body=fake.text()[:140], author=u)
        db.session.add(p)
    db.session.add(u)
db.session.commit()
