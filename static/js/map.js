"use strict";

//map rendering

var map, infowindow;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: 43.654,
      lng: -79.383,
    },
    zoom: 10,
  });

  var input = document.getElementById("search");
  var searchBox = new google.maps.places.SearchBox(input);

  map.addListener("bounds_changed", function () {
    searchBox.setBounds(map.getBounds());

    var markers = [];

    searchBox.addListener("places_changed", function () {
      var places = searchBox.getPlaces();

      if (places.length === 0) return;

      markers.forEach(function (e) {
        e.setMap(null);
      });
      markers = [];

      var bounds = new google.maps.LatLngBounds();

      places.forEach(function (p) {
        if (!p.geometry) return;

        markers.push(
          new google.maps.Marker({
            map: map,
            title: p.name,
            position: p.geometry.location,
          })
        );

        if (p.geometry.viewport) bounds.union(p.geometry.viewport);
        else bounds.extend(p.geometry.location);
      });
      map.fitBounds(bounds);
    });
  });
}
