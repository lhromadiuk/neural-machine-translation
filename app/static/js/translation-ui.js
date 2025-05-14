const languageOptions = {
    en: "English",
    de: "German",
};

const sourceSelect = document.getElementById('source_lang');
const targetSelect = document.getElementById('target_lang');

function updateTargetOptions() {
    const selectedSource = sourceSelect.value;
    const currentTarget = targetSelect.value;

    targetSelect.innerHTML = '';

    for (const [code, name] of Object.entries(languageOptions)) {
        if (code !== selectedSource) {
            const option = document.createElement('option');
            option.value = code;
            option.textContent = name;

            if (code === currentTarget) {
                option.selected = true;
            }

            targetSelect.appendChild(option);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateTargetOptions();
    sourceSelect.addEventListener('change', updateTargetOptions);
});


// Swap button
document.getElementById('swap_btn').addEventListener('click', function () {
    const sourceSelect = document.getElementById('source_lang');
    const targetSelect = document.getElementById('target_lang');
    const tempLang = sourceSelect.value;
    sourceSelect.value = targetSelect.value;
    updateTargetOptions();
    for (let option of targetSelect.options) {
        if (option.value === tempLang) {
            targetSelect.value = tempLang;
            break;
        }
    }
    const inputText = document.getElementById('input_text');
    const outputText = document.getElementById('output_text');
    const tempText = inputText.value;
    inputText.value = outputText.value;
    outputText.value = tempText;
});

// To avoid updating translation after every keystroke
let coolDownTimer;
document.getElementById('input_text').addEventListener('input', function () {
    clearTimeout(coolDownTimer);
    coolDownTimer = setTimeout(() => {
        const text = this.value;
        const sourceLang = document.getElementById('source_lang').value;
        const targetLang = document.getElementById('target_lang').value;

        fetch('/api/translate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({input_text: text, source_lang: sourceLang, target_lang: targetLang})
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('output_text').value = data.output_text;
            });
    }, 500);
});
