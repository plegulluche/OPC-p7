document.querySelector('#submit-button').addEventListener('click', getInput);
// phrase test : Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?
function getInput(event) {
    event.preventDefault();
    console.log('insidegetInput')

    let input = document.querySelector('#input-text').value;
    let ul = document.querySelector('#items');
    let li = document.createElement('li');
    li.appendChild(document.createTextNode(input));
    ul.appendChild(li);
    document.querySelector('#my-form').reset();
    console.log('ending getinput')

    const sentence = document.querySelector('li').textContent;

    if (sentence !== '' && sentence !== undefined) {
        fetch(`${window.origin}/process`, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(sentence),
            cache: 'no-cache',
            headers: new Headers({ 'Content-Type': 'application/json'})
        })
        .then((response) => {
            if (response.status !== 200) {
                let li2 = document.createElement('li');
                li2.appendChild(document.createTextNode('Désolé mais je n\'ai pas compris ta requète'));
                ul.appendChild(li2);
                console.log(`response status Not 200: ${response.status}`);
                return ;
            }
        response.json().then((data) => {
            const backData = JSON.stringify(data)
            console.log(backData);
            let li3 = document.createElement('li');
            li3.appendChild(document.createTextNode(backData));
            ul.appendChild(li3);
        })
        })
    }
       
}

