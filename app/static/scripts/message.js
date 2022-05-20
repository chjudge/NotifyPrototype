async function setState(element) {
    const state = element.value;
    console.log(`fetching state ${state}`);
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

            if (counties.size === 0) {
                const allSelect = document.createElement('option');
                allSelect.value = '';
                allSelect.innerText = 'All';
                countySelect.appendChild(allSelect);
            }
            else {
                counties.forEach(county => {
                    const option = document.createElement('option');
                    option.value = county;
                    option.innerHTML = county;
                    countySelect.appendChild(option);
                });
            }
        });
}

function validateJSON(response) {
    if (response.ok) {
        return response.json();
    } else {
        return Promise.reject(response);
    }
}