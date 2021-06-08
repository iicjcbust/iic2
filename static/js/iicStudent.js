const team = [
  { name: "Samarth Gupta", branch: "B.tech CE", year: "3rd", rollNo: "18001003108", email: "samarth.btp.1234@gmail.com", phone: "8058503435", image: "Samarth.png" },
  { name: "Vibhor Agarwal", branch: "B.tech ECE", year: "3rd", rollNo: "18001008061", email: "vibhoragarwal199@gmail.com", phone: "9999504382", image: "Vibhor.png" },
  { name: "Chirag Goyal ", branch: "B.Tech EL", year: "3rd", rollNo: "18001007016", email: "goyalchirag2001@gmail.com ", phone: "9811076788", image: "Chirag.png" },
  { name: "Yogesh Yadav", branch: "Btech CE ", year: "3rd", rollNo: "18001003134", email: "yogeshyadav32321212@gmail.com", phone: "8685916322", image: "Yogesh.png" },
  { name: "Jyoti rani", branch: "Btech CE", year: "3rd", rollNo: "18001003052", email: "dy01804@gmail.com", phone: "9899204158", image: "Jyoti.png" },
  { name: "Praveen Kumar", branch: "Btech CE", year: "3rd", rollNo: "18001003091", email: "kharbpraveen86@gmail.com", phone: "8700046679", image: "Praveen.png" },
  { name: "Avinash", branch: "Btech CE", year: "2nd", rollNo: "19001003025", email: "avinashsingh880086@gmail.com ", phone: "8800860298", image: "avinash.jpg" },
  { name: "Elesh Garg", branch: "B.tech CE", year: "2nd", rollNo: "19001003042", email: "eleshgarg@gmail.com", phone: "7082629964", image: "Elesh Garg.png" },
    { name: "Ritik Goyal", branch: "B.tech CE", year: "2nd", rollNo: "19001003100", email: "Ritikgoyal1710@gmail.com", phone: "7357721883", image: "Ritik.png" },
    { name: "Ritik Panchal", branch: "B.tech IT", year: "2nd", rollNo: "19001011052", email: "ritikpanchal768@gmail.com", phone: "8700002896", image: "Ritik Panchal.png" },
    { name: "Paras Arora", branch: "Btech. ME ", year: "2nd", rollNo: "19001013082", email: "aroraparas1010@gmail.com", phone: "9255492409", image: "Paras.png" },
    { name: "Jai Mudgil", branch: "Btech Me", year: "2nd", rollNo: "19001013051", email: "jaimudgil2001@gmail.com", phone: "9518090897", image: "Jai.png" },
    { name: "Harsh", branch: "BTech Me", year: "2nd", rollNo: "19001013042", email: "harshmiglani9050@gmail.com", phone: "9050366436", image: "Harsh.png" },
    { name: "Guranshish Bhutra", branch: "BBA ", year: "2nd", rollNo: "19001301015", email: "guranshishbhutra@gmail.com", phone: "9312078822", image: "Guranshish.png" },
    { name: "Khushi gupta", branch: "Btech CE", year: "1st", rollNo: "20031003058", email: "khushigg451@gmail.com", phone: "7838704008", image: "Khushi.png" },

]

const teamContainer = document.querySelector(".teamContainer")
let html = "";
for (const item of team) {
    html += `<div class="expert-item">
        <div class="expert-image">
          <img src="/static/images/student_photos/${item.image}" alt="">
        </div>
        <div class="expert-content">
          <div class="expert-name">${item.name}</div>
          <div>
            <div>[${item.branch}] ${item.year} year</div>
            <div>${item.rollNo}</div>
            <div class="icons"><span><i class="bi bi-envelope-fill"></i></span><span>${item.email}</span></div>
            <div class="icons"><span><i class="bi bi-telephone-fill"></i></span><span>${item.phone}</span></div>
          </div>
        </div>
      </div>`
}
teamContainer.innerHTML = html