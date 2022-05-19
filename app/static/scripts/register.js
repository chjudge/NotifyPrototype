window.addEventListener("DOMContentLoaded", function () {
    // attach an event listener to the state dropdown
    const state = document.getElementById("state");
    state.addEventListener("change", setState);
});


async function setState(element) {
    const state = element.value;
    const counties = fetch(`/api/counties/${state}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then(validateJSON)
        .then(response => response['counties'])
        .then(counties => {
            const countySelect = document.getElementById('county');
            countySelect.innerHTML = '';

            counties = new Set(counties);

            if (counties.length == 0) {
                const pleaseSelect = document.createElement('option');
                pleaseSelect.value = '';
                pleaseSelect.innerText = 'Please select a state first';
            }
            else {
                const allOption = document.createElement('option');
                allOption.value = 'all';
                allOption.innerHTML = 'All';
                countySelect.appendChild(allOption);
                counties.forEach(county => {
                    const option = document.createElement('option');
                    option.value = county;
                    option.innerHTML = county;
                    countySelect.appendChild(option);
                });
            }
        });
}

function updateCounties(params) {
    var county = document.getElementById('county');
    county.choices = [];
}

function validateJSON(response) {
    if (response.ok) {
        return response.json();
    } else {
        return Promise.reject(response);
    }
}