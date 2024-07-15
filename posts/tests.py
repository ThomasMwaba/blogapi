from django.test import TestCase

from . models import Post

from django.contrib.auth import get_user_model

# Create your tests here.

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret',
        )
        
        cls.post = Post.objects.create(
            author=cls.user,
            title = 'django',
            body='learning django',
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(self.post.title,'django')
        self.assertEqual(self.post.body,"learning django")
        self.assertEqual(str(self.post),'django')
