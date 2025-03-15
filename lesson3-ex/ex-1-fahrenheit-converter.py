def convert_to_celsius(ce_temp):
    return (float(ce_temp) * 9/5) + 32

print('Enter celsius temperature: ')
ce_temp = input()
print('Conversion to fahr: ' + str(convert_to_celsius(ce_temp)))