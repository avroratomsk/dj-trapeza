// import "./import/modules";
// import "./import/components";
// import "./import/inputMask";
// import "./import/script";

// new VenoBox({
//   selector: ".index-gallery__item"
// });


// Вычисляем ширину scrolllbar

let widthScrollBar = window.innerWidth - document.documentElement.clientWidth;

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
      this.innerHTML = '<span class="label_mb">Категории</span><i class="fa-solid fa-sliders"></i>';
    } else {
      this.innerHTML = '<span class="label_mb">Категории</span><i class="fa-solid fa-xmark"></i>';
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

/**
 * Получние товаров из категории асинхронно
 */

const categoryLink = document.querySelectorAll('.category-link');

if (categoryLink) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Получаем CSRF токен
  categoryLink.forEach(btn => {
    btn.addEventListener('click', function (e) {
      categoryLink.forEach(item => item.classList.remove('_active'));
      btn.classList.add('_active');
      e.preventDefault();
      branch_slug = localStorage.getItem('branch');
      const categoryId = this.dataset.id;
      console.log(branch_slug, categoryId);
      fetch('/catalog/get_data/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ category_id: categoryId, branch_slug: branch_slug })
      })
        .then(response => response.json())
        .then(data => {
          let data_product = data.data
          if (document.getElementById('address')) {
            document.getElementById('address').innerText = data.branch[3]
          }
          if (document.getElementById('phone')) {
            document.getElementById('phone').innerText = data.branch[2]
          }
          if (document.getElementById('time-work')) {
            document.getElementById('time-work').innerText = data.branch[4]
          }
          if (document.getElementById('weekend')) {
            document.getElementById('weekend').innerText = data.branch[5]
          }
          if (document.getElementById('map')) {
            document.getElementById('map').innerHTML = data.branch[6]
          }

          if (Array.isArray(data_product)) {
            dataArray = Object.values(data_product)
            const productsContainer = document.getElementById('products-grid');
            productsContainer.classList.remove('no-grid');
            productsContainer.innerHTML = '';
            if (dataArray.length > 0) {
              dataArray.forEach(product => {
                const productElement = document.createElement('div');
                productElement.classList.add('tab__content-item', 'card-product')
                productElement.innerHTML = `
                      <a href="${product.url}" class="card-product__image">
                        <img src="${product.image}" alt="${product.name}" title="${product.name}" />
                      </a>
                      <a href="${product.url}" class="card-product__name">${product.name}</a>
                      <p class="card-product__price">${product.price} ₽</p>
                      <div class="card-product__btns">
                        <a href="${product.url}" class="card-product__btn">Подробнее</a>
                      </div>
                    `;
                productsContainer.appendChild(productElement);
              })
            } else {
              productsContainer.innerHTML = '<p class="empty">Для данной категории меню дня не заполнено, посмотрите следующие категории</p>';
              productsContainer.classList.add('no-grid');
            }
          } else {
            console.log("Не массив");
            const dataArray = Object.values(data_product);
            dataArray.forEach(product => {
              const productsContainer = document.getElementById('products-grid');
              productsContainer.classList.remove('no-grid');
              productsContainer.innerHTML = '';
              if (product.length > 0) {
                product.forEach(item => {
                  const productElement = document.createElement('div');
                  productElement.classList.add('tab__content-item', 'card-product')
                  productElement.innerHTML = `
                    <a href="${item.url}" class="card-product__image">
                      <img src="${item.image}" alt="${item.name}" title="${item.name}" />
                    </a>
                    <a href="${item.url}" class="card-product__name">${item.name}</a>
                    <p class="card-product__price">${item.price} ₽</p>
                    <div class="card-product__btns">
                      <a href="${item.url}" class="card-product__btn">Подробнее</a>
                    </div>
                  `;
                  productsContainer.appendChild(productElement);
                })
              } else {
                productsContainer.innerHTML = '<p class="empty">Для данной категории меню дня не заполнено, посмотрите следующие категории</p>';
                productsContainer.classList.add('no-grid');
              }
            });
          }
        })
        .catch(error => console.error('Error', error))
    })
  })
}

function changeInfo() { }

document.addEventListener('DOMContentLoaded', function () {
  if (localStorage.getItem('branch')) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Получаем CSRF токен
    branch_slug = localStorage.getItem('branch')
    // console.log(branch_slug);
    const categoryId = 1;
    fetch('/catalog/get_data/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      body: JSON.stringify({ category_id: categoryId, branch_slug: branch_slug })
    })
      .then(response => response.json())
      .then(data => {
        let data_product = data.data
        if (document.getElementById('address')) {
          document.getElementById('address').innerText = data.branch[3]
        }
        if (document.getElementById('phone')) {
          document.getElementById('phone').innerText = data.branch[2]
        }
        if (document.getElementById('time-work')) {
          document.getElementById('time-work').innerText = data.branch[4]
        }
        if (document.getElementById('weekend')) {
          document.getElementById('weekend').innerText = data.branch[5]
        }
        if (document.getElementById('map')) {
          document.getElementById('map').innerHTML = data.branch[6]
        }

        if (Array.isArray(data_product)) {
          dataArray = Object.values(data_product)
          const productsContainer = document.getElementById('products-grid');
          if (productsContainer) {
            productsContainer.classList.remove('no-grid');
            productsContainer.innerHTML = '';
          }
          if (dataArray.length > 0) {
            dataArray.forEach(product => {
              const productElement = document.createElement('div');
              productElement.classList.add('tab__content-item', 'card-product')
              productElement.innerHTML = `
                    <a href="${product.url}" class="card-product__image">
                      <img src="${product.image}" alt="${product.name}" title="${product.name}" />
                    </a>
                    <a href="${product.url}" class="card-product__name">${product.name}</a>
                    <p class="card-product__price">${product.price} ₽</p>
                    <div class="card-product__btns">
                      <a href="${product.url}" class="card-product__btn">Подробнее</a>
                    </div>
                  `;
              productsContainer.appendChild(productElement);
            })
          } else {
            if (productsContainer) {
              productsContainer.innerHTML = '<p class="empty">Для данной категории меню дня не заполнено, посмотрите следующие категории</p>';
              productsContainer.classList.add('no-grid');
            }
          }
        } else {
          console.log("Не массив");
          const dataArray = Object.values(data_product);
          dataArray.forEach(product => {
            const productsContainer = document.getElementById('products-grid');
            productsContainer.classList.remove('no-grid');
            productsContainer.innerHTML = '';
            if (product.length > 0) {
              product.forEach(item => {
                const productElement = document.createElement('div');
                productElement.classList.add('tab__content-item', 'card-product')
                productElement.innerHTML = `
                  <a href="${item.url}" class="card-product__image">
                    <img src="${item.image}" alt="${item.name}" title="${item.name}" />
                  </a>
                  <a href="${item.url}" class="card-product__name">${item.name}</a>
                  <p class="card-product__price">${item.price} ₽</p>
                  <div class="card-product__btns">
                    <a href="${item.url}" class="card-product__btn">Подробнее</a>
                  </div>
                `;
                productsContainer.appendChild(productElement);
              })
            } else {
              productsContainer.innerHTML = '<p class="empty">Для данной категории меню дня не заполнено, посмотрите следующие категории</p>';
              productsContainer.classList.add('no-grid');
            }
          });
        }
      })
      .catch(error => console.error('Error', error))
  } else {
    setInterval(openPopupSetFilial, 0)
    lockScroll(widthScrollBar)
    unLockScroll()
  }
})

function openPopupSetFilial() {
  document.documentElement.classList.add('_lock');
  document.getElementById('popup-delivery').classList.add('_show');
  lockScroll(widthScrollBar);
  const branchSelectionBtn = document.querySelectorAll('.form__btn-branch')
  if (branchSelectionBtn) {
    branchSelectionBtn.forEach(btn => {
      btn.addEventListener('click', getProduct)
      console.log('Тут2');
    })
  }
}

function getProduct(e) {
  let branch_slug = e.target.dataset.slug
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Получаем CSRF токен
  e.preventDefault();
  localStorage.setItem('branch', branch_slug)
  const categoryId = 1;
  console.log('Тут3');
  fetch('/catalog/get_data/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({ category_id: categoryId, branch_slug: branch_slug })
  })
    .then(response => response.json())
    .then(data => {
      console.log(`${data}----------------------`);
    })
    .catch(error => console.error('Error', error))

}

const closePopupBtns = document.querySelectorAll('.popup__close');

if (closePopupBtns) {
  closePopupBtns.forEach(btn => {
    btn.addEventListener('click', function (e) {
      console.log(btn);
      parent = btn.closest('.popup');
      console.log(parent);
      if (parent) {
        parent.classList.remove('_show');
        document.documentElement.classList.remove('_lock');
      }
    })
  })
}

function lockScroll(widthScrollBar) {
  document.documentElement.classList.add('_lock');
  document.documentElement.style.paddingRight = widthScrollBar + 'px';
}

function unLockScroll() {
  document.documentElement.classList.remove('_lock');
  document.documentElement.style.paddingRight = '0px';
}

const branchSelectionBtn = document.querySelectorAll('.change-filial');

if (branchSelectionBtn) {
  branchSelectionBtn.forEach(btn => {
    btn.addEventListener('click', (e) => {
      unLockScroll();
      document.getElementById('popup-delivery').classList.remove('_show');
    })
  })
}


const indexBlogTabTigger = document.querySelectorAll('.index-blog__tigger');
if (indexBlogTabTigger) {
  indexBlogTabTigger.forEach(btn => {
    btn.addEventListener('click', showTab)
  })
}

function showTab(e) {
  indexBlogTabTigger.forEach(item => item.classList.remove('_active'))
  document.querySelectorAll('.index-blog__grid').forEach(item => item.classList.remove('_active'));

  this.classList.add('_active');

  tabContent = document.getElementById(this.dataset.id);
  tabContent.classList.add('_active');

}

/**
 * Всплывающие окна
 */

const popupBtn = document.querySelectorAll('[data-popup]')
if (popupBtn) {
  popupBtn.forEach(btn => {
    btn.addEventListener('click', openPopup)
  })
}

function openPopup(e) {
  popup = document.getElementById(this.dataset.popup)

  popup.classList.add('_show');
  document.documentElement.classList.add('_lock');
}


/**
 * Рейтинг в виде звуздочек
 */

const ratingItemList = document.querySelectorAll('.form-reviews__star');
const inputSaveRating = document.querySelector('#form-reviews__rating');
if (ratingItemList) {
  const ratingItemArray = Array.prototype.slice.call(ratingItemList);

  ratingItemArray.forEach(item => {
    item.addEventListener('click', function (e) {
      const { rating } = item.dataset;
      item.parentNode.dataset.ratingTotal = rating;
      inputSaveRating.value = rating;
    })
  })
}