const MIN_CURRENT_PAGE = 0;
const MAX_CURRENT_PAGE = 3;
let currentPage = 0;
let pageArr = [".page-one", ".page-two", ".page-three", ".page-four"];

let isWheelEventActive = true;

document.addEventListener("wheel", (e) => {
  if (!isWheelEventActive) {
    return;
  }

  if (isWheelUp(e)) {
    prevPage();
  }

  if (isWheelDown(e)) {
    nextPage();
  }

  isWheelEventActive = false;
  setTimeout(() => {
    isWheelEventActive = true;
  }, 750);
});

function isWheelUp(e) {
  return e.deltaY < 0;
}

function isWheelDown(e) {
  return e.deltaY > 0;
}

function prevPage() {
  if (currentPage > MIN_CURRENT_PAGE) {
    const nowPage = document.querySelector(pageArr[currentPage]);
    nowPage.classList.add("animate__animated", "animate__fadeOutDown", "animate__fast");
    const prevPage = document.querySelector(pageArr[--currentPage]);
    prevPage.classList.remove("animate__fadeOutUp", "animate__heartBeat", "animate__fadeInUp");
    prevPage.classList.add("animate__animated", "animate__fadeInDown", "animate__fast");
  }
}

function nextPage() {
  if (currentPage < MAX_CURRENT_PAGE) {
    const nowPage = document.querySelector(pageArr[currentPage]);
    nowPage.classList.add("animate__animated", "animate__fadeOutUp", "animate__fast");
    const nextPage = document.querySelector(pageArr[++currentPage]);
    nextPage.classList.remove("hide", "animate__fadeOutDown");
    nextPage.classList.add("animate__animated", "animate__fadeInUp", "animate__fast");
  }
}