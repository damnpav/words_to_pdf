import os
import sys
import subprocess

# Get directory from command line arguments
try:
    input_dir = sys.argv[1]
except IndexError:
    print("Please provide a directory path.")
    sys.exit(1)

for filename in os.listdir(input_dir):
    if filename.endswith('.docx'):
        doc_path = os.path.join(input_dir, filename)
        pdf_path = os.path.join(input_dir, filename[:-5] + '.pdf')  # Change file extension to .pdf

        # Perform conversion using LibreOffice
        subprocess.run(['/Applications/LibreOffice.app/Contents/MacOS/soffice', '--headless', '--convert-to', 'pdf', '--outdir', input_dir, doc_path])
