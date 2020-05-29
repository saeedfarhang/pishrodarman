const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');

        navLinks.forEach((link, index) => {
            console.log(index);
            link.style.animation = 'navLinkFade 0.5 ease forwards ${index / 7}s'
        });
        burger.classList.toggle('toggle');
    });


}


navSlide();