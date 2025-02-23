function removePrevResults() {
    const cont = document.getElementById("results")
    if (cont) {
        cont.remove()
    }
}
async function fetchWorkOrders(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            const errorMessage = `Failed to fetch tracker data: ${response.statusText}`;
            console.error(errorMessage);
            throw new Error(errorMessage);
        }
        return await response.json();
    } catch (error) {
        console.error("Error in fetchWorkOrders:", error);
        throw error;
    }
}

function addLoadingBox() {
    const loadingBox = document.createElement('div');
    Object.assign(loadingBox.style, {
        position: 'fixed',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        padding: '20px 40px',
        backgroundColor: 'rgba(0, 0, 0, 0.8)',
        color: '#fff',
        fontSize: '18px',
        borderRadius: '8px',
        zIndex: '1000'
    });
    loadingBox.textContent = 'Loading...';
    const container = document.querySelector("main") || document.body;
    container.appendChild(loadingBox);
    return loadingBox;
}


function displayData(data) {
    const itemsContainer = document.createElement("ul")
    itemsContainer.classList.add('list-group')
    itemsContainer.id = "results"

    JSON.parse(data.result).forEach(itemData => {
        const listItem = document.createElement("li");
        listItem.className = "list-group-item d-flex align-items-center";
        listItem.innerHTML = `
        <div class="d-flex w-100">
            <div class="flex-shrink-0">
                <img src="${itemData.Image}" alt="${itemData.title}" class="rounded border img-fluid" style="width: 80px; height: 80px; object-fit: cover;">
            </div>
            <div class="ms-3 flex-grow-1">
                <div class="d-flex justify-content-between">
                    <h5 class="mb-0">${itemData.title}</h5>
                    <p class="fw-bold text-primary">$${itemData["pricing.price"].toFixed(2)}</p>
                </div>
                <p class="text-muted small mt-2">${itemData.Store}</p>
            </div>
        </div>`;
        itemsContainer.appendChild(listItem);
    });

    document.querySelector("main").appendChild(itemsContainer)


}

async function submitSearch() {
    const loader = addLoadingBox();
    removePrevResults()
    const keyWordInput = document.getElementById("grocery-input").value;
    try {
        console.log("Searching for:", keyWordInput);
        const data = await fetchWorkOrders(`/search/${keyWordInput}`);
        displayData(data)
    } catch (error) {
        console.error("Error during search submission:", error);
    } finally {
        setTimeout(() => {
            loader.remove();
        }, 500);
    }
}
