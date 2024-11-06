const id = document.getElementById("id_username");
const id_btn = document.getElementById("check-username");

function idCheck() {
  if (id.value.length > 0) {
    id_btn.style.backgroundColor = "#ffd739";
  }
}

id.addEventListener("input", idCheck);

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
