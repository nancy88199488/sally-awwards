from django.test import TestCase
from .models import Profile,MyProjects,Rating
from django.contrib.auth.models import User

class ProfileTest(TestCase):
    def setUp(self):
        self.user= User(username = 'salome',password = 'mnbvcxzasdfghjkl')
        self.user = Profile(user = self.user,user = 1,Bio = 'tests',image = 'test.jpg',date_craeted='jan,28.202')

    def test_instance(self):
        self.assertTrue(isinstance(self.user,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.user.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

class MyProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = MyProjects(title = 'testT',image = 'test.jpg',description = 'testD',user ='salome', projecturl = 'https://test.com',datecreated='Dec,01.202')


    def test_save_project(self):
        self.new_post.save_project()
        images = MyProjects.objects.all()
        self.assertEqual(len(images),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        images = MyProjects.objects.all()
        self.assertEqual(len(images),1)    

class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='salome')
        self.myProjects = MyProjects.objects.create(id=1, title='test myProjects', image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, url='http://ur.coml')
        self.rating = Rating.objects.create(id=1, design=6, usability=7, content=9, user=self.user, myProjects=self.myProjects)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)        