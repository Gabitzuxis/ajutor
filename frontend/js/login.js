async function login(){

let u=document.getElementById("user").value
let p=document.getElementById("pass").value

let r=await fetch("/login",{
method:"POST",
headers:{'Content-Type':'application/json'},
body:JSON.stringify({
username:u,
password:p
})
})

let d=await r.json()

if(d.status=="ok")
location.href="dashboard.html"
}
