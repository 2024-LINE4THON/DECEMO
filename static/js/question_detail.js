//입력했을 때 저장 버튼 색 바꾸기
const submit_btn = document.querySelector(".submit");
const text_box = document.querySelector("textarea");

text_box.addEventListener("input", function () {
  if (text_box.value) {
    submit_btn.style.backgroundColor = "#ffd739";
    submit_btn.disabled = false;
  } else {
    submit_btn.style.backgroundColor = ""; // 기본색
    submit_btn.disabled = true;
  }
});

//저장 버튼 누르면 모달창 띄우기
const modal = document.querySelector(".modal");
const modalOpen = document.querySelector(".submit-btn button");
const modalClose = document.querySelector(".close_btn");

modalOpen.addEventListener("click", function (event) {
  event.preventDefault();
  modal.style.display = "flex";
});

modalClose.addEventListener("click", function () {
  modal.style.display = "none";
});
