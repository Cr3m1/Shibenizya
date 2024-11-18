import random

# Список слів для гри
# Це список слів, одне з яких випадковим чином буде обрано для гри
words = ['програміст', 'компютер', 'інтелект', 'мистецтво', 'робот', 'алгоритм']

# Функція для випадкового вибору слова з списку
def choose_word():
    return random.choice(words)

# Функція для відображення поточного стану слова
# Якщо літера вже була відгадана, вона буде показана, інакше - замість неї відображається "_"
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Основна функція гри "Шибениця"
def hangman():
    word = choose_word()  # Вибираємо випадкове слово
    guessed_letters = set()  # Множина для зберігання вже відгаданих літер
    attempts = 6  # Кількість спроб, які даються гравцю
    guessed = False  # Змінна для відстеження, чи слово повністю відгадано
    
    print("Ласкаво просимо до гри 'Шибениця'!")  # Привітання
    
    # Основний цикл гри, триває доки є спроби або слово не відгадане
    while attempts > 0 and not guessed:
        # Відображаємо поточний стан слова і кількість залишених спроб
        print(f"\nСлово: {display_word(word, guessed_letters)}")
        print(f"Залишилося спроб: {attempts}")
        
        # Ввід гравця, який повинен ввести одну літеру
        guess = input("Введіть літеру: ").lower()
        
        # Перевірка, що введена одна літера і вона є літерою алфавіту
        if len(guess) == 1 and guess.isalpha():
            # Якщо літера вже була відгадана раніше
            if guess in guessed_letters:
                print(f"Ви вже відгадали цю літеру: {guess}")
            # Якщо літери немає у загадному слові
            elif guess not in word:
                print(f"Такої літери немає у слові: {guess}")
                attempts -= 1  # Зменшуємо кількість залишених спроб
            # Якщо літера є у слові
            else:
                print(f"Чудово! Літера {guess} є у слові!")
                guessed_letters.add(guess)  # Додаємо літеру до списку відгаданих
                # Перевіряємо, чи відгадані всі літери у слові
                if set(word) <= guessed_letters:
                    guessed = True
        else:
            print("Введіть одну літеру.")  # Повідомлення про помилку, якщо введено не те

    # Якщо слово відгадане
    if guessed:
        print(f"\nВітає
