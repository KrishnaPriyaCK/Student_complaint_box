
function validatePhoneNumber() {
    var phoneNumber = document.getElementById('id_userphone').value;
    var phoneNumberPattern = /^[0-9]+$/;

    if (phoneNumber.length > 10 || !phoneNumber.match(phoneNumberPattern)) {
        alert('Please enter a valid phone number with 10 or fewer digits and no characters.');
        return false;
    }

    return true;
}

document.getElementById('request').onsubmit = function () 
{
    return validatePhoneNumber();
};
function validateName() {
    var name = document.getElementById('id_username').value;
    var namePattern = /^[a-zA-Z\s]*$/;

    if (name.trim() === '' || !name.match(namePattern)) {
        alert('Please enter a valid name with no special characters or numbers.');
        return false;
    }

    return true;
}

document.getElementById('request').onsubmit = function () 
{
    return validatePhoneNumber() && validateName();
};




function validateAcknowledgementForm() {

    var ackmesg = document.querySelector('input[name="ackmesg"]').value;


    if (ackmesg.trim() === '') {
        alert('Please enter an acknowledgment message.');
        return false;
    }

    return true;
}

document.getElementById('request').onsubmit = function () {
    return validateAcknowledgementForm();
};

