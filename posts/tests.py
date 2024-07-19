from django.test import TestCase

from . models import Post

from django.contrib.auth import get_user_model

# Create your tests here.

class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # creates a test user
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret',
        ) 
        
        # creates a test post
        cls.post = Post.objects.create(
            author=cls.user,
            title = 'django',
            body='learning django',
        )  
        
    def test_post_model(self):
        '''Checks that the Post model's fields are set correctly'''
        self.assertEqual(self.post.author.username,"testuser") 
        self.assertEqual(self.post.title,'django')
        self.assertEqual(self.post.body,"learning django")
        self.assertEqual(str(self.post),'django')
