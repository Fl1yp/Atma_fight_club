let mask = document.querySelector(".mask");

window.addEventListener("DOMContentLoaded", () => {
    // Устанавливаем таймер на 3 секунды
    setTimeout(() => {
        mask.classList.add("hide"); // Скрываем лоадер
        setTimeout(() => {
            mask.remove(); // Удаляем лоадер из DOM

            // Модальное окно
            var delay_popup = 10000; // Задержка в миллисекундах
            setTimeout(function () {
                openModal(); // Открываем модальное окно
            }, delay_popup);

        }, 600); // Время, через которое лоадер будет удален
    }, 3000); // Таймер на 3 секунды
});

// Функция для открытия модального окна
function openModal() {
    document.getElementById('parent_popup').style.display = 'block';
    document.body.classList.add('no-scroll'); // Добавляем класс для блокировки прокрутки
}

// Функция для закрытия модального окна
function closeModal() {
    document.getElementById('parent_popup').style.display = 'none';
    document.body.classList.remove('no-scroll'); // Убираем класс для разблокировки прокрутки
}

document.querySelectorAll('.faq details').forEach((item) => {
    item.addEventListener('toggle', (event) => {
        if (event.target.open) {
            document.querySelectorAll('.faq details').forEach((otherItem) => {
                if (otherItem !== event.target) {
                    otherItem.removeAttribute('open');
                }
            });
        }
    });
});
