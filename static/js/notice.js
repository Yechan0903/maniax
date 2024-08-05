function toggleNotice(element) {
  element.classList.toggle("open");
  const content = element.querySelector(".notice-content");
  const arrow = element.querySelector(".arrow");

  if (element.classList.contains("open")) {
    content.style.display = "block";
    arrow.style.transform = "rotate(180deg)";
    element.style.height = "auto";
  } else {
    content.style.display = "none";
    arrow.style.transform = "rotate(0deg)";
    element.style.height = "auto";
  }
}
