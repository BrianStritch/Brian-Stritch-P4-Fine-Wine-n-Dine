window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
});


setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

function navTogglerMain() {
    var toggleMain = document.getElementById("navbarSupportedContent-main");
    toggleMain.classList.toggle("collapse");
  }
function navTogglerAlt() {
    var toggleBooking = document.getElementById("navbarSupportedContent");
    toggleBooking.classList.toggle("collapse");
  }

function navToggler() {
    navTogglerMain();
    navTogglerAlt();
  }

