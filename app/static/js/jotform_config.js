JotForm.newDefaultTheme = true;
JotForm.extendsNewTheme = false;
JotForm.singleProduct = false;
JotForm.newPaymentUIForNewCreatedForms = false;
JotForm.texts = {
  confirmEmail: "E-mail does not match",
  pleaseWait: "Please wait...",
  validateEmail: "You need to validate this e-mail",
  confirmClearForm: "Are you sure you want to clear the form",
  lessThan: "Your score should be less than or equal to",
  incompleteFields:
    "There are incomplete required fields. Please complete them.",
  required: "This field is required.",
  requireOne: "At least one field required.",
  requireEveryRow: "Every row is required.",
  requireEveryCell: "Every cell is required.",
  email: "Enter a valid e-mail address",
  alphabetic: "This field can only contain letters",
  numeric: "This field can only contain numeric values",
  alphanumeric: "This field can only contain letters and numbers.",
  cyrillic: "This field can only contain cyrillic characters",
  url: "This field can only contain a valid URL",
  currency: "This field can only contain currency values.",
  fillMask: "Field value must fill mask.",
  uploadExtensions: "You can only upload following files:",
  noUploadExtensions:
    "File has no extension file type (e.g. .txt, .png, .jpeg)",
  uploadFilesize: "File size cannot be bigger than:",
  uploadFilesizemin: "File size cannot be smaller than:",
  gradingScoreError: "Score total should only be less than or equal to",
  inputCarretErrorA: "Input should not be less than the minimum value:",
  inputCarretErrorB: "Input should not be greater than the maximum value:",
  maxDigitsError: "The maximum digits allowed is",
  minCharactersError:
    "The number of characters should not be less than the minimum value:",
  maxCharactersError:
    "The number of characters should not be more than the maximum value:",
  freeEmailError: "Free email accounts are not allowed",
  minSelectionsError: "The minimum required number of selections is ",
  maxSelectionsError: "The maximum number of selections allowed is ",
  pastDatesDisallowed: "Date must not be in the past.",
  dateLimited: "This date is unavailable.",
  dateInvalid: "This date is not valid. The date format is {format}",
  dateInvalidSeparate: "This date is not valid. Enter a valid {element}.",
  ageVerificationError:
    "You must be older than {minAge} years old to submit this form.",
  multipleFileUploads_typeError:
    "{file} has invalid extension. Only {extensions} are allowed.",
  multipleFileUploads_sizeError:
    "{file} is too large, maximum file size is {sizeLimit}.",
  multipleFileUploads_minSizeError:
    "{file} is too small, minimum file size is {minSizeLimit}.",
  multipleFileUploads_emptyError:
    "{file} is empty, please select files again without it.",
  multipleFileUploads_uploadFailed:
    "File upload failed, please remove it and upload the file again.",
  multipleFileUploads_onLeave:
    "The files are being uploaded, if you leave now the upload will be cancelled.",
  multipleFileUploads_fileLimitError: "Only {fileLimit} file uploads allowed.",
  dragAndDropFilesHere_infoMessage: "Drag and drop files here",
  chooseAFile_infoMessage: "Choose a file",
  maxFileSize_infoMessage: "Max. file size",
  generalError:
    "There are errors on the form. Please fix them before continuing.",
  generalPageError:
    "There are errors on this page. Please fix them before continuing.",
  wordLimitError: "Too many words. The limit is",
  wordMinLimitError: "Too few words.  The minimum is",
  characterLimitError: "Too many Characters.  The limit is",
  characterMinLimitError: "Too few characters. The minimum is",
  ccInvalidNumber: "Credit Card Number is invalid.",
  ccInvalidCVC: "CVC number is invalid.",
  ccInvalidExpireDate: "Expire date is invalid.",
  ccInvalidExpireMonth: "Expiration month is invalid.",
  ccInvalidExpireYear: "Expiration year is invalid.",
  ccMissingDetails: "Please fill up the credit card details.",
  ccMissingProduct: "Please select at least one product.",
  ccMissingDonation: "Please enter numeric values for donation amount.",
  disallowDecimals: "Please enter a whole number.",
  restrictedDomain: "This domain is not allowed",
  ccDonationMinLimitError: "Minimum amount is {minAmount} {currency}",
  requiredLegend: "All fields marked with * are required and must be filled.",
  geoPermissionTitle: "Permission Denied",
  geoPermissionDesc: "Check your browser's privacy settings.",
  geoNotAvailableTitle: "Position Unavailable",
  geoNotAvailableDesc:
    "Location provider not available. Please enter the address manually.",
  geoTimeoutTitle: "Timeout",
  geoTimeoutDesc: "Please check your internet connection and try again.",
  selectedTime: "Selected Time",
  formerSelectedTime: "Former Time",
  cancelAppointment: "Cancel Appointment",
  cancelSelection: "Cancel Selection",
  noSlotsAvailable: "No slots available",
  slotUnavailable:
    "{time} on {date} has been selected is unavailable. Please select another slot.",
  multipleError:
    "There are {count} errors on this page. Please correct them before moving on.",
  oneError:
    "There is {count} error on this page. Please correct it before moving on.",
  doneMessage: "Well done! All errors are fixed.",
  doneButton: "Done",
  reviewSubmitText: "Review and Submit",
  nextButtonText: "Next",
  prevButtonText: "Previous",
  seeErrorsButton: "See Errors",
  notEnoughStock: "Not enough stock for the current selection",
  notEnoughStock_remainedItems:
    "Not enough stock for the current selection ({count} items left)",
  soldOut: "Sold Out",
  justSoldOut: "Just Sold Out",
  selectionSoldOut: "Selection Sold Out",
  subProductItemsLeft: "({count} items left)",
  startButtonText: "START",
  submitButtonText: "Submit",
  submissionLimit:
    "Sorry! Only one entry is allowed. Multiple submissions are disabled for this form.",
  reviewBackText: "Back to Form",
  seeAllText: "See All",
  progressMiddleText: "of",
  fieldError: "field has an error.",
  error: "Error",
};
JotForm.newPaymentUI = true;
JotForm.replaceTagTest = true;
JotForm.submitError = "jumpToFirstError";
window.addEventListener("DOMContentLoaded", function () {
  window.brandingFooter.init({
    formID: 233635142103444,
    campaign: "powered_by_jotform_le",
    isCardForm: false,
    isLegacyForm: true,
  });
});
try {
  var isEUDomain = /(?:eu.jotform)|(?:jotformeu.com)/.test(
    window.location.host
  );
  var isHipaaDomain = /(?:hipaa.jotform)/.test(window.location.host);
  var isProhibitedParameterExists =
    /(?:wfTaskID|PCI_preSubmitRequest|wfTaskType)/.test(window.location.search);
  var isEditMode = JotForm.isEditMode();
  if (
    !isEUDomain &&
    !isHipaaDomain &&
    !isProhibitedParameterExists &&
    !isEditMode
  ) {
    var sesApiUrl = /jotform.pro/.test(window.location.host)
      ? "/API"
      : "https://api.jotform.com";
    function sendOpenId(uuid, eventType) {
      navigator.sendBeacon(
        sesApiUrl +
          "/form/" +
          233635142103444 +
          "/event/" +
          uuid +
          "/" +
          eventType,
        {}
      );
    }
    var formOpenId = "";
    if (window.crypto) {
      formOpenId = window.crypto
        .getRandomValues(new BigUint64Array(1))
        .toString();
    } else {
      formOpenId = (Math.random() * 16).toString(16).slice(2);
    }
    sendOpenId = sendOpenId.bind(this, formOpenId);
    function sendOpenIdOnSubmit() {
      var currentForm = $("233635142103444");
      currentForm.addEventListener("submit", function () {
        sendOpenId("clientSubmitClick_V5");
      });
      var openIdInput = currentForm.querySelector('[name="formOpenId_V5"]');
      if (!openIdInput) {
        openIdInput = document.createElement("input");
        openIdInput.setAttribute("type", "hidden");
        openIdInput.setAttribute("name", "formOpenId_V5");
        currentForm.appendChild(openIdInput);
      }
      openIdInput.value = formOpenId;
    }
    sendOpenId("clientFormView_V5");
    if (
      document.readyState == "complete" ||
      (this.jsForm &&
        (document.readyState === undefined ||
          document.readyState === "interactive"))
    ) {
      sendOpenIdOnSubmit();
    } else {
      document.ready(sendOpenIdOnSubmit);
    }
  }
} catch (openIdBlockError) {
  console.log(openIdBlockError);
}

JotForm.init(function () {
  /*INIT-START*/
  if (typeof $("input_80").spinner !== "undefined") {
    $("input_80").spinner({
      imgPath: "https://cdn.jotfor.ms/images/",
      width: "310",
      maxValue: "30",
      minValue: "0",
      allowNegative: false,
      addAmount: 1,
      value: "0",
    });
  }
  $("input_80").up(2).setAttribute("tabindex", "");
  if (typeof $("input_87").spinner !== "undefined") {
    $("input_87").spinner({
      imgPath: "https://cdn.jotfor.ms/images/",
      width: "310",
      maxValue: "30",
      minValue: "0",
      allowNegative: false,
      addAmount: 1,
      value: "0",
    });
  }
  $("input_87").up(2).setAttribute("tabindex", "");
  /*INIT-END*/
});
setTimeout(function () {
  JotForm.paymentExtrasOnTheFly([
    null,
    {
      name: "clickTo",
      qid: "1",
      text: "Diabetes Health Prediction",
      type: "control_head",
    },
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    {
      description: "",
      name: "Age",
      qid: "20",
      text: "What is your age range?",
      type: "control_radio",
    },
    {
      description: "",
      name: "Income",
      qid: "21",
      text: "What is your annual income range?",
      type: "control_radio",
    },
    null,
    null,
    null,
    {
      description: "",
      name: "HighBP",
      qid: "25",
      text: "Do you have high blood pressure?",
      type: "control_radio",
    },
    {
      description: "",
      name: "GenHlth",
      qid: "26",
      text: "Would you say that in general your health is",
      type: "control_scale",
    },
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    {
      description: "",
      name: "EmailAddress",
      qid: "48",
      subLabel: "example@example.com",
      text: "Please share your email address",
      type: "control_email",
    },
    null,
    null,
    null,
    null,
    null,
    null,
    { name: "input55", qid: "55", text: "提交", type: "control_button" },
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    {
      description: "",
      name: "HighChol",
      qid: "67",
      text: "Do you have high cholesterol?",
      type: "control_radio",
    },
    {
      description: "",
      name: "CholCheck",
      qid: "68",
      text: "Have you had a cholesterol check in the last 5 years?",
      type: "control_radio",
    },
    null,
    {
      description: "",
      name: "Smoker",
      qid: "70",
      text: "Have you smoked at least 100 cigarettes in your entire life?",
      type: "control_radio",
    },
    {
      description: "",
      name: "Stroke",
      qid: "71",
      text: "Have you ever had a stroke?",
      type: "control_radio",
    },
    {
      description: "",
      name: "HeartDiseaseorAttack",
      qid: "72",
      text: "Do you have coronary artery disease or have you experienced a heart attack?",
      type: "control_radio",
    },
    {
      description: "",
      name: "PhysActivity",
      qid: "73",
      text: "Have you engaged in physical activity (excluding work) in the past 30 days?",
      type: "control_radio",
    },
    {
      description: "",
      name: "Fruits",
      qid: "74",
      text: "Do you consume at least one fruit daily?",
      type: "control_radio",
    },
    {
      description: "",
      name: "Veggies",
      qid: "75",
      text: "Do you consume at least one serving of vegetables daily?",
      type: "control_radio",
    },
    {
      description: "",
      name: "AnyHealthcare",
      qid: "76",
      text: "Do you have healthcare insurance?",
      type: "control_radio",
    },
    {
      description: "",
      name: "NoDocbcCost",
      qid: "77",
      text: "Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?",
      type: "control_radio",
    },
    null,
    null,
    {
      description: "",
      name: "MentHlth",
      qid: "80",
      subLabel: "",
      text: "Now thinking about your mental health, which includes stress, depression, and problems with emotions, for  how many days during the past 30 days was your mental health not good? It is in days, scale will be between 0-30",
      type: "control_spinner",
    },
    {
      description: "",
      name: "DiffWalk",
      qid: "81",
      text: "Do you have serious difficulty walking or climbing stairs?",
      type: "control_radio",
    },
    null,
    {
      description: "",
      name: "Sex",
      qid: "83",
      text: "What is your gender?",
      type: "control_radio",
    },
    null,
    {
      description: "",
      name: "Education",
      qid: "85",
      text: "Please select your highest level of education",
      type: "control_radio",
    },
    {
      description: "",
      name: "HvyAlcoholConsump",
      qid: "86",
      text: "Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)",
      type: "control_radio",
    },
    {
      description: "",
      name: "PhysHlth",
      qid: "87",
      subLabel: "",
      text: "Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? It is in days, scale will be between 0-30",
      type: "control_spinner",
    },
    null,
    {
      name: "generalHealth",
      qid: "89",
      text: "General Health",
      type: "control_head",
    },
    {
      name: "mentalHealth",
      qid: "90",
      text: "Mental Health",
      type: "control_head",
    },
    {
      name: "physicalHealth",
      qid: "91",
      text: "Physical Health",
      type: "control_head",
    },
    null,
    null,
    {
      description: "",
      name: "BMI",
      qid: "94",
      subLabel:
        "BMI = kg\u002Fm² where kg is a person’s weight in kilograms and m² is their height in meters squared.",
      text: "Your Body Mass Index (BMI)",
      type: "control_number",
    },
    { name: "divider", qid: "95", text: "Divider", type: "control_divider" },
    { name: "divider96", qid: "96", text: "Divider", type: "control_divider" },
  ]);
}, 20);
