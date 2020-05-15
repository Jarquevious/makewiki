from django.test import TestCase

# Create your tests here.
def test_detail_page(self):
        """ Tests the slug generated when saving a Page. """
        user = User.objects.create()
        user.save()