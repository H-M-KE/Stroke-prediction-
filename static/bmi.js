function updateWeight() {
    const weight = document.getElementById("weightRange").value;
    document.getElementById("weightValue").innerText = weight;
    calculateBMI();
}

function updateHeight() {
    const height = document.getElementById("heightRange").value;
    document.getElementById("heightValue").innerText = height;
    calculateBMI();
}

function calculateBMI() {
    const weight = document.getElementById("weightRange").value;
    const height = document.getElementById("heightRange").value / 100; // convert cm to meters
    const bmi = (weight / (height * height)).toFixed(1);
    document.getElementById("bmiValue").innerText = bmi;

    let status;
    let color;

    if (bmi < 18.5) {
        status = "Underweight";
        color = "blue"; // Color for Underweight
    } else if (bmi < 24.9) {
        status = "Normal weight";
        color = "green"; // Color for Normal weight
    } else if (bmi < 29.9) {
        status = "Overweight";
        color = "orange"; // Color for Overweight
    } else {
        status = "Obesity";
        color = "red"; // Color for Obesity
    }
    document.getElementById("statusValue").innerText = status;
    document.getElementById("statusValue").style.color = color;
}



