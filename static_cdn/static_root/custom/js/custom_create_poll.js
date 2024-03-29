const container = document.getElementById('input-container');
var maxInputAllowed = 6;
var inputCount = 3;


function addInput() {
    inputCount++; // Increment input count by one
    if (inputCount > maxInputAllowed) {
        const btnAdd = document.getElementById('btn-add');
        btnAdd.remove();
        return;
    }
    let input = document.getElementById('id_option_' + inputCount);

    setAttributes(input, {'type':'text', 'class': 'textinput textInput form-control'});
}