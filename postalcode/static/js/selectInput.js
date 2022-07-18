function selectInput() {
    var p = document.querySelectorAll("p");
    console.log(p)
    p.onclick = function (event) {
        var getValue = event.target.textContent;   //Text
        console.log(event.target.textContent);
        $("#search-input").val(getValue);
        closeSearchList()
    }
}