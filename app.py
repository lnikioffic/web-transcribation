from transcribation import get_audio_text
import streamlit as st
from uuid import uuid1


def save_uploaded_file(uploaded_file, save_path):
    try:
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        st.error(f"Ошибка при сохранении файла: {e}")
        return False


def main():
    st.title("Загрузка и транскрибация видео файла")
    uploaded_file = st.file_uploader("Выберите файл", type=["mp4"])

    # Если файл загружен
    if uploaded_file is not None:
        # Чтение содержимого файла
        file_save_path = (
            f"./{uuid1()}-{uploaded_file.name}"  # Путь для сохранения файла
        )
        if save_uploaded_file(uploaded_file, file_save_path):
            st.success(f"Файл успешно сохранён: {file_save_path.split('/')[-1]}")

            file_contents = get_audio_text(file_save_path)
            
            # Вывод содержимого файла
            st.text_area(
                "Содержимое файла:", file_contents, height=300, key="file_contents"
            )


if __name__ == "__main__":
    main()
