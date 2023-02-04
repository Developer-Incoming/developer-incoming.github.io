let greeting = document.getElementById("greeting");

getGreeting = () => {
    let date = new Date();
    let h = date.getHours();

    // one liner 2 conditioner ternary statement :skull:
    return h >= 5 && h < 12 ? "Good morning" : (h >= 12 && h < 18 ? "Good afternoon" : "Good evening");
}

greeting.textContent = getGreeting();
