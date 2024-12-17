# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist


# YAHAN MAINE EK EMPTY FILE CREAT KARLI

my_file = open( "Empty File.txt", 'x')
my_file.close()

# YAHAN MAINE EK FILE CREATE KARI AURR USMEIN KUCH LIKHA

my_file = open('Chapter 09\My_City.txt', "w")
my_file.write('My city name is Karachi, Its the largest city of Pakistan')
my_file.close()

# YAHAN MAINE USS HII FILE KE ANDER THORA SA AURR MASALA ADD KARDIA

my_file = open('Chapter 09\My_City.txt', 'a')
my_file.write('. Its situated in Sindh, Its the biggest economical power of Pakistan!')
my_file.close()

# YAHAN MEIN USS HII FILE KO READ KARWA RAHA HOON

my_file = open("Chapter 09\My_City.txt", 'r')
print(my_file.read())



