# Usual Preamble
# Importing Libraries for file acess and handling json
import json
import os
import glob


#######################################JSON Merger########################################
# Function name     : merge()
# Input Paramters   : JSON file dict 1, JSON file dict 2
# Output Parameters : Merged file dict
def json_merge(filename1, filename2):
    for key in filename2:
    	# if key is present in both files
        if key in filename1:
        	# if value type is dict object
            if isinstance(filename1[key], dict) and isinstance(filename2[key], dict): 
                merge(filename1[key], filename2[key])
            # if value type is not dict object, then merge those values  
            else:
              filename1[key] = filename1[key] +  filename2[key]
        # if key is not present in filename 1, then add as new entry  
        else: 
            filename1.update( {key : filename2[key]} )
    return filename1

###########################################################################################



###########################   Getting input paramters from User ###########################
# 1. Folder Path
# 2. Input File Base Name
# 3. Output FIle Base Name
# 4. Max File Size
PATH                    = input("Enter complete folder path               :")
INPUT_FILE_BASE_NAME    = input("Enter base name for input file           :")
OUTPUT_FILE_BASE_NAME   = input("Enter base name for output file          :")
MAX_FILE_SIZE           = int(input("Enter the maximum file size (bytes)  	:") ) 

#########################################################################################




####################################### Folder Path ########################################
# Change working directory to the PATH specified
PATH = PATH + '\\'
os.chdir(PATH)
# Counter for output file suffix name
count = 1

############################################################################################




############################# Collecting json data files ###################################
# Prefix : INPUT_FILE_BASE_NAME
# Suffix : Numericals in Ascending order like 1,2,3,.....12,13,....
data = glob.glob(PATH + INPUT_FILE_BASE_NAME +'*.json', recursive=True)
# Sorting JSON Data files in Ascending order like 1,2,....11,12,....
data = sorted(data, key=lambda a: int(a.split('data')[1].split('.json')[0] ) )
n = len(data)

###########################################################################################



################################  Output Filename  #########################################
# Output filename
# Prefix : OUTPUT_FILE_BASE_NAME given by User
# Suffix : counter 
OUTPUT_FILE_BASE_NAME = OUTPUT_FILE_BASE_NAME + str(n)

#############################################################################################


########################################### Merging JSON #####################################
file_1 = open(data[0], 'r')
file_2 = open(data[1], 'r')
json_data_1 = json.load(file_1)
json_data_2 = json.load(file_2)
file_1.close()
file_2.close()
inital_merged_file = open(OUTPUT_FILE_BASE_NAME+'.json', 'w') 
json.dump(json_merge(json_data_1,json_data_2),inital_merged_file)
inital_merged_file.close()


for file in range(2,n):
	file_1 = open(data[file], 'r')
	file_2 = open(OUTPUT_FILE_BASE_NAME+'.json','r')

	json_data_1=json.load(file_2)
	json_data_2=json.load(file_1)

	file_2.close()
	file_1.close()
	merged_file = open(OUTPUT_FILE_BASE_NAME+'.json','w')
	# f.seekg(0)
	# f.truncate()
	json.dump(json_merge(json_data_1,json_data_2),merged_file)
	merged_file.close()

print("\nMerging of JSON files have been completed")
print("Merged filename is ",str(OUTPUT_FILE_BASE_NAME + '.json'))

##################################################################################



######################## Checking the size of Merged file ########################
# If greater than MAX_FILE_SIZE specified bt user, then message gets popped

file_size = os.path.getsize(OUTPUT_FILE_BASE_NAME + '.json')

if file_size > MAX_FILE_SIZE:
	print("Merged File is greater than MAX_FILE_SIZE specified.",str(file_size)," bytes")
else:
	print("Merged file is within allowable maximum file size.",str(file_size), "  bytes")

#################################################################################


