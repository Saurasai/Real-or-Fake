async function classifyContent() {
    const content = document.getElementById('content').value;
    if (!content) {
        alert("Please enter some content to classify.");
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/classify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content })
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('category').innerText = data.category;
        document.getElementById('confidence').innerText = (data.confidence * 100).toFixed(2) + '%';
        document.getElementById('result').style.display = 'block';
    } else {
        alert("Error: " + response.statusText);
    }
}
