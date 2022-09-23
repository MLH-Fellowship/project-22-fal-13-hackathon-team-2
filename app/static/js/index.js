// Accordion

var li_items = document.querySelectorAll(".accordion_wrap ul li");
var ul = document.querySelector(".accordion_wrap ul");

li_items.forEach(function(item) {
    item.addEventListener("click", function() {
        li_items.forEach(function(item) {
            item.classList.remove("active");
        })
        item.classList.add("active");
    });
});

// work

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}