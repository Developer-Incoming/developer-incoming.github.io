let greeting = document.getElementById("greeting");

getGreeting = () => {
    var d = new Date();
    return d.getHours() >= 5 && d.getHours() < 12 ? "Good morning" : (d.getHours() >= 12 && d.getHours() < 6 ? "Good afternoon" : "Good evening");
}

greeting.textContent = getGreeting();
