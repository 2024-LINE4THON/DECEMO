document.addEventListener("DOMContentLoaded", function () {
  const submitBtn = document.querySelector(".submit");
  const textBox = document.querySelector("textarea");
  const modal = document.querySelector(".modal");
  const modal_popup = document.querySelector(".modal-popup");
  const modalClose = document.querySelector(".close_btn");

  // 입력 시 저장 버튼 활성화
  if (textBox) {
    textBox.addEventListener("input", function () {
      if (textBox.value.trim()) {
        submitBtn.style.backgroundColor = "#ffd739";
        submitBtn.disabled = false;
      } else {
        submitBtn.style.backgroundColor = ""; // 기본색
        submitBtn.disabled = true;
      }
    });
  }

  // 저장 버튼 클릭 시 폼을 AJAX로 제출
  if (submitBtn) {
    submitBtn.addEventListener("click", function (event) {
      event.preventDefault(); // 기본 폼 제출 방지

      const formData = new FormData(document.querySelector(".answer"));

      fetch("", {
        method: "POST",
        body: formData,
        headers: {
          "X-Requested-With": "XMLHttpRequest", // AJAX 요청 표시
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "success") {
            modal_popup.style.display = "flex"; // 성공 시 모달창 표시
            modal.style.display = "flex";
            modal.style.filter = "blur(10px)";
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  }

  // 모달의 확인 버튼 클릭 시 캘린더 페이지로 이동
  if (modalClose) {
    modalClose.addEventListener("click", function () {
      window.location.href = "/question/calendar/"; // 캘린더 페이지로 이동
    });
  }
});
