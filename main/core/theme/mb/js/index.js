let widthScrollBar = window.innerWidth - document.documentElement.clientWidth;

/**
 * Функция отктия и закрытия строку поиска  и фильтрацию по убыванию/возрастанию
 *
 * Оптимизировать код
 */

const openSearchBtn = document.getElementById("open-search");
if (openSearchBtn) {
    openSearchBtn.addEventListener("click", function (e) {
        this.classList.toggle("_active");
        document.getElementById("single-search").classList.toggle("_active");

        if (!this.classList.contains("_active")) {
            this.innerHTML = "<i class=\"fa-solid fa-magnifying-glass\"></i>";
        } else {
            this.innerHTML = "<i class=\"fa-solid fa-xmark\"></i>";
        }
    });
}

const openFilterBtn = document.getElementById("open-filter");
if (openFilterBtn) {
    openFilterBtn.addEventListener("click", function (e) {
        this.classList.toggle("_active");
        document.getElementById("filter-sort").classList.toggle("_active");

        if (!this.classList.contains("_active")) {
            this.innerHTML = "<span class=\"label_mb\">Категории</span><i class=\"fa-solid fa-sliders\"></i>";
        } else {
            this.innerHTML = "<span class=\"label_mb\">Категории</span><i class=\"fa-solid fa-xmark\"></i>";
        }
    });
}

/**
 * Фильтр по цене
 *
 * * Разобраться в скрипке
 */

const rangeInput = document.querySelectorAll(".price-input__range input");
const priceInputField = document.querySelectorAll(".price-input__field input");
const progress = document.querySelector("#prodgress");
const priceGap = 1000;


if (rangeInput) {
    rangeInput.forEach(input => {
        input.addEventListener("input", (e) => {
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

        });
    });
}

const orderBtn = document.querySelectorAll(".filter-sort__value");

orderBtn.forEach(btn => {
    btn.addEventListener("click", function () {
    });
});

const regNum = document.querySelectorAll(".reg-num");
if (regNum) {
    regNum.forEach(num => {
        const phoneNumber = num.href.replace("tel:", "");
        const newNumber = clearSimvol(phoneNumber.replace("8", "+7"));
        num.href = `tel:${newNumber}`;
    });
}

function clearSimvol(str) {
    return str.replace(/[\s.,%,),(,-]/g, "");
}

/**
 * Вспомогательные общие функции
 */

function bodyLock() {
    let widthScrollBar = window.innerWidth - document.documentElement.clientWidth;
    document.documentElement.style.marginRight = widthScrollBar + "px";
    document.documentElement.classList.add("_lock");
    document.querySelector(".header").style.paddingRight = widthScrollBar + "px";
}

function bodyUnLock() {
    document.documentElement.style.marginRight = "0px";
    document.querySelector(".header").style.paddingRight = "0px";
    document.documentElement.classList.remove("_lock");
}

/**
 * Получние товаров из категории асинхронно
 */

function getProductForBranch(categoryId, branchSlug) {
    const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
    fetch("/catalog/get_data/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({category_id: categoryId, branch_slug: branchSlug})
    })
        .then(response => response.json())
        .then(data => {
            let data_product = data.data;
            if (document.getElementById("address")) {
                document.getElementById("address").innerText = data.branch[3];
            }
            if (document.getElementById("phone")) {
                document.getElementById("phone").innerText = data.branch[2];
            }
            if (document.getElementById("time-work")) {
                document.getElementById("time-work").innerText = data.branch[4];
            }
            if (document.getElementById("weekend")) {
                document.getElementById("weekend").innerText = data.branch[5];
            }
            if (document.getElementById("map")) {
                document.getElementById("map").innerHTML = data.branch[6];
            }

            if (document.getElementById("footer-phone")) {
                document.getElementById("footer-phone").innerText = data.branch[2];
                console.log(data.branch[2]);
            }

            if (document.getElementById("header-phone")) {
                document.getElementById("header-phone").innerText = data.branch[2];
                console.log(data.branch[2]);
            }

            if (document.getElementById("footer-addres")) {
                document.getElementById("footer-addres").innerText = data.branch[3];
            }

            if (document.getElementById("footer-time-work")) {
                document.getElementById("footer-time-work").innerText = data.branch[4];
            }

            if (document.getElementById("footer-weekend")) {
                document.getElementById("footer-weekend").innerText = data.branch[5];
            }

            if (Array.isArray(data_product)) {
                const dataArray = Object.values(data_product);
                const productsContainer = document.getElementById("products-grid");
                if (productsContainer) {
                    productsContainer.classList.remove("no-grid");
                    productsContainer.innerHTML = "";
                    if (dataArray.length > 0) {
                        dataArray.forEach(product => {
                            let prodcut_price = product.price;
                            const productElement = document.createElement("div");
                            productElement.classList.add("tab__content-item", "card-product");
                            productElement.innerHTML =
                `<a href="${product.url}" class="card-product__image">
                <img src="${product.image}" alt="${product.name}" title="${product.name}" />
                <a href="${product.url}" class="card-product__name">${product.name}</a>
      
                <div class="card-product__info">
                  <p class="card-product__weight">${product.weight} гр.</p>
                  <div class="card-product__line"></div>
                  <p class="card-product__price">${prodcut_price} ₽</p>
                </div>
                <div class="card-product__info">
                  <p class="card-product__weight">${product.weight_two} гр.</p>
                  <div class="card-product__line"></div>
                  <p class="card-product__price">${product.price_two} ₽</p>
                </div>
                <div class="card-product__btns">
                  <a href="${product.url}" class="card-product__btn">Описание</a>
                </div>
                  `;
                            productsContainer.appendChild(productElement);
                        });
                    } else {
                        if (productsContainer) {
                            productsContainer.innerHTML = "<p class=\"empty\">Для данной категории меню дня не заполнено, посмотрите следующие категории</p>";
                            productsContainer.classList.add("no-grid");
                        }
                    }
                }
            }
        })
        .catch(error => console.error("Error", error));
}

function getProductService(categoryId) {
    const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
    console.log(csrfToken);
    fetch("/service/get_data_service/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({category_id: categoryId})

    })
        .then(response => response.json())
        .then(data => {
            const dataArray = Object.values(data);
            const productsContainer = document.getElementById("service-menu");
            productsContainer.innerHTML = "";
            dataArray.forEach(item => {
                item.forEach(product => {
                    console.log(product);
                    const productElement = document.createElement("div");
                    productElement.classList.add("card-product");
                    productElement.innerHTML =
            `
              <div class="card-product__image">
                <img src="${product.image}" alt="${product.name}" title="${product.name}" />
              </div>
              <p class="card-product__name">${product.name}</p>
              <p class="card-product__weight">Цена: ${product.price}</p>
            `;
                    productsContainer.appendChild(productElement);
                    console.log(productsContainer);
                });
            });
        })
        .catch(error => console.error("Error", error));
}

const serviceLink = document.querySelectorAll(".service-link");
serviceLink?.forEach(btn => {
    btn.addEventListener("click", function () {
        serviceLink.forEach(item => item.classList.remove("_active"));
        btn.classList.add("_active");
        const categoryId = this.dataset.id;
        console.log(categoryId);
        getProductService(categoryId);
    });
});


const categoryLink = document.querySelectorAll(".category-link");

categoryLink?.forEach(btn => {
    btn.addEventListener("click", function (e) {
        categoryLink.forEach(item => item.classList.remove("_active"));
        btn.classList.add("_active");
        e.preventDefault();
        const branch_slug = localStorage.getItem("branch");
        const categoryId = this.dataset.id;
        getProductForBranch(categoryId, branch_slug);
    });
});


document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem("branch")) {
        const branch_slug = localStorage.getItem("branch");
        const categoryId = 1;
        getProductForBranch(categoryId, branch_slug);
        categoryLink.forEach(btn => {
            if (btn.dataset.name == "Супы" || btn.dataset.name == "Суп" || btn.dataset.name == "Первое" || btn.dataset.name == "Первые блюда") {
                btn.classList.add("_active");
            }
        });
    } else {
        let interval = setInterval(function () {
            openPopupSetFilial();
            clearInterval(interval);
            document.documentElement.classList.add("_lock");
            document.getElementById("popup-delivery").classList.add("_show");
            lockScroll(widthScrollBar);
        });
        lockScroll(widthScrollBar);
        unLockScroll();
    }
});

function openPopupSetFilial() {
}

const branchSelectionBtns = document.querySelectorAll(".form__btn-branch");

branchSelectionBtns?.forEach(btn => {
    btn.addEventListener("click", function (e) {
        getProduct(e);
        document.getElementById("popup-delivery").classList.remove("_show");
        document.documentElement.classList.remove("_lock");
    });
});

function getProduct(e) {
    let branch_slug = e.target.dataset.slug;
    e.preventDefault();
    document.getElementById("popup-delivery").classList.remove("_show");
    localStorage.setItem("branch", branch_slug);
    const categoryId = 1;
    getProductForBranch(categoryId, branch_slug);
}

const branchSelection = document.querySelector(".fillal__title");
branchSelection.addEventListener("click", function (e) {
    console.log(e.currentTarget);
    lockScroll();
    document.getElementById("popup-delivery").classList.add("_show");
});

const closePopupBtns = document.querySelectorAll(".popup__close");

if (closePopupBtns) {
    closePopupBtns.forEach(btn => {
        btn.addEventListener("click", function (e) {
            parent = btn.closest(".popup");
            if (parent) {
                bodyUnLock();
                parent.classList.remove("_show");
                document.documentElement.classList.remove("_lock");
            }
        });
    });
}

function lockScroll(widthScrollBar) {
    document.documentElement.classList.add("_lock");
    document.documentElement.style.paddingRight = widthScrollBar + "px";
}

function unLockScroll() {
    document.documentElement.classList.remove("_lock");
    document.documentElement.style.paddingRight = "0px";
}

const branchSelectionBtn = document.querySelectorAll(".change-filial");

if (branchSelectionBtn) {
    branchSelectionBtn.forEach(btn => {
        btn.addEventListener("click", (e) => {
            console.log("click");
            unLockScroll();
            document.getElementById("popup-delivery").classList.remove("_show");
        });
    });
}

const indexBlogTabTigger = document.querySelectorAll(".index-blog__tigger");
if (indexBlogTabTigger) {
    indexBlogTabTigger.forEach(btn => {
        btn.addEventListener("click", showTab);
    });
}

function showTab(e) {
    indexBlogTabTigger.forEach(item => item.classList.remove("_active"));
    document.querySelectorAll(".index-blog__grid").forEach(item => item.classList.remove("_active"));

    this.classList.add("_active");

    tabContent = document.getElementById(this.dataset.id);
    tabContent.classList.add("_active");

}

/**
 * Всплывающие окна
 */

const popupBtn = document.querySelectorAll("[data-popup]");
if (popupBtn) {
    popupBtn.forEach(btn => {
        btn.addEventListener("click", openPopup);
    });
}

function openPopup(e) {
    bodyLock();
    popup = document.getElementById(this.dataset.popup);
    popup.classList.add("_show");
    document.documentElement.classList.add("_lock");
}


/**
 * Рейтинг в виде звуздочек
 */

const ratingItemList = document.querySelectorAll(".form-reviews__star");
const inputSaveRating = document.querySelector("#form-reviews__rating");
if (ratingItemList) {
    const ratingItemArray = Array.prototype.slice.call(ratingItemList);

    ratingItemArray.forEach(item => {
        item.addEventListener("click", function (e) {
            const {rating} = item.dataset;
            item.parentNode.dataset.ratingTotal = rating;
            inputSaveRating.value = rating;
        });
    });
}


const reviewsButtons = document.querySelectorAll(".reviews__btn");
if (reviewsButtons) {
    reviewsButtons.forEach(btn => {
        btn.addEventListener("click", getReviewsText);
    });
}

function getReviewsText(e) {
    let previeousElement = this.previousElementSibling.innerText;
    console.log(previeousElement);
    const openPopup = document.querySelector("#popup-reviews");
    let popupContent = openPopup.querySelector(".popup__text");
    popupContent.innerText += previeousElement;
}

/**
 * Submenu мобильная версия сайта
 */

const navSubmenuBtn = document.querySelectorAll(".nav__submenu-btn");
if (navSubmenuBtn) {
    navSubmenuBtn.forEach(btn => {
        btn.addEventListener("click", function (e) {
            this.parentNode.classList.toggle("_show");
        });
    });
}

let burger = document.getElementById("burger");
if (burger) {
    burger.addEventListener("click", function (e) {
        console.log("click");
        console.log(e.target);
        this.classList.toggle("_active");
        document.querySelector(".nav").classList.toggle("_show");
    });
}

// Проверяем, установлены ли куки
if (!document.cookie.split("; ").find(row => row.startsWith("cookie_consent="))) {
    // Если куки не установлены, показываем уведомление
    document.getElementById("cookie-notice").style.display = "block";
}

// Обработчик для кнопки согласия
document.getElementById("accept-cookies").addEventListener("click", function() {
    console.log("click");
    // Устанавливаем куки на 1 год
    document.cookie = "cookie_consent=true; max-age=" + 60 * 60 * 24 * 365 + "; path=/";
    // Скрываем уведомление
    document.getElementById("cookie-notice").style.display = "none";
});


