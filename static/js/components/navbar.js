document.addEventListener('DOMContentLoaded', function() {
    const initNavbar = () => {
        const homeIcon = document.querySelector('.home-icon');
        const dateIcon = document.querySelector('.date-icon');

        const setIconState = (activeIcon, inactiveIcon) => {
            // 활성화할 아이콘 설정
            activeIcon.classList.add('active');
            activeIcon.querySelector('img').src = `/static/assets/img/${activeIcon.classList.contains('home-icon') ? 'home' : 'date'}-ON.png`;
            activeIcon.querySelector('div').style.color = '#FFD52B';

            // 비활성화할 아이콘 설정
            inactiveIcon.classList.remove('active');
            inactiveIcon.querySelector('img').src = `/static/assets/img/${inactiveIcon.classList.contains('home-icon') ? 'home' : 'date'}-OFF.png`;
            inactiveIcon.querySelector('div').style.color = '#2A2A2A';
        };

        homeIcon.addEventListener('click', function() {
            if (!this.classList.contains('active')) {
                setIconState(this, dateIcon);
            }
        });

        dateIcon.addEventListener('click', function() {
            if (!this.classList.contains('active')) {
                setIconState(this, homeIcon);
            }
        });
    };

    initNavbar();
});