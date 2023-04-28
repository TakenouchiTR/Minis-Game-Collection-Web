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

def update_error_message(file_path, original_message, updated_message):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    if original_message in file_content:
        file_content = file_content.replace(original_message, updated_message)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_content)
    else:
        print("Error: error message not found in the file.")

if __name__ == "__main__":
    html_file_path = "index.html"
    script_code = "if ('serviceWorker' in navigator) { navigator.serviceWorker.register('serviceworker.js'); }"
    original_message = 'The following features required to run Godot projects on the Web are missing:'
    updated_message = '\\nThese components should become available upon a refresh.\\n\\nThe following features required to run Godot projects on the Web are missing:'

    insert_script_tag(html_file_path, script_code)
    update_error_message(html_file_path, original_message, updated_message)
