var changeBtn1 = document.getElementById("loginBtn1")
var changeBtn2 = document.getElementById("loginBtn2")
changeBtn1.onclick = function () {
    document.getElementById("container2").classList.add("unMark")
    document.getElementById("container").classList.remove("unMark")
}
changeBtn2.onclick = function () {
    document.getElementById("container2").classList.remove("unMark")
    document.getElementById("container").classList.add("unMark")
}
