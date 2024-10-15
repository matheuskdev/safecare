// main.js
import { attachPatientValidationHandlers, removePatientValidationHandlers } from './formValidation.js';

document.addEventListener('DOMContentLoaded', function() {
    const extraFieldsContainer = document.getElementById('showPatient');
    const radioShowFields = document.getElementById('patient_yes');
    const radioHideFields = document.getElementById('patient_no');


    radioShowFields.addEventListener('change', function() {
        extraFieldsContainer.style.display = 'flex';
        attachPatientValidationHandlers();
    });

    radioHideFields.addEventListener('change', function() {
        extraFieldsContainer.style.display = 'none';
        removePatientValidationHandlers();
    });


    if (radioShowFields.checked) {
        extraFieldsContainer.style.display = 'flex';
        attachPatientValidationHandlers();
    } else {
        extraFieldsContainer.style.display = 'none';
    }
});
