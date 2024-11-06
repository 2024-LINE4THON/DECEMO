const id = document.getElementById("id_username");
const id_btn = document.getElementById("check-username");
const password = document.getElementById("id_password");
const password_check = document.getElementById("id_password_confirm");
const login_btn = document.getElementById("login_btn");

function idCheck() {
  if (id.value.length > 0) {
    id_btn.style.backgroundColor = "#ffd739";
  }
}

id.addEventListener("input", idCheck);

id.addEventListener("input", setColor);
password.addEventListener("input", setColor);
password_check.addEventListener("input", setColor);

function setColor() {
  if (id.value.length > 0 && password.value.length > 0 && password_check.value.length > 0) {
    login_btn.style.backgroundColor = "#FFD739";
  }
}

$(document).ready(function () {
  $("#check-username").click(function () {
    const username = $("#id_username").val();
    $.ajax({
      url: checkUsernameUrl,
      data: {
        username: username,
      },
      dataType: "json",
      success: function (data) {
        if (data.is_taken) {
          $(".modal").show();
        } else {
          id_btn.style.backgroundColor = "#dadada";
        }
      },
    });
  });
});

//팝업 닫기
function close_pop(flag) {
  $(".modal").hide();
}
