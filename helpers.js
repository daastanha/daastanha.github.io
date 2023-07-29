function detect_lang_direction(data) {
    var direction = "ltr";
    if (data.indexOf("ا") > -1) {
        direction = "rtl";
    }
    return direction;
}