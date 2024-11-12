const id = document.getElementById("id_username");
const password = document.getElementById("id_password");
const btn = document.getElementById("login_btn");
const p = document.getElementById("modal_p");

function setColor() {
  if (id.value.length > 0 && password.value.length > 0) {
    btn.style.backgroundColor = "#FFD739";
  }
}

id.addEventListener("input", setColor);
password.addEventListener("input", setColor);

function showPopup(message) {
  $(document).ready(function () {
    p.innerHTML = message;
    $(".modal").show();
  });
}

//팝업 Close 기능
function close_pop(flag) {
  $(".modal").hide();
}
