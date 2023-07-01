

document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    navbarToggler.addEventListener('click', function() {
        if (navbarToggler.classList.contains('collapsed')) {
        navbarToggler.innerHTML = '<span class="fa-solid fa-bars"></span>';
        } else {
        navbarToggler.innerHTML = '<span class="fa-solid fa-xmark"></span>';
        }
    });
});