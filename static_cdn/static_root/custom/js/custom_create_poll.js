var formfield = document.getElementById('formfield');

function addInput() {
    var input_tags = formfield.getElementsByTagName('input');
    if (input_tags.length > 6) {
        alert('حداکثر گزینه ها 6 عدد میباشد');
        return;
    }

    var newField = document.createElement('input');
    var newFieldName = input_tags.length + 1

    newField.setAttribute('type', 'text');
    newField.setAttribute('name', 'option_' + newFieldName);
    newField.setAttribute('placeholder', 'گزینه ' + newFieldName);
    newField.setAttribute('class', 'textinput textInput form-control');
    formfield.appendChild(newField);
}

function removeInput() {
    var input_tags = formfield.getElementsByTagName('input');
    if (input_tags.length > 3) {
        formfield.removeChild(input_tags[(input_tags.length) - 1]);
    }else {
        alert('حداقل گزینه ها 2 عدد میباشد')
    }
}