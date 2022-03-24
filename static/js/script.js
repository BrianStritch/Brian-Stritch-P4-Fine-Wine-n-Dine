/*!
* Start Bootstrap - Business Casual v7.0.6 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
})


setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);


function toggleHide(){
    let edit_btn = document.getElementById('edit_review');
    edit_btn.classList.toggle('hide')

}



document.querySelector( document ).ready(function() {
    document.querySelector("#id_booking_date").datepicker({ 
        format: 'dd-mm-yyyy'
    });
    document.querySelector("#id_booking_date").addEventListener("change", function () {
        var fromdate = document.querySelector(this).value;
        alert(fromdate);
    });
}); 