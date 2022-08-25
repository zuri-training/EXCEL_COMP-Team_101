const label = document.querySelector("label");
const fileChosenDisplay = document.querySelector("#file-chosen");
const uploadForm = document.querySelector("#upload_form");
const input_file = document.querySelector("#id_file_url");
const progress_bar = document.querySelector(".progress");
const error = document.querySelector(".error");
const continueBtn = document.querySelector(".continue");

function errorDisplay(value) {
  error.classList.add("show");
  error.textContent = value;

  setTimeout(function () {
    error.classList.remove("show");
  }, 2000);
}

function formSuccess(link) {
  input_file.disabled = true;
  label.style.background = "#aaa";
  uploadForm.reset();
  continueBtn.href = link;
  continueBtn.style.display = "inline-block";
}

$("#id_file_url").change(function (e) {
  e.preventDefault();

  $form = uploadForm;
  var formData = new FormData(uploadForm);

  const media_data = this.files[0];
  fileChosenDisplay.textContent = this.files[0].name;

  progress_bar.classList.add("not-visible");

  if (media_data != null) {
    if (media_data.size > 5242880) {
      errorDisplay("File cannot exceed 5mb");
    } else {
      if (
        media_data.type != "text/csv" &&
        media_data.type !=
          "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" &&
        media_data.type != "application/vnd.ms-excel"
      ) {
        errorDisplay("Allowed format is CSV, XLSX, XLS");
      } else {
        progress_bar.classList.remove("not-visible");

        $.ajax({
          type: "POST",
          url: " /members/ff/",
          data: formData,
          dataType: "json",
          beforeSend: function () {},
          xhr: function () {
            const xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener("progress", (e) => {
              if (e.lengthComputable) {
                const percentProgress = Math.round((e.loaded / e.total) * 100);
                console.log(percentProgress);
                progress_bar.innerHTML = `<div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: ${percentProgress}%" aria-valuenow="${percentProgress}" aria-valuemin="0" aria-valuemax="100">${percentProgress}%</div>`;
              }
            });
            return xhr;
          },
          success: function (response) {
            formSuccess(`/members/file/${response.data}`);
          },
          error: function (err) {
            console.log(err);
          },
          cache: false,
          contentType: false,
          processData: false,
        });
      }
    }
  }
});
