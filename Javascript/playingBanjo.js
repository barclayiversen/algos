function areYouPlayingBanjo(name) {
    var name_ = name.toUpperCase();
    if(name_[0] === "R"){
        return name + " plays banjo";
    }
    else{
        return name + " does not play banjo";
    }
}