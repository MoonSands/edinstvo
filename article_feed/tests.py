from django.test import TestCase
from .models import *

class reportsGroupModelTest(TestCase):
    
    def test_str_representation(self):
        group = reportsGroup.objects.create(name='TestGroup', slug='testgroup')
        expected_object_name = '%s' % (group.name)
        self.assertEqual(expected_object_name,str(group))
    
    

class reportsModelTest(TestCase):
    
    def test_str_representation(self):
        report = reports.objects.create(name='TestReport')
        expected_object_name = '%s' % (report.name)
        self.assertEqual(expected_object_name,str(report))

class faqModelTest(TestCase):
    
    def test_str_representation(self):
        QA = faq.objects.create(question='HUH?', answer='sheesh')
        expected_object_name = '%s' % (QA.question)
        self.assertEqual(expected_object_name,str(QA))

class productsModelTest(TestCase):
    
    def test_str_representation(self):
        product = products.objects.create(name='TestProduct', price='300')
        expected_object_name = '%s' % (product.name)
        self.assertEqual(expected_object_name,str(product))

class dataFromFormsModelTest(TestCase):
    
    def test_str_representation(self):
        formdata = dataFromForms.objects.create(name='Bob', phone = 89612992003, email = "bob@email.com", message = 'hi')
        expected_object_name = f'{formdata.email}'
        self.assertEqual(expected_object_name,str(formdata))

class postsModelTest(TestCase):
    
    def test_str_representation(self):
        post_ex = post.objects.create(title = 'TestPost', content = {})
        expected_object_name = '%s' % (post_ex.title)
        self.assertEqual(expected_object_name,str(post_ex))

#class postCategoryModelTest(TestCase):
    
#    def test_str_representation(self):
#        cat = postCategory.objects.create(name='TestCat', slug='testcat')
#        expected_object_name = '%s' % (cat.name)
#        self.assertEqual(expected_object_name,str(cat))

class docsModelTest(TestCase):
    
    def test_str_representation(self):
        doc = docs.objects.create(name='TestDoc')
        expected_object_name = '%s' % (doc.name)
        self.assertEqual(expected_object_name,str(doc))


