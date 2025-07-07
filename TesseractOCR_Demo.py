from tesserocr import PyTessBaseAPI
import tesserocr

images = ['D:/D365_BC_AI/Invoice/Thapthai.jpg', 'D:/D365_BC_AI/Invoice/Thapthai#1.jpg']

with PyTessBaseAPI(path='tessdata-main\\', lang="eng+tha") as api:
    for img in images:
        #ลบช่องว่างแต่ละตัวอักษร
        api.SetVariable('preserve_interword_spaces', '1')
        api.SetImageFile(img)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.

# print(tesserocr.tesseract_version())  # print tesseract-ocr version
# print(tesserocr.get_languages())  # prints tessdata path and list of available languages