// main.js
import {
  attachPatientValidationHandlers,
  removePatientValidationHandlers,
} from "./formValidation.js";

import {
  attachOcurrenceValidationHandlers,
} from "./formOcurrenceValidation.js";

import { removeRequired } from "./formValidation.js"


document.addEventListener("DOMContentLoaded", function () {
  const extraFieldsContainer = document.getElementById("showPatient");
  const radioShowFields = document.getElementById("id_patient_involved_0");
  const radioHideFields = document.getElementById("id_patient_involved_1");


  radioShowFields.addEventListener("change", function () {
    extraFieldsContainer.style.display = "flex";
    attachPatientValidationHandlers();
  });

  radioHideFields.addEventListener("change", function () {
    extraFieldsContainer.style.display = "none";
    removePatientValidationHandlers();
  });

  if (radioShowFields.checked) {
    extraFieldsContainer.style.display = "flex";
    attachPatientValidationHandlers();
    attachOcurrenceValidationHandlers();
  } else {
    extraFieldsContainer.style.display = "none";
    attachOcurrenceValidationHandlers();
    removeRequired();
  }
});
