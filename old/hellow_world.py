first_name="peter"
last_name="koukoulis"
print (first_name.title() + " " + last_name.title())

some_str='string with spaces to the right '
print ("\nPrint with right spaces intact : " + "'" + some_str + "'" + "\nPrint with right spaces stripped : '" + some_str.rstrip() + "'" )

some_str='  string with spaces to the right '
print ("\nPrint with left & right spaces intact : " + "'" + some_str + "'" + "\nPrint with left spaces stripped and right spaces intact : '" + some_str.rstrip() + "'" )

some_str='  string with spaces to the right '
print ("\nPrint with left & right spaces intact : " + "'" + some_str + "'" + "\nPrint with left & right spaces stripped : '" + some_str.strip() + "'" )
