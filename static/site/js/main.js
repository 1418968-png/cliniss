(function () {
    var menuButton = document.querySelector('.menu-toggle');
    var nav = document.querySelector('.site-nav');
    var actions = document.querySelector('.header-actions');

    if (menuButton && nav && actions) {
        menuButton.addEventListener('click', function () {
            var isOpen = nav.classList.toggle('is-open');
            actions.classList.toggle('is-open', isOpen);
            menuButton.setAttribute('aria-expanded', String(isOpen));
        });
    }

    var accessState = JSON.parse(localStorage.getItem('clinissAccess') || '{}');
    if (accessState.images === true && accessState.imagesMode !== 'muted-v2') {
        accessState.images = false;
    }
    accessState.imagesMode = 'muted-v2';

    function applyAccessState() {
        document.body.classList.toggle('access-font', Boolean(accessState.font));
        document.body.classList.toggle('access-contrast', Boolean(accessState.contrast));
        document.body.classList.toggle('access-no-images', Boolean(accessState.images));
        document.querySelectorAll('[data-access-toggle]').forEach(function (button) {
            var key = button.getAttribute('data-access-toggle');
            button.setAttribute('aria-pressed', String(Boolean(accessState[key])));
        });
        localStorage.setItem('clinissAccess', JSON.stringify(accessState));
    }

    document.querySelectorAll('[data-access-toggle]').forEach(function (button) {
        button.addEventListener('click', function () {
            var key = button.getAttribute('data-access-toggle');
            accessState[key] = !accessState[key];
            applyAccessState();
        });
    });

    applyAccessState();

    var cookieBanner = document.getElementById('cookie-banner');
    var cookieAccepted = localStorage.getItem('clinissCookieAccepted') === '1';
    if (cookieBanner && !cookieAccepted) {
        cookieBanner.classList.add('is-visible');
    }

    document.querySelectorAll('[data-cookie-accept]').forEach(function (button) {
        button.addEventListener('click', function () {
            localStorage.setItem('clinissCookieAccepted', '1');
            if (cookieBanner) {
                cookieBanner.classList.remove('is-visible');
            }
        });
    });
})();
