# Copyright (c) 2022 RWTH Aachen - Werkzeugmaschinenlabor (WZL)
# Contact: Simon Cramer, s.cramer@wzl-mq.rwth-aachen.de

from absl import logging
from datetime import datetime
import os
import pandas as pd
from pandas_profiling import ProfileReport
from s3_smart_open.filehandler import get_filenames, read_pd_fth, to_s3

def create_profiling_reports(input_path,output_path,dataset_rows,filename_list,file_type=None):
    """generates a pandas profiling html report and save them to the output path

    Args:
        input_path ([type]): Path where feather files can be found
        output_path ([type]): Path for saving the html reports
        dataset_rows ([type]): Amount of rows for Report Dataset.
        filename_list (list): List of Filenames for the Reports. If the List is empty, a report is created for every feather file in the input_path dir
    """    
    feather_filenames = get_filenames(input_path,filenames_list=filename_list,file_types=file_type)
    assert len(feather_filenames) > 0 , 'Length of List = 0. At least one element is required'

    if not feather_filenames:
        logging.warning('No files found to report!')
    else:
        for i in range(0,len(feather_filenames)):
            dataset = read_pd_fth(input_path,feather_filenames[i])
            if dataset_rows:
                if dataset.shape[0]  > int(dataset_rows):
                    dataset = dataset.sample(n = int(dataset_rows))
                    dataset = dataset.reset_index(drop=True)
                else:
                    if dataset.shape[0] >= 10000:
                        logging.warning('Creating the report can take some time! More than 10000 rows!')
            filename = os.path.splitext(feather_filenames[i])[0]+"_"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.html'
            report = ProfileReport(dataset,title= "{}".format(feather_filenames[i]),config_file="report_config.yml",progress_bar=False)
            tmp_save_name = 'tmp_report.html'
            report.to_file(tmp_save_name)
            to_s3(output_path,filename,tmp_save_name)
            os.remove(tmp_save_name)


