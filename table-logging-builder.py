import os
import csv
import logging

filename = '.\\tables.csv'
sampleFiles = [
    ('TABLES','.\\TABLEsample.sql'),
    ('TRIGGERS','.\\TRIGGERsample.sql')
    ]
rawsample = ''
todo = []
logging.basicConfig(level= logging.DEBUG, filename='table-logging-builder.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

logging.info("Start Building")

if __name__ == '__main__':
    if not os.path.exists(filename):
        logging.info('Generating file...')
        with open(filename, 'w') as file:
            file.write('')
    else:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            logging.info('Appending rows to ToDo list:')
            for row in reader:
                logging.info('{}.{}'.format(row[0], row[1]))
                todo.append((row[0], row[1]))
    
    for sample in sampleFiles:
        directory = sample[0]
        if not os.path.exists(directory):
            logging.info('Making {} directory.'.format(directory))
            os.mkdir(directory)
    
    for samplefile in sampleFiles:
        rawsample = ''
        if not os.path.exists(samplefile[1]):
            logging.error('Missing {} file to copy.'.format(samplefile[1]))
        else:
            with open(samplefile[1], 'r') as sqlfile:
                logging.info('Loading SQL Sample {} into memory...'.format(samplefile[0]))
                rawsample = sqlfile.read()
            for row in todo:
                tempdata = rawsample.replace('{?}', '{}.{}'.format(row[0], row[1]).upper())
                logging.info('Writing alter {} to file'.format(row[1].upper()))
                with open('{}\\{}.sql'.format(samplefile[0], row[1].upper()), 'w') as outfile:
                    outfile.write(tempdata)