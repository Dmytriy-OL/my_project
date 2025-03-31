document.addEventListener("DOMContentLoaded", function () {
    if (!Cookies.get("cookieConsent")) {
        let popup = document.createElement("div");
        popup.id = "cookie-popup";
        popup.innerHTML = `
            <div class="cookie-content">
                <p>Цей сайт використовує файли cookie для забезпечення найкращого досвіду. Продовжуючи, ви погоджуєтесь з нашою <a href="/privacy-policy">Політикою конфіденційності</a>.</p>
                <button id="accept-cookies">Прийняти</button>
            </div>
        `;
        document.body.appendChild(popup);

        document.getElementById("accept-cookies").addEventListener("click", function () {
            Cookies.set("cookieConsent", "true", { expires: 365 });
            popup.remove();
        });
    }
});
