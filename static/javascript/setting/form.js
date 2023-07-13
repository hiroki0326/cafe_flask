// 編集ボタンをクリックするとボタンが消えて保存ボタンが現れる
function enableEdit(button) {
  var row = button.parentNode.parentNode;
  var nameSpan = row.querySelector('.name');
  var nameInput = row.querySelector('.name.edit-input');
  var ageSpan = row.querySelector('.age');
  var ageInput = row.querySelector('.age.edit-input');
  var emailSpan = row.querySelector('.email');
  var emailInput = row.querySelector('.email.edit-input');
  var reservationDateSpan = row.querySelector('.reservation_date');
  var reservationDateInput = row.querySelector('.reservation_date.edit-input');
  var reservationTimeSpan = row.querySelector('.reservation_time');
  var reservationTimeInput = row.querySelector('.reservation_time.edit-input');
  var editButton = row.querySelector('.edit-button');
  var submitButton = row.querySelector('.submit-button');
  var deleteButton = row.querySelector('.delete-button');

  row.classList.add('edit-mode');
  nameSpan.style.display = 'none';
  nameInput.style.display = 'inline-block';
  nameInput.readOnly = false;
  ageSpan.style.display = 'none';
  ageInput.style.display = 'inline-block';
  ageInput.readOnly = false;
  emailSpan.style.display = 'none';
  emailInput.style.display = 'inline-block';
  emailInput.readOnly = false;
  reservationDateSpan.style.display = 'none';
  reservationDateInput.style.display = 'inline-block';
  reservationDateInput.readOnly = false;
  reservationDateInput = row.querySelector('.reservation_date.edit-input');
  reservationTimeSpan.style.display = 'none';
  reservationTimeInput.style.display = 'inline-block';
  reservationTimeInput.readOnly = false;
  editButton.style.display = 'none';
  submitButton.style.display = 'inline-block';
  deleteButton.style.display = 'none';
}

// 新規ボタンをクリックするとボタンが消えてフォームが現れる
function enableNew() {
  var form = document.getElementById("form");
  if (form.style.display === "none") {
    form.style.display = "block";
    var button = document.getElementById("new-button");
    button.innerHTML = "閉じる";
  } else {
    form.style.display = "none";
    var button = document.getElementById("new-button");
    button.innerHTML = "新規作成";
  }
}

// 保存ボタン
function submitForm(button) {
  var form = button.parentNode.parentNode.parentNode;
  form.submit();
}

// 削除アラート表示
function confirmDelete(id, index) {
  switch (index) {
  case "user":
    if (confirm("本当に削除してもよろしいですか？")) {
      // 削除処理の実行
      window.location.href = "/setting/cafe/reservation/delete/" + id;
    }
  case "menu":
    if (confirm("本当に削除してもよろしいですか？")) {
      // 削除処理の実行
      window.location.href = "/setting/cafe/menu/delete/" + id;
    }
  }
}