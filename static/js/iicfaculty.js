const members = [
  { NAME: "Prof. Lakhwinder", Designation: "President", Email: "lakhwinder2003@gmail.com", Phone: "99583004400" ,image: "Prof. Lakhwinder Singh.jpeg"},
  { NAME: "Dr. Sapna Gambhir", Designation: "Vice President", Email: "sapnagambhir@gmail.com", Phone: "9810340200" ,image: "Dr. Sapna Gambhir.jpeg"},
  { NAME: "Dr.Parul Tomar", Designation: "Convenor", Email: "ptomar_p@hotmail.com", Phone: "9818923336", image: "Dr. Parul Tomar.jpg"},
  { NAME: "Mr. Ajay", Designation: "Incubation Cell Coordinator", Email: "ajay.b.ibc@gmail.com", Phone: "8295203756" ,image: "Mr. Ajay Sharma.jpg"},
  { NAME: "Ms. Rashmi Chawla", Designation: "Innovation Cell Coordinator", Email: "rashmichawlaymca@gmail.com", Phone: "9810368881", image: "Ms. Rashmi Chawla.jpeg"},
  { NAME: "Dr. Rashmi Polpli", Designation: "Start-Up Cell Coordinator", Email: "rashmimukhija@gmail.com", Phone: "9810862658" ,image: "Dr. Rashmi Popli.jpeg"},
  { NAME: "Dr. Ashlesha Gupta", Designation: "IPR Cell Coordinator", Email: "gupta_ashlesha@yahoo.co.in", Phone: "9891466310" ,image: "Dr. Ashlesha Gupta.jpg"},
  { NAME: "Mr. Jitender (PRO)", Designation: "Social Media Coordinator", Email: "proymcaust@gmail.com", Phone: "8447141780", image: "Mr. Jitender.jpg"},
  { NAME: "Dr. Vishal Puri", Designation: "Intership Coordinator", Email: "vpuri@jcboseust.ac.in", Phone: "9122446666", image: "Dr. Vishal Puri.jpg"},
  { NAME: "Dr. Krishan Verma ", Designation: "ARIIA Coordinator", Email: "dr.krishanverma.me@gmail.com", Phone: "9896596710" ,image: "Dr. Krishan Verma.png"},
  { NAME: "Ms. Jyotsana Chawla", Designation: "NIRF Coordinator", Email: "jyotsanachawla@rediffmail.com", Phone: "9990234880" ,image: "Ms. Jyotsana Chawla.jpg"},

  // { NAME: "Dr. Sakshi", Designation: "EL", Email: "sakshibangia@gmail.com", Phone: "8860988607", image: "Dr. Sakshi Kalra.jpeg"},
  // { NAME: "Dr. Sheilza Jain", Designation: "ECE", Email: "sheilzajain@gmail.com", Phone: "9818886957" ,image: "Dr. Sheilza Jain.jpeg" },
  // { NAME: "Dr. Rewa", Designation: "CE", Email: "rewa10.sh@gmail.com", Phone: "9582236664", image: "Dr. Rewa Sharma.jpeg"},
  // { NAME: "Dr. Somvir", Designation: "EVS", Email: "somvirbajar@gmail.com", Phone: "8950000270" ,image: "Dr. Somvir Bajar.jpg"},
  // { NAME: "Dr. Anurag", Designation: "chemistry", Email: "anurag.sunda@gmail.com", Phone: "9982560729", image: "Dr. Anurag.jpg"},
  // { NAME: "Dr. Suraj", Designation: "EVS", Email: "surajgoyal87@gmail.com", Phone: "9417728292" ,image: "Dr. Suraj (copy).jpg"},
  // { NAME: "Dr. Poonam Garg", Designation: "CE", Email: "poonamgarg1984@gmail.com", Phone: "9899284595" ,image: "Dr. Poonam Garg.jpeg"},
  // { NAME: "Dr. Manvi", Designation: "CE", Email: "manvi.siwach@gmail.com", Phone: "9971599791", image: "Dr. Manvi.jpeg"},
  // { NAME: "Dr. Yogita", Designation: "Physics", Email: "ybatraiuac@gmail.com", Phone: "9910046111", image: "Dr. Yogita.jpg"},
  // { NAME: "Ms. Gunjan Gumber", Designation: "MBA", Email: "gunjangumber@gmail.com", Phone: "9810695278", image: "Dr. Gunjan Gumber.jpeg"},
  // { NAME: "Ms. Anubha Gautam", Designation: "EL", Email: "gautamanubha.12@gmail.com", Phone: "9990287227" ,image: "Ms. Anubha Gautam.jpeg"},
  // { NAME: "Mr. Aditya", Designation: "animation", Email: "adikumar8397@gmail.com", Phone: "8630528397", image: "Mr. Jitender.jpg"},
  // { NAME: "Dr. Nikhil Derv", Designation: "MECH", Email: "nikhildevgarg@gmail.com", Phone: "9711812394" ,image: "Nikhil Dev.jpg"},
]

const membersContainer = document.querySelector(".membersContainer")
let html = "";
for (const item of members) {
  html += `<div class="expert-item">
      <div class="expert-image">
        <img src="/static/images/External Experts/${item.image}" alt="">
      </div>
      <div class="expert-content">
        <div class="expert-name">${item.NAME}</div>
        <div>
          <div>[${item.Designation}]</div>
          <div class="icons"><span><i class="bi bi-envelope-fill"></i></span><span>${item.Email}</span></div>
          <div class="icons"><span><i class="bi bi-telephone-fill"></i></span><span>${item.Phone}</span></div>
        </div>
      </div>
    </div>`
}
membersContainer.innerHTML = html