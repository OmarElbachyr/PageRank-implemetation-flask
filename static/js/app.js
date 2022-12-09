/*
<div class="input-group mb-3">
  <span class="input-group-text">2</span>
  <input type="text" class="form-control" placeholder="osos">
</div>

*/



function produceInputs() {
    const input = document.getElementById('inputs-number');
    let inputsNumber = input.value;
    removeInputs()
    console.log(inputsNumber)
    if (inputsNumber > 0) {

        for (let i = 1; i <= inputsNumber; i++) {
            let li = document.createElement('li');
            let div = document.createElement('div');
            let span = document.createElement('span');
            let input = document.createElement('input');
            // let page = document.createElement('label');



            div.setAttribute('class', 'input-group mb-3');
            span.setAttribute('class', 'input-group-text');

            input.setAttribute('type', 'text');
            input.setAttribute('class', 'form-control');
            input.setAttribute('placeholder', '1-2... or leave it blank');
            input.setAttribute('name', 'sources-' + i);
            // {#inputDiv.setAttribute('class', 'input-div')#}

            div.appendChild(span).innerText = i;
            div.appendChild(input);

            li.appendChild(div);



            document.getElementById('wrapper').appendChild(li);
            //document.getElementById('container').appendChild(e)
            // {#document.getElementsByClassName('inputs-div')[0].appendChild(page).innerText = i;#}

            // {#document.getElementsByClassName('inputs-div')[0].appendChild(document.createElement('br'))#}
        }

        let li = document.createElement('li');
        let button = document.createElement('button');

        button.setAttribute('type', 'submit');
        button.setAttribute('class', 'btn btn-primary btn-sm m-1');

        li.appendChild(button).innerText = 'Get';


        document.getElementById('wrapper').appendChild(li)
    }
    else if (inputsNumber == 0) {
        alert('Please enter a number!')
    }
    else {
        alert('Enter positive numbers only!')
    }

}

function removeInputs() {
    // {#const inputs = document.querySelector('.inputs-div').childNodes#}
    const inputs = document.getElementById('wrapper').childNodes;
    document.getElementById('inputs-number').value = '';

    console.log(inputs.length);

    for (let i = inputs.length - 1; i >= 0; i--) {
        let item = inputs[i];
        item.remove();
    }

}