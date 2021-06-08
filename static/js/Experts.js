const expert = [
    { name: "Mr. Sumit Jain", designation: "Phocket Infotech Pvt. Ltd., New Delhi", email: "Sumit.jain@phocket.com", phone: "9313220115", role: "Expert from nearby Industry/ Industry association/ Ecosystem Enablers", image: "Mr. Sumit Jain.jpeg" },

    { name: "Mr. Anil Bareja", designation: "Managing Director,Bareja Solar & Projects Pvt. Ltd., New Delhi", email: "bareja.a@gmail.com", phone: "9654965471, 8076561823", role: "Start-up / Alumni entrepreneur", image: "Mr. Anil Bareja.jpeg" },

    { name: "Mr. Manish Pradhan", designation: "Swichan Trademart Pvt. Ltd.", email: "Manish.Pradhan13@yahoo.com", phone: "9971092448", role: "Start-up / Alumni entrepreneur", image: "Mr. Manish Pradhan.jpeg" },

    { name: "Dr. Keerti Gupta", designation: "Patent Agent,Lakshay Groups, Noida", email: "Dr.keerti@gmail.com", phone: "9899571115", role: "I P Expert", image: "Dr. Keerti Gupta.jpeg" },

    { name: "Mr. Suneel wattal", designation: "Department of IT, Electronics and Communication, Govt. Of Haryana", email: "suwattal@gmail.com", phone: "9811872377", role: "", image: "Mr. Sunil Wattal.jpeg" },

    

]

const expertContainer = document.querySelector(".expertContainer")
let html = "";
for (const item of expert) {
    html += `<div class="expert-item">
        <div class="expert-image">
          <img src="/static/images/External Experts/${item.image}" alt="">
        </div>
        <div class="expert-content">
          <div class="expert-name">${item.name}</div>
          <div>
          <h6 class=" grey-text mb-3">${item.designation}</h6>
            
            <div class="icons"><span><i class="bi bi-envelope-fill"></i></span><span>${item.email}</span></div>
            <div class="icons"><span><i class="bi bi-telephone-fill"></i></span><span>${item.phone}</span></div>
            <div>${item.role}</div>
          </div>
        </div>
      </div>`
}
expertContainer.innerHTML = html