const weightInput = document.getElementById('weight');
const heightInput = document.getElementById('height');
const bmiResult = document.getElementById('bmi-result');

document.querySelector('button').addEventListener('click', calculateBMI);

function calculateBMI() {
    const weight = parseFloat(weightInput.value);
    const height = parseFloat(heightInput.value);

    if (isNaN(weight) || isNaN(height)) {
        bmiResult.textContent = 'Please enter valid numbers';
        return;
    }

    const bmi = weight / (height / 100) ** 2;
    const result = `Your BMI is ${bmi.toFixed(2)}`;

    if (bmi < 18.5) {
        result += ' (Underweight)';
    } else if (bmi < 25) {
        result += ' (Normal)';
    } else if (bmi < 30) {
        result += ' (Overweight)';
    } else {
        result += ' (Obese)';
    }

    bmiResult.textContent = result;
}