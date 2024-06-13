import os
import base64
import PyPDF2
import PIL.Image
import re
from pdf2image import convert_from_path
import pandas as pd
from PIL import Image
from tqdm import tqdm


class Chart2CodeDataset:
    def __init__(self, dataset_dir, direct_dir=None) -> None:
        super().__init__()
        self._load_data(dataset_dir, direct_dir)

    def _load_data(self, dataset_dir, direct_dir=None):
        # raw data default to be pdf
        self.raw_data = self._get_all_files(dataset_dir, ".pdf")
        self.raw_data.sort()
        # check all the raw data files have corresponding png files
        for data in self.raw_data:
            if not os.path.exists(data.replace(".pdf", ".png")):
                print("Converting pdf to png: ", data)
                self._convert_single_page_pdf_to_png(data, data.replace(".pdf", ".png"))

        # check all the raw data files have corresponding direct generated png files
        if direct_dir:
            for data in self.raw_data:
                direct_generated_pdf_file = data.replace(dataset_dir, direct_dir)
                if not os.path.exists(direct_generated_pdf_file):
                    print(
                        "Direct generated file not found: ", direct_generated_pdf_file
                    )
                    raise FileNotFoundError
                else:
                    if not os.path.exists(
                        direct_generated_pdf_file.replace(".pdf", ".png")
                    ):
                        print("Converting pdf to png: ", direct_generated_pdf_file)
                        self._convert_single_page_pdf_to_png(
                            direct_generated_pdf_file,
                            direct_generated_pdf_file.replace(".pdf", ".png"),
                        )
        # new_raw = []
        # done = pd.read_json("/Users/shichufan/Downloads/Princess-s-CHI/results/chart2code_claude-3-opus-20240229_DirectAgent_results.json0", lines=True)
        # for _ in self.raw_data:
        #     if _ not in done["file"].values:
        #         new_raw.append(_)
        # self.raw_data = new_raw

    def __getitem__(self, idx):
        return {
            "file": self.raw_data[idx],
        }

    def _encode_base_image(self, file):
        with open(file, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def _get_all_files(self, dataset_dir, file_type):
        selected_files = []
        for root, dirs, files in os.walk(dataset_dir):
            for file in files:
                if file.endswith(file_type):
                    selected_files.append(root + "/" + file)
        return selected_files

    def _convert_single_page_pdf_to_png(self, pdf_path, output_path, dpi=120):
        images = convert_from_path(pdf_path, dpi=dpi)
        images[0].save(output_path, "PNG")

    def _get_pdf_dimensions(self, pdf_path):
        file_idx = pdf_path.split("/")[-1].split("_")[0]
        width = self.dimensions_info[self.dimensions_info["idx"] == file_idx][
            "width"
        ].values[0]
        height = self.dimensions_info[self.dimensions_info["idx"] == file_idx][
            "height"
        ].values[0]
        return width, height
        # pdf_file = open(pdf_path, "rb")
        # pdf_reader = PyPDF2.PdfReader(pdf_file)
        # # We only have 1 page
        # for page_num in range(len(pdf_reader.pages)):
        #     page = pdf_reader.pages[page_num]
        #     width = page.mediabox.right - page.mediabox.left
        #     height = page.mediabox.top - page.mediabox.bottom
        #     # print(f"Page {page_num+1}: Width = {width}, Height = {height}")
        # pdf_file.close()
        # return width, height

    def _extract_code(self, text):
        code = re.findall(r"```python(.*?)```", text, re.DOTALL)
        return code

    def _resize_pdf_pages(self, input_pdf, output_pdf, scale_factor):
        with open(input_pdf, "rb") as fr:
            reader = PyPDF2.PdfReader(fr)
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                page.scale_by(scale_factor)
                writer.add_page(page)

            with open(output_pdf, "wb") as fw:
                writer.write(fw)

    def __len__(self):
        return len(self.raw_data)


class GPT4EvaluationDataset:
    def __init__(self, original_dataset_dir, generated_dataset_dir) -> None:
        super().__init__()
        self._load_data(
            original_dataset_dir,
            generated_dataset_dir,
        )

    def _load_data(self, original_dataset_dir, generated_dataset_dir):
        # raw data default to be pdf
        self.raw_data = self._get_all_files(original_dataset_dir, ".pdf")
        # check all the raw data files have corresponding png files
        for data in self.raw_data:
            if not os.path.exists(data.replace(".pdf", ".png")):
                print("Converting pdf to png: ", data)
                self._convert_single_page_pdf_to_png(data, data.replace(".pdf", ".png"))
        # check all the raw data files have corresponding generated png files
        for data in self.raw_data:
            # all the generated files are default to be pdf
            generated_pdf_file = data.replace(
                original_dataset_dir, f"{generated_dataset_dir}"
            )
            if not os.path.exists(generated_pdf_file):
                print("Generated file not found: ", generated_pdf_file)
                raise FileNotFoundError
            else:
                if not os.path.exists(generated_pdf_file.replace(".pdf", ".png")):
                    print("Converting pdf to png: ", generated_pdf_file)
                    self._convert_single_page_pdf_to_png(
                        generated_pdf_file, generated_pdf_file.replace(".pdf", ".png")
                    )
        new_raw = []
        for _ in tqdm(range(len(self.raw_data))):
            if not self._is_png_white(
                self.raw_data[_]
                .replace(original_dataset_dir, f"{generated_dataset_dir}")
                .replace(".pdf", ".png")
            ):
                new_raw.append(self.raw_data[_])
            # else:
            #     import pdb

            #     pdb.set_trace()
        self.raw_data = new_raw

    def _is_white(self, rgb):
        r, g, b = rgb
        return r > 254 and g > 254 and b > 254

    def _is_png_white(self, png_path):
        image = Image.open(png_path)
        width, height = image.size

        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                if not self._is_white(pixel):
                    return False
        return True

    def _get_all_files(self, dataset_dir, file_type):
        selected_files = []
        for root, dirs, files in os.walk(dataset_dir):
            for file in files:
                if file.endswith(file_type):
                    selected_files.append(root + "/" + file)
        return selected_files

    def _convert_single_page_pdf_to_png(self, pdf_path, output_path, dpi=350):
        images = convert_from_path(pdf_path, dpi=dpi)
        images[0].save(output_path, "PNG")

    def __getitem__(self, idx):
        return {
            "file": self.raw_data[idx],
        }

    def __len__(self):
        return len(self.raw_data)

    def is_white(rgb):
        r, g, b = rgb
        return r > 254 and g > 254 and b > 254

    def is_png_white(png_path):
        image = Image.open(png_path)
        width, height = image.size

        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                if not is_white(pixel):
                    return False
        return True


class Code4EvaluationDataset:
    def __init__(
        self, original_dataset_dir, generated_dataset_dir, template_type
    ) -> None:
        super().__init__()
        self._load_data(original_dataset_dir, generated_dataset_dir, template_type)

    def _load_data(self, original_dataset_dir, generated_dataset_dir, template_type):
        # raw data default to be py
        raw_data = self._get_all_files(original_dataset_dir, ".py")

        print("original_dataset_dir: ", original_dataset_dir)
        print("generated_dataset_dir: ", generated_dataset_dir)

        # check all the raw data files have corresponding generated files
        new_raw_data = []
        for data in raw_data:
            generated_py_file = data.replace(
                original_dataset_dir, f"{generated_dataset_dir}/{template_type}"
            )
            if os.path.exists(generated_py_file):
                new_raw_data.append(data)
                # print("Generated file not found: ", generated_py_file)
                # raise FileNotFoundError
        self.raw_data = new_raw_data

    def _get_all_files(self, dataset_dir, file_type):
        selected_files = []
        for root, dirs, files in os.walk(dataset_dir):
            for file in files:
                if file.endswith(
                    file_type
                ):  #  and "bar" in file and "43" not in file and "52" not in file and "24" not in file and "pie_15" not in file
                    selected_files.append(root + "/" + file)
        return selected_files

    def __getitem__(self, idx):
        return {
            "file": self.raw_data[idx],
        }

    def __len__(self):
        return len(self.raw_data)
