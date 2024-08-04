function openOverlay() {
  document.getElementById("overlay").style.display = "flex";
}

// Close overlay
function closeOverlay() {
  document.getElementById("overlay").style.display = "none";
}

function openAddOverlay() {
  document.getElementById("addOverlay").style.display = "flex";
}

// Close overlay
function closeAddOverlay() {
  document.getElementById("addOverlay").style.display = "none";
}

document.getElementById("allBtn").addEventListener("click", function () {
  document.getElementById("allContent").style.display = "block";
  document.getElementById("followContent").style.display = "none";
  this.classList.add("active");
  document.getElementById("followBtn").classList.remove("active");
});

document.getElementById("followBtn").addEventListener("click", function () {
  document.getElementById("allContent").style.display = "none";
  document.getElementById("followContent").style.display = "block";
  this.classList.add("active");
  document.getElementById("allBtn").classList.remove("active");
});
