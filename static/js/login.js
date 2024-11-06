const id = document.getElementById("id_username");
const password = document.getElementById("id_password");
const btn = document.getElementById("login_btn");

function setColor() {
  if (id.value.length > 0 && password.value.length > 0) {
    btn.style.backgroundColor = "#FFD739";
  }
}

id.addEventListener("input", setColor);
password.addEventListener("input", setColor);
