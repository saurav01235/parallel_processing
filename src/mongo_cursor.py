db = dbclient[docdb_database]
col = db[docdb_collection]





from multiprocessing import Pool
import datetime



def process(i):
  doc_list = []
  print('start time :',datetime.datetime.now())
  docdb_query_parameters = {"u_asset_id": {"$in":i}}
  if ui_asset_id_lst:
      data_cursor=col.find(docdb_query_parameters)
  else:
    data_cursor=col.find({})
    
  for dt in data_cursor:
    doc_list.append({"src_trb_id":dt["src_trb_id"],"file_name": dt["_id"]})
  print('End time :',datetime.datetime.now())
  return doc_list







result = []  
lst = []
for i in range(0,3070,1):
  lst.append(ui_asset_id_lst[i:i+1])
# lst = []
# for i in range(0,10,1):
#   lst.append(ui_asset_id_lst[i:i+1])
# Define the dataset
dataset = lst

# Run this with a pool of 5 agents having a chunksize of 3 until finished
agents = 20
chunksize = 1
cnt = 0
with Pool(processes=agents) as pool:
  cnt = cnt + 1
  print('start time :',datetime.datetime.now(), " count ", cnt)
  result = result + pool.map(process, dataset, chunksize)
  print('End time :',datetime.datetime.now(), " count ", cnt)

# Output the result
# print ('Result:  ' + str(result))




