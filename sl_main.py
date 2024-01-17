import streamlit as st
import compare as comp


def main():
    st.title("Сравнение 2-ух текстов на Streamlit")

    # Окна для ввода текста
    text_input1 = st.text_area("Введите текст 1:", "")
    text_input2 = st.text_area("Введите текст 2:", "")

    # Кнопка для запуска
    if st.button("Сравнить тексты"):
        # Вызываем функцию для сравнения текстов
        result = comp.compare_texts(text_input1, text_input2)

        # Выводим результат
        st.write("Результат сравнения текстов:")
        st.write(result)

if __name__ == "__main__":
    main()
