# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"101204.0","system":"med"},{"code":"10992.0","system":"med"},{"code":"13563.0","system":"med"},{"code":"25054.0","system":"med"},{"code":"30996.0","system":"med"},{"code":"33837.0","system":"med"},{"code":"3847.0","system":"med"},{"code":"41015.0","system":"med"},{"code":"41781.0","system":"med"},{"code":"45948.0","system":"med"},{"code":"46066.0","system":"med"},{"code":"47504.0","system":"med"},{"code":"54252.0","system":"med"},{"code":"56385.0","system":"med"},{"code":"56647.0","system":"med"},{"code":"59083.0","system":"med"},{"code":"66104.0","system":"med"},{"code":"66773.0","system":"med"},{"code":"9711.0","system":"med"},{"code":"99232.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('aspiration-pneumonitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["aspiration-pneumonitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["aspiration-pneumonitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["aspiration-pneumonitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
