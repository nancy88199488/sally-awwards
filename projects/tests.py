from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile,Projects,Review


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='salome', password='mnbvcxzzlkjhgfdsa')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class ProjectsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='salome')
        self.new_post =Projects.objects.create(id=1, title='test post',projectscreenshot = 'test.jpg', description='desc',
                                        user=self.user, projecturl='http://test.com',datecreated='jul,07,2021')

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Projects))

    def test_save_post(self):
        self.post.save_post()
        post =Projects.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts =Projects.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post =Projects.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post =Projects.search_project('test')
        self.assertTrue(len(post) < 1)


class ReviewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='salome')
        self.new_post =Projects.objects.create(id=1, title='test post', projectscreenshot = 'test.jpg', description='desc',
                                        user=self.user, projecturl='http://test.com')
        self.rate = Review.objects.create(id=1, design=6, usability=7, content=9, user=self.user, new_post=self.new_post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Review))

    def test_save_rate(self):
        self.rate.test_save_rate()
        rate = Review.objects.all()
        self.assertTrue(len(rate) > 0)

    def test_get_post_rate(self, id):
        self.rate.save()
        rate = Review.get_rate(post_id=id)
        self.assertTrue(len(rate) == 1) 