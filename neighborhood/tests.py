from django.test import TestCase
from .models import Profile, NeighbourHood, Business, Post
from django.contrib.auth.models import User


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Vickie', password='787898')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Vickie')
        self.post = Post.objects.create(id=1, title='test post', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='desc',
                                        user=self.user, url='http://ur.coml')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)


    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)


class ProfileTestClass(TestCase):
    """
    Test profile class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1,username='a')
        self.hood = Neighbourhood(name='hood', location='muchas', user=self.user)
        self.hood.save_hood()
        self.profile = Profile(user=self.user, hood = self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.pro, Profile))


    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.pro.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        """
        Function to test that a profile can be deleted
        """
        self.profile.save_profile()
        self.profile.del_profile()


class BusinessTestClass(TestCase):
    """
    Test business class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbour(name='hood', location='muchas', user=self.user)
        self.hood.save_hood()
        self.business = Business(name="kansas", email="shaggy@gmail.com", user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_search_business(self):
        self.business.save()
        business = business.search_project('test')
        self.assertTrue(len(business) > 0)
    
    def test_save_method(self):
        """
        Function to test that neighbourhood is being saved
        """
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.business.save_business()
        self.business.delete_business()

    def test_update_method(self):
        """
        Function to test that a neighbourhood's details can be updated
        """
        self.business.save_business()
        new_business = Business.objects.filter(name='kansas').update(name='kansas')
        business = Business.objects.get(name='kansas')
        self.assertTrue(business.name, 'kansas')




class PostsTestClass(TestCase):
    """
    Test posts class and its functions
    """
    def setUp(self):
        self.user = User.objects.create(id =1, username='a')
        self.hood = Neighbour(name='talanta', location='mtaani', user=self.user)
        self.hood.save_hood()
        self.post = Posts(body="rolling", user=self.user, hood=self.hood)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))

    
    def test_save_method(self):
        """
        Function to test that a post is being saved
        """
        self.post.save_posts()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        """
        Function to test that a neighbourhood can be deleted
        """
        self.post.save_posts()
        self.post.del_posts()

    def test_update_method(self):
        """
        Function to test that a post's details can be updated
        """
        self.post.save_posts()
        new_posts = Posts.objects.filter(body='bizna').update(body='biznas')
        bizes = Posts.objects.get(body='biznas')
        self.assertTrue(bizes.body, 'biznas')

        
 


