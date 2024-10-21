function saveNotes() {
    const userNotes = document.getElementById('userNotes').value;
    localStorage.setItem('notes', userNotes);
}

// Function to load and display saved notes from localStorage
function loadNotes() {
    const userNotes = localStorage.getItem('notes');
    if (userNotes) {
        document.getElementById('userNotes').value = userNotes;
    }
}

// Event listener for the "Save Notes" button
const saveButton = document.getElementById('saveNotes');
saveButton.addEventListener('click', saveNotes);

// Load and display saved notes when the page loads
window.addEventListener('load', loadNotes);





// Function to calculate and update the number of trades
function updateNumberOfTrades() {
    // Retrieve trade data from localStorage (assuming it's stored as an array)
    const tradeData = JSON.parse(localStorage.getItem('tradeData')) || [];

    // Calculate the number of trades
    const numberOfTrades = tradeData.length;

    // Update the "Number of Trades" in the HTML
    const numberOfTradesElement = document.getElementById('numberOfTrades');
    numberOfTradesElement.textContent = numberOfTrades;
}

// Call the function to update the number of trades when the page loads
window.addEventListener('load', updateNumberOfTrades);





const exchangeRateForm = document.getElementById('exchangeRateForm');
const currencyPairInput = document.getElementById('currencyPair');
const exchangeRateResult = document.getElementById('exchangeRateResult');

exchangeRateForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const currencyPair = currencyPairInput.value.trim().toUpperCase();
    if (!currencyPair) {
        return;
    }

    const apiKey = '6ec430efe5-76594741e4-s0mq50';

    // Construct the API request URL with the user-specified currency pair
    const apiUrl = `https://api.fastforex.io/fetch-one?from=${currencyPair}&to=USD&api_key=${apiKey}`;

    try {
        const response = await fetch(apiUrl);
        if (response.ok) {
            const data = await response.json();
            const rate = data.result[0].val;
            exchangeRateResult.textContent = `Exchange Rate for ${currencyPair}: ${rate}`;
        } else {
            exchangeRateResult.textContent = 'Error fetching exchange rate data.';
        }
    } catch (error) {
        exchangeRateResult.textContent = 'An error occurred.';
    }
});

