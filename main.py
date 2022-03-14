# Copyright (c) 2022 RWTH Aachen - Werkzeugmaschinenlabor (WZL)
# Contact: Simon Cramer, s.cramer@wzl-mq.rwth-aachen.de

from absl import logging, app, flags
import pandas_profiling_report as ppr
import os

FLAGS = flags.FLAGS

flags.DEFINE_string('output_path',
                     default=None,
                     help="Path for saving the hmtl report.")

flags.DEFINE_string('input_path',
                     default=None,
                     help="Savepath feather data dir")
                  
flags.DEFINE_string('dataset_rows_max',
                      default=None,
                      help="Amount of rows for Report Dataset.")

flags.DEFINE_list('filename_list',
                    default=[],
                    help="List of Filenames for the Reports. If List is empty, a report is created for every feather file in the input_path dir")
flags.DEFINE_list('file_types',default=['.fth'],help='Default, feather files for report')

flags.mark_flag_as_required('input_path')
flags.mark_flag_as_required('output_path')


def main(argv):
    """Creates a Pandas Profiling HTML Report for Pandas Dataframes

    Required flags:
        - input_path
        - output_path

    Raises:
        ValueError: If input or output Path do not exist.
    """    
    del argv

    logging.info('----Start----')
    ppr.create_profiling_reports(FLAGS.input_path,FLAGS.output_path,FLAGS.dataset_rows_max,FLAGS.filename_list,FLAGS.file_types)
    logging.info('----End----')

if __name__ == '__main__':
  app.run(main)