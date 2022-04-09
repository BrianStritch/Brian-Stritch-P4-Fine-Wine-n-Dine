/*!
* Start Bootstrap - Business Casual v7.0.6 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
});


setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

function navToggler() {
    var toggleMain = document.getElementById("navbarSupportedContent-main");
    toggleMain.classList.toggle("collapse");
    var toggleBooking = document.getElementById("navbarSupportedContent-booking");
    toggleBooking.classList.toggle("collapse");
    var toggleReviews = document.getElementById("navbarSupportedContent-reviews");
    toggleReviews.classList.toggle("collapse");
    var toggleAdmin = document.getElementById("navbarSupportedContent-admin");
    toggleAdmin.classList.toggle("collapse");
  }
