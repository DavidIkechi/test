// Initialize Swiper (carousel)
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  cssMode: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  mousewheel: true,
  keyboard: true,
});

// Change favicon with theme
lightSchemeIcon = document.querySelector("link#fav-green");
darkSchemeIcon = document.querySelector("link#fav-white");

function onUpdate() {
  if (matcher.matches) {
    lightSchemeIcon.remove();
    document.head.append(darkSchemeIcon);
  } else {
    document.head.append(lightSchemeIcon);
    darkSchemeIcon.remove();
  }
}

matcher = window.matchMedia("(prefers-color-scheme: dark)");
matcher.addListener(onUpdate);
onUpdate();

// LOGIN MODAL
let loginModal = document.querySelector(".login-modal");

function hideLoginModal() {
  loginModal.style.display = "none";
}
function showLoginModal() {
  loginModal.style.display = "block";
}

// MOBILE MENU
const menu = document.querySelector(".mobile_menu");
const openMenu = document.querySelector(".hamburger");
const closeMenu = document.querySelector(".hamburger_close");

openMenu.onclick = () => {
  menu.classList.add("showMenu");
  document.querySelector(".mobile_search").style.display = "none";
  openMenu.style.display = "none";
  closeMenu.style.display = "block";
};

closeMenu.onclick = () => {
  menu.classList.remove("showMenu");
  document.querySelector(".mobile_search").style.display = "block";
  openMenu.style.display = "flex";
  closeMenu.style.display = "none";
};

// PASSWORD SHOW/HIDE   ||
function passwordToggle() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
    document.querySelector(".bi-eye").style.display = "none";
    document.querySelector(".bi-eye-slash").style.display = "block";
    // x.classList.remove("bi-eye");
    // x.classList.add("bi-eye-slash");
  } else {
    x.type = "password";
    document.querySelector(".bi-eye").style.display = "block";
    document.querySelector(".bi-eye-slash").style.display = "none";
  }
}
