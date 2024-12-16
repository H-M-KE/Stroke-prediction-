function validateForm() {
    let isValid = true;

    // Clear previous error messages
    document.getElementById('name-error').innerText = '';
    document.getElementById('age-error').innerText = '';
    document.getElementById('bmi-error').innerText = '';
    document.getElementById('glucose-error').innerText = '';

    // Validate Name
    const name = document.getElementById('name').value;
    if (name.trim() === '') {
        document.getElementById('name-error').innerText = 'Name is required.';
        isValid = false;
    }

    // Validate Age
    const age = document.getElementById('age').value;
    if (age < 0 || age > 120) {
        document.getElementById('age-error').innerText = 'Please enter a valid age.';
        isValid = false;
    }

    // Validate BMI
    const bmi = document.getElementById('bmi').value;
    if (bmi < 10 || bmi > 50) {
        document.getElementById('bmi-error').innerText = 'BMI must be between 10 and 50.';
        isValid = false;
    }

    // Validate Glucose Level
    const glucose = document.getElementById('glucose').value;
    if (glucose < 0 || glucose > 400) {
        document.getElementById('glucose-error').innerText = 'Please enter a valid glucose level.';
        isValid = false;
    }

    return isValid;
}