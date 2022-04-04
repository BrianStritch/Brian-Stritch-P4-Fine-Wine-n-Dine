from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from reviews.models import Review, Comment
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

class TestCommentModel(TestCase):  

    @classmethod
    def setUpTestData(cls):
        user = User(
                id=1,
                email='test@test.com',
                username='test_username',
                password='testpassword',
                first_name='test_first',
                last_name='test_last'
            )
        user.save()
        review = Review(
            id=100,
            title = 'test_review_for_all_tests',
            author = user,           
            content = 'test_content',
        )
        review.save()
        comment = Comment(
            post = review,
            name = 'test_comment_name_for_all_tests',
            body = 'test_comment_body',
        )
        comment.save()
    
    def test_Create_Review(self):
        user = User.objects.get(email='test@test.com')
        review = Review(
            title = 'test_review',
            author = user,           
            content = 'test_content',
        )
        review.save()        
        self.assertTrue(review.save)

    def test_test_create_comment(self):
        user = User.objects.get(email='test@test.com')
        review = Review.objects.get(title='test_review_for_all_tests')
        comment = Comment(
            post = review,
            name = 'test_comment_name',
            body = 'test_comment_body',
        )
        comment.save()
        self.assertTrue(comment.save)

    def test_comment_model_string(self):
        user = User.objects.get(email='test@test.com')
        review = Review.objects.get(title='test_review_for_all_tests')
        comment = Comment.objects.get(name='test_comment_name_for_all_tests')
        
        self.assertEqual(
            str(f"Comment {comment.body} by {comment.name}"), 
            'Comment test_comment_body by test_comment_name_for_all_tests'
            )

    def test_Edit_review(self):
        review = Review.objects.get(title='test_review_for_all_tests')
        review.title = 'new_title'
        review.save()
        review = Review.objects.get(title='new_title')
        self.assertEqual(review.title, 'new_title')    
    
    def test_Edit_comment(self):
        comment = Comment.objects.get(name='test_comment_name_for_all_tests')
        comment.name = 'new_name'
        comment.save()
        comment = Comment.objects.get(name='new_name')
        self.assertEqual(comment.name, 'new_name')

    def test_Delete_review(self):
        review = Review.objects.get(title='test_review_for_all_tests')        
        self.assertTrue(review.delete())    
    
    def test_delete_comment(self):
        comment = Comment.objects.get(name='test_comment_name_for_all_tests')        
        self.assertTrue(comment.delete())

    def test_create_review_page(self):
            url = reverse('create_review')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'reviews/create_review.html')
            self.assertContains(response, 'reviews')

    def test_Edit_review_page_result(self):
        review = Review.objects.get(title='test_review_for_all_tests')
        review.title = 'new_title'
        review.save()
        review = Review.objects.get(title='new_title')
        self.assertEqual(review.title, 'new_title')
        response = self.client.post(
            reverse('edit_review', kwargs={'pk': review.id}), 
            {'title': 'test_new_review_title'})
        self.assertEqual(response.status_code, 200)


    def test_delete_review_page_result(self):
        review = Review.objects.get(id=100)        
        self.assertTrue(review)
        review.delete()
        self.assertTrue(review.delete)
        response = self.client.post(
            reverse('edit_review', kwargs={'pk': 100}), 
            {'title': 'test_new_review_title'})
        self.assertNotEqual(response.status_code, 200)
