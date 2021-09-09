//SELECTORS

const submitButton = document.querySelector('#submit-button');
const inputField = document.querySelector('#input-text');
const chatBoxContainer = document.querySelector('#inner-box');


//LISTENERS
submitButton.addEventListener('click', getInput);


//FUNCTIONS
// phrase test : Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?


function getInput(event) {
    event.preventDefault();
   
    //Create textbox card with text to the right.
    function createCardRight(data) {
        let divCardRight = document.createElement("div");
        divCardRight.setAttribute("class", 'card text-end');
        divCardRight.innerHTML = `<div class="card-body p-3 m-3"><h5 class="card-title">YOU</h5><p class="card-text">${data}</p></div>`
        chatBoxContainer.appendChild(divCardRight);
    }

    //Create textbox card with text to the left.
    function createCardLeft(data) {
        let divCardLeft = document.createElement('div');
        divCardLeft.setAttribute('class', 'card');
        divCardLeft.innerHTML = `<div class="card-body p-3 m-3"><h5 class="card-title">GrandPYBOT</h5><p>${data}</p></div>`
        chatBoxContainer.appendChild(divCardLeft);
    }

    function addDivforImg() {
        let divForMap = document.createElement('div');
        divForMap.setAttribute("class", 'card');
        divForMap.innerHTML = "<div id='map'></div>";
        chatBoxContainer.appendChild(divForMap);
    }
    //Select value of input field
    let inputValue = inputField.value;
    createCardRight(inputValue);
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
                let rep = 'désolé je n\'ai pas compris, essaye de me donner le pays ca peut m\'aider.'
                createCardLeft(rep)
                return ;
            }

        response.json().then((data) => {
                    
                    let lat = data.google_response.lat
                    let long = data.google_response.lng
                    addDivforImg();
                    map = new google.maps.Map(document.getElementById('map'), {
                        center: {lat:lat, lng:long},
                        zoom:16
                    })
                    const marker = new google.maps.Marker({
                        position: {lat:lat, lng:long},
                        map: map,
                    });
                    createCardLeft("voici l'adresse que tu m'as demandée :  " + data.google_response.address);
                    createCardLeft("D'ailleurs savais-tu que " + data.wiki_response.extract);
                    createCardLeft("Voici un lien sur ce lieu si tu veux en apprendre plus :  " + "<a href="+data.wiki_response.url_wikipedia+">Vers Wikipedia et au delà !</a>")
                    
                    
                    
                    
                    
                })
            })
        }
    }