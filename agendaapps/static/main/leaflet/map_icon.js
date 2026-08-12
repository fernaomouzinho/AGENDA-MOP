var LeafIcon = L.Icon.extend({
    options: {
        iconSize:     [34, 34],
        iconAnchor:   [12, 33],
        popupAnchor:  [5, -30]
    }
});

var buildingIcon = new LeafIcon({iconUrl: 'https://gis.adn.gov.tl/static/main/map_icons/school.png'});
var bridgeIcon = new LeafIcon({iconUrl: 'http://gis.adn.gov.tl/static/main/map_icons/bridge.png'});
var hospitalIcon = new LeafIcon({iconUrl: 'https://gis.adn.gov.tl/static/main/map_icons/hospital.png'});
var culvertIcon = new LeafIcon({iconUrl: 'https://gis.adn.gov.tl/static/main/map_icons/culvert.png'});