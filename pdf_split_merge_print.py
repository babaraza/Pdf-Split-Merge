import win32api
import win32print
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_split_print(path_to_files, page_to_extract):
    """
    Goes to a specified folder
    Then finds all folders
    Then finds all pdf files within the folders
    Then extracts the requested page number from each pdf file
    Then combines the extracted pages into one pdf file
    Optional: Can also print the final pdf file

    :param path_to_files: The full path to the folder/subfolders with the pdf files
    :param page_to_extract: The page number which the user wants to exract
    :return:
    """

    # Creating a path with the path provided by user
    path = Path(path_to_files)

    # Finding all folders
    folders = path.glob("*")

    # Going through each folder
    for folder in folders:

        # Creating a new PdfFileWriter object to store all extracted pages
        # Creating this every time a folder is accessed
        # So previous extracted pages are not appended
        pdf_writer = PdfFileWriter()

        # Going through each pdf file
        for file in folder.glob('*.pdf'):

            # Creating a PdfFileReader object with each file found above
            pdf = PdfFileReader(str(file))

            # Extract the page number the user wants and add it to PdfFileWriter object
            pdf_writer.addPage(pdf.getPage(page_to_extract))

        # Create the name of the file including full parent path and folder name to identify pdf
        # Example Compiled - 2019.pdf
        output_filename = f'{path_to_files}/Compiled - {folder.name}.pdf'

        # Create a pdf file with the above output_filename
        # Then append all the pages from the PdfFileWriter object
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        # Print success message for creating file for each folder
        print(f'Created: {folder.name} file')

        # Uncomment the following to enable Print Feature

        # printer_name = win32print.GetDefaultPrinter()
        # handle = win32print.OpenPrinter(printer_name)
        # attributes = win32print.GetPrinter(handle, 2)
        # win32print.SetPrinter(handle, 2, attributes, 0)
        # win32api.ShellExecute(0, 'print', output_filename, '.', '/manualstoprint', 0)
        # win32print.ClosePrinter(printer_name)


if __name__ == '__main__':
    # Getting the full path of the folder containing the pdf files (this supports sub folders)
    base_path = input('Enter full path to folder with pdf files > ')
    page_number = input('Enter the page number to extract > ')

    # Calling the main function to start program
    # Subtracting 1 from page number because 0 is the first page
    pdf_split_print(base_path, int(page_number)-1)
