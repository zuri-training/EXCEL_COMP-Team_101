import pandas as pd
import os
from django.conf import settings


def html_open_csv(file_url):
    data = pd.read_csv(file_url)

    return data.to_html()


def bg(x, y):
    # print(y)
    # # print(x)
    for i in x.index.values:
        # print(x.index.values)
        print(x)
        return ['background: blue' if i in y else '']


def pan(full_file_name, operation, file_extension, file_name):
    # FILE PATH FOR BOTH UPLOADED AND NEW UPLOADS
    actual_file = f"{settings.MEDIA_ROOT}/uploaded/document/{full_file_name}"
    uploaded_file_path = f"{settings.MEDIA_ROOT}/corrected/document/"

    data = None

    if file_extension == ".csv":
        data = pd.read_csv(actual_file)

    elif file_extension == ".xls" or file_extension == ".xlsx":
        print("i")
        data = pd.read_excel(actual_file)
        print("y")

    # File Operation Logic
    if len(data) > 0:
        if operation == 'rem_dupl':
            data.drop_duplicates(inplace=True)
            if file_extension == ".csv":
                data.to_csv(
                    f"{uploaded_file_path}/{full_file_name}", index=False)
            elif file_extension == ".xlsx" or file_extension == '.xls':
                data.to_excel(f"{uploaded_file_path}/{full_file_name}",
                              index=False, engine='openpyxl')

        elif operation == 'highlight_only':
            duplicates = data[data.duplicated(keep=False)]

            exp = data.to_excel("sample.xlsx", engine='openpyxl')
        # elif operation == 'two_files_with_dup':
        #     pass


# duplicates_index = duplicates.index.values
# data.drop_duplicates(inplace=True)
