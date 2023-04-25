def insert_script_tag(file_path, script_code):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    script_tag = f"<script>{script_code}</script>"
    head_close_tag = "</head>"

    if head_close_tag in file_content:
        file_content = file_content.replace(head_close_tag, f"{script_tag}\n{head_close_tag}")

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_content)
    else:
        print("Error: </head> tag not found in the file.")


if __name__ == "__main__":
    html_file_path = "index.html"
    script_code = "if ('serviceWorker' in navigator) { navigator.serviceWorker.register('serviceworker.js'); }"

    insert_script_tag(html_file_path, script_code)
