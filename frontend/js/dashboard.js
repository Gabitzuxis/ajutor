async function generate(){

let script=document.getElementById("script").value

let prompts=document
.getElementById("prompts")
.value
.split("\n")

let speed=document.getElementById("speed").value

await fetch("/generate",{
method:"POST",
headers:{'Content-Type':'application/json'},
body:JSON.stringify({
script:script,
prompts:prompts,
speed:speed
})
})

let d=document.getElementById("download")

d.href="/download"

d.style.display="block"

}
