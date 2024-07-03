import PyPDF2
from PIL import Image, ImageDraw
import numpy as np
from tqdm import tqdm

def pdf_to_image(pdf_path):
    op_list = []
    pdf = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    page = pdf.pages[0]  # Assuming you want to process the first page

    # Extract page dimensions
    page_width = int(page.mediabox.width)
    page_height = int(page.mediabox.height)

    # Create a blank image
    image = Image.new('RGB', (page_width, page_height), 'white')
    draw = ImageDraw.Draw(image)

    def visitor_svg(op, args, cm, tm):
        op_list.append((op, args, cm, tm))

    page.extract_text(visitor_operand_before=visitor_svg)

    return op_list


def extract_values(op_list):
    cs_correct, sc_correct = False, False  # Flag to indicate if 'cs' (color space) and 'sc' (color encoding) are correct

    last_move = 0
    y_list, y_lists = [], []

    # Iterate over the list of operations
    for idx, (op, args, cm, tm) in tqdm(enumerate(op_list)):

        if op == b'm':  # Move to
            if cs_correct and sc_correct:
                if idx - last_move != 132 and len(
                        y_list):  # Skip lines that are not part of the three long lines of red points
                    y_lists.append(y_list)
                    y_list = []
                last_move = idx

        elif op == b'l':  # Line to
            end_x, end_y = args
            if cs_correct and sc_correct:
                y_list.append(float(end_y))

        elif op == b'sc' or op == b'cs' or op == b'SC' or op == b'CS':
            if op == b'cs' or op == b'CS':
                cs_correct = '/Cs3' in args
            if op == b'sc' or op == b'SC':
                sc_correct = all([f'{float(x):.2}' in ['0.8', '0.039', '0.13'] for x in args if
                                  isinstance(x, PyPDF2.generic._base.FloatObject)])

    y_lists.append(y_list)

    inter_val_1 = (y_lists[0][-1] + y_lists[1][0]) / 2
    inter_val_2 = (y_lists[1][-1] + y_lists[2][0]) / 2

    y_combined = np.concatenate(
        [y_lists[0], [inter_val_1], y_lists[1], [inter_val_2], y_lists[2]])  # Combined list of y values
    y = y_combined / -28.3465 + 2  # Convert to mV and apply a 1.5 mV offset
    y = y - np.mean(y)
    return y

