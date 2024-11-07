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
