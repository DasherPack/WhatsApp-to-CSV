from chatparsers import WhatsAppParser
import os

directory = os.getcwd()

path = input("Path to raw exported chat:\n")
file_name = input("Name of the file (not including .csv)\n")

parser = WhatsAppParser(path)
parser.parse_file_into_df()
parser.df.to_csv(f'{directory}/csv/{file_name}.csv', index = False)
print(f"Sucess! File at {directory}/csv/{file_name}.csv")
