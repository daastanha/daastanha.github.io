function detect_lang_direction(data) {
    // Unicode ranges for RTL scripts: Arabic (0600–06FF), Hebrew (0590–05FF), Persian subset
    if (/[\u0590-\u05FF\u0600-\u06FF]/.test(data)) {
        return "rtl";
    }
    return "ltr";
}
