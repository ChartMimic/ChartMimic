import PyPDF2
import fitz
import pandas as pd
from tqdm import tqdm
from argparse import ArgumentParser
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

def pdf_to_image(pdf_path, page_number):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

def concat_images_vertically(img1, img2):
    width = max(img1.width, img2.width)
    height = img1.height + img2.height
    result = Image.new('RGB', (width, height))
    result.paste(img1, (0, 0))
    result.paste(img2, (0, img1.height))
    return result

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--input_dir", type=str, default=f"{os.environ['PROJECT_PATH']}/results"
    )
    args = parser.parse_args()

    input_dir = args.input_dir

    data = pd.read_json(
        f"{input_dir}/chart2code_gpt-4-vision-preview_DirectAgent_results.json",
        lines=True,
    )  # just used to read path

    for i in tqdm(range(len(data))):
        filename = os.path.basename(data["file"][i])
        output_dir = f"{input_dir}/concate_chart2code_gpt-4-vision-preview_DirectAgent_results/direct_checker/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file =  output_dir + filename.replace("pdf", "png")

        files = []
        files.append(f"{os.environ['PROJECT_PATH']}/dataset/ori/" + filename)

        if os.path.exists(f"{input_dir}/chart2code_gpt-4-vision-preview_DirectAgent_results/direct_checker/" + filename):
            files.append(f"{input_dir}/chart2code_gpt-4-vision-preview_DirectAgent_results/direct_checker/" + filename)
        else:
            continue
        # files.append(f"{input_dir}/chart2code_gpt_HintEnhancedAgent_results/hintenhanced/" + filename)
        # files.append(f"{input_dir}/chart2code_gpt_SelfRevisionAgent_results/selfrevision/" + filename)
        # files.append(f"{input_dir}/chart2code_gpt_ScaffoldAgent_results/scaffold/" + filename)

        ##################################### Concat to PNG #####################################
        # concate the files
        imgs = [ pdf_to_image(file, 0) for file in files]
        # files = [open(file, "rb") for file in files]
        result = concat_images_vertically(imgs[0], imgs[1])

        result.save(output_file)
        ##################################### Concat to PNG #####################################

        ##################################### Concat to PDF #####################################
        # # concate the files
        # files = [open(file, "rb") for file in files]

        # readers = [PyPDF2.PdfReader(file) for file in files]

        # # Create a new PDF writer
        # writer = PyPDF2.PdfWriter()

        # # Add all pages to the writer
        # for reader in readers:
        #     for page in reader.pages:
        #         writer.add_page(page)

        # # Write to a new PDF file
        # with open(output_file, "wb") as output_pdf:
        #     writer.write(output_pdf)

        # # close the files
        # for file in files:
        #     file.close()
        ##################################### Concat to PDF #####################################
            
        
