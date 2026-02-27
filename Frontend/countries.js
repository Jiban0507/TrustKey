const countryCodes = [
  { code: "+91", name: "India" },
  { code: "+880", name: "Bangladesh" },
  { code: "+1", name: "USA" },
  { code: "+44", name: "UK" },
  { code: "+61", name: "Australia" },
  { code: "+81", name: "Japan" },
  { code: "+49", name: "Germany" },
  { code: "+33", name: "France" },
  { code: "+39", name: "Italy" },
  { code: "+86", name: "China" },
  { code: "+7", name: "Russia" },
  { code: "+34", name: "Spain" },
  { code: "+55", name: "Brazil" },
  { code: "+27", name: "South Africa" },
  { code: "+82", name: "South Korea" },
  { code: "+966", name: "Saudi Arabia" },
  { code: "+971", name: "UAE" },
  { code: "+92", name: "Pakistan" },
  { code: "+94", name: "Sri Lanka" },
  { code: "+93", name: "Afghanistan" }
];


window.onload = function () {
  const dropdownList = document.getElementById("dropdownList");
  const selected = document.getElementById("selectedCode");
  const hiddenInput = document.getElementById("countryCode");


  hiddenInput.value = "+91";


  countryCodes.forEach(item => {
    const div = document.createElement("div");
    div.textContent = `${item.code} (${item.name})`;


    div.onclick = function() {
      selected.textContent = div.textContent;
      hiddenInput.value = item.code;
      dropdownList.style.display = "none";
    };


    dropdownList.appendChild(div);
  });


  selected.onclick = function() {
    dropdownList.style.display =
      dropdownList.style.display === "block" ? "none" : "block";
  };
};