async function login(){

let user=document.getElementById("user").value
let pass=document.getElementById("pass").value

let r=await fetch("/login",{
method:"POST",
headers:{'Content-Type':'application/json'},
body:JSON.stringify({username:user,password:pass})
})

let data=await r.json()

if(data.status=="ok")
location.href="dashboard.html"
}
