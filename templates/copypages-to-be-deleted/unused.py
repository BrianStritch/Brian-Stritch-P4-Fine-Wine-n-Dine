

# class Test_home_page_url(TestCase):

#     def test_********_page_url(self):
#         """Test the url for "home"
#         """

#         response = self.client.get('' + str(self.userName))
#         self.assertEqual(response.status_code, 200)
    

# class Test_home_page_url(TestCase):

#     def test_*******_page_url(self):
#         """Test the url for "home"
#         """

#         response = self.client.get('' + str(self.userName))
#         self.assertEqual(response.status_code, 200)


# class Test_home_page_url(TestCase):

#     def test_********_page_url(self):
#         """Test the url for "home"
#         """

#         response = self.client.get('' + str(self.userName))
#         self.assertEqual(response.status_code, 200)
    

# class Test_home_page_url(TestCase):

#     def test_*******_page_url(self):
#         """Test the url for "home"
#         """

#         response = self.client.get('' + str(self.userName))
#         self.assertEqual(response.status_code, 200)


# class Test_home_page_url(TestCase):

#     def test_********_page_url(self):
#         """Test the url for "home"
#         """

#         response = self.client.get('' + str(self.userName))
#         self.assertEqual(response.status_code, 200)

# 2
# class TestHomePageViews(TestCase):
#     """
#     A class for testing home views
#     """
#     def test_get_home_page(self):
#         """
#         This test checks that the index page
#         is displayed
#         """
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'index.html', 'base.html')

# # 3
# class TestOpeningHoursView(TestCase):
#     """
#     A class for testing opening hours page views
#     """
#     def test_get_openingHours_page(self):
#         """
#         This test checks that the opening hours page
#         is displayed
#         """
#         response = self.client.get('/opening_hours/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/opening-times.html', 'base.html')

# # 4
# class TestMenuViews(TestCase):
#     """
#     A class for testing menu views
#     """
#     def test_get_menu_page(self):
#         """
#         This test checks that the menu page
#         is displayed
#         """
#         response = self.client.get('/menu/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/menu.html', 'base.html')




# # 5
# class TestUserprofileViews(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         User.objects.create_user(
#             id=1,
#             email='test@test.com',
#             username='test_username',
#             password='testpassword',
#             first_name='test_first',
#             last_name='test_last'
#         )

#     """
#     A class for testing user profile views
#     """
#     def test_get_profile_page(self):
#         """
#         This test checks that the profile page
#         is displayed
#         ****************************************************************************************************************
#         THis test workss just needs a user to be logged in 
#         """
                
#         self.client.login(username='test_username', password='testpassword')
#         user = User.objects.get(id=1)
#         response = self.client.get('/profile/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/profile.html', 'base.html')

# # 6
# class TestSignUpView(TestCase):
#     """
#     A class for testing sign up page views
#     """
#     def test_sign_up_page(self):
#         """
#         This test checks that the sign up page
#         is displayed correctly
#         """
#         response = self.client.get('/sign_up_now/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/sign_up.html', 'base.html')

# # 7
# class Test_test_test(TestCase):

#     def test_done_defaults_to_True(self):
#             user = User()
#             user.email='testUser@test.com',
#             user.username='testuser',
#             user.password='testpassword',
#             user.first_name='test_first',
#             user.last_name='test_last'
            
#             user.save()
#             self.assertTrue(user.save)




























# class Test------------View(TestCase):
#     """
#     A class for testing ----------- page views
#     """
#     def test_get_---------------_page(self):
#         """
#         This test checks that the ---------------- page
#         is displayed
#         """
#         response = self.client.get('/------------/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/------------.html', 'base.html')
# class Test------------View(TestCase):
#     """
#     A class for testing ----------- page views
#     """
#     def test_get_---------------_page(self):
#         """
#         This test checks that the ---------------- page
#         is displayed
#         """
#         response = self.client.get('/------------/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/------------.html', 'base.html')


# class Test------------View(TestCase):
#     """
#     A class for testing ----------- page views
#     """
#     def test_get_---------------_page(self):
#         """
#         This test checks that the ---------------- page
#         is displayed
#         """
#         response = self.client.get('/------------/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/------------.html', 'base.html')


# class TestEditProfileView(TestCase):
#     """
#     A class for testing edit_profile page views
#     """
#     def test_get_edit_profile_page(self):
#         """
#         This test checks that the edit_profile page
#         is displayed
#         """
#         response = self.client.get('/edit_profile/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/edit_profile.html', 'base.html')






   

   
    # path(
    #     'about/',
    #     views.About.as_view(),
    #     name='about'
    #     ),
    
  
    # path(
    #     'nannys_alternative/edit_profile/',
    #     views.Edit_profile.as_view(),
    #     name='edit_profile'
    #     ),
    # path(
    #     'nannys_alternative/delete_profile/<int:pk>/',
    #     views.DeleteProfile.as_view(),
    #     name='delete_profile'
    #     ),




    
        # review = Review.objects.get(title='test_new_review_title')
        # self.assertEqual(review.title, 'test_new_review_title')




    # def test_update_book(self):
    #     book = Book.objects.create(title='The Catcher in the Rye')

        

    #     self.assertEqual(response.status_code, 302)

    #     book.refresh_from_db()
    #     self.assertEqual(book.author, 'J.D. Salinger')


    












    # def test_Edit_comment(self):
    #     comment = Comment.objects.get(name='test_comment_name_for_all_tests')
    #     comment.name = 'new_name'
    #     comment.save()
    #     comment = Comment.objects.get(name='new_name')
    #     self.assertEqual(comment.name, 'new_name')
    #     response = self.client.post(
    #         reverse('reviews_detail', kwargs={'pk': comment.id}), 
    #         {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'})
        
        
    # def test_update_book(self):
    #     book = Book.objects.create(title='The Catcher in the Rye')

    #     response = self.client.post(
    #         reverse('book-update', kwargs={'pk': book.id}), 
    #         {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'})

    #     self.assertEqual(response.status_code, 302)

    #     book.refresh_from_db()
    #     self.assertEqual(book.author, 'J.D. Salinger')







        ################################################################################################################
    # def test_front_end(self):        
    #     user = User.objects.get(email='test@test.com')
    #     self.client.login(username='test_username', password='testpassword')
    #     review = Review.objects.get(title='test_review_for_all_tests')        
    #     args = {'review': review}
    #     page = self.client.get('/reviews/reviews/')
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTrue(user.is_authenticated)
    #     self.assertTemplateUsed(page, 'reviews/reviews.html')





   



#     def test_get_edit_product_page(self):        
#         self.client.login(username='testname', password='testpass')
#         user_edit = EditProfileForm()               
#         user_edit.email= 'test@test.ie',
#         user_edit.first_name= 'test_first_name',
#         user_edit.last_name= 'test_last_name',
#         user_edit.password1= 'testpass',
#         user_edit.password2= 'testpass',
            
#         user_edit.save()
#         test_edit_form = EditProfileForm(instance=user_edit)
#         args = {'user_edit': user_edit, 'test_edit_form': test_edit_form}
#         page = self.client.get('/edit_profile/1/', args)
#         self.assertEqual(page.status_code, 200)
#         self.assertTemplateUsed(page, 'nannys_alterantive/edit_pofile.html')
# # # 2
# class Test_user_details_edit_form(TestCase):

#     def test_edit_user_register_form(self):
#         user = User(
#             'username': 'testname',
#             'email': 'test@test.ie',
#             'first_name': 'test_first_name',
#             'last_name': 'test_last_name',
#             'password1': 'testpass',
#             'password2': 'testpass',
#         )
#         user.save()

#         user_form = UserAccountDetailsForm({
#                 'username': 'newtestname',
#                 'email': 'newtest@test.ie',
#                 'first_name': 'new_test_first_name',
#                 'last_name': 'new_test_last_name',
#                 'password1': 'new_testpass',
#                 'password2': 'new_testpass',
#             })
#         user_form.save()
#         user = User.objects.get(username='testname')
#         self.client.login(username='testname', password='testpass')
#         self.assertTrue(user_form.save())
#         self.assertTrue(user.is_authenticated)
#         self.assertTrue(user_form.is_valid)
#         self.assertEquals(user.username, 'testname')
#         self.assertEquals(user.email, 'test@test.ie')
#         self.assertEquals(user.username, 'test_first_name')

    

# # 2
# class TestSaveUser3(TestCase):

#     def test_done_defaults_to_True(self):
#         user = User(
#             email='testUser@test.com',
#             username='testuser',
#             password='testpassword',
#             first_name='test_first',
#             last_name='test_last'
#         )
#         user.save()
#         self.assertTrue(user.save)
        
        
        
# # 3
# class TestSaveUser3(TestCase):    

#     def test_done_defaults_to_True(self):
#         user = User()
#         user.email='testUser@test.com'
#         user.username='testuser'
#         user.password='testpassword'
#         user.first_name='test_first'
#         user.last_name='test_last'
    
#     user.save()
#     self.assertTrue(user.save)



# form.save()

        #user = User.objects.get(username='testname')
        #####self.assertEquals(user.username, 'testuser')


        #self.assertTrue(new_user_data.save())
        #self.assertTrue(user.is_authenticated)
        #self.assertTrue(user_form.is_valid)



        # self.assertEquals(user.username, 'testuser')
        # self.assertEquals(user.email, 'testUser@test.com')
        # self.assertEquals(user.first_name, 'test_first')
        # self.assertEquals(user.last_name, 'test_last')




  # # 4

    # def test_get_menu_page(self):
    #     """
    #     This test checks that the menu page
    #     is displayed
    #     """        
    #     user = User.objects.get(id=1)
    #     self.client.login(username='test_username', password='testpassword') 
    #     response = self.client.get('/menu/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'nannys_alternative/menu.html', 'base.html')

    # 5


# # 7
# class Test_test_test(TestCase):

#     def test_done_defaults_to_True(self):
#             user = User()
#             user.email='testUser@test.com',
#             user.username='testuser',
#             user.password='testpassword',
#             user.first_name='test_first',
#             user.last_name='test_last'
            
#             user.save()
#             self.assertTrue(user.save)





    # def test_sign_up_page(self):
    #     """
    #     This test checks that the sign up page
    #     is displayed correctly
    #     """        
    #     user = User.objects.get(id=1)
    #     self.client.login(username='test_username', password='testpassword') 
    #     response = self.client.get('/sign_up_now/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'nannys_alternative/sign_up.html', 'base.html')

    # def test_done_defaults_to_True(self):
    #         user = User()
    #         user.email='testUser@test.com',
    #         user.username='testuser',
    #         user.password='testpassword',
    #         user.first_name='test_first',
    #         user.last_name='test_last'
            
    #         user.save()
    #         self.assertTrue(user.save)








    ################################################################################################################
    # def test_front_end(self):        
    #     user = User.objects.get(email='test@test.com')
    #     self.client.login(username='test_username', password='testpassword')
    #     review = Review.objects.get(title='test_review_for_all_tests')        
    #     args = {'review': review}
    #     page = self.client.get('/reviews/reviews/')
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTrue(user.is_authenticated)
    #     self.assertTemplateUsed(page, 'reviews/reviews.html')

    # review = Review.objects.get(title='test_new_review_title')
    # self.assertEqual(review.title, 'test_new_review_title')




    # def test_update_book(self):
    #     book = Book.objects.create(title='The Catcher in the Rye')

        

    #     self.assertEqual(response.status_code, 302)

    #     book.refresh_from_db()
    #     self.assertEqual(book.author, 'J.D. Salinger')















    # def test_Edit_comment(self):
    #     comment = Comment.objects.get(name='test_comment_name_for_all_tests')
    #     comment.name = 'new_name'
    #     comment.save()
    #     comment = Comment.objects.get(name='new_name')
    #     self.assertEqual(comment.name, 'new_name')
    #     response = self.client.post(
    #         reverse('reviews_detail', kwargs={'pk': comment.id}), 
    #         {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'})
        
        
    # def test_update_book(self):
    #     book = Book.objects.create(title='The Catcher in the Rye')

    #     response = self.client.post(
    #         reverse('book-update', kwargs={'pk': book.id}), 
    #         {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'})

    #     self.assertEqual(response.status_code, 302)

    #     book.refresh_from_db()
    #     self.assertEqual(book.author, 'J.D. Salinger')






    