let checkbox_quest = document.querySelectorAll('.quest_label input:first-child')
let elementHidden = document.querySelectorAll('.more_info .hidden')

const checkbox_quest_size = checkbox_quest.length - 1

for(let i = 0; i <= checkbox_quest_size; i++){
    checkbox_quest[i].addEventListener('change', function(){
        let input = elementHidden[i].parentNode.querySelectorAll('input[type=text], input[type=number]')
        if(this.checked){
            elementHidden[i].removeAttribute('hidden')
        }else{
            input.forEach((value) => {
                value.value = ''
            })
            elementHidden[i].setAttribute('hidden', true)
        }
    })
}