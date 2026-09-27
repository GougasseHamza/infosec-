(function () {
    var cookieName = "analytics_id";
    var parts = document.cookie.split(";");
    var aid = "";

    for (var i = 0; i < parts.length; i++) {
        var one = parts[i].trim();
        if (one.indexOf(cookieName + "=") === 0) {
            aid = one.substring(cookieName.length + 1);
        }
    }

    if (aid === "") {
        aid = "P-" + Math.random().toString(16).substring(2) + Date.now().toString(16);
        document.cookie = cookieName + "=" + aid + "; Max-Age=2592000; Path=/; SameSite=Lax";
    }

    var url = "http://analytics.localhost:9100/collect";
    url += "?aid=" + encodeURIComponent(aid);
    url += "&publisher=" + encodeURIComponent(location.host);
    url += "&page=" + encodeURIComponent(location.pathname);

    var pixel = new Image();
    pixel.src = url;
    console.log("analytics event sent", aid, location.host, location.pathname);
})();
