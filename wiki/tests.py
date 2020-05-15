from django.test import TestCase

# Create your tests here.
def test_detail_page(self):
        """ Tests the slug generated when saving a Page. """
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
        