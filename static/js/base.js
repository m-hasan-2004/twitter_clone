// static/js/base.js

// Function to toggle the mobile menu
document.getElementById('hamburger').addEventListener('click', function () {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
});
