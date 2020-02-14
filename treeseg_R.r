# Copy .rxp files to new folder with hierarchy compatible with treeseg --------
# Set registered scan directory path remember it should be / not \ in the path
i_directory <- "G:/Registered/D100-C-2019-10-03.RiSCAN"

# Set new output directory path
o_directory <- "D:/new_scan"

# Create output directory if not currently exists
if (!dir.exists(o_directory)){
  dir.create(o_directory)
}

# Get the folder paths that contain rxp files
all_dir <- list.dirs(path = paste0(i_directory, "/SCANS/"), full.names = TRUE, recursive = F)

for(i in all_dir){
  d_name <- paste0(o_directory, "/Scanpos", substring(i,nchar(i)-3+1)) # Combine Scanpos with last 3 digits from folder path
  if (!dir.exists(d_name)){ # check if the folder exists
    dir.create(d_name)
  }
  file_name <- list.files(paste0(i, "/SINGLESCANS/"), pattern = "[^a-z].rxp") # avoid .residual.rxp using regular expression
  print(paste("Start copying", file_name, "from", d_name)) # Print out to console for easy troubleshooting
  file.copy(paste0(i, "/SINGLESCANS/", file_name), 
            d_name) # destination folder
  print(paste("Finish copying", file_name, "from", d_name)) # Print out to console for easy troubleshooting
}
print("Done")



# Rename .DAT files -------------------------------------------------------
# Set directory that contains .DAT files. It must be /matrix (create it yourself)
i_directory <- "G:/Test" # 

DAT_list <- list.files(path = i_directory,pattern="*.DAT", full.names = T, recursive = F)
for(DAT_file in DAT_list){
  file.rename(DAT_file, paste0(i_directory, "/", substring(i,nchar(i)-3+1), ".dat"))
}
