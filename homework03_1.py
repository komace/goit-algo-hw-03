import os
import shutil
import argparse


# Функція виконує основну роботу — рекурсивне копіювання файлів із сортуванням за розширеннями.
def copy_files_recursive(src_dir, dest_dir):
    try:
        # Рекурсія по директоріях: якщо поточний елемент у директорії є піддиректорією, функція викликає сама себе для обробки вмісту цієї піддиректорії.
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                copy_files_recursive(src_path, dest_dir)
            else:
                # Обробка файлів:
                file_ext = os.path.splitext(item)[1][1:]   # Отримати розширення файлу без крапки 
                # Створення підпапок для розширень:
                if file_text:
                    ext_dir = os.path.join(dest_dir, file_ext)
                else:
                    ext_dir = os.path.join(dest_dir,"no_extension")


                os.makedirs(ext_dir, exist_ok=True)
                dest_path = os.path.join(ext_dir, item)
                # Копіювання файлів:
                shutil.copy2(src_path, dest_path)
                print(f"Скопійовано {src_path} до {dest_path}")    

    # Обробка помилок: Якщо під час копіювання виникає помилка, програма не зупиняється, а просто повідомляє про це.
                
    except Exception as e:
        print(F"Помилка при копіюванні {src_path}: {e}")  

# Функція відповідає за обробку аргументів командного рядка та виклик основної логіки.

def main():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів та сортування за розширеннями")
    parser.add_argument("src_dir", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir",type=str, nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    args = parser.parse_args()
    
    # Перевірка існування директорії:
    if not os.path.isdir(args.src_dir):
        print(f"Директорія {args.src_dir} не існує або не є директорією.")
        return

    # Створення директорії призначення:
    os.makedirs(args.dest_dir, exist_ok=True)
    # Виклик основної функції: Запускає процес копіювання.
    copy_files_recursive(args.src_dir, args.dest_dir)
    print(f"Копіювання завершено. Файли скопійовано до {args.dest_dir}")   

if __name__ == "__main__":
    main()    
