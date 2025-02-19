import sys

# This function reads the content of a .txt file
# makes sure it is a .txt file before attempting to read it
def open_file(txt_file_path):
    if not txt_file_path.endswith('.txt'):
        print('File must be a .txt file') # or show some other error message
        return
    with open(txt_file_path, 'r') as f:
        return f.read()
    
# this takes a txt file, opens it and converts it to a html file string in a sense
# there is most likely a better way to accomplish this, but this is a simple way to do it
# my thinking here is to just add this html string to a html file
def txt_to_html(txt_file_path):
    text = open_file(txt_file_path)
    if not text:
        return
    lines = text.split('\n')
    html_lines = [f'<p>{line}</p>' for line in lines]
    html = '<html><body>' + ''.join(html_lines) + '</body></html>'

    return html


# this takes the html string and writes it to a file at a specified path
# as of right now the file has to exist, but we can add a check to see if it exists and create it if it doesn't
# it also verifies that the file is a .html file
def write_html(html, html_file_path):
    if not html_file_path.endswith('.html'):
        print('File must be a .html file') # or show some other error message idk yet how we will show errors
    with open(html_file_path, 'w') as f:
        f.write(html)


# this is the main function that will be called when the script is run
# all it does is take the txt file locatio nand html file location and calls the other functions to run
def main(txt_file, html_file):
    html = txt_to_html(txt_file)
    if html:
        write_html(html, html_file)


# silly python way of ensureing main runs, it also makes it so that it takes command line arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python txt_to_html.py <input_txt_file> <output_html_file>")
    else:
        main(sys.argv[1], sys.argv[2])