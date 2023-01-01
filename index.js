urlFragmentScroll = function() {
    let urlFragment = document.URL.split("#")[1];
    
    alert(urlFragment);
    document.getElementByClassName(urlFragment + "Frag").scrollIntoView();
}
