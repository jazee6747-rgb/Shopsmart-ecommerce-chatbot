function send() {
  let msg = document.getElementById("msg").value;

  fetch("https://shopsmart-ecommerce-chatbot-2.onrender.com", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("chat").innerHTML +=
      "<p><b>You:</b> " + msg + "</p>" +
      "<p><b>Bot:</b> " + data.reply + "</p>";
  });

  document.getElementById("msg").value = ""; // clear input
}
