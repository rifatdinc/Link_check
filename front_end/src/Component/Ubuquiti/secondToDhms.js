const secondsToDhms = (seconds) => {
    seconds = Number(seconds);
    var d = Math.floor(seconds / (3600 * 24));
    var h = Math.floor(seconds % (3600 * 24) / 3600);
    var m = Math.floor(seconds % 3600 / 60);
    var s = Math.floor(seconds % 60);

    var dDisplay = d > 0 ? d + (d === 1 ? " gün, " : "gün, ") : "";
    var hDisplay = h > 0 ? h + (h === 1 ? " saat, " : "saat, ") : "";
    var mDisplay = m > 0 ? m + (m === 1 ? " dk, " : "dk, ") : "";
    var sDisplay = s > 0 ? s + (s === 1 ? " sn" : "sn") : "";
    return dDisplay + hDisplay + mDisplay + sDisplay;
}

export default secondsToDhms