document.getElementById("verifyForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const dob = document.getElementById("dob").value;
  const futureYear = document.getElementById("futureYear").value;
  const countryCode = document.getElementById("countryCode").value;
  const mobileNumber = document.getElementById("mobileNumber").value.trim();
  const aadhaar = document.getElementById("aadhaar").value.trim();

  const fullMobile = countryCode + mobileNumber;

  try {
    const response = await fetch("http://127.0.0.1:5000/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        dob: dob,
        future_year: futureYear,
        mobile: fullMobile,
        aadhaar: aadhaar
      })
    });

    const result = await response.json();

    // ✅ Save result in localStorage
    localStorage.setItem("verifyResult", JSON.stringify(result));

    // ✅ Redirect to result.html
    window.location.href = "result.html";

  } catch (error) {
    alert("Error connecting to backend.");
  }
});

document.getElementById("clearBtn").addEventListener("click", function() {
  document.getElementById("verifyForm").reset();
});