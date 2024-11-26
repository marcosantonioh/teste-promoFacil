

const carouselSlide = document.getElementById('carousel-slide');
        const carouselItems = document.querySelectorAll('.carousel-item');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');

        let counter = 0;
        const size = 859; // Width of each slide

        function updateCarousel() {
            carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
        }

        nextBtn.addEventListener('click', () => {
            counter = (counter + 1) % carouselItems.length;
            updateCarousel();
        });

        prevBtn.addEventListener('click', () => {
            counter = (counter - 1 + carouselItems.length) % carouselItems.length;
            updateCarousel();
        });

        function autoSlide() {
            counter = (counter + 1) % carouselItems.length;
            updateCarousel();
        }

        setInterval(autoSlide, 5000); // Slide automatically every 5 seconds

        window.onload = updateCarousel;












/************************* */

var msgCookies = document.getElementById("cookies-msg")

function aceito(){

    localStorage.lgpd = "sim"
    msgCookies.classList.remove('mostrar')

}

if (localStorage.lgpd == "sim"){
    msgCookies.classList.remove('mostrar')
}else{
    msgCookies.classList.add('mostrar')
}









document.addEventListener('DOMContentLoaded', () => {
    const perfilLink = document.getElementById('perfilLink');
    const dropdownMenu = document.getElementById('dropdownMenu');

    perfilLink.addEventListener('click', (e) => {
        e.preventDefault(); // Evita o comportamento padrão do link
        dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
    });

    window.addEventListener('click', (event) => {
        if (!perfilLink.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });

    const configLink = document.getElementById('configLink');
    configLink.addEventListener('click', (e) => {
        e.preventDefault(); // Evita o comportamento padrão do link
        window.location.href = 'gerenciar_perfil.html'; // Substitua pelo URL da página de configurações do empresário
    });


    const logoutLink = document.getElementById('logoutLink');
    logoutLink.addEventListener('click', (e) => {
        e.preventDefault(); // Evita o comportamento padrão do link
        window.location.href = 'promocoes_user.html'; // Substitua pelo URL da página de logout
    });
});






const scrollToTopBtn = document.getElementById('scroll-to-top');

scrollToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth' 
    });
});

window.addEventListener('scroll', () => {
    if (window.scrollY > 200) {
        scrollToTopBtn.classList.add('show');
    } else {
        scrollToTopBtn.classList.remove('show');
    }
});

