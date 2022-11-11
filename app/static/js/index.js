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


var sizeFooter = function(){
    $(".webfooter").css("padding-bottom", "0px").css("padding-bottom", $(window).height() - $("body").height())
}
$(window).resize(sizeFooter);
// Initialize and add the map


/*function initMap() {
    // The location of Trips
    const Trips = {{ map.address }};
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 1,
      center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
    });
  }*/
  