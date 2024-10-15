// formValidation.js
const currentDate = new Date();

const patientName = document.getElementById('patientName');
const birthDate = document.getElementById('birthDate');
const attendance = document.getElementById('attendance');
const record = document.getElementById('record');
const internmentDate = document.getElementById('internmentDate');


const nameError = document.getElementById('nameError');
const birthDateError = document.getElementById('birthDateError');
const attendanceError = document.getElementById('attendanceError');
const recordError = document.getElementById('recordError');
const internmentDateError = document.getElementById('internmentDateError');
const birthInternmentDateError = document.getElementById('birthInternmentDateError');

function showError(element, message) {
    element.textContent = message;
    element.style.color = 'red';
}

function clearError(element) {
    element.textContent = '';
}

/*
    Validade Patient
*/

function validatePatientName() {
    const name = patientName.value.trim();
    if (name === '') {
        showError(nameError, 'Nome do paciente não pode ser vazio ou apenas espaços.');
        return false;
    } else {
        clearError(nameError);
        return true;
    }
}

function validateBirthDate() {
    const birthDateValue = new Date(birthDate.value);
    const minDate = new Date('1900-01-01');

    if (birthDateValue > currentDate) {
        showError(birthDateError, 'Data de nascimento não pode ser maior que a data atual.');
        return false;
    } else if (birthDateValue < minDate) {
        showError(birthDateError, 'Data de nascimento não pode ser menor que 1900.');
        return false;
    } else {
        clearError(birthDateError);
        return true;
    }
}

function validateAttendance() {
    const attendanceValue = attendance.value.trim();
    if (!/^\d{5,}$/.test(attendanceValue)) {
        showError(attendanceError, 'Atendimento deve conter apenas números e ter pelo menos 5 dígitos.');
        return false;
    } else {
        clearError(attendanceError);
        return true;
    }
}

function validateRecord() {
    const recordValue = record.value.trim();
    if (!/^\d{5,}$/.test(recordValue)) {
        showError(recordError, 'Registro deve conter apenas números e ter pelo menos 5 dígitos.');
        return false;
    } else {
        clearError(recordError);
        return true;
    }
}

function validateInternmentDate() {
    const internmentDateValue = new Date(internmentDate.value);
    const minDate = new Date('2000-01-01');

    if (internmentDateValue > currentDate) {
        showError(internmentDateError, 'Data de internação não pode ser maior que a data atual.');
        return false;
    } else if (internmentDateValue < minDate) {
        showError(internmentDateError, 'Data de internação não pode ser menor que 2000.');
        return false;
    } else {
        clearError(internmentDateError);
        return true;
    }
}

function validateBirthInternmentDate(){
    const birthDateValue = new Date(birthDate.value);
    const internmentDateValue = new Date(internmentDate.value);

    if (internmentDateValue < birthDateValue){
        showError(birthInternmentDateError, 'Data de internação não pode ser maior que a data de nascimento.');
        return false;
    } else {
        clearError(birthInternmentDateError);
        return true;
    }
}


/*
    Validate Ocurrence
*/

const ocurrenceDate = document.getElementById('ocurrenceDate');
const ocurrenceDateError = document.getElementById('ocurrenceDateError');
const validateOcurrenceDate = () => {
    const ocurrenceDateValue = new Date(ocurrenceDate.value);
    const minDate = new Date('2010-01-01');

    if (ocurrenceDate > ocurrenceDateValue ){
        showError(ocurrenceDateError, 'Data da ocorrência não pode ser maior que a data atual');
        return false;
    }else if(ocurrenceDate < minDate ){
        showError(ocurrenceDateError, `Data da ocorrência não pode ser menor que ${minDate}`);
        return false
    }else{
        clearError(ocurrenceDateError);
        return true;
    }

}



// Add event listeners in validation
export function attachPatientValidationHandlers() {
    // Patient
    patientName.addEventListener('input', validatePatientName);
    birthDate.addEventListener('blur', validateBirthDate);
    birthDate.addEventListener('blur', validateBirthInternmentDate);
    attendance.addEventListener('input', validateAttendance);
    record.addEventListener('input', validateRecord);
    internmentDate.addEventListener('blur', validateInternmentDate);
    internmentDate.addEventListener('blur', validateBirthInternmentDate);
}

// Remove event listeners in validation
export function removePatientValidationHandlers() {
    patientName.removeEventListener('input', validatePatientName);
    birthDate.removeEventListener('blur', validateBirthDate);
    birthDate.removeEventListener('blur', validateBirthInternmentDate);
    attendance.removeEventListener('input', validateAttendance);
    record.removeEventListener('input', validateRecord);
    internmentDate.removeEventListener('blur', validateInternmentDate);
    internmentDate.removeEventListener('blur', validateBirthInternmentDate);
}

//
export const attachOcurrenceValidationHandlers = () => {
    validateOcurrenceDate.addEventListener('blur', validateOcurrenceDate);
}