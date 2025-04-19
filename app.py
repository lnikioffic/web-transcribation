# from transcribation import get_audio_text
import streamlit as st

#print(get_audio_text('test_video.mp4'))


def main():
    st.title("Загрузка и просмотр текстового файла")
    uploaded_file = st.file_uploader("Выберите файл", type=["txt", "mp4"])

    # Если файл загружен
    if uploaded_file is not None:
        # Чтение содержимого файла
        file_contents = uploaded_file.read().decode("utf-8")

        # Вывод содержимого файла
        st.text_area("Содержимое файла:", file_contents, height=300)


if __name__ == "__main__":
    main()