document.addEventListener("DOMContentLoaded", () => {
  const daysContainer = document.querySelector(".days");

  const days = [
    { day: 1, usage: "5h 13m" },
    { day: 2, usage: "6h 4m" },
    { day: 3, usage: "5h 52m" },
    { day: 4, usage: "5h 16m" },
    { day: 5, usage: "7h 2m" },
    { day: 6, usage: "5h 03m" },
    { day: 7, usage: "5h 46m" },
    { day: 8, usage: "8h 13m" },
    { day: 9, usage: "6h 42m" },
    { day: 10, usage: "4h 23m" },
    { day: 11, usage: "" },
    { day: 12, usage: "" },
    { day: 13, usage: "" },
    { day: 14, usage: "" },
    { day: 15, usage: "" },
    { day: 16, usage: "" },
    { day: 17, usage: "" },
    { day: 18, usage: "" },
    { day: 19, usage: "" },
    { day: 20, usage: "" },
    { day: 21, usage: "" },
    { day: 22, usage: "" },
    { day: 23, usage: "" },
    { day: 24, usage: "" },
    { day: 25, usage: "" },
    { day: 26, usage: "" },
    { day: 27, usage: "" },
    { day: 28, usage: "" },
    { day: 29, usage: "" },
    { day: 30, usage: "" },
    { day: 31, usage: "" },
  ];

  days.forEach((day) => {
    const dayElement = document.createElement("div");
    dayElement.classList.add("day");
    dayElement.innerHTML = `
            <div>${day.day}</div>
            <div class="usage-time">${day.usage}</div>
        `;
    daysContainer.appendChild(dayElement);
  });
});
