from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page


# Create your tests here.
def test_detail_page(self):
    """ Test to see if slug generated when saving a Page."""

    # Create a user and save to the database
    user = User.objects.create()
    user.save()
    
    # Create a page and save to the database
    page = Page(title="My Detail Test Page", content="details_test", author=user)
    page.save()
    
    # Slug is generated matches with what we expect
    slug = page.slug
    response = self.client.get(f'/{slug}/')

    self.assertEqual(response.status_code, 200)
    
    info = self.client.get('/')
    self.assertContains(info, 'makewiki', html=True)
    

def test_edit_page(self):
    """Test edit page."""

    # Test data that will be displayed on the screen
    user = User.objects.create()
    user.save()

    page = Page.objects.create(title="My Test Page", content="edit_test", author=user)
    page.save()

    # Make a GET request to the MakeWiki homepage that will get a response back
    post_data = {
    'title': 'Who', 
    'content': 'Are you?', 
    'author': user.id, 
    }

    response = self.client.post('/form/', data=post_data)

    # Check if response is 200
    self.assertEqual(response.status_code, 200)

    # Check the number of pages passed to the template matches the number of pages in the database
    end = self.client.get('/')
    result = end.context['pages']

    self.assertQuerysetEqual(result, ['<Page: My Test Page>', '<Page: Test>'], ordered=False)

def test_page_creation(self):

    # Create user object and save it
    user = User.objects.create()
    user.save()

    # Create a page 
    page = Page.objects.create(title="The Test Page", content="edit_test", author=user)
    page.save()

    post_data = {
    'title': 'COVID19', 
    'content': 'Mass Testing is Underway', 
    'author': user.id 
    }

    response = self.client.post('/form/', data = post_data)

    self.assertEqual(response.status_code, 302)

    page_object = Page.objects.get(title='COVID19')

    self.assertEqual(page_object.content, 'Mass Testing is Underway')