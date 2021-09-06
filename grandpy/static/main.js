//SELECTORS

const submitButton = document.querySelector('#submit-button');
const inputField = document.querySelector('#input-text');
const ulContainer = document.querySelector('#items');


//LISTENERS
submitButton.addEventListener('click', getInput);


//FUNCTIONS
// phrase test : Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?
function getInput(event) {
    event.preventDefault();
    //Create li
    function addLiToUl(value) {
        let li = document.createElement('li');
        li.setAttribute('class', 'text-message')
        li.appendChild(document.createTextNode(value));
        ulContainer.appendChild(li);
    }
    //Select value of input field
    let inputValue = inputField.value;
    addLiToUl(inputValue);
    //Reseting the input field 
    document.querySelector('#my-form').reset();
    

    //Fetch to backend.
    if (inputValue !== '' && inputValue !== undefined) {
        fetch(`${window.origin}/process`, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(inputValue),
            cache: 'no-cache',
            headers: new Headers({ 'Content-Type': 'application/json'})
        })
        .then((response) => {
            if (response.status !== 200) {
                let rep = 'désolé je n\'ai pas compris'
                addLiToUl(rep)
                return ;
            }

        response.json().then((data) => {
                    backEndData = data   
                    console.log(data.google_response.lat)
                    
            })
        
        })
    }
    
    
}

