import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

import django
# Import settings
django.setup()

from blog.models import Post
from django.contrib.auth.models import User

# user = User.objects.first()
# pust_pub = Post(title="blog post 3", content="This is my third blog post", author_id=user.id)
# pust_pub.save()
# all_posts = Post.objects.all()
# for i in all_posts:
#     print(i.author.pk)
