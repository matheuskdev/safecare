// formValidation.js

const currentDate = new Date();

const ocurrenceDate = document.getElementById("id_ocurrence_date");
const ocurrenceTime = document.getElementById("id_ocurrence_time");
const descriptionOcurrence = document.getElementById("id_description_ocurrence");
const immediateAction = document.getElementById("id_immediate_action");

const ocurrenceDateError = document.getElementById("ocurrenceDateError");
const ocurrenceTimeError = document.getElementById("ocurrenceTimeError");
const descriptionOcurrenceError = document.getElementById("descriptionOcurrenceError");
const immediateActionError = document.getElementById("immediateActionError");


function showError(element, message) {
    element.textContent = message;
    element.style.color = "red";
}
  
  function clearError(element) {
    element.textContent = "";
}

/*
    Validate Ocurrence
*/

function validateOcurrenceDate() {
  const ocurrenceDateValue = new Date(ocurrenceDate.value + "T00:00:00");
  const minDate = new Date("2010-01-01");

  if (ocurrenceDateValue > currentDate) {
    showError(
      ocurrenceDateError,
      "Data da ocorrência não pode ser maior que a data atual"
    );
    return false;
  } else if (ocurrenceDate < minDate) {
    showError(
      ocurrenceDateError,
      `Data da ocorrência não pode ser menor que ${minDate}`
    );
    return false;
  } else {
    clearError(ocurrenceDateError);
    return true;
  }
}

function validateOcurrenceTime() {
  const ocurrenceDateValue = new Date(
    ocurrenceDate.value + "T00:00:00"
  ).toLocaleDateString("pt-BR", { timeZone: "America/Recife" });
  const ocurrenceTimeValue = ocurrenceTime.value;
  const currentTime = currentDate.toTimeString().slice(0, 5);
  const recifeCurrentTime = new Date().toLocaleDateString("pt-BR", {
    timeZone: "America/Recife",
  });

  if (ocurrenceDateValue === recifeCurrentTime) {
    if (ocurrenceTimeValue > currentTime) {
      showError(
        ocurrenceTimeError,
        "A hora da ocorrência não pode ser maior que a hora atual"
      );
      return false;
    } else {
      clearError(ocurrenceTimeError);
      return true;
    }
  }
}

function validateDescriptionOcurrence() {
    const descriptionOcurrenceValue = descriptionOcurrence.value.trim();
    if (descriptionOcurrenceValue === "") {
      showError(
        descriptionOcurrenceError,
        "Descrição da ocorrência não pode ser vazia ou apenas espaços."
      );
      return false;
    } else {
      clearError(descriptionOcurrenceError);
      return true;
    }
}

function validateimmediateAction() {
    const immediateActionValue = immediateAction.value.trim();
    if (immediateActionValue === "") {
      showError(
        immediateActionError,
        "Ação imediata não pode ser vazia ou apenas espaços."
      );
      return false;
    } else {
      clearError(immediateActionError);
      return true;
    }
}

// Add event listeners in validation
export function attachOcurrenceValidationHandlers() {
  ocurrenceDate.addEventListener("blur", validateOcurrenceDate);
  ocurrenceTime.addEventListener("blur", validateOcurrenceTime);
  descriptionOcurrence.addEventListener("input", validateDescriptionOcurrence);
  immediateAction.addEventListener("input", validateimmediateAction);
}
