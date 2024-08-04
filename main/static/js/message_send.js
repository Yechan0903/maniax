function sendMessage() {
  const confirmation = document.getElementById("confirmation");
  confirmation.style.display = "block";

  setTimeout(() => {
    confirmation.style.display = "none";
    window.location.href = "message.html";
  }, 10000);
}
