// import "./import/modules";
// import "./import/components";
// import "./import/inputMask";
// import "./import/script";

// new VenoBox({
//   selector: ".index-gallery__item"
// });

console.log("Работает");

/**
 * Функция отктия и закрытия строку поиска  и фильтрацию по убыванию/возрастанию
 * 
 * Оптимизировать код
 */

const openSearchBtn = document.getElementById('open-search');
if (openSearchBtn) {
  openSearchBtn.addEventListener('click', function (e) {
    this.classList.toggle('_active');
    document.getElementById('single-search').classList.toggle('_active');

    if (!this.classList.contains('_active')) {
      this.innerHTML = '<i class="fa-solid fa-magnifying-glass"></i>';
    } else {
      this.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    }
  })
}

const openFilterBtn = document.getElementById('open-filter');
if (openFilterBtn) {
  openFilterBtn.addEventListener('click', function (e) {
    this.classList.toggle('_active');
    document.getElementById('filter-sort').classList.toggle('_active');

    if (!this.classList.contains('_active')) {
      this.innerHTML = '<i class="fa-solid fa-sliders"></i>';
    } else {
      this.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    }
  })
}

/**
 * Фильтр по цене 
 * 
 * Разобраться в скрипке 
 */

const rangeInput = document.querySelectorAll(".price-input__range input");
const priceInputField = document.querySelectorAll(".price-input__field input");
const progress = document.querySelector('#prodgress');
const priceGap = 1000;


if (rangeInput) {
  rangeInput.forEach(input => {
    input.addEventListener('input', (e) => {
      const minValue = parseInt(rangeInput[0].value);
      const maxValue = parseInt(rangeInput[1].value);

      if (maxValue - minValue < priceGap) {
        if (e.target.className === "price-input__range-min") {
          rangeInput[0].value = maxValue - priceGap;
        } else {
          rangeInput[1].value = minValue + priceGap;
        }
      } else {
        priceInputField[0].value = minValue;
        priceInputField[1].value = maxValue;
        progress.style.left = (minValue / rangeInput[0].max) * 100 + "%";
        progress.style.right = 100 - (maxValue / rangeInput[1].max) * 100 + "%";
      }


    })

  })
}


/**
 * Рейтинг в виде звездочек
 */

const ratingItemList = document.querySelectorAll('.form__star');
const inputSaveRating = document.querySelector('#form-reviews__rating');
if (ratingItemList) {
  const ratingItemArray = Array.prototype.slice.call(ratingItemList);

  ratingItemArray.forEach(item => {
    item.addEventListener('click', function (e) {
      const { rating } = item.dataset;
      item.parentNode.dataset.ratingTotal = rating;
      // inputSaveRating.value = rating;
    })
  })
}

/**
 * Просмотр полного описания продукта
 */

const btnViewProduct = document.querySelectorAll('.product-desc');
if (btnViewProduct) {
  btnViewProduct.forEach(btn => btn.addEventListener('click', viewProduct));
}

function viewProduct(e) {
  let parentNodeHtml = this.closest('.card-product').querySelector('.card-product__info').innerHTML;
  let popupView = document.querySelector('.popup-view .popup__grid');
  console.log(popupView);

  if (popupView) {
    popupView.innerHTML = parentNodeHtml;
  }
}

const orderBtn = document.querySelectorAll('.filter-sort__value');

orderBtn.forEach(btn => {
  btn.addEventListener('click', function (e) {
    // e.preventDefault();
  })
})

const regNum = document.querySelectorAll('.reg-num');
if (regNum) {
  regNum.forEach(num => {
    phoneNumber = num.href.replace('tel:', '');
    newNumber = clearSimvol(phoneNumber.replace('8', "+7"));
    num.href = `tel:${newNumber}`;
  });
}
function clearSimvol(str) {
  return str.replace(/[\s.,%,),(,-]/g, '');
}


// Функция для сохранения выбранного филиала в localStorage
function saveSelectedBranch(branchId) {
  localStorage.setItem("selectedBranch", branchId);
}

// Функция для получения выбранного филиала из localStorage
function getSelectedBranch() {
  return localStorage.getItem("selectedBranch");
}

document.addEventListener('DOMContentLoaded', function () {
  const branchSelect = document.getElementById('branch-select');

  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Получаем CSRF токен

  const selectedBranch = getSelectedBranch();
  if (selectedBranch) {
    branchSelect.value = selectedBranch;

    fetch('/get_product/', {
      method: 'POST',
      body: JSON.stringify({ branch_id: selectedBranch }),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken // Добавляем CSRF токен к запросу
      }
    })
      .then(response => response.text())
      .then(data => {
        document.getElementById('product').innerHTML = data;
      });
  }

  branchSelect.addEventListener('change', function () {
    saveSelectedBranch(this.value);

    fetch('/get_product/', {
      method: 'POST',
      body: JSON.stringify({ branch_id: this.value }),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      }
    })
      .then(response => response.text())
      .then(data => {
        document.getElementById('product').innerHTML = data;
      });
  });
});