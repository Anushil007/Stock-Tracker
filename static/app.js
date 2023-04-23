const notificationSelect = document.getElementById("notification");
const emailinput = document.getElementById("email-input");
const phoneinput = document.getElementById("phone-input");

notificationSelect.addEventListener("change", function() {
  const notificationType = notificationSelect.value;

  if (notificationType === "text-message") {
    // emailinput.style.display = "none";
    // phoneinput.style.display = "block";
  } else {
    // phoneinput.style.display = "none";
    // emailinput.style.display = "block";
  }
});