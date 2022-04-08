# Manual Testing Documentation
In this stage, the developer requested several colleagues to follow the steps outlined below for each of the pages and to document any error messages or UX discrepencies so that they could be addressed after this process was complete. 

Testers were requested to also test the "Navigation UX" (outlined below) on each of the pages as they were conducting those tests to ensure that there was no possible issues relating to specific pages. 

## Navigation UX
### Nav Bar
#### Pre-Login 
- Click on the Nanny's Logo and confirm that it redirects to the homepage (index.html)
- Click on the "home" button on the NavBar links and confirm that it redirects to the homepage (index.html)
- Click on the "reviews" button on the NavBar links and confirm that it redirects to the About Us page
- Click on the "menu" button on the NavBar links and confirm that it redirects to the About Us page
- Click on the "gallery" button on the NavBar links and confirm that it redirects to the About Us page
- Click on the "About Us" button on the NavBar links and confirm that it redirects to the About Us page
- Click on the "opening hours" button on the NavBar links and confirm that it redirects to the About Us page
- Click on the "register" button on the NavBar links and confirm that it redirects to the Sign Up page
- Click on the "Log In" button on the NavBar links and confirm that it redirects to the Login page

#### Post-Login
- Click on the "bookings" button on the NavBar links and confirm that it redirects to the bookings page
- Click on the "Log Out" button on the NavBar links and confirm that you are redirected to the homepage and that a message is displayed confirming that you have logged out

### Footer
- Click on the social media and confirm that it redirects to the relevant social platform

#### Post-Login-User
- Click on the "Bookings" button on the navigation links and confirm that it redirects to the Bookings page
- Click on a Booking and confirm that it redirects to the Bookings details page
- Click on the create Booking button in navigation links and confirm that it redirects to the create Bookings page
- Click on the edit Booking button in booking details and confirm that it redirects to the edit Bookings page
- Click on the delete Booking button in booking details and confirm that it redirects to the delete Bookings page
- Click on the create reviews button in navigation links and confirm that it redirects to the create reviews page

- Click on the "reviews" button on the navigation links and confirm that it redirects to the reviews page
- Click on the create reviews button in navigation links and confirm that it redirects to the create reviews page
- Click on reviews and confirm that it redirects to the reviews details page
- Click on the create comment button in reviews detail page and confirm that it posts the comment details to the admin for approval
- Click on the edit reviews button in reviews details and confirm that it redirects to the edit review page
- Click on the delete reviews button in reviews details and confirm that it redirects to the delete review page
- Click on the edit comments button in reviews details and confirm that it redirects to the edit comments page
- Click on the delete comments button in reviews details and confirm that it redirects to the delete comments page
- Click on the "Logged in as : *** username *** " link on the upper nav menu and confirm that it redirects to the user Profile details page


## Accounts App
### Sign Up Page
- Enter "testuser" (which exists in the DB) into the Username field and fill out the rest of the form fields correctly. Click on "Create Account" and confirm that an error message appears stating: "A user with that username already exists"
- Enter a unique username and email address correctly. Enter password into the "Password" field and an incorrect password into "Confirm Password". Click on "Create Account" and confirm that an error message appears stating: "Passwords do not match"
- Leave any field blank and on the "Create Account" button to confirm that an error message prompts the user to fill in the blank field with the following message "Please fill in this field"
- Fill out all details correctly and click on the "Create Account" button. Confirm that the user is redirected to the "Profile" page and a success message appears stating "You have successfully registered"
- Click on the "Sign In" button in the upper navigation menu and confirm that the user is redirected to the "Login" page

### Login Page
- Enter the username you used to test the Sign Up page in the previous test into the username field, as well as an incorrect password into the password field and click the "Log In" button. Confirm that an error message is displayed stating "Your username or password are incorrect"
- Enter an incorrect username into the username field, as well as any password into the password field and click the "Log In" button. Confirm that an error message is displayed stating "Your username or password are incorrect"
- Leave any field blank and on the "Log In" button to confirm that an error message prompts the user to fill in the blank field with the following message "Please fill in this field"
- Enter the username you used to test the Sign Up page in the previous test into the username field, as well as the corresponding correct password into the password field and click the "Log In" button. Confirm that you are redirected to the "home" page and a link appears in the naviagtion menu stating "logged in as : testuser" and includes your correct username (i.e. logged in as : testuser)
- Click on the "Sign Up" link text next to the "Log In" button and confirm that the user is redirected to the "Sign Up" page

### Profile Page
#### Regular Users
- Click on the "Edit Profile" button and confirm that you are redirected to the Edit User page
- Click on the "Delete Profile" button and confirm that you are redirected to the Homepage and that a message is displayed confirming that your account has been deleted

- After having created a booking on the website
    - Confirm that your booking is displaying in the bookings page
    - Click on the booking in the bookings page and confirm that you are redirected to the bookings detail page for that specific booking
    - Click on the "Edit booking" button and confirm that you are redirected to the Edit booking page
    - Click on the "Delete booking" button and confirm that the booking is deleted

- After having created a review on the website
    - Confirm that the "Your Review" is displaying in the reviews page
    - Click on the review in the reviews page and confirm that you are redirected to the reviews detail page for that specific review
    - Click on the "Edit Review" button and confirm that you are redirected to the Edit Review page
    - Click on the "Delete Review" button and confirm that the review is deleted

- After having created a comment on the website
    - Confirm that your comment was submitted for approval when a message is displayed stating that your comment has been submitted for approval.
    - Click on the "Edit comment" button and confirm that you are redirected to the Edit comment page
    - Click on the "Delete comment" button and confirm that the comment is deleted

#### Staff Users
- Log in with the "admin" account and confirm that there are additonal navigation links showing the extra features available to staff 
- Click on the "Admin Bookings" naviagtion link and confirm that you are redirected to the Admin Bookings page
- Click on the "pending Bookings" naviagtion link and confirm that you are redirected to the pending Bookings page
- Click on the "approved Bookings" naviagtion link and confirm that you are redirected to the approved Bookings page
- Click on the "completed Bookings" naviagtion link and confirm that you are redirected to the completed Bookings page
- Click on the "Admin Panel" naviagtion link and confirm that you are redirected to the Django Admin Panel page

### Edit User Page
#### Regular Users
- Fill in all fields correctly , click on "Update" and confirm that you are redirected back to the Profile page confirming that your changes have been saved
- Leave all items blank, click on "Update Account" and confirm that a message is displayed prompting the user that certain fields are required
- Click on the "Back" button and confirm that you are redirected to the Profile page without any changes being saved
### Edit User Page in django admin
#### Staff Users
- Fill out form correctly and then;
    - Confirm that at the end of the edit user form a checkbox is present to make the user either staff or not staff
    - Change the setting to the opposite of the current setting 
    - Click "save" and confirm that you are redirected to the django admin page and a message appears confirming changes have been saved
- Click on the "Back" button and confirm that you are redirected to the django admin page without any changes being saved

## Site_pages App 
### About Page
- Click on the "contact us and about" button and confirm that you are redirected to the contact us and about page

### Menu Page
- Click on the "menu" button and confirm that you are redirected to the menu page which displays the menu

### opening hours Page
- Click on the "opening hours" button and confirm that you are redirected to the opening hours page

### gallery Page
- Click on the "gallery" button and confirm that you are redirected to the gallery page populated with images related to the guests reviews

### Index Page / Homepage
#### Pre-Login 
- Click on the nannys logo or the home link and confirm you are redirected to the home page
- Click on the "Sign Up" button and confirm you are redirected to the Sign Up page
- Click on the "Log In" button and confirm you are redirected to the Log In page
- Click on the "contact us and about" button and confirm that you are redirected to the contact us and about page
- Click on the "menu" button and confirm that you are redirected to the menu page
- Click on the "opening hours" button and confirm that you are redirected to the opening hours page
- Click on the "gallery" button and confirm that you are redirected to the gallery page

#### Post-Login 
- Click on the nannys logo or the home link and confirm you are redirected to the home page
- Click on the "logged in as : *** username ***" link and confirm you are redirected to the profile page
- Click on the "Log out" button and confirm you are redirected to the Log out page
- Click on the "contact us and about" button and confirm that you are redirected to the contact us and about page
- Click on the "menu" button and confirm that you are redirected to the menu page
- Click on the "opening hours" button and confirm that you are redirected to the opening hours page
- Click on the "gallery" button and confirm that you are redirected to the gallery page

## Bookings App 
### Bookings Page
- Click on the "Bookings" button on the navigation links and confirm that it redirects to the Bookings page
- Click on a Booking and confirm that it redirects to the Bookings details page
- Click on the create Booking button in navigation links and confirm that it redirects to the create Bookings page
- Click on the edit Booking button in booking details and confirm that it redirects to the edit Bookings page
- Click on the delete Booking button in booking details and confirm that it redirects to the delete Bookings page
- Click on the create reviews button in navigation links and confirm that it redirects to the create reviews page

- After having created a booking on the website
    - Confirm that your booking is displaying in the bookings page
    - Click on the booking in the bookings page and confirm that you are redirected to the bookings detail page for that specific booking
    - Click on the "Edit booking" button and confirm that you are redirected to the Edit booking page
    - Click on the "Delete booking" button and confirm that the booking is deleted

### Create booking Page
- Fill out the create booking form and submit booking and confirm that it redirects to the bookings page displaying your new booking.
- Submit the create bookings form wihout any data and confirm that it displaying an error message "fields required".
- submit the booking form with a previously created booking details and confirm that a duplication booking cannot be created.

### Booking detail Page
- Click on booking and confirm that it redirects to the bookings details page
- Click on the edit booking button in bookings details and confirm that it redirects to the edit booking page
- Click on the delete booking button in bookings details and confirm that it redirects to the delete booking page

- After having created a booking on the website
    - Confirm that your booking is displaying in the bookings page
    - Click on the booking in the bookings page and confirm that you are redirected to the bookings detail page for that specific booking
    - Click on the "Edit booking" button and confirm that you are redirected to the Edit booking page
    - Click on the "Delete booking" button and confirm that the booking is deleted


### Edit booking Page
- Confirm that the page renders with the booking review form pre-populated with the details of the selected booking.
- Test the form
    - Fill in all fields correctly - Click on the "update" button and confirm that you are redirected to the bookings page and that it displays the updated booking.
    - Fill in all fields correctly with the below exceptions, click on the "update" button and confirm that you are prompted to fill in the missing field
        - Leave the date field blank
        - Leave the number of guests field blank
        - Leave the additional comments field blank
        - Leave the dietary noted field blank

### Delete booking page
- Confirm that the page renders prompting to delete the selected booking, displaying the booking details of the selected booking.
- Confirm that on deleting that you are redirected to the bookings page and your booking has been deleted.

## Reviews App 
### Reviews Page
- Click on the "reviews" button on the navigation links and confirm that it redirects to the reviews page
- Click on the create reviews button in navigation links and confirm that it redirects to the create reviews page

### Create review Page
- Fill out the create reviews form and submit review and confirm that it redirects to the reviews page displaying your new review.
- Submit the create reviews form wihout any data and confirm that it displaying an error message "fields required".

### Reviews detail Page
- Click on reviews and confirm that it redirects to the reviews details page
- Click on the create comment button in reviews detail page and confirm that it posts the comment details to the admin for approval
- Click on the edit reviews button in reviews details and confirm that it redirects to the edit review page
- Click on the delete reviews button in reviews details and confirm that it redirects to the delete review page
- Click on the edit comments button in reviews details and confirm that it redirects to the edit comments page
- Click on the delete comments button in reviews details and confirm that it redirects to the delete comments page

- After having created a review on the website
    - Confirm that the "Your Review" is displaying in the reviews page
    - Click on the review in the reviews page and confirm that you are redirected to the reviews detail page for that specific review
    - Click on the "Edit Review" button and confirm that you are redirected to the Edit Review page
    - Click on the "Delete Review" button and confirm that the review is deleted

- After having created a comment on the website
    - Confirm that your comment was submitted for approval when a message is displayed stating that your comment has been submitted for approval.
    - Click on the "Edit comment" button and confirm that you are redirected to the Edit comment page
    - Click on the "Delete comment" button and confirm that the comment is deleted

### Edit review Page
- Confirm that the page renders with the edit review form pre-populated with the details of the selected review.
- Test the form
    - Fill in all fields correctly - Click on the "update" button and confirm that you are redirected to the reviews page and that it displays the updated review.
    - Fill in all fields correctly with the below exceptions, click on the "update" button and confirm that you are prompted to fill in the missing field
        - Leave the title field blank
        - Leave the content field blank
        - Leave the excerpt field blank
        - Do not select any image for the image field

### Delete review page
- Confirm that the page renders prompting to delete the selected review, displaying the review details of the selected review.
- Confirm that on deleting that you are redirected to the reviews page and your review has been deleted.
